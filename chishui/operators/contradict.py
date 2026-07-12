"""Contradict · 主要矛盾与结构诊断

Kernel #2 · 前置: investigate · 位置: 管道第二站
"""

from kernel.interfaces import operator


@operator(position=2, requires=['investigate'], enables=['stage_judge', 'concentrate', 'align'], kernel=True)
def contradict(situation: str, calibrated_objects: str) -> str:
    """找出当前局面中真正限制结果的主要矛盾，区分纸面关系和现实控制点。

    这张算符回答三个问题:
    1. 并存的几组冲突里，到底哪一组最限制结果
    2. 当前到底是哪一方、哪一种条件在主导局面
    3. 纸面上的角色安排和现实里的控制点，到底差在哪里

    运行步骤:
    1. 停止把所有问题等权并列，暂停纯道德化定性
    2. 判断局面性质: 结构性冲突、阶段性失配、对象分化，还是局部事件
    3. 区分表层症状和深层结构——查清谁依赖谁、谁受限于谁
    4. 区分纸面关系和现实控制点: 谁名义负责 vs 谁实际拍板
    5. 列出当前并存的几组主要冲突
    6. 找出当前最限制结果的主要矛盾（判别标准: 解决它 → 其他矛盾连带缓解）
    7. 判断哪一方在当前占主导（主要方面）
    8. 识别次要矛盾和局部风险
    9. 判断转化条件: 什么新事实会让主要矛盾移动

    常见误判:
    - 把声音最大或最新发生的问题当成主要矛盾
    - 把"主要方面"理解成道德上更坏的一方
    - 只会报出主要矛盾但说不清它为什么主导

    最小产出:
    - 冲突地图（主导 vs 非主导已区分）
    - 主要矛盾 + 为什么它最限制结果
    - 主要方面 + 为什么当前由它定义局面
    - 纸面关系与现实控制点的差异
    - 转化条件

    跨文明验证:
    黑格尔/马克思辩证法 · TRIZ · 系统思维 · 根本原因分析 · 矛盾论

    输出格式:
    ```json
    {
      "contradiction_map": [
        {"name": "矛盾名称", "type": "structural/phasal/relational/...",
         "principal": true/false, "description": "..."}
      ],
      "principal_contradiction": "最限制结果的矛盾",
      "why_principal": "为什么它主导",
      "principal_aspect": "当前主导方面",
      "paper_vs_reality_gaps": ["名义X vs 实际Y"],
      "secondary_contradictions": ["次要矛盾1"],
      "transformation_conditions": ["转化条件1"],
      "principal_explains_secondaries": true/false
    }
    ```
    """
