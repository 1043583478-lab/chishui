"""Full pipeline simulation tests — end-to-end operator chains with mock LLM."""

import pytest
from operators import *
from kernel.interfaces import all as all_operators, get as get_operator, run


@pytest.fixture
def ops():
    o = all_operators()
    assert len(o) == 8
    return o


def mock_llm(prompt: str) -> str:
    op_name = prompt.split('\n')[0].split(': ')[1]
    responses = {
        'investigate':   '对象已校准。结构事实: 团队沟通断裂。',
        'contradict':    '主要矛盾: 名义扁平化 vs 实际无人拍板。',
        'stage_judge':   '当前阶段: 相持。转段信号: 两周无阻塞。',
        'concentrate':   '支点: 周例会制度化。主攻方向: 拍板权归属。',
        'align':         '盟友: 技术负责人。需设边界: 越级汇报者。',
        'communicate':   '策略: 有理有利有节。',
        'execute':       '路线: 明确拍板权→试运行→评估。',
        'review':        '修正: 沟通策略需更早介入。回流: concentrate。',
    }
    return responses.get(op_name, 'ok')


FULL_CHAIN = ['investigate', 'contradict', 'stage_judge', 'concentrate',
              'align', 'communicate', 'execute', 'review']


class TestRegistry:
    def test_eight_operators_registered(self, ops):
        assert len(ops) == 8

    def test_all_kernel_operators_present(self, ops):
        for name in ['investigate', 'contradict', 'stage_judge', 'concentrate']:
            assert name in ops
            assert ops[name].kernel

    def test_all_application_operators_present(self, ops):
        for name in ['align', 'communicate', 'execute', 'review']:
            assert name in ops
            assert not ops[name].kernel

    def test_review_enables_loopback(self, ops):
        enables = ops['review'].enables
        assert 'investigate' in enables
        assert 'contradict' in enables
        assert 'stage_judge' in enables


class TestFullPipeline:
    def test_full_chain_executes_in_order(self, ops):
        context = {}
        for name in FULL_CHAIN:
            result = run(name, mock_llm, situation="团队协作混乱", **context)
            assert result, f"{name} returned empty"
            context[name] = result

    def test_full_chain_all_outputs_differ(self, ops):
        context = {}
        for name in FULL_CHAIN:
            context[name] = run(name, mock_llm, situation="x", **context)
        outputs = list(context.values())
        assert len(set(outputs)) == 8, "all 8 outputs should differ"

    def test_minimum_chain(self, ops):
        r1 = run('investigate', mock_llm, situation="方向迷茫", goal="判断转型")
        r2 = run('contradict', mock_llm, situation="同上", calibrated_objects=r1)
        assert r1 and r2

    def test_war_mode_chain_kernel_only(self, ops):
        for name in ['contradict', 'stage_judge', 'concentrate']:
            assert ops[name].kernel, f"{name} should be kernel for war mode"

    def test_farming_mode_operators_present(self, ops):
        for name in ['investigate', 'execute', 'review']:
            assert name in ops


class TestGetOperator:
    def test_found(self, ops):
        op = get_operator('investigate')
        assert op is not None and op.name == 'investigate'

    def test_not_found(self, ops):
        assert get_operator('nonexistent') is None
