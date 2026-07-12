"""Communicate · 沟通策略与表达治理

Application #6 · 前置: align · 位置: 管道第六站
"""

from kernel.interfaces import operator


@operator(position=6, requires=['align'], enables=['execute'], kernel=False)
def communicate(alliance_map: str, key_judgments: str) -> str:
    """把结构判断翻译成各受众能听懂、能响应、有证据链支撑的说法。

    这张算符回答:
    1. 判断不差但一说就空、一公开就偏时，怎么校准
    2. 对不同对象怎么说——同一套话对所有人通发是最常见错误
    3. 冲突中怎么做到有理、有利、有节

    运行步骤:
    1. 区分受众: 谁需要被说服、谁需要被团结、谁只需被通知
    2. 针对每类受众校准说法——"到什么山上唱什么歌"
    3. 建立证据链: 每个关键判断列出支撑的事实/数据/事件
    4. 如果是外部冲突 → 有理有利有节:
       - 有理（自卫）: 不打第一枪
       - 有利（胜利）: 有把握打赢才打
       - 有节（休战）: 打赢立刻停，主动讲和
    5. 如果是内部反馈 → 团结—批评—团结:
       - 从团结的愿望出发
       - 经过真实的批评
       - 达到新的团结
    6. 检查: 对象能听懂 + 证据链支撑 + 不会被断章取义

    关键区分:
    - 有理有利有节 = 外部冲突的操作规范
    - 团结—批评—团结 = 内部反馈的操作规范
    - 两套逻辑不能混用

    输出格式:
    ```json
    {
      "audiences": [
        {"name": "...", "type": "persuade/unite/inform/boundary",
         "calibrated_message": "...", "evidence_chain": ["证据1"]}
      ],
      "conflict_strategy": {
        "mode": "external_conflict/internal_feedback/neither",
        "justified": "自卫原则: ...",
        "advantageous": "胜利把握: ...",
        "restrained": "休战线: ...",
        "unity_criticism_unity_path": "团结→批评→新团结"
      },
      "evidence_chain": {
        "judgment": "关键判断",
        "supporting_facts": ["事实1", "事实2"],
        "weak_points": ["证据薄弱处"]
      }
    }
    ```
    """
