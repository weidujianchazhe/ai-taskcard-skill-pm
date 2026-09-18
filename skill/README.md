# 项目管理AI轻量化接力（使用指南）

> 版本 v1.2.1

> 这是一份**通用型项目管理技能模板**：任何项目都可以复制本模板建立自己的协同工作区；支持多 AI / 跨平台 / 跨时间 / 跨项目接力工作。
>
> 核心哲学：**项目可以复杂沉重，AI 接手只读所需**——负担不随项目规模增长。
>
> 本文件是**使用指南**（面向人与首次接入的 AI）；协议正文唯一权威源 = `SKILL.md`，本文件不重复承载规则细则。

## 一、这个模板解决什么

| 问题 | 方案 |
|---|---|
| 切换 AI 后无法衔接 | 每次工作结束写交接/总结 + 覆盖式状态 + 登记任务卡 |
| 新 AI 要读全部文档（算力浪费） | **任务卡驱动接手**：任务卡定位 → MAP 认结构 → reports 衔接，按需读取 |
| 指令模糊、AI 走错任务 | 任务卡含**涉及文件路径 + 上次交接指针**，精准到达，不靠猜 |
| 交接文件太啰嗦 | 最小交接模板（只写本任务需要的信息）+ 完成型只写简化总结 |
| 改动历史无法追溯 | INDEX 一行一条 + 指向完整交接记录 |
| 多 AI 同时工作互相踩 | 任务卡承接认领 + 按模块/分支分工 + 独立交接文件 |
| 文档越攒越大 | 覆盖式状态 + 只读所需 + 滚动归档；MAP 只记结构不记进展 |
| 技能自身事务污染项目档案 | **元管理分流**：复盘/版本/恢复登记全走 REVIEWS.md，reports/INDEX 只存工作记录 |

## 二、目录结构（物理隔离）

技能源包（外面，通用型）与项目工作区层（里面，被管理）物理隔离——**管理目录建在工程路径之外**（不混入源码树、不被打包）；项目工作区为技能实例化副本（含协议文件），工程源码永不写入管理目录。

```
# 项目工作区（每项目一个 · 文件组成以第三节「工作区文件清单」为准）
{WORKSPACE_ROOT}\<项目名>\        # 工作区根 {WORKSPACE_ROOT} 初始化时向用户确认一次（默认或自定义）
├── SKILL.md             # 协议入口（工作区自包含协议；MAP「协同协议详见 SKILL.md」即指向此文件）
├── MAP.md               # 项目地图：环境/规则/协议/路径注册表（低频，只在新结构时写）
├── STATE.md             # 当前状态：人读区（3 行摘要）+ AI 区（条目级覆盖式；首次/跨模块/审视时读）
├── REVIEWS.md           # 元管理记录：技能复盘/恢复登记（追加式；不进 reports/INDEX）
├── tasks\               # 任务卡目录：每卡一文件按工作命名（人读定位区 + AI 字段区；接手第一入口）
├── INDEX.md             # 记录目录：类型标记 [接力]/[完成]/[废弃]（追溯索引 + 人读表格）
├── reports\             # 工作档案：交接记录/简化总结（每次一篇，沿锚点读；只存项目工作记录）
├── archives\            # 归档（只进不出）
│   ├── done\            # 完成卡归档（初始化即创建，完成型收工移卡目标）
│   └── INDEX_archived.md  # INDEX 不可变全量归档（初始化即创建）
└── tools\               # 可选工具区（按需拉动，不进接手路径）
    └── README.md        # 工具区入口（总说明 + 三铁律 + 内置工具表；子规范按需从技能源包拉取）
```

## 三、初始化流程（新项目接入）

