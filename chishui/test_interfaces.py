"""Unit tests for kernel/interfaces.py — Operator, registry, runner."""

import pytest
from kernel.interfaces import Operator, operator, all, get, run, _OPERATORS


class TestOperatorDataclass:
    """Operator data class construction and run behavior."""

    def test_defaults(self):
        op = Operator(name="test", doc="does something")
        assert op.name == "test"
        assert op.doc == "does something"
        assert op.position == 0
        assert op.requires == []
        assert op.enables == []
        assert op.kernel is True

    def test_explicit_values(self):
        op = Operator(name="contradict", doc="analyze", position=2,
                      requires=["investigate"], enables=["stage_judge"], kernel=True)
        assert op.position == 2
        assert op.requires == ["investigate"]
        assert op.enables == ["stage_judge"]

    def test_run_builds_prompt_with_inputs(self):
        op = Operator(name="investigate", doc="调查对象并校准事实", position=1)
        calls = []
        result = op.run(lambda p: calls.append(p) or "done", situation="混乱", goal="理清")
        assert result == "done"
        assert len(calls) == 1
        assert "investigate" in calls[0]
        assert "调查对象并校准事实" in calls[0]
        assert "混乱" in calls[0]

    def test_run_passes_all_keyword_args(self):
        op = Operator(name="t", doc="x")
        result = op.run(lambda p: p, a=1, b=2)
        assert "'a': 1" in result
        assert "'b': 2" in result


class TestRegistry:
    """Operator registration, lookup, and execution via the module-level API."""

    @pytest.fixture(autouse=True)
    def isolated_registry(self):
        """Back up global registry, restore after each test."""
        saved = dict(_OPERATORS)
        _OPERATORS.clear()
        yield
        _OPERATORS.clear()
        _OPERATORS.update(saved)

    def test_decorator_registers_operator(self):
        @operator(position=1, kernel=True)
        def investigate(situation: str, goal: str) -> str:
            """调查对象并校准事实。"""
        assert "investigate" in _OPERATORS
        op = _OPERATORS["investigate"]
        assert op.position == 1
        assert op.kernel is True
        assert "调查对象" in op.doc

    def test_decorator_stores_requires_and_enables(self):
        @operator(position=2, requires=["investigate"], enables=["stage_judge"])
        def contradict(situation: str) -> str:
            """找主要矛盾。"""
        assert _OPERATORS["contradict"].requires == ["investigate"]
        assert _OPERATORS["contradict"].enables == ["stage_judge"]

    def test_all_returns_independent_copy(self):
        @operator()  # noqa
        def a() -> str: """a"""
        @operator()  # noqa
        def b() -> str: """b"""
        result = all()
        assert "a" in result and "b" in result
        result.clear()
        assert "a" in _OPERATORS  # original unaffected

    def test_get_returns_operator_when_found(self):
        @operator()
        def temp_op() -> str: """x"""
        op = get("temp_op")
        assert op is not None
        assert op.name == "temp_op"

    def test_get_returns_none_when_missing(self):
        assert get("nonexistent_xyz") is None

    def test_run_executes_by_name(self):
        @operator()
        def temp_op(situation: str, goal: str) -> str:
            """调查。"""
        result = run("temp_op", lambda p: "simulated", situation="x", goal="y")
        assert result == "simulated"

    def test_run_raises_keyerror_for_unknown(self):
        with pytest.raises(KeyError):
            run("nonexistent", lambda p: "x")

    def test_empty_docstring_handled(self):
        @operator()
        def no_doc() -> str:  # noqa
            pass
        assert _OPERATORS["no_doc"].doc == ""

    def test_none_requires_defaults_to_empty_list(self):
        @operator()
        def f() -> str:  # noqa
            """x"""
        assert _OPERATORS["f"].requires == []

    def test_kernel_false_for_application(self):
        @operator(kernel=False)
        def align() -> str:
            """x"""
        assert _OPERATORS["align"].kernel is False
