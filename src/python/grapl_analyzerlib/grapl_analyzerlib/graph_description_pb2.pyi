# @generated by generate_proto_mypy_stubs.py.  Do not edit!
import sys
from google.protobuf.descriptor import (
    Descriptor as google___protobuf___descriptor___Descriptor,
    FileDescriptor as google___protobuf___descriptor___FileDescriptor,
)

from google.protobuf.internal.containers import (
    RepeatedCompositeFieldContainer as google___protobuf___internal___containers___RepeatedCompositeFieldContainer,
    RepeatedScalarFieldContainer as google___protobuf___internal___containers___RepeatedScalarFieldContainer,
)

from google.protobuf.message import (
    Message as google___protobuf___message___Message,
)

from typing import (
    Iterable as typing___Iterable,
    Mapping as typing___Mapping,
    MutableMapping as typing___MutableMapping,
    Optional as typing___Optional,
    Text as typing___Text,
)

from typing_extensions import (
    Literal as typing_extensions___Literal,
)


builtin___bool = bool
builtin___bytes = bytes
builtin___float = float
builtin___int = int


DESCRIPTOR: google___protobuf___descriptor___FileDescriptor = ...

class Session(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    primary_key_properties: google___protobuf___internal___containers___RepeatedScalarFieldContainer[typing___Text] = ...
    primary_key_requires_asset_id: builtin___bool = ...
    created_time: typing___Text = ...
    last_seen_time: typing___Text = ...
    terminated_time: typing___Text = ...

    def __init__(self,
        *,
        primary_key_properties : typing___Optional[typing___Iterable[typing___Text]] = None,
        primary_key_requires_asset_id : typing___Optional[builtin___bool] = None,
        created_time : typing___Optional[typing___Text] = None,
        last_seen_time : typing___Optional[typing___Text] = None,
        terminated_time : typing___Optional[typing___Text] = None,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"created_time",b"created_time",u"last_seen_time",b"last_seen_time",u"primary_key_properties",b"primary_key_properties",u"primary_key_requires_asset_id",b"primary_key_requires_asset_id",u"terminated_time",b"terminated_time"]) -> None: ...
type___Session = Session

class Static(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    primary_key_properties: google___protobuf___internal___containers___RepeatedScalarFieldContainer[typing___Text] = ...
    primary_key_requires_asset_id: builtin___bool = ...

    def __init__(self,
        *,
        primary_key_properties : typing___Optional[typing___Iterable[typing___Text]] = None,
        primary_key_requires_asset_id : typing___Optional[builtin___bool] = None,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"primary_key_properties",b"primary_key_properties",u"primary_key_requires_asset_id",b"primary_key_requires_asset_id"]) -> None: ...
type___Static = Static

class IdStrategy(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...

    @property
    def session(self) -> type___Session: ...

    @property
    def static(self) -> type___Static: ...

    def __init__(self,
        *,
        session : typing___Optional[type___Session] = None,
        static : typing___Optional[type___Static] = None,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions___Literal[u"session",b"session",u"static",b"static",u"strategy",b"strategy"]) -> builtin___bool: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"session",b"session",u"static",b"static",u"strategy",b"strategy"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions___Literal[u"strategy",b"strategy"]) -> typing_extensions___Literal["session","static"]: ...
type___IdStrategy = IdStrategy

