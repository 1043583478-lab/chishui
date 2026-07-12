"""Investigate · 调查研究与对象校准

Kernel #1 · 前置: 无 · 位置: 管道入口
"""

from kernel.interfaces import operator


@operator(position=1, requires=[], enables=['contradict', 'stage_judge', 'communicate'], kernel=True)
def investigate(situation: str, goal: str) -> str:
    """对用户在模糊局面中的叙述做调查研究与对象校准。

    这张算符回答三个问题：
    1. 这件事到底服务谁、影响谁、争取谁、处理谁
    2. 当前被当成"事实"的东西里，哪些只是转述、印象或表面现象
    3. 最小证据入口从哪里进，才不至于靠脑补推进后续判断

    运行步骤:
    1. 暂停现成结论，承认当前对事实和对象的了解可能不完整
    2. 划清对象: 服务谁、争取谁、处理谁、说给谁听、谁在承担代价
    3. 回到对象的真实处境: 利益位置、当前约束、历史形成过程
    4. 建立最小证据入口: 关键样本、现场信号、代表事件——至少占一条
    5. 区分结构事实与局部表象、名义包装、单点情绪
    6. 校验现有判断是否真正对准对象，而不是只对准内部想象

    不适用情形:
    - 当前必须先止血的紧急场景 → 先止损再调查
    - 对象已高度明确且反馈稳定 → 不必上升为系统调查
    - 不能把"先调查"当成无限延期判断的借口

    最小产出:
    - 服务对象、受影响对象、争取对象、非服务对象已区分
    - 结构事实与局部表象已分开
    - 最小证据入口已建立
    - 已能回答"这套动作到底替谁解决问题"

    跨文明验证:
    科学方法 · 福尔摩斯 · 丰田生产方式 · 军事情报 · 贝叶斯推理 · 反对本本主义

    输出格式:
    ```json
    {
      "service_object": "谁是被服务的对象",
      "affected_objects": ["受影响方1", "受影响方2"],
      "target_objects": ["争取对象1"],
      "non_service_objects": ["非服务对象1"],
      "structural_facts": ["结构事实1", "结构事实2"],
      "surface_appearances": ["表面现象1"],
      "evidence_anchors": ["证据锚点1"],
      "remaining_gaps": ["仍待确认1"],
      "can_proceed": true/false
    }
    ```
    """
