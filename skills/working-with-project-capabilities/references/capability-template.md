# 正式 Capability 初始化模板（正式版）

**日期**：2026-03-20  
**适用范围**：使用 capability 文档作为当前真相来源的项目

---

## 1. 模板定位

本模板用于创建正式 capability 的首版文档。

目标：

- 让新 capability 从创建当天起即可进入维护流程
- 让 capability 从首版起即可被发现、被读取、被更新
- 让文档从首版起即可接受验收标准检查

本模板面向“首版可用”，不要求首版即完备。

---

## 2. 使用原则

- 先保证结构完整，再逐步补全内容
- 只记录当前真相，不记录历史讨论
- 未确认内容必须显式标记
- 首版允许偏轻，但不得缺少骨架
- 首版创建后应立即进入 capability-index 发现链路

---

## 3. 模板正文

```markdown
# {capability-id}

## Quick Read

- **id**: `{capability-id}`
- **name**: {capability-name}
- **summary**: {one-sentence purpose}
- **scope**: {what is included; what is excluded}
- **entry_points**:
  - {entry-point-1}
- **shared_with**:
  - {shared-rule-or-none}
- **check_on_change**:
  - {check-item-1}
- **last_verified**: {YYYY-MM-DD}

---

## Capability Summary

{3-6 lines describing responsibility, boundary, and core behavior}

---

## Entries

| Entry        | Trigger               | Evidence | Notes  |
| ------------ | --------------------- | -------- | ------ |
| {entry-name} | {how it is triggered} | `{path}` | {note} |

---

## Current Rules

### CR-001: {rule-name}

{current rule}

**Evidence**: `{path}:{line-or-range}`

---

## Impact Surface

| Area   | What to check                 | Evidence |
| ------ | ----------------------------- | -------- |
| {area} | {regression or linkage check} | `{path}` |

---

## Shared Rules Dependency

| Shared Rule           | Dependency          | Lifted      |
| --------------------- | ------------------- | ----------- |
| {shared-rule-or-none} | {dependency detail} | {yes-or-no} |

---

## Uncertainties

- {uncertainty-or-none}

---

## Known Consumers

| Consumer        | Usage                         | Evidence |
| --------------- | ----------------------------- | -------- |
| {consumer-name} | {how it uses this capability} | `{path}` |

---

## Archive Pointer

- {archive-pointer-or-none}
```

---

## 4. 各区块填写约束

### 4.1 Quick Read

要求：

- 可在极短时间内完成筛选
- 不写大段正文
- 必须体现入口、范围、联动检查点

### 4.2 Capability Summary

要求：

- 只描述当前能力边界
- 不写实现细节堆砌
- 不写历史演化过程

### 4.3 Entries

要求：

- 列出现存入口
- 区分触发入口、命令分发点、统一提交点（如存在）
- 不得遗漏已存在入口

### 4.4 Current Rules

要求：

- 只写当前真实规则
- 每条规则应有证据位置
- 未验证规则不得写入此区

### 4.5 Impact Surface

要求：

- 必须能转化为修改后的检查清单
- 不写空泛描述
- 应覆盖多入口、边界场景、共享机制联动

### 4.6 Shared Rules Dependency

要求：

- 默认写当前依赖
- 不因“未来可能复用”而提前上提
- 未达到 shared-rule 条件时写明“否”

### 4.7 Uncertainties

要求：

- 任何未确认内容放在此处
- 不得混入 Current Rules

### 4.8 Known Consumers

要求：

- 列出主要使用该能力的模块/组件
- 包括 import 该能力的文件、调用该能力 API 的组件
- 便于变更影响分析
- 无消费者时写 "None identified"

### 4.9 Archive Pointer

要求：

- 仅指向已退出 current 区的内容
- 不在此处重复写正文

---

## 5. 首版通过标准

一份首版 capability 文档，至少满足以下条件：

- 结构完整
- Quick Read 可筛选
- Entries 可发现
- Current Rules 仅写当前真相
- 证据位置可定位
- 未确认内容已显式标记
- 可被 capability-index 收录
- last_verified 已填写
- Known Consumers 已识别（可为空）

---

## 6. 定位

本模板是“正式 capability 首版初始化模板”，不是最终完备模板。

其目标是让 capability 尽快进入可维护状态，而不是在创建当次追求信息穷尽。