class NodeProperty(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    increment_only_uint_prop: builtin___int = ...
    decrement_only_uint_prop: builtin___int = ...
    immutable_uint_prop: builtin___int = ...
    increment_only_int_prop: builtin___int = ...
    decrement_only_int_prop: builtin___int = ...
    immutable_int_prop: builtin___int = ...
    immutable_str_prop: typing___Text = ...

    def __init__(self,
        *,
        increment_only_uint_prop : typing___Optional[builtin___int] = None,
        decrement_only_uint_prop : typing___Optional[builtin___int] = None,
        immutable_uint_prop : typing___Optional[builtin___int] = None,
        increment_only_int_prop : typing___Optional[builtin___int] = None,
        decrement_only_int_prop : typing___Optional[builtin___int] = None,
        immutable_int_prop : typing___Optional[builtin___int] = None,
        immutable_str_prop : typing___Optional[typing___Text] = None,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions___Literal[u"decrement_only_int_prop",b"decrement_only_int_prop",u"decrement_only_uint_prop",b"decrement_only_uint_prop",u"immutable_int_prop",b"immutable_int_prop",u"immutable_str_prop",b"immutable_str_prop",u"immutable_uint_prop",b"immutable_uint_prop",u"increment_only_int_prop",b"increment_only_int_prop",u"increment_only_uint_prop",b"increment_only_uint_prop",u"property",b"property"]) -> builtin___bool: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"decrement_only_int_prop",b"decrement_only_int_prop",u"decrement_only_uint_prop",b"decrement_only_uint_prop",u"immutable_int_prop",b"immutable_int_prop",u"immutable_str_prop",b"immutable_str_prop",u"immutable_uint_prop",b"immutable_uint_prop",u"increment_only_int_prop",b"increment_only_int_prop",u"increment_only_uint_prop",b"increment_only_uint_prop",u"property",b"property"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions___Literal[u"property",b"property"]) -> typing_extensions___Literal["increment_only_uint_prop","decrement_only_uint_prop","immutable_uint_prop","increment_only_int_prop","decrement_only_int_prop","immutable_int_prop","immutable_str_prop"]: ...
type___NodeProperty = NodeProperty

class NodeDescription(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    class PropertiesEntry(google___protobuf___message___Message):
        DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
        key: typing___Text = ...

        @property
        def value(self) -> type___NodeProperty: ...

        def __init__(self,
            *,
            key : typing___Optional[typing___Text] = None,
            value : typing___Optional[type___NodeProperty] = None,
            ) -> None: ...
        def HasField(self, field_name: typing_extensions___Literal[u"value",b"value"]) -> builtin___bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"key",b"key",u"value",b"value"]) -> None: ...
    type___PropertiesEntry = PropertiesEntry

    node_key: typing___Text = ...
    node_type: typing___Text = ...

    @property
    def properties(self) -> typing___MutableMapping[typing___Text, type___NodeProperty]: ...

    @property
    def id_strategy(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[type___IdStrategy]: ...

    def __init__(self,
        *,
        properties : typing___Optional[typing___Mapping[typing___Text, type___NodeProperty]] = None,
        node_key : typing___Optional[typing___Text] = None,
        node_type : typing___Optional[typing___Text] = None,
        id_strategy : typing___Optional[typing___Iterable[type___IdStrategy]] = None,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"id_strategy",b"id_strategy",u"node_key",b"node_key",u"node_type",b"node_type",u"properties",b"properties"]) -> None: ...
type___NodeDescription = NodeDescription

class IdentifiedNode(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    class PropertiesEntry(google___protobuf___message___Message):
        DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
        key: typing___Text = ...

        @property
        def value(self) -> type___NodeProperty: ...

        def __init__(self,
            *,
            key : typing___Optional[typing___Text] = None,
            value : typing___Optional[type___NodeProperty] = None,
            ) -> None: ...
        def HasField(self, field_name: typing_extensions___Literal[u"value",b"value"]) -> builtin___bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"key",b"key",u"value",b"value"]) -> None: ...
    type___PropertiesEntry = PropertiesEntry

    node_key: typing___Text = ...
    node_type: typing___Text = ...

    @property
    def properties(self) -> typing___MutableMapping[typing___Text, type___NodeProperty]: ...

    def __init__(self,
        *,
        properties : typing___Optional[typing___Mapping[typing___Text, type___NodeProperty]] = None,
        node_key : typing___Optional[typing___Text] = None,
        node_type : typing___Optional[typing___Text] = None,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"node_key",b"node_key",u"node_type",b"node_type",u"properties",b"properties"]) -> None: ...
type___IdentifiedNode = IdentifiedNode