0. 先读 `SKILL.md`（技能入口：定位/触发时机/使用流程/初始化检查清单）
1. **确认工作区根 {WORKSPACE_ROOT}**（默认或自定义——一次确认，所有项目归入该根；管理目录子文件夹由技能自动创建，无需用户事先建文件夹）
> **先查重**：确认工作区根后、建目录前，先探测该根下是否已有此项目管理实例；有 → 先归并/确认唯一正本，禁止另起新目录。
2. **按「工作区文件清单」建立工作区**（不整包复制；两条初始化路径共用本清单，存量接入见 LEGACY_ONBOARDING.md）：
   - **实例化**（模板改名后重填）：`MAP.template.md` → `MAP.md`、`STATE.template.md` → `STATE.md`、`INDEX.template.md` → `INDEX.md`、`REVIEWS.template.md` → `REVIEWS.md`
   - **原样复制**：`SKILL.md`（协议入口，随工作区走）、`tasks\TASK_CARD.template.md`（格式参考）、`designs\DESIGN_CARD.template.md`（设计卡格式参考）、`reports\HANDOVER.template.md`（格式参考）、`archives\README.md`、`tools\README.md`
   - **创建空目录/文件**：`tasks\`、`reports\`、`archives\done\`、`archives\INDEX_archived.md`
   - **不进工作区**（留技能源包，按需拉取）：`README.md`、`BLUEPRINT.md`、`LEGACY_ONBOARDING.md`、`tools\` 各子目录规范（checks / visualize / schedule / report / custom）
3. 打开 `MAP.md`，替换两类占位符——`[]` 人填项（见下）与 `{}` 运行期变量（`{WORKSPACE_ROOT}` 需向用户确认一次，`{PLATFORM}`/`{SHELL}` 按环境填写）：
   - `[项目名称]`、`[工程路径]`、`[技术栈]`、`[不涉及的模块/边界]`、`[运行命令]`、`[打包命令]`、`[项目特有规则]`、`[技能源包路径]`（缺失补全与版本过时检测用）
   - 确认规则段配置：INDEX 主文件行数 / STATE 字数上限 / reports 归档阈值 / AI 定期排查开关 / 协作模式（light/standard/coordination）
4. 在 `tasks\` 登记第一条任务卡（每卡一文件，按工作命名，含人读定位区）
5. 告知参与 AI：**"协同工作区在 {WORKSPACE_ROOT}\<项目名>\，先读 tasks\ 里对应的任务卡"**

> **存量项目（已开工、无管理结构）**：不执行以上第 2~4 步初始化，而是读 `LEGACY_ONBOARDING.md` 执行接入——按同一份「工作区文件清单」创建管理目录 + 轻量登记当前信息，历史靠渐进整理，不做深度整理。

## 四、接手流程（任务卡驱动 · 精准到达）

1. 读对应任务卡 → 命中（描述/要点/涉及文件/上次交接）；指令模糊时按任务卡兜底，仍不明则问用户
2. 要点够用 → 直接开工；要点不够 → 沿"上次交接"读 `reports\` 上一篇（[接力] 链）
3. 读 reports 后**提炼增量覆盖回任务卡**（提炼回卡——下次接手不必再读这篇）
4. 按任务卡"涉及文件"路径 → 读具体工作文件，开工
5. 需要全局判断时（首次接手/跨模块/审视）：读 `STATE.md`（含人读区）与 `MAP.md`；深度追溯查 `INDEX.md`（按 [接力] 标记定位）

> 只要「收工分流」被遵守（有下一步 → 完整交接 + 覆盖式更新任务卡；无下一步 → 简化总结 + 移卡到 archives\done\），即使项目放置半年，接手成本也恒定 ≈ 任务卡一张 + 偶尔 1 次 reports。

## 五、协议速览（细则以 `SKILL.md` 为唯一权威源）

1. **任务卡驱动**：接手先读对应任务卡定位，开工前在卡「承接」认领，不漫读全项目
2. **收工四件套**：交接 reports → 卡更新/移卡 → INDEX 登记 → STATE 更新（并行时条目级写）；未完成必须建卡，完成移卡 archives\done\ 不删卡
3. **最小交接**：6 块 + 第 7 块「任务卡更新」（有对应任务卡时必填）；工程有 git 时「改动点」每条附 commit hash
4. **命名与编号**：reports `YYYY-MM-DD_主题_AI标识.md`（AI 标识含短码，写前 list 防重名）；编号 XXNNNN——分支先在 MAP 登记、数字按数值递增、撞号 +1 重试留痕
5. **并发写规则**：写前读 / 写后验 / STATE 条目级写；跨分支冲突不比编号、不以时间戳裁决，留痕交管理者
6. **覆盖式更新**：任务卡/STATE 永远只留最新，历史归 reports + INDEX；reports 达 MAP「reports 归档阈值」（默认 20）即滚动归档；STATE 字数达 MAP「STATE 字数上限」（默认 15k）即把历史段移入 reports\，只留当前快照
7. **档案红线**：reports\ 与 archives\ 禁删禁移（唯一例外 = 收工归档流程，移后同步 INDEX 行指向）；新增文件/路径/分支登记 MAP
8. **元管理分流**：技能自身事务写 REVIEWS.md，不进 reports/INDEX；人工检查按需、收工门禁在完成前强制、定期排查仅开关开启后运行，门禁失败阻塞完成
9. **进度锚点**：工作中落点即覆盖写卡上「进度锚点」行——中断沿锚点 + git status 续作，收工沉淀后清「—」
10. **人读区由 AI 区自动生成**（任务←描述首句、状态←状态字段、下一步←要点①），覆盖时同步重写

> **更新/瘦身/简化/合并本技能前，先逐条过 `SKILL.md` 第八节「变更保护区」门禁**（功能零损失 / 交叉影响检查 / 接手成本不升 / **成本归属三原则**：写路径恒定·快照与总账分工·主文件容量即封顶 / 承重结构保留 / 环环相扣六问自检 / **对账思想**：时间·编号·身份·凭证四锚点是审计接口，编号规则非格式偏好）；**改动与门禁冲突时 AI 必须弹窗提醒用户，未经确认不得执行**。

## 六、目录模板文件说明

| 文件 | 说明 |
|---|---|
| `SKILL.md` | 技能入口与协议唯一权威源（定位/触发/流程/核心协议/检查清单/查看视图/维护规范/变更保护区） |
| `MAP.template.md` | 项目地图骨架，复制为 `MAP.md` 后填占位符（固定四段：环境/规则/协议/路径；协议段为 SKILL.md 派生快照） |
| `STATE.template.md` | 当前状态快照骨架（人读区 3 行 + 进展/阻塞/决策点/时间戳，条目级覆盖式；字数上限见 MAP「STATE 字数上限」，默认 15k，超限时历史段移入 `reports\`） |
| `tasks\TASK_CARD.template.md` | 任务卡骨架（稳定 TASK-ID、DESIGN-ID、EVENT-ID、并发元数据与收工门禁） |
| `designs\DESIGN_CARD.template.md` | 设计卡生命周期模板；仅已批准设计卡可生成执行任务卡 |
| `reports\HANDOVER.template.md` | 最小交接模板（6 块 + 第 7 块任务卡更新），每条记录一个文件 |
| `INDEX.template.md` | 记录目录（类型标记 [接力]/[完成]/[废弃]，初始化时创建；行永不丢失——超 N 行移入归档文件） |
| `LEGACY_ONBOARDING.md` | 存量项目接入指南（附带文件：轻量登记 + 渐进整理，不进主协议必读流程） |
| `REVIEWS.template.md` | 技能复盘模板（元管理：阻碍→根因→建议→处置，四段一句话；**初始化时实例化为工作区 REVIEWS.md**） |
| `BLUEPRINT.md` | 设计蓝图（6 条要点即权威速记；只记设计要点、不承载协议，不参与版本同步；HTML 版为包外补充文档） |
| `archives\README.md` | 归档说明（只进不出，防误删） |
| `tools\` | 可选工具区（checks/visualize/schedule/report/custom 规范留技能源包按需拉取），按需新增守三铁律 |

## 七、双平台命令示例（PowerShell / bash）

> 命令全部参数化：`{WORKSPACE_ROOT}`（工作区根，初始化确认）、`{PROJECT_NAME}`（项目名）、`{SHELL}`（powershell / bash）。
> 管理目录由技能自动创建；以下命令供初始化/日常维护参考。

| 场景 | PowerShell（{SHELL}=powershell） | bash（{SHELL}=bash） |
|---|---|---|
| 查看工作区根是否存在 | `Test-Path "{WORKSPACE_ROOT}"` | `test -d "$WORKSPACE_ROOT" && echo ok` |
| 创建管理目录和归档索引 | `New-Item -ItemType Directory -Force -Path "{WORKSPACE_ROOT}\{PROJECT_NAME}\tasks","{WORKSPACE_ROOT}\{PROJECT_NAME}\reports","{WORKSPACE_ROOT}\{PROJECT_NAME}\archives\done"; New-Item -ItemType File -Force -Path "{WORKSPACE_ROOT}\{PROJECT_NAME}\archives\INDEX_archived.md"` | `mkdir -p "$WORKSPACE_ROOT/$PROJECT_NAME"/{tasks,reports,archives/done}; touch "$WORKSPACE_ROOT/$PROJECT_NAME/archives/INDEX_archived.md"` |
| 查看目录结构 | `Get-ChildItem -Recurse "{WORKSPACE_ROOT}\{PROJECT_NAME}"` | `ls -R "$WORKSPACE_ROOT/$PROJECT_NAME"` |
| 运行项目（如适用） | `{运行命令}`（按 MAP 环境段） | `{运行命令}`（按 MAP 环境段） |
| 打包项目（如适用） | `{打包命令}`（按 MAP 环境段） | `{打包命令}`（按 MAP 环境段） |

> 环境约定：命令按 `{PLATFORM}`（win / mac / linux）与 `{SHELL}` 二选一使用，不跨平台混用；路径分隔符随平台（Windows `\` / POSIX `/`）。

## 八、使用前提与平台兼容

**使用前提**：本技能为本地项目管理工程，需具备**本地文件系统 + 命令/文件执行能力**——能落盘管理目录、读写任务卡与交接文件。

**平台按能力维度判定，不枚举平台名称**：具备上述能力的平台（Harness 类 / IDE Agent / 桌面工作区 Agent 等）自动兼容；不依赖任何平台私有接口、技能系统或 API（技能系统有则装，无则按文档读取）。

**不适用环境**：无本地文件能力的场景（网页对话 / 移动端 App / 纯对话 / API 裸调）不满足使用前提，本技能不适用。
