"""8 reasoning operators: 4 Kernel + 4 Application."""

from operators.investigate import investigate
from operators.contradict import contradict
from operators.stage_judge import stage_judge
from operators.concentrate import concentrate
from operators.align import align
from operators.communicate import communicate
from operators.execute import execute
from operators.review import review

from kernel.interfaces import all as all_operators
from kernel.interfaces import get as get_operator

__all__ = [
    'investigate', 'contradict', 'stage_judge', 'concentrate',
    'align', 'communicate', 'execute', 'review',
    'all_operators', 'get_operator',
]