class MergedNode(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    class PropertiesEntry(google___protobuf___message___Message):
        DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
        key: typing___Text = ...

        @property
        def value(self) -> type___NodeProperty: ...

        def __init__(self,
            *,
            key : typing___Optional[typing___Text] = None,
            value : typing___Optional[type___NodeProperty] = None,
            ) -> None: ...
        def HasField(self, field_name: typing_extensions___Literal[u"value",b"value"]) -> builtin___bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"key",b"key",u"value",b"value"]) -> None: ...
    type___PropertiesEntry = PropertiesEntry

    uid: builtin___int = ...
    node_key: typing___Text = ...
    node_type: typing___Text = ...

    @property
    def properties(self) -> typing___MutableMapping[typing___Text, type___NodeProperty]: ...

    def __init__(self,
        *,
        properties : typing___Optional[typing___Mapping[typing___Text, type___NodeProperty]] = None,
        uid : typing___Optional[builtin___int] = None,
        node_key : typing___Optional[typing___Text] = None,
        node_type : typing___Optional[typing___Text] = None,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"node_key",b"node_key",u"node_type",b"node_type",u"properties",b"properties",u"uid",b"uid"]) -> None: ...
type___MergedNode = MergedNode

class Edge(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    to: typing___Text = ...
    edgeName: typing___Text = ...

    def __init__(self,
        *,
        to : typing___Optional[typing___Text] = None,
        edgeName : typing___Optional[typing___Text] = None,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"edgeName",b"edgeName",u"from",b"from",u"to",b"to"]) -> None: ...
type___Edge = Edge

class MergedEdge(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    from_uid: typing___Text = ...
    from_node_key: typing___Text = ...
    to_uid: typing___Text = ...
    to_node_key: typing___Text = ...
    edgeName: typing___Text = ...

    def __init__(self,
        *,
        from_uid : typing___Optional[typing___Text] = None,
        from_node_key : typing___Optional[typing___Text] = None,
        to_uid : typing___Optional[typing___Text] = None,
        to_node_key : typing___Optional[typing___Text] = None,
        edgeName : typing___Optional[typing___Text] = None,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"edgeName",b"edgeName",u"from_node_key",b"from_node_key",u"from_uid",b"from_uid",u"to_node_key",b"to_node_key",u"to_uid",b"to_uid"]) -> None: ...
type___MergedEdge = MergedEdge

class EdgeList(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...

    @property
    def edges(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[type___Edge]: ...

    def __init__(self,
        *,
        edges : typing___Optional[typing___Iterable[type___Edge]] = None,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"edges",b"edges"]) -> None: ...
type___EdgeList = EdgeList

class MergedEdgeList(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...

    @property
    def edges(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[type___MergedEdge]: ...

    def __init__(self,
        *,
        edges : typing___Optional[typing___Iterable[type___MergedEdge]] = None,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"edges",b"edges"]) -> None: ...
type___MergedEdgeList = MergedEdgeList

class GraphDescription(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    class NodesEntry(google___protobuf___message___Message):
        DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
        key: typing___Text = ...

        @property
        def value(self) -> type___NodeDescription: ...

        def __init__(self,
            *,
            key : typing___Optional[typing___Text] = None,
            value : typing___Optional[type___NodeDescription] = None,
            ) -> None: ...
        def HasField(self, field_name: typing_extensions___Literal[u"value",b"value"]) -> builtin___bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"key",b"key",u"value",b"value"]) -> None: ...
    type___NodesEntry = NodesEntry

    class EdgesEntry(google___protobuf___message___Message):
        DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
        key: typing___Text = ...

        @property
        def value(self) -> type___EdgeList: ...

        def __init__(self,
            *,
            key : typing___Optional[typing___Text] = None,
            value : typing___Optional[type___EdgeList] = None,
            ) -> None: ...
        def HasField(self, field_name: typing_extensions___Literal[u"value",b"value"]) -> builtin___bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"key",b"key",u"value",b"value"]) -> None: ...
    type___EdgesEntry = EdgesEntry


    @property
    def nodes(self) -> typing___MutableMapping[typing___Text, type___NodeDescription]: ...

    @property
    def edges(self) -> typing___MutableMapping[typing___Text, type___EdgeList]: ...

    def __init__(self,
        *,
        nodes : typing___Optional[typing___Mapping[typing___Text, type___NodeDescription]] = None,
        edges : typing___Optional[typing___Mapping[typing___Text, type___EdgeList]] = None,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"edges",b"edges",u"nodes",b"nodes"]) -> None: ...
