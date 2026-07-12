"""Integration tests for the 8-operator pipeline — dependencies, chains, mode routing."""

import pytest
from operators import *
from kernel.interfaces import all as all_operators


@pytest.fixture
def ops():
    """All 8 operators must be registered by the operators package import."""
    o = all_operators()
    assert len(o) == 8, f"Expected 8, got {len(o)}: {list(o.keys())}"
    return o


class TestDependencyChain:
    def test_all_requires_exist(self, ops):
        for name, op in ops.items():
            for req in op.requires:
                assert req in ops, f"{name} requires '{req}', not registered"

    def test_dependency_positions_ordered(self, ops):
        for name, op in ops.items():
            for req in op.requires:
                assert ops[req].position < op.position, \
                    f"{name} (pos {op.position}) requires {req} (pos {ops[req].position})"

    def test_investigate_has_no_requires(self, ops):
        assert ops["investigate"].requires == []

    def test_review_loops_back_to_investigate(self, ops):
        assert "investigate" in ops["review"].enables
        assert "contradict" in ops["review"].enables
        assert "stage_judge" in ops["review"].enables

    def test_all_positions_1_through_8(self, ops):
        positions = [op.position for op in ops.values()]
        assert sorted(positions) == [1, 2, 3, 4, 5, 6, 7, 8]


class TestKernelApplicationSplit:
    def test_first_four_are_kernel(self, ops):
        kernel = [n for n, op in ops.items() if op.kernel]
        assert kernel == ["investigate", "contradict", "stage_judge", "concentrate"]

    def test_last_four_are_application(self, ops):
        app = [n for n, op in ops.items() if not op.kernel]
        assert app == ["align", "communicate", "execute", "review"]


class TestMinimumViableChains:
    def test_investigate_enables_contradict(self, ops):
        assert "contradict" in ops["investigate"].enables
        assert ops["contradict"].requires == ["investigate"]

    def test_can_simulate_minimum_chain(self, ops):
        def mock(p):
            return "ok"
        r1 = ops["investigate"].run(mock, situation="x", goal="y")
        r2 = ops["contradict"].run(mock, situation="x", calibrated_objects=r1)
        assert r1 == r2 == "ok"

    def test_contradict_requires_investigate(self, ops):
        assert ops["contradict"].requires == ["investigate"]


class TestModeRouting:
    WAR = ["contradict", "stage_judge", "concentrate"]
    FARMING = ["investigate", "execute", "review"]

    def test_war_chain_all_kernel(self, ops):
        for name in self.WAR:
            assert ops[name].kernel, f"{name} should be kernel"

    def test_war_chain_enables_form_path(self, ops):
        for i in range(len(self.WAR) - 1):
            assert self.WAR[i + 1] in ops[self.WAR[i]].enables, \
                f"{self.WAR[i]} does not enable {self.WAR[i + 1]}"

    def test_farming_chain_all_exist(self, ops):
        for name in self.FARMING:
            assert name in ops


class TestEdgeCases:
    def test_registry_key_matches_operator_name(self, ops):
        for key, op in ops.items():
            assert key == op.name, f"key '{key}' != name '{op.name}'"

    def test_no_duplicate_enables(self, ops):
        for name, op in ops.items():
            assert len(op.enables) == len(set(op.enables)), \
                f"{name} duplicate enables: {op.enables}"
