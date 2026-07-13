# 赤水 · Chishui

> 这是一个简单的人类思维模型+AI推理框架。
通过拆解毛选七册，得到超过14种skills，结合问题拆解+信息调查+矛盾分析+行动指引，为提问者提供解决问题的对策以及方法。
这是一个严格意义来说和模型无关的推理内核。

## 六层架构

```
🗣️ Layer 5: Voice      — 教员语言风格。底层做分析，顶层说话。
🔄 Layer 4: Dialogue    — 五阶段对话 + 六步连环追问 + 五错误模式检测。
🔗 Layer 3: Pipeline    — 8 算符链，不可跳步，提问预算递减，澄清闭合才进分析。
⚙️ Layer 2: Operators   — 每个算符是 typed Python pseudo-tool，docstring 即 LLM 执行规范。
📐 Layer 1: Grammar     — 算符间依赖关系由各算子装饰器参数定义（requires/enables/position）。
📖 Layer 0: Ontology    — ontology.md 共享概念词汇表。定义，不执行。变化极慢。
```

## 8 算符

| # | 算符 | 类型 | 前置 | 一句话 |
|---|------|------|------|--------|
| 1 | `investigate` | Kernel | 无 | 结论产生于调查的末尾 |
| 2 | `contradict` | Kernel | investigate | 复杂局面的解剖刀 |
| 3 | `stage_judge` | Kernel | contradict | 持久战三阶段科学推演 |
| 4 | `concentrate` | Kernel | stage_judge | 选唯一方向，造局部绝对优势 |
| 5 | `align` | Application | contradict + stage_judge | 把朋友搞多，把敌人搞少 |
| 6 | `communicate` | Application | align | 有理有利有节 |
| 7 | `execute` | Application | concentrate + communicate | 弹钢琴，中心工作只有一个 |
| 8 | `review` | Application | execute → loop | 实践→认识→再实践→再认识 |

## 关键设计决策

**算符是代码，不是文档。** 每个算符是一个 typed Python 函数，docstring 就是 LLM 可解释的执行规范。

**Interface/Implementation 分离。** 算符的签名稳定，实现可替换——换底层 LLM 只需换 `run()` 传入的 `llm_fn`。

**Kernel 4 + Application 4。** Kernel 是跨文明收敛的通用推理原语，变化极慢。Application 是 Kernel 在特定场景的组合展开。

**管道刚性 + 对话柔性。** 分析时走刚性管道（不可跳步），对话时走追问引擎（反问、追问、把选择权还给用户）。两套逻辑同时运行。

## 项目结构

```
chishui/
├── SKILL.md               # 技能入口 + 读取顺序
├── README.md              # 本文件
├── ontology.md            # 共享概念词汇表
├── book_overview.md       # 毛选整书分析
├── mental_models.md       # 12 个毛选心智模型详释
├── kernel/
│   └── interfaces.py      # @operator 装饰器 + 注册表 + 执行器
├── operators/
│   ├── __init__.py
│   └── [8 个算符].py       # investigate, contradict, stage_judge, concentrate,
│                          #   align, communicate, execute, review
├── pipeline/
│   └── protocol.md        # 澄清协议 + 三段响应格式
├── protocols/
│   ├── dialogue.md        # 五阶段对话 + 连环追问 + 教员口吻 + 错误模式
│   ├── chaiju.md          # 四步拆局工作法
│   └── html_report.md     # HTML 报告生成规范
├── app/
│   ├── kernel.html        # 单文件 Web 终端
│   ├── mao_quotes.js      # 50 条毛选语录
│   └── api_config.json    # API Key 配置模版
```

## 一句话

**Kernel changes very slowly. Models change rapidly. Operators are permanent. LLMs are runtime.**

"把理论当箭，把现实当靶。"
