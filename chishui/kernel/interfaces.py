"""Operator registry via @operator decorator. Operators are LLM prompts — the only runtime is simulate."""

from dataclasses import dataclass, field
from typing import Callable, Optional


_OPERATORS: dict[str, 'Operator'] = {}


@dataclass
class Operator:
    """A reasoning primitive: typed pseudo-tool executable via LLM simulation."""
    name: str
    doc: str
    position: int = 0
    requires: list[str] = field(default_factory=list)
    enables: list[str] = field(default_factory=list)
    kernel: bool = True

    def run(self, llm_fn: Callable, **inputs) -> str:
        """Execute via LLM simulation."""
        prompt = f"执行推理算符: {self.name}\n算符说明: {self.doc}\n输入: {inputs}"
        return llm_fn(prompt)


def operator(position: int = 0, requires: list[str] = None,
             enables: list[str] = None, kernel: bool = True):
    """Decorator: register a Python function as a reasoning operator."""
    def wrapper(func) -> Operator:
        op = Operator(
            name=func.__name__,
            doc=func.__doc__ or '',
            position=position,
            requires=requires or [],
            enables=enables or [],
            kernel=kernel,
        )
        _OPERATORS[func.__name__] = op
        return op
    return wrapper


def all() -> dict[str, Operator]:
    return dict(_OPERATORS)


def get(name: str) -> Optional[Operator]:
    return _OPERATORS.get(name)


def run(name: str, llm_fn: Callable, **inputs) -> str:
    """Execute an operator by name via LLM simulation."""
    op = _OPERATORS[name]
    return op.run(llm_fn, **inputs)