type___GraphDescription = GraphDescription

class IdentifiedGraph(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    class NodesEntry(google___protobuf___message___Message):
        DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
        key: typing___Text = ...

        @property
        def value(self) -> type___IdentifiedNode: ...

        def __init__(self,
            *,
            key : typing___Optional[typing___Text] = None,
            value : typing___Optional[type___IdentifiedNode] = None,
            ) -> None: ...
        def HasField(self, field_name: typing_extensions___Literal[u"value",b"value"]) -> builtin___bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"key",b"key",u"value",b"value"]) -> None: ...
    type___NodesEntry = NodesEntry

    class EdgesEntry(google___protobuf___message___Message):
        DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
        key: typing___Text = ...

        @property
        def value(self) -> type___EdgeList: ...

        def __init__(self,
            *,
            key : typing___Optional[typing___Text] = None,
            value : typing___Optional[type___EdgeList] = None,
            ) -> None: ...
        def HasField(self, field_name: typing_extensions___Literal[u"value",b"value"]) -> builtin___bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"key",b"key",u"value",b"value"]) -> None: ...
    type___EdgesEntry = EdgesEntry


    @property
    def nodes(self) -> typing___MutableMapping[typing___Text, type___IdentifiedNode]: ...

    @property
    def edges(self) -> typing___MutableMapping[typing___Text, type___EdgeList]: ...

    def __init__(self,
        *,
        nodes : typing___Optional[typing___Mapping[typing___Text, type___IdentifiedNode]] = None,
        edges : typing___Optional[typing___Mapping[typing___Text, type___EdgeList]] = None,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"edges",b"edges",u"nodes",b"nodes"]) -> None: ...
type___IdentifiedGraph = IdentifiedGraph

class MergedGraph(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    class NodesEntry(google___protobuf___message___Message):
        DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
        key: typing___Text = ...

        @property
        def value(self) -> type___MergedNode: ...

        def __init__(self,
            *,
            key : typing___Optional[typing___Text] = None,
            value : typing___Optional[type___MergedNode] = None,
            ) -> None: ...
        def HasField(self, field_name: typing_extensions___Literal[u"value",b"value"]) -> builtin___bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"key",b"key",u"value",b"value"]) -> None: ...
    type___NodesEntry = NodesEntry

    class EdgesEntry(google___protobuf___message___Message):
        DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
        key: typing___Text = ...

        @property
        def value(self) -> type___MergedEdgeList: ...

        def __init__(self,
            *,
            key : typing___Optional[typing___Text] = None,
            value : typing___Optional[type___MergedEdgeList] = None,
            ) -> None: ...
        def HasField(self, field_name: typing_extensions___Literal[u"value",b"value"]) -> builtin___bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"key",b"key",u"value",b"value"]) -> None: ...
    type___EdgesEntry = EdgesEntry


    @property
    def nodes(self) -> typing___MutableMapping[typing___Text, type___MergedNode]: ...

    @property
    def edges(self) -> typing___MutableMapping[typing___Text, type___MergedEdgeList]: ...

    def __init__(self,
        *,
        nodes : typing___Optional[typing___Mapping[typing___Text, type___MergedNode]] = None,
        edges : typing___Optional[typing___Mapping[typing___Text, type___MergedEdgeList]] = None,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"edges",b"edges",u"nodes",b"nodes"]) -> None: ...
type___MergedGraph = MergedGraph