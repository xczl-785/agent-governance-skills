# Agent-First Governance Skills

[English README](README.md)

当 agent 开始长期参与项目，真正危险的不是它不会执行单次任务，而是它读错当前真相：把旧计划当现状，把归档当入口，把临时结论当规则，把代码行为和文档边界改散。

这个仓库收集一组可复用的治理型 skills，用来让 agent 在长期项目中持续对齐当前真相、能力边界和已验证证据。

它的目标不是把文档写漂亮，而是让 agent 在长期参与项目时，始终能找到可信的当前真相、理解稳定的能力边界，并基于已验证证据继续工作。这些 skills 重点降低 agent 因文档漂移、权威冲突、入口混乱、历史材料误曝光和行为边界缺失而做错事的概率，让长期运行的 agent 更平稳，也让冷启动 agent 能更快接入项目、读懂上下文并安全开始工作。

## 解决的问题

Agent-first 项目在持续推进后，常见风险不是单点知识缺失，而是项目真相逐渐失去可读性和可维护性：

- 文档、计划和实现开始互相漂移。
- 多份文档看起来都像当前权威来源。
- 入口文档把 agent 引向过期、冲突或职责混杂的材料。
- roadmap、计划、归档、工作记录和临时结论长期堆在一起。
- 行为变更缺少稳定的能力边界，代码和文档无法一起维护。
- 新接入的 agent 需要重新猜测阅读顺序、当前规则和安全修改范围。
- 团队反复依赖一次性 prompt 约束 agent，而不是沉淀可复用的运行机制。

## 如何解决

这个仓库的 skills 不是通用写作模板，而是面向 agent 长期运行的治理机制：

- 建立安全阅读路径：让 agent 先知道从哪里读、什么是当前真相、什么只是历史或参考。
- 显式管理文档权威：发现冲突时不猜测真相，而是区分可自动修复、可安全隔离、需要人类决策。
- 维护能力边界：把行为入口、当前规则、影响面、共享依赖和验证证据放到可发现的位置。
- 支持冷启动接入：让新 agent 能通过稳定入口快速理解项目上下文，而不是全仓盲读。
- 沉淀可复用规则：把一次性协作经验转化为可安装、可迁移、可持续维护的 skill。

## 当前 Skills

### `doc-entropy-governance`

用于治理文档熵增，恢复 agent 和维护者都能安全使用的当前真相路径。

它关注的是文档系统本身是否还可靠：入口是否清楚，权威是否唯一，历史材料是否误暴露，roadmap 和计划是否承担了过多职责。它不会替维护者猜测语义真相，而是把问题分成可自动修复、可安全隔离和需要人类决策三类，优先降低误导风险。

典型使用场景：

- 多份文档看起来都像同一主题的权威来源。
- 入口文档把读者或 agent 引向过期、冲突或职责混杂的材料。
- roadmap、计划、归档和工作记录混在一起，无法判断当前状态。
- 需要清理文档治理问题，但不能安全地自动选择真相。

### `working-with-project-capabilities`

用于在项目已经采用 capability 文档，或维护者明确决定采用该机制时，维护行为变更和能力边界之间的一致性。

这里的 capability 文档不是普通说明文档，而是某个稳定项目能力的当前真相来源：它记录能力边界、入口、当前规则、影响面、共享依赖、消费者和验证证据。这个 skill 的重点是让 agent 在改代码前能找到相关能力边界，改完后能把已验证的当前真相写回文档。

典型使用场景：

- 行为变更需要和已有 capability 文档保持一致。
- 新行为已经形成独立能力边界，需要被稳定维护。
- capability 文档和代码实现需要一起更新。
- 需要生成临时 capability index，让当前能力文档可被发现。

这个 skill 不会在空白项目中自动引入 capability 机制。只有项目已经使用 capability 文档，或用户明确确认要采用该机制时，才会创建或维护相关文档。

## 推荐使用方式

对于较大的仓库，先用代码结构探索工具确认真实入口、消费者、所有权边界和依赖影响面，再把判断写进治理文档或 capability 文档。不要把未经验证的推测写成当前真相。

涉及实现变更时，推荐使用 TDD 流程：

1. 先用聚焦的失败测试描述期望行为。
2. 再实现刚好能让测试通过的生产代码。
3. 行为被测试保护后再做重构。
4. 验证代码后，再更新相关 capability 或治理文档。

如果问题是“agent 读文档会被误导”，优先使用 `doc-entropy-governance`。如果问题是“代码行为变更需要和能力边界同步”，优先使用 `working-with-project-capabilities`。

## 运行规则

通用的 agent-first 协作规则放在 [docs/agent-first-operating-rules.zh-CN.md](docs/agent-first-operating-rules.zh-CN.md)。

这些规则不直接放进某个具体 skill，因为它们描述的是跨 skill 的运行原则。后续如果某组规则形成了明确触发场景、执行循环和输出契约，可以再提升为独立 skill。

## 安装

把需要的 skill 目录复制到你的 agent 工具的 skill 目录：

```powershell
Copy-Item .\skills\doc-entropy-governance <your-skills-dir>\doc-entropy-governance -Recurse
Copy-Item .\skills\working-with-project-capabilities <your-skills-dir>\working-with-project-capabilities -Recurse
```

如果只需要其中一个，可以只复制对应目录。其他支持 skill 指令包的 agent runtime 也可以复用同样的目录内容。

## 目录结构

```text
skills/
  doc-entropy-governance/
    SKILL.md
    examples/
    references/
  working-with-project-capabilities/
    SKILL.md
    agents/
    references/
    scripts/
docs/
  agent-first-operating-rules.zh-CN.md
```

## 发布维护建议

每个 skill 应保持自包含：

- 在 `SKILL.md` 中放触发条件和主流程。
- 在 `references/` 中放可复用的深层指导。
- 在 `scripts/` 中放可执行辅助脚本。
- 在 `examples/` 中放预期输出或使用模式。
- 避免机器本地路径、私有项目名、密钥和不稳定的历史记录。

## License

MIT. See [LICENSE](LICENSE).
