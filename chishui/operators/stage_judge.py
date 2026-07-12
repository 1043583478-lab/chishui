"""StageJudge · 阶段判断与趋势推演

Kernel #3 · 前置: contradict · 位置: 管道第三站
"""

from kernel.interfaces import operator


@operator(position=3, requires=['contradict'], enables=['concentrate', 'align', 'execute'], kernel=True)
def stage_judge(contradiction_map: str, time_facts: str) -> str:
    """判断当前处于持久战的哪个阶段，推演趋势轨迹。

    这张算符回答:
    1. 旧打法开始失灵时，现在还在旧阶段、进入过渡带，还是已进入收口期
    2. 哪些因素随时间增强，哪些随时间衰减
    3. 从全部因素的交互作用推导轨迹——不是单因外推

    运行步骤:
    1. 列出所有矛盾因素的时间趋势——哪些在增强？哪些在削弱？
    2. 分析全部因素的交互作用。单因论导致错误: 只看强弱→亡国论；只看进步→速胜论
    3. 判断当前所处阶段:
       - 战略防御: 敌强我弱。保存实力，建根据地，不决战
       - 战略相持: 力量对比开始变化，最难也最决定性
       - 战略反攻: 我强敌弱。集中优势，各个歼灭
    4. 区分量的损失和质的积累——第一阶段在输地盘但赢经验
    5. 推演趋势轨迹——不只判断现在在哪，还判断往哪走
    6. 识别转段信号

    元判断（必须先做）:
    - 战争模式: 生死攸关、资源匮乏、对手强大 → 用三阶段框架
    - 耕种模式: 稳定成长、日常积累 → 不用三阶段框架，切换算子

    常见误判:
    - 把早期量的损失误读为必败证据
    - 以为自己已在反攻，其实还在防御——然后把自己打垮
    - 速胜论和亡国论犯的是同一个错误: 片面性

    跨文明验证:
    库恩: 科学革命的结构 · 克劳塞维茨: 战争论 · 克里斯滕森: 颠覆式创新 · 论持久战

    输出格式:
    ```json
    {
      "mode": "war/farming",
      "stage": "defense/stalemate/counterattack",
      "growing_factors": [{"factor": "...", "trend": "accelerating/steady"}],
      "declining_factors": [{"factor": "...", "trend": "decelerating/steady"}],
      "quantitative_losses": ["量的损失"],
      "qualitative_gains": ["质的积累"],
      "trend_trajectory": "往哪个方向走",
      "transition_signals": ["转段信号1"],
      "mode_error_risk": "如果模式判断错了，最大的风险是..."
    }
    ```
    """
