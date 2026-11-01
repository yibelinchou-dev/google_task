# Stage 3 — 用户研究（中文版）

**Pipeline**: `pipe_2026-11-01_001`  
**研究时间**: 2026-11-01T13:47:13Z  
**建议**: **建议验证**（置信度：中）

## 面向 Google Tasks「难民」的多列表待办工具

> 帮拥有几十个列表的重度用户恢复快速切列表、归档/搜索，并低摩擦迁出被 iOS 回退折磨的 Google Tasks。

## 市场规模（美元）

- **TAM（总市场）**: $5,000,000,000
- **SAM（可服务市场）**: $800,000,000
- **SOM（首年现实目标）**: $15,000,000

## 目标用户

### Google Tasks 十年重度用户（30–40个列表）

痛点强度 8/10 · 付费意愿 7/10 · 约 500,000 人

- 「我用了 Google Tasks 十多年，一天多次，有30–40个列表」
- 「我现在被迫去找别的东西了」

### 多列表 iPad/iPhone 待办切换者

痛点强度 7/10 · 付费意愿 6/10 · 约 800,000 人

- 「这已经不再高效，我需要找新的了」
- 「作为最大的科技公司，它又笨又不稳定，远不如 gTasks 流畅」

## 现有方案与弱点

| 方案 | 定价 | 主要弱点 |
|------|------|----------|
| Todoist | $0–$5/user/mo (Pro) | 迁几十个 Google Tasks 列表仍偏手工 · 未主打一键替代 Google Tasks |
| Apple 提醒事项 / Things 3 | Free / $49.99 one-time | 提醒事项弱于多列表重度流 · Things 仅苹果生态且日历能力不一 |
| gTasks（第三方客户端） | Freemium / IAP | 仍依赖 Google Tasks 后端与 API 限额 · 无法应对谷歌服务端砍功能 |

## 产品假设

6–8 周 MVP：iOS 优先多列表侧栏、全文搜索、带时间戳归档、Google Tasks 导入与日历重复同步、迁移清单；以列表回退差评为获客钩子，功率用户 $4–8/月或 $40/年。

## 商业判断（V2）

**机会分数**: **3360**（高机会）

| 维度 | 分数 | 说明 |
|------|-----:|------|
| 痛点强度 | 8/10 | |
| 频率 | 8/10 | |
| ROI / 经济影响 | 5/10 | Primarily daily friction minutes for multi-list navigation a |
| 迁移意愿 | 7/10 | 迁移成本=7/10 |
| 付费主体存在 | 8/10 | 付款人：Same individual on personal App Store / subscription card |
| 持续性 | 6/10 | 未知 |
| 竞争（除） | 8/10 | |
| 替代方案质量（除） | 4/10 | |

### 迁移成本

Decade of lists and personal reference data create high sunk cost and Google ecosystem lock-in; learning curve for another task app is moderate if import works.

### 用户现有替代方案

- Horizontal scrolling across many lists
- Using browser Google Tasks for search
- Third-party clients like gTasks still on Google backend
- Manual move to Todoist/Things/Reminders

Workarounds are clumsy; browser search helps but mobile regressions remain; gTasks does not remove Google dependency.

### 付费主体映射

- **使用者**：Individual power user living in Google Tasks daily
- **受益者**：Same individual (personal productivity / reference system)
- **付款人**：Same individual on personal App Store / subscription card
- **推动者**：Longtime user publicly writing 1★ switch-intent reviews

## 外部信号（Phase 2c）

**模式**：全市场 broad · 聚类 `migration@ask_hn`

**GitHub 持续性预填**：5/10 — Cluster persistence_hint=unknown; no GitHub lifecycle data.

**建议分数（启发式）**：迁移意愿=1 替代方案÷=1 持续性=5


## 置信度依据

- 来源数：1 · 产品数：1 · 跨 run：True
- 有明确切换意愿：True
- 有付费/损失信号：False
- 依据：八条 Google Tasks App Store 差评同指多列表导航回退与切换意图，且与 10-30 跑次同簇再现；但仍是单商店单产品——中等置信，宜 validate 而非 build+high。

## 证据账本

### [强] 十年重度用户把 Tasks 当个人资料库，iOS 列表菜单回退后被迫寻找替代。

- `app_store` · Google Tasks: 「I’m now being forced to look for something different」
- `app_store` · Google Tasks: 「I’ve used Google Tasks for 10+ years, multiple times a day, with 30–40 lists」

仍需假设：
- Users will pay for import+better list UX rather than wait for Google to restore the menu.

### [中] 汉堡/列表导航回退在多列表用户中产生明确切换意图。

- `app_store` · Google Tasks: 「I need to find a new now because this is no longer efficient」

仍需假设：
- Enough users will complete migration if import is one-click.

### [中] 缺应用内搜索与归档，Completed 区拥堵，浏览器体验更好。

- `app_store` · Google Tasks: 「Browser version works better because you can key word search, but not in the app」

仍需假设：
- Search+archive are table-stakes for paid power users.

### [中] 用户已公开对比官方客户端不如第三方 gTasks。

- `app_store` · Google Tasks: 「not nearly as smooth and intuitive as gTasks」

仍需假设：
- Willingness to try another client extends to leaving Google Tasks backend.

## 尚未验证的假设

- 新独立待办仅靠列表体验就能从 Todoist/Things 抢到付费转化。
- 谷歌不会在一个版本周期内恢复多列表下拉。
- 用户会把十年个人资料库交给独立开发者。

## 下一步验证

1. **[高] 触达 30 名提到列表/汉堡菜单/切换的 1★ 评论用户，提供引导导入 + $39/年创始价 waitlist。** — ≥8 回复；≥5 进 waitlist；≥3 完成导入试用。
2. **[高] 做出可点多列表侧栏+搜索/归档原型；对 20+ 列表用户做 5 场可用性测试。** — ≥4/5 表示若导入可用会在 30 天内切换。

## 研究结论

11-01 全量重跑（HN+GitHub+App Store；PH/Reddit 仍无凭证）再次出现 Google Tasks App Store 回声：20 条合并帖中 8 条落在该簇。ICE 单帖最高是 Agent 记忆与产品寿命，但 Stage3 优先多成员 Tasks 簇。注意单源回声与赛道拥挤；下一步访谈与付费导入 waitlist。
