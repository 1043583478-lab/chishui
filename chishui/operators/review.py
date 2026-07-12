"""Review · 实践检验与纠偏复盘

Application #8 · 前置: execute · 位置: 管道终点 → 回流入口

回流目标: investigate / contradict / stage_judge
"""

from kernel.interfaces import operator


@operator(position=8, requires=['execute'],
          enables=['investigate', 'contradict', 'stage_judge'], kernel=False)
def review(action_result: str, original_judgment: str) -> str:
    """一轮行动跑完后，让结果真正回流成再判断——不只要情绪总结或自动胜利论。

    这张算符回答:
    1. 执行结果和原始判断之间哪里一致、哪里偏离
    2. 是执行问题（方案对但没做好）还是判断问题（方案本身不对）
    3. 应该回流到哪个算符重开分析

    运行步骤:
    1. 放下情绪包袱再启动分析——"放下包袱，开动机器"
    2. 对照执行前的判断和实际结果——哪里一致，哪里偏离
    3. 区分: 执行问题（方案对但没做好）or 判断问题（方案本身不对）
    4. 如果是判断问题 → 回溯到对应算符:
       主要矛盾错了 → contradict · 阶段错了 → stage_judge
       对象校准错了 → investigate
    5. 用 16 字算法提炼: 去粗取精、去伪存真、由此及彼、由表及里
    6. 形成修正方案: 保留什么、调整什么、放弃什么
    7. 预期: 第一次几乎一定不对——这是正常的
    8. 决定回流方向

    不能用的场景:
    - 不可重复的一次性事件（实践—认识循环不成立）
    - 纯形式领域（数学、逻辑——真理验证不通过实践结果）

    输出格式:
    ```json
    {
      "comparison": {
        "matched": ["判断正确的部分"],
        "deviated": ["偏离的部分"],
        "unexpected": ["完全意外"]
      },
      "error_type": "execution_error/judgment_error/mixed",
      "root_cause_operator": "追溯到哪个算符的判断错误",
      "correction_vector": {
        "keep": ["保留什么"],
        "adjust": ["调整什么"],
        "abandon": ["放弃什么"]
      },
      "loopback_target": "investigate/contradict/stage_judge",
      "loopback_reason": "为什么回到这个算符",
      "sixteen_chars": "去粗取精→... 去伪存真→... 由此及彼→... 由表及里→...",
      "baggage_check": "是否已放下情绪包袱再分析"
    }
    ```
    """
