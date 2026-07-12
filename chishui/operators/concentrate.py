"""Concentrate · 力量对比与资源集中

Kernel #4 · 前置: stage_judge · 位置: 管道第四站
"""

from kernel.interfaces import operator


@operator(position=4, requires=['stage_judge'], enables=['align', 'execute'], kernel=True)
def concentrate(stage_vector: str, resources: str) -> str:
    """资源有限时，选唯一进攻方向，创造局部绝对优势，接受其他方向暂时损失。

    这张算符回答:
    1. 支点和底盘在哪里——力量最小但效果最大的点
    2. 唯一进攻方向是什么——集中压倒性力量
    3. 哪里该守、该压、该收

    运行步骤:
    1. 列出所有可用力量和资源
    2. 识别支点——力量最小但效果最大的点
    3. 选择唯一进攻方向: 敌之较弱者、较少援助者、地形有利者
    4. 在这一点上集中绝对优势（压倒性力量）
    5. 其他所有方向只用最小力量牵制——接受局部损失
    6. 区分底盘（必须守的）、支点（必须攻的）、亮点（锦上添花）
    7. 制定转用兵力的顺序: 全歼此点后，转用兵力于下一个目标

    常见误判:
    - "弹钢琴"不是同时推进——十个指头都动，但不能同时按下去
    - 分散的原因是恐惧——不敢让任何地方出问题
    - 战略上接受弱势 ≠ 每个地方都弱——在具体行动点必须压倒性优势

    注意: 对"数量优势"的依赖假设。很多创造活动质量不由数量决定——
    10 个平庸工程师不会比 1 个天才更"强"。

    跨文明验证:
    兵力集中原则 · 核心竞争力 · 刻意练习 · 集中优势兵力(1936)

    输出格式:
    ```json
    {
      "available_forces": ["力量1", "力量2"],
      "fulcrum": "支点（最大杠杆点）",
      "main_direction": "唯一进攻方向",
      "why_this_direction": "为什么选它",
      "force_allocation": {
        "main_attack": "集中多少力量",
        "containment": "牵制多少力量",
        "defense_baseline": "守底线多少力量"
      },
      "accepted_losses": ["接受的暂时损失1"],
      "base_positions": ["必须守的根据地"],
      "rotation_sequence": "全歼此点后的下一个目标",
      "war_mode_reminder": "战略持久 + 战役速决，两层同时成立"
    }
    ```
    """
