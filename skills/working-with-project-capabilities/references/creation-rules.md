# 新 Capability 创建规则（正式版）

**日期**：2026-03-20  
**适用范围**：使用 capability 文档作为当前真相来源的项目

---

## 1. 目标

本规则用于定义：当项目需要新增 capability 时，agent 应如何判断、创建、初始化并纳入后续维护流程。

本规则同时适用于：
- 已有 capability 的项目
- 完全空白的项目

---

## 2. 创建判断规则

### 2.1 应创建新 capability 的情况

满足以下任一情况时，应创建新 capability：
- 当前需求无法稳定归入已有 capability
- 新需求具有独立入口、独立规则、独立影响面
- 已有 capability 文档已无法清晰承载新增行为
- 预计后续会独立演化、独立维护
- 当前项目尚无 capability 文档，但需求已形成独立行为闭环

### 2.2 不应创建新 capability 的情况

以下情况不应创建新 capability：
- 只是已有 capability 的新增入口
- 只是已有 capability 的边界条件
- 只是 shared-rule 的新增应用点
- 只是局部 UI 差异，不形成独立行为闭环
- 只是已有 capability 的实现细节变化

---

## 3. 空白场景规则

当项目处于完全空白场景时，不应默认自动引入 capability 机制。

只有在以下条件成立时，才允许创建首个 capability：
- 用户已明确确认当前仓库要采用 capability 机制
- 当前需求已形成独立行为闭环，值得进入 capability 治理

执行顺序为：
1. 明确询问并确认：是否为当前仓库启用 capability 机制
2. 识别当前需求对应的首个能力边界
3. 创建首版 capability 文档
4. 用临时脚本生成临时 capability-index 内容
5. 再按 capability workflow 进入后续维护

要求：
- 未确认启用前，不得自动创建首个 capability
- 一旦确认启用，不得因为“没有现成 capability”而退回全仓盲读模式
- 不得等待 capability 体系完整后再开始
- 首个 capability 可以偏轻，但结构必须完整

---

## 4. 创建后的最小初始化要求

新 capability 首版至少包含：
- `Quick Read`
- `Capability Summary`
- `Entries`
- `Current Rules`
- `Impact Surface`
- `Shared Rules Dependency`

如有未确认内容，增加：
- `Uncertainties`
- `待验证项`（如项目当前需要）

要求：
- 首版允许不完备
- 但不得缺少结构骨架
- 不得把未验证内容写成当前规则

---

## 5. 创建后的纳入流程

创建完成后，应立即进入以下流程：
1. 将 capability 文档纳入当前区
2. 通过临时或正式 capability-index 机制让其可被发现
3. 在后续修改中按 capability workflow 读取与维护
4. 当部分内容失效时，移出当前区并归档

---

## 6. 与 shared-rule 的边界

新 capability 创建时，默认规则留在 capability 内。

仅当出现以下信号时，才考虑上提 shared-rule：
- 多个 capability 同时依赖该规则
- 一处规则修改联动多个 capability
- 多份 capability 文档出现重复规则文本
- 该规则本质上描述的是共享机制

在未出现这些信号前，不得过早上提。

---

## 7. 硬规则

- 不得默认假设 capability 已存在。
- 不得在项目空白时未经确认就引入 capability 机制。
- 一旦确认启用，不得因为项目空白而跳过 capability 结构。
- 不得把局部入口变化误判为新 capability。
- 不得把未验证内容写入 `Current Rules`。
- 不得在新 capability 创建后跳过发现层接入。

---

## 8. 完成标志

一次新 capability 创建，满足以下条件才算完成：
- 已完成是否创建的判断
- 已产出首版 capability 文档
- 文档结构完整
- 未确认内容已显式标记
- 已进入临时或正式 capability-index 发现链路

---

## 9. 定位

本规则是 capability workflow 的补充规则。

其职责不是定义单个 capability 的内容，而是定义 capability 从无到有的建立条件与最小落库流程。



## Capability Index Rule

`capability-index` is a discovery layer only.

It should contain only the minimum fields needed to find the right capability, such as:
- id
- name
- summary
- entry points
- shared_with
- path

Do not put Current Rules, Impact Surface, or long module lists into the index.
