"""Execute · 执行路线与组织换挡

Application #7 · 前置: concentrate + communicate · 位置: 管道第七站
"""

from kernel.interfaces import operator


@operator(position=7, requires=['concentrate', 'communicate'], enables=['review'], kernel=False)
def execute(communication_strategy: str, force_distribution: str) -> str:
    """把方向翻成动作链，安排好节奏——弹钢琴，中心工作只有一个。

    这张算符回答:
    1. 旧口径、旧规则、旧节奏接不住新阶段时，怎么把判断接成动作链
    2. 多条线怎么安排节奏——中心工作只有一个，其他配合
    3. 怎么"抓紧"——抓而不紧等于不抓

    运行步骤:
    1. 把路线翻成可执行动作链——每步: 做什么、谁做、何时完成、观察什么信号
    2. 确定中心工作——只有一个。其他都是配合
    3. "抓紧": 伸着巴掌抓不住，把手握起来但样子像抓还是抓不住
    4. 区分不同区域节奏: 成熟区可普推，新区先试点
    5. 安民告示——事先通知，让大家准备
    6. 每个动作带观察点: 做完后看什么信号判断方向对不对
    7. 设定退出条件: 什么信号表明需要切换路线或回退

    常见误判:
    - 把弹钢琴理解成 multitasking——不是同时推进
    - 执行计划太刚性，没有观察点和退出条件
    - 对所有区域用同一个节奏

    输出格式:
    ```json
    {
      "center_of_gravity": "唯一中心工作",
      "action_chain": [
        {"step": 1, "action": "...", "owner": "...", "deadline": "...",
         "observation_signal": "...", "if_signal_absent": "..."}
      ],
      "supporting_actions": ["配合动作1", "配合动作2"],
      "regional_pacing": {
        "mature_areas": "普推节奏",
        "new_areas": "试点节奏"
      },
      "advance_notice": "安民告示: 事先通知什么",
      "exit_conditions": ["触发回退的信号1"],
      "piano_metaphor_check": "十指都动，中心工作有没有被淹没？"
    }
    ```
    """
