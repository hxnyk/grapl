from datetime import timedelta
from typing import Any, Dict, List
from unittest import TestCase

import hypothesis
import pytest
from grapl_analyzerlib.test_utils.strategies.asset_view_strategy import (
    AssetProps,
    asset_props_strategy,
)
from grapl_common.debugger.vsc_debugger import wait_for_vsc_debugger
from grapl_common.grapl_logger import get_module_grapl_logger
from grapl_tests_common.clients.engagement_edge_client import EngagementEdgeClient
from grapl_tests_common.clients.graphql_endpoint_client import GraphqlEndpointClient
from grapl_tests_common.scenarios.create_lens_with_nodes_in_scope import *

LOGGER = get_module_grapl_logger()

GqlLensDict = Dict[str, Any]

wait_for_vsc_debugger(service="graphql_endpoint_tests")


@pytest.mark.integration_test
class TestGraphqlEndpoint(TestCase):
    @hypothesis.given(
        asset_props=asset_props_strategy(),
    )
    @hypothesis.settings(deadline=timedelta(seconds=10))
    def test_create_lens_shows_up_in_graphql(
        self,
        asset_props: AssetProps,
    ) -> None:
        graph_client = GraphClient()
        graphql_client = GraphqlEndpointClient(jwt=EngagementEdgeClient().get_jwt())

        lens = create_lens_with_nodes_in_scope(self, graph_client, asset_props)
        lens_name = lens.get_lens_name()
        assert lens_name

        # Check that this lens shows up in the "show all lenses" view
        # NOTE: This test could be somewhat finicky, since it just gets the first 1000 lenses
        gql_lenses = _query_graphql_endpoint_for_lenses(graphql_client)
        assert lens_name in [l["lens_name"] for l in gql_lenses]

        # Query by that lens name
        gql_lens = graphql_client.query_for_scope(lens_name)
        # For some reason, upon create, `lens.uid` comes back as a string like "0x5"
        assert gql_lens["uid"] == int(lens.uid, 0)  # type: ignore
        assert gql_lens["lens_name"] == lens_name
        # Check the nodes in scope
        assert len(gql_lens["scope"]) == 1
        # Ensure we strip the Entity and Base types
        assert gql_lens["scope"][0]["dgraph_type"] == ["Asset"]
        assert gql_lens["scope"][0]["hostname"] == asset_props["hostname"]

    def test_describe_asset_type(
        self,
    ) -> None:
        graphql_client = GraphqlEndpointClient(jwt=EngagementEdgeClient().get_jwt())

        result = _query_graphql_about_type("Asset", graphql_client)
        assert result["name"] == "Asset"

        uid_looks_like = {"name": "uid", "type": {"name": "Int", "kind": "SCALAR"}}
        assert any(x for x in result["fields"] if x == uid_looks_like)


def _query_graphql_endpoint_for_lenses(
    gql_client: GraphqlEndpointClient,
) -> List[GqlLensDict]:
    # Just get *all* lenses
    query = """
    {
        lenses(first: 1000, offset: 0) {
            uid,
            node_key,
            lens_name,
            score, 
            lens_type,
        }
    }
    """
    resp = gql_client.query(query)
    return resp["lenses"]


def _query_graphql_about_type(type_name: str, graphql_client: GraphqlEndpointClient):
    query = """
    query QueryGraphqlAboutType($type_name: String!) {
    __type(name: $type_name) {
        name
        fields {
        name
        type {
            name
            kind
        }
        }
    }
    }
    """
    resp = graphql_client.query(query, {"type_name": type_name})
    return resp["__type"]
