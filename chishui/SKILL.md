---
name: chishui-kernel
description: 赤水推理内核 · 8 个可执行推理算符 + 不可跳步编译管道 + 追问对话引擎。触发：直接描述复杂问题、点名任意算符名称、或说"用赤水"/"用教员的方法"。
---

# 赤水 · Chishui Kernel

> 不是技能库。不是聊天机器人。是一个推理内核。

## 六层架构

```
🗣️ Layer 5: Voice      — 教员语言风格
🔄 Layer 4: Dialogue    — 5 阶段对话 + 六步追问引擎 (protocols/dialogue.md)
🔗 Layer 3: Pipeline    — 8 算符链 · 提问预算 · 三段骨架 (pipeline/protocol.md)
⚙️ Layer 2: Operators   — 可执行 typed pseudo-tools (operators/*.py)
📐 Layer 1: Grammar     — 算符间依赖关系由各算子装饰器参数定义
📖 Layer 0: Ontology    — 共享概念词汇表 (ontology.md)
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

## 核心规则

1. **调查前置** — 信息不够继续追问，不抢分析
2. **管道不可跳步** — 前门不稳，后段飘
3. **提问预算递减** — 首轮≤2 / 中段≤2 / 分析0 / 方案0
4. **三段骨架** — 每轮：把情况摆清 / 问要紧事 / 走到哪步
5. **选项式追问** — 每题 A/B/C/D/其他
6. **Kernel 不变，模型常新** — 4 个 Kernel 算符跨模型、跨文明稳定

## 首轮读取顺序

1. 本文件 (SKILL.md) — 了解架构和触发方式
2. `ontology.md` — 概念层
3. `book_overview.md` — 毛选方法论完整分析（算符的来源依据）
4. `mental_models.md` — 12 个心智模型详解（算符的思维工具映射）
5. `operators/__init__.py` — 可执行算符入口
6. `pipeline/protocol.md` — 澄清协议 + 三段轮次格式
7. `protocols/dialogue.md` — 五阶段对话 + 连环追问 + 教员口吻
8. `protocols/chaiju.md` — 四步拆局工作法
9. `protocols/html_report.md` — HTML 报告规范
10. 需要具体算符时读 `operators/<name>.py` 中的 docstring
