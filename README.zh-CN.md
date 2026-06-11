# Agent Governance Skills

一组可复用的 Codex skills，用于让 agent 的工作持续对齐项目中的稳定真相来源。

## Skills

### `doc-entropy-governance`

当文档系统已经无法给读者或 agent 提供安全的当前真相路径时使用。

典型场景：

- 多份文档看起来都像同一主题的权威来源。
- 入口文档把读者引向过期或冲突内容。
- roadmap、计划、归档、工作记录混在一起承担多个职责。
- 需要清理文档治理问题，但不能自动猜测语义权威。

这个 skill 偏向低风险治理清理：能机械修复的直接修复，不能选择真相但能降低误导暴露的先安全隔离，真正需要人类判断的权威问题再集中交给维护者决策。

### `working-with-project-capabilities`

当项目已经使用 capability 文档，或维护者明确决定引入 capability 机制时使用。

典型场景：

- 行为变更需要和已有 capability 文档保持一致。
- 新行为需要形成稳定的能力边界。
- capability 文档和代码实现需要一起维护。
- 需要生成临时 capability index，让当前能力文档可被发现。

这个 skill 会在空白项目中引入 capability 机制前先询问确认，避免把治理机制强行塞进不需要它的仓库。

## 推荐工作流

对于较大的仓库，建议把这些 skills 和 `codegraph` 这类代码结构探索工具配合使用。代码图可以帮助确认真实入口、消费者、所有权边界和依赖影响面，避免把未经验证的判断写进当前真相文档。

涉及实现变更时，推荐使用 TDD 流程：

1. 先用聚焦的失败测试描述期望行为。
2. 再实现刚好能让测试通过的生产代码。
3. 行为被测试保护后再做重构。
4. 验证代码后，再更新相关 capability 或治理文档。

这样可以让文档更新建立在证据上，而不是建立在推测上。

## 安装

把需要的 skill 目录复制到 Codex skills 目录：

```powershell
Copy-Item .\skills\doc-entropy-governance $env:USERPROFILE\.codex\skills\doc-entropy-governance -Recurse
Copy-Item .\skills\working-with-project-capabilities $env:USERPROFILE\.codex\skills\working-with-project-capabilities -Recurse
```

如果只需要其中一个，可以只复制对应目录。

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
