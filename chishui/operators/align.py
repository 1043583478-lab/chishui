"""Align · 联盟边界与关系分层

Application #5 · 前置: contradict + stage_judge · 位置: 管道第五站
"""

from kernel.interfaces import operator


@operator(position=5, requires=['contradict', 'stage_judge'],
          enables=['communicate', 'execute'], kernel=False)
def align(force_distribution: str, key_players: str) -> str:
    """多方局势里判断谁是主体、谁可联、谁可争取、谁必须设边界。

    这张算符回答:
    1. 各方利益、恐惧、依赖、底线
    2. 谁是坚定盟友、谁是中间力量、谁是主要对手
    3. 敌我矛盾 vs 内部矛盾——混淆这两类是最大错误

    运行步骤:
    1. 列出所有相关方，标注每方的利益、恐惧、依赖、底线
    2. 分清三类: 坚定盟友（根本利益一致）、中间力量（可争取）、
       主要对手（根本利益对立）
    3. 区分敌我矛盾和内部矛盾
    4. 判断可团结对象: 在主要矛盾上一致的人，不要求所有问题上一致
    5. 画出边界: 对谁让步、让到什么程度、什么不能让步
    6. 决定对每类对象的策略: 团结、争取、中立、斗争、设边界

    关键原则:
    - 把朋友搞得多多的，把敌人搞得少少的
    - 不要四面出击: 弱势时克制树敌
    - 敌友关系随阶段变化——今天的盟友可能是明天的中间力量

    输出格式:
    ```json
    {
      "parties": [
        {"name": "...", "interests": "...", "fears": "...",
         "dependencies": "...", "bottom_line": "..."}
      ],
      "classification": {
        "allies": [{"name": "...", "basis": "根本利益一致在..."}],
        "middle_forces": [{"name": "...", "basis": "在主要矛盾上有交集"}],
        "opponents": [{"name": "...", "basis": "根本利益对立"}]
      },
      "contradiction_type": {
        "enemy_contradictions": ["敌我矛盾"],
        "internal_contradictions": ["内部矛盾"]
      },
      "strategies": {
        "unite": ["团结谁"],
        "win_over": ["争取谁"],
        "neutralize": ["中立谁"],
        "resist": ["对抗谁"],
        "set_boundary": ["设边界谁"]
      },
      "boundaries": ["什么不能让步"],
      "dont_strike_all_directions_check": "是否犯了四面出击的错误"
    }
    ```
    """
