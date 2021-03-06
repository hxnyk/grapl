import unittest
from typing import Callable, Optional

import hypothesis
import pytest
from analyzer_executor_lib.analyzer_executor import AnalyzerExecutor
from hypothesis import strategies as st

SAMPLE_ADDR = "localhost"
SAMPLE_PORT = "12345"

ReturnsAnalyzerExecutor = Callable[..., AnalyzerExecutor]

NonemptyStringStrategy = st.text(min_size=3, max_size=64)


class AnalyzerExecutorCacheDeleters:
    def __init__(self, analyzer_executor: AnalyzerExecutor) -> None:
        self.analyzer_executor = analyzer_executor

    def delete_msg_cache(self, file: str, node_key: str, msg_id: str) -> None:
        event_hash = self.analyzer_executor.to_event_hash((file, node_key, msg_id))
        self.analyzer_executor.message_cache.delete(event_hash)

    def delete_hit_cache(self, file: str, node_key: str) -> None:
        event_hash = self.analyzer_executor.to_event_hash((file, node_key))
        self.analyzer_executor.hit_cache.delete(event_hash)


@pytest.fixture
def executor_fixture(monkeypatch) -> ReturnsAnalyzerExecutor:
    def _AnalyzerExecutorSingleton(
        stub_env: bool = False,
        env_addr: Optional[str] = None,
        env_port: Optional[str] = None,
    ) -> AnalyzerExecutor:
        with monkeypatch.context() as mp:
            if stub_env:
                if env_addr:
                    mp.setenv("MESSAGECACHE_ADDR", env_addr)
                    mp.setenv("HITCACHE_ADDR", env_addr)
                else:
                    mp.delenv("MESSAGECACHE_ADDR", raising=False)
                    mp.delenv("HITCACHE_ADDR", raising=False)

                if env_port:
                    mp.setenv("MESSAGECACHE_PORT", env_port)
                    mp.setenv("HITCACHE_PORT", env_port)
                else:
                    mp.delenv("MESSAGECACHE_PORT", raising=False)
                    mp.delenv("HITCACHE_PORT", raising=False)

            # force singleton to reinitialize,
            # this should be idempotent?
            AnalyzerExecutor._singleton = None
            return AnalyzerExecutor.singleton()

    return _AnalyzerExecutorSingleton


@pytest.mark.integration_test
def test_connection_info(executor_fixture: ReturnsAnalyzerExecutor) -> None:
    """
    Ensures exceptions are raised for incomplete connection info.
    """

    with pytest.raises(ValueError):
        ae = executor_fixture(stub_env=True, env_addr=SAMPLE_ADDR, env_port=None)

    with pytest.raises(ValueError):
        ae = executor_fixture(stub_env=True, env_addr=None, env_port=SAMPLE_PORT)

    with pytest.raises(ValueError):
        ae = executor_fixture(stub_env=True, env_addr=None, env_port=None)


@hypothesis.given(
    k1=NonemptyStringStrategy,
    k2=NonemptyStringStrategy,
)
@hypothesis.settings(
    # Doesn't like the Pytest fixture mixed with Hypothesis givens.
    # It's okay, since the fixture just returns a function.
    suppress_health_check=[hypothesis.HealthCheck.function_scoped_fixture]
)
@pytest.mark.integration_test
def test_hit_cache(
    executor_fixture: ReturnsAnalyzerExecutor,
    k1: str,
    k2: str,
) -> None:
    """
    Initializes the AnalyzerExecutor singleton with Redis connection params
    sourced from the environment, expecting hit cache to populate.
    """
    ae = executor_fixture(stub_env=False)

    assert not ae.check_hit_cache(k1, k2)
    ae.update_hit_cache(k1, k2)
    assert ae.check_hit_cache(k1, k2)
    # Clean up, because Hypothesis provides duplicate inputs
    AnalyzerExecutorCacheDeleters(ae).delete_hit_cache(k1, k2)
    assert not ae.check_hit_cache(k1, k2)


@hypothesis.given(
    k1=NonemptyStringStrategy,
    k2=NonemptyStringStrategy,
    k3=NonemptyStringStrategy,
)
@hypothesis.settings(
    # Doesn't like the Pytest fixture mixed with Hypothesis givens.
    # It's okay, since the fixture just returns a function.
    suppress_health_check=[hypothesis.HealthCheck.function_scoped_fixture]
)
@pytest.mark.integration_test
def test_message_cache(
    executor_fixture: ReturnsAnalyzerExecutor,
    k1: str,
    k2: str,
    k3: str,
) -> None:
    """
    Initializes the AnalyzerExecutor singleton with Redis connection params
    sourced from the environment, expecting message cache to populate.
    """
    ae = executor_fixture(stub_env=False)

    assert not ae.check_msg_cache(k1, k2, k3)
    ae.update_msg_cache(k1, k2, k3)
    assert ae.check_msg_cache(k1, k2, k3)
    # Clean up, because Hypothesis provides duplicate inputs
    AnalyzerExecutorCacheDeleters(ae).delete_msg_cache(k1, k2, k3)
    assert not ae.check_msg_cache(k1, k2, k3)
