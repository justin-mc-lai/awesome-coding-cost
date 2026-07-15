# 💰 Awesome Coding Cost

[![License: CC BY 4.0](https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/)
[![Plans Tracked](https://img.shields.io/badge/plans-36-blue)](README.md)
[![Updated](https://img.shields.io/badge/updated-2026--07--15-green)](README.md)

> 各大模型/云厂商/聚合商/AI IDE Coding Plan 实际成本对比 — 每元能买多少 Token？**每个套餐名点击直达订阅页面。**
>
> 受 [awesome-coding-plan](https://github.com/mahonzhan/awesome-coding-plan) 启发，采纳其 [Issue #24](https://github.com/mahonzhan/awesome-coding-plan/issues/24) 的「每元 Token 数 / 每亿 Token 成本」量化方案。

---

> 彻底说透：模型厂商直营 · 聚合中转商 · AI IDE · API 按量计费
> 
> 参考 [awesome-coding-plan](https://github.com/mahonzhan/awesome-coding-plan) · Issue [#24 每元 Token 数/每亿 Token 成本](https://github.com/mahonzhan/awesome-coding-plan/issues/24)
>
> 共收录 **36** 个套餐：厂商直营 16 | 聚合中转 5 | AI IDE 8 | API 按量 7

---

# 定价模式全景：四种玩法，一张图看懂

2026 年的 AI 编码市场，定价模式可以归为四种：

| 模式 | 代表 | 核心逻辑 | 透明度 |
|------|------|----------|:--:|
| **5h 刷新制** | Claude/ChatGPT/Kimi/GLM | 包月价买"每5小时刷新一次"的额度池 | ⭐⭐⭐⭐ |
| **月总量制** | MiniMax/小米 MiMo | 一次买断整个月的 Token 预算 | ⭐⭐⭐⭐⭐ |
| **Credit 黑盒** | Cursor/Copilot/Trae/CodeBuddy | 包月买 credits，但 1 credit ≠ 固定 Token | ⭐ |
| **API 按量** | DeepSeek/OpenAI/Anthropic | 用多少付多少，明码标价 | ⭐⭐⭐⭐⭐ |

### 核心概念

- **每元 Token 数**：花 1 元买到多少 Token → **越大越好**
- **每亿 Token 成本**：买 1 亿 Token 要多少钱 → **越小越好**
- **额度倍率**：套餐 Token 折算价值 ÷ 包月价格 → **越高越划算**（需模型 API 单价，暂标 N/A）

---

## 二、厂商直营 Coding Plan 横评

### 海外双雄

| 套餐 | 价格 | 模型 | TPS | 月度 Token(亿) | 每元 Token 数 | 每亿 Token 成本 | 备注 |
|------|------|------|:--:|:--:|:--:|:--:|------|
| ⭐ [Claude Pro](https://claude.ai/upgrade) ($20/月) | $20 | Claude Fable 5 (Claude Code) | / | 15.88 | 7940万 | $1.3 | 2026.7 最新模型 Fable 5; 5h刷新359次/3966万Token; 周额度+50%; 倍率63.6碾压全场; 429频繁 |
| ⭐ [ChatGPT Plus](https://chatgpt.com/pricing) ($20/月) | $20 | GPT-5.6-Sol (Codex CLI) | / | 6.16 | 3080万 | $3.2 | GPT-5.6-Sol 最新旗舰; 45-225次/5h; 周2190次/1.54亿; 倍率21.8; 限流比Claude宽松 |
| ⭐ [SuperGrok](https://grok.com/supergrok) ($30/月) | $30 | Grok 4.5 (Grok Build) | / | N/A | N/A | N/A | xAI出品; Grok 4.5模型; 图文视频生成; Grok Build Agent; X实时搜索; 多Agent并发推理(Contemplating模式) |
| [SuperGrok Heavy](https://grok.com/supergrok) ($300/月) | $300 | Grok 4.5 (最高额度) | / | N/A | N/A | N/A | 16个专家模式Agent并行; 最高使用上限; 专属支持+抢先体验; 首3月67%折扣 |

#### 深度解读

**Claude Pro ($20/月) — 名义上的倍率之王**

Claude Pro 的月度额度倍率高达 63.6，这意味着你花 $20 买到的计算资源，如果按 API 单价买需要 $1,273。但这是"名义"上的——Claude Pro 的 429 限流非常频繁，大量用户反映实际可用额度远低于理论值。

**ChatGPT Plus ($20/月) — 稳定但不够大方**

ChatGPT Plus 的月度额度约为 Claude Pro 的 1/3，但 GPT-5.6-Sol 在 Codex CLI 中的体验极好，且限流相对宽松。如果你用 Codex CLI 作为主力 harness，ChatGPT Plus 是更务实的选择。

### 国内四强

| 套餐 | 价格 | 模型 | TPS | 月度 Token(亿) | 每元 Token 数 | 每亿 Token 成本 | 备注 |
|------|------|------|:--:|:--:|:--:|:--:|------|
| ⭐ [Kimi Code Allegretto](https://www.kimi.com/membership/pricing) (¥159-199/月) | ¥199 | Kimi K2.7 | 27 | 14.28 | 718万 | ¥13.9 | K2.7 最新模型; 新会员体系¥159(年付)/¥199(月付); API不限速(多agent并发不429); 多模态; SWE-bench Verified 80.2% |
| ⭐ [MiniMax Coding Plan Plus](https://platform.minimaxi.com/subscribe/token-plan) (¥49/月) | ¥49 | MiniMax M2.7 (MIT 开源, 10B 激活) | 52 | 24 | 4898万 | ¥2.0 | MIT 开源 10B 激活参数; 周限制已取消, 额度实在; 工具调用准确率76.8%(超Opus4.6); 代码能力偏弱但量最大; 老套餐数据 |
| 👍 [GLM Coding Plan Pro](https://open.bigmodel.cn/glm-coding) (¥149/月) | ¥149 | GLM 5.2 | 26 | 6.4 | 430万 | ¥23.3 | 代码能力国内最强; 不支持多模态; 高峰期(14-18)3倍额度; 算力紧缺需抢购; 2026年已涨3次价 |
| 👍 [火山方舟 Coding Plan Lite](https://www.volcengine.com/activity/codingplan) (¥40/月) | ¥40 | 豆包 Seed 2.0 Pro | 86 | 3.2 | 800万 | ¥12.5 | 每日00:00限量释放; TPS 86.6 最快; 倍率15.18; 国内唯一原生支持Codex Responses API |
| 👍 [京东云 Coding Plan](https://www.jdcloud.com/cn/pages/codingplan) (¥19.9/月起(首购)) | ¥19.9 | DeepSeek V4/GLM 5.2/MiniMax M2.7/Qwen3.6/Kimi K2.7 等 | / | N/A | N/A | N/A | 首购¥19.9最低价; Pro ¥99.9(90000次/月); 每天10:30开抢; 近50款模型 |
| 👍 [阶跃星辰 Step Plan](https://platform.stepfun.com/subscribe) (¥49/月起) | ¥49 | Step-3.5-Flash (196B/11B 激活) | / | N/A | N/A | N/A | 全档位高速推理不加价; 用量为同档友商2倍+; 推广期价格; 海外$9.99比国内¥99略便宜 |
| [Kimi Code Andante](https://www.kimi.com/membership/pricing) (¥39-49/月) | ¥49 | Kimi K2.7 | 27 | 0.84 | 171万 | ¥58.3 | Allegretto 1/20 额度; ¥49 毫无性价比 |
| [GLM Coding Plan Lite](https://open.bigmodel.cn/glm-coding) (¥49/月) | ¥49 | GLM 5.2 | 26 | 1.28 | 261万 | ¥38.3 | Pro 1/5 额度; 5h仅80次; 高峰期3倍消耗; 毫无性价比 |
| [阿里云 Coding Plan Lite](https://www.aliyun.com/benefit/scene/tokenplan) (¥40/月 (已下线)) | ¥40 | Qwen 3.5 Plus | 52 | 6.0 | 1500万 | ¥6.7 | 2026.3.20 停售; 4.13 停续费; 转向Token Plan; Qwen Code免费层1000→100次/天 |
| [小米 MiMo Token Plan Pro](https://platform.xiaomimimo.com/#/token-plan) (¥329/月) | ¥329 | MiMo V2.5 Pro (1T MoE) | 46 | 38 | 1155万 | ¥8.7 | 1T MoE, 100万上下文; 性价比极高但有衰减; 多agent并发易429; 稳定性待观察 |
| [移动云 Coding Plan](https://ecloud.10086.cn/portal/act/codingplan) (¥7.9/月起(首月)) | ¥7.9 | MiniMax M2.5 | / | N/A | N/A | N/A | 运营商首家Coding Plan; 首月¥7.9后¥40; Pro ¥200; 广东另有AI融合套餐 |
| [天翼云 Coding Plan](https://ctxirang.ctyun.cn/maas/codingPlan) (¥49/月起) | ¥49 | GLM-5.2/GLM-5.1/GLM-4.7 等 | / | N/A | N/A | N/A | 电信运营商; 与智谱共享模型但额度更低; 每日10:00释放库存 |

#### 深度解读

**Kimi Code Allegretto (¥199/月) — 国内综合首选**

月 14.28 亿 Token，每元 718 万 Token，每亿 Token 成本 ¥13.9。Kimi K2.6 还是国内少数支持多模态的 Coding 模型。但有用户反馈升级 K2.6 后 429 错误频繁、容易死循环。

**GLM Coding Plan Pro (¥149/月) — 代码能力最强，但限流严重**

GLM 5.1 的 SWE-Bench Pro 得分是国内最高的，纯代码能力无可争议。但 ¥149 套餐每月仅 6.4 亿 Token（Kimi 的 45%），且算力极度紧缺，429 频率比 Kimi 还高。

**MiniMax Coding Plus (¥49/月) — 曾经的性价比之王**

¥49 = 24 亿 Token，每元 4898 万 Token，每亿 Token 成本仅 ¥2.0。但这是旧套餐数据，现已改版。且 MiniMax M2.7 的代码能力与 Kimi/GLM 有明显差距。

**火山方舟 (¥40/月) — 抢到就是赚到**

每日 00:00 限量释放库存，TPS 高达 86.6，是所有 Coding Plan 中最快的。倍率 15.18，如果能稳定抢到，性价比极高。

---

## 三、聚合中转商：批发 API → 零售订阅

| 套餐 | 价格 | 模型 | TPS | 月度 Token(亿) | 每元 Token 数 | 每亿 Token 成本 | 备注 |
|------|------|------|:--:|:--:|:--:|:--:|------|
| ⭐ [OpenCode Go](https://opencode.ai/go) ($10/月 (首月 $5)) | $10 | GLM-5.2/Kimi K2.7/DeepSeek V4 Pro/Qwen3.6/MiniMax M2.7 等 | / | 3.22 | 3220万 | $3.1 | 多模型聚合; 倍率 6; 支持多种 Agent harness |
| ⭐ [NVIDIA NIM](https://build.nvidia.com) (免费) | 免费 | DeepSeek V4 Pro/GLM-5.2/DeepSeek V4 Flash/MiniMax M2.7 | / | N/A | 免费 🎁 | 免费 | 不限量白嫖首选; 速度无保证; 部分模型为量化版; 免费不可持续 |
| 👍 [Ollama Pro](https://ollama.com/pricing) ($20/月) | $20 | GLM-5.2/MiniMax M2.7/Qwen3.6/DeepSeek V4 Flash 等 | / | 11.12 | 5560万 | $1.8 | Free 版 50x; 开源模型为主; 估值为近似值 |
| 👍 [Fireworks Fire Pass](https://app.fireworks.ai/fire-pass) ($7/周) | $7/周 | Kimi K2.6 Turbo | / | N/A | N/A | N/A | Kimi K2.6 Turbo 无限 Token 调用; 周付模式灵活 |
| [OpenRouter](https://openrouter.ai) (部分模型限免) | 免费 | 多模型 (HY3-Preview/MiniMax M2.7/DeepSeek V4 Pro 等) | / | N/A | 免费 🎁 | 免费 | 中转聚合平台, 按用量计费; 部分限免模型 |

### 中转商的本质

中转商（OpenCode、Ollama、Fireworks、NVIDIA NIM）的核心商业模式是：**批发采购各家模型的 API 额度 → 打包成统一订阅卖给用户**。

这带来了两个关键后果：

1. **多模型是卖点**：一个月费同时用 Kimi + GLM + DeepSeek + Qwen，确实方便
2. **单模型深度不如直营**：中转商要赚钱，单模型的额度必然不如厂商直营的 Coding Plan

**谁适合用中转商？**
- 需要在多个模型间切换做 A/B 测试的开发者
- 不想被单一厂商锁定的团队
- 海外用户访问国内模型不方便时

**NVIDIA NIM 的白嫖陷阱**：不限量免费很诱人，但速度无保证、部分模型为量化版、免费策略不可持续。当个备用可以，当主力会疯。

---

## 四、AI IDE 聚合：最不透明的黑盒

| 套餐 | 价格 | 模型 | TPS | 月度 Token(亿) | 每元 Token 数 | 每亿 Token 成本 | 备注 |
|------|------|------|:--:|:--:|:--:|:--:|------|
| 👍 [Cursor Pro](https://cursor.com/pricing) ($20/月) | $20 | 多模型 (Auto/Composer) | / | N/A | N/A | N/A | IDE 内集成 Agent; $20 API usage; 倍率 >=1 |
| 👍 [Windsurf Pro](https://windsurf.com/pricing) ($20/月 (2周试用)) | $20 | Premium Model + SWE-1.5 无限 | / | N/A | N/A | N/A | 8-101 msg/day; SWE-1.5 不限量; Quota-based 不透明 |
| 👍 [GitHub Copilot Pro](https://github.com/features/copilot/plans) ($10/月) | $10 | 多模型 | / | N/A | N/A | N/A | IDE 原生集成; 补全+Chat; 倍率 1.5 |
| 👍 [CodeBuddy 个人专业版](https://www.codebuddy.cn/pricing) (¥59/月) | ¥59 | 多模型 | / | N/A | N/A | N/A | 阿里出品; 限时加赠 2000 Credits; 国内 IDE 首选 |
| 👍 [Trae Pro](https://www.trae.ai/pricing) ($10/月 (7天免费)) | $10 | 多模型 | / | N/A | N/A | N/A | 字节出品; Bonus 随机赠送(有收到$130); 补全不限量 |
| [Kiro Pro](https://kiro.dev/pricing) ($20/月 (首月免费)) | $20 | 多模型 | / | N/A | N/A | N/A | ⚠️退出付款页丢失免费资格; $0.04/credit 超量 |
| [Augment Code INDIE](https://www.augmentcode.com/pricing) ($20/月) | $20 | 多模型 | / | N/A | N/A | N/A | 倍率 1.25; 较新的玩家 |
| [Zed Pro](https://zed.dev/pricing) ($10/月) | $10 | Claude Sonnet 4.6 | / | 0.044 | 44万 | $227.3 | 编辑器原生集成; 补全不限; $5/440万Token; 倍率 0.5 |

### AI IDE 套餐的共同问题

Cursor、Windsurf、Copilot、Trae、CodeBuddy —— 这些 AI IDE 的定价有一个共同特征：**用 credits/请求数计费，用户完全不知道 1 credit = 多少 Token**。

| IDE | 月费 | 额度描述 | 你能知道 Token 数吗？ |
|-----|:--:|------|:--:|
| Cursor | $20 | $20 API usage | ❌ |
| Windsurf | $20 | 8-101 msg/day | ❌ |
| Copilot | $10 | $15 credits | ❌ |
| CodeBuddy | ¥59 | 2000 Credits | ❌ |
| Trae | $10 | $20 Basic + Bonus | ❌ |

**为什么 IDE 不公开 Token 数？**

因为 IDE 场景下，模型调用是"后台自动"的——补全、内联建议、Agent 模式、Composer 模式各自消耗不同，厂商可以随意调整"1 credit = 多少 Token"而不通知用户。

**选购建议**：把 AI IDE 套餐当作"编辑器增强"而非"算力购买"。如果你的核心需求是大量 Agent 编码，IDE 套餐不够——你需要一个厂商直营 Coding Plan + API 按量计费做补充。

---

## 五、API 按量计费：最透明的方案

### 国内 API

| 模型 | 输入价格 | 备注 |
|------|:--:|------|
| ⭐ [DeepSeek V4 Flash (API)](https://platform.deepseek.com) | ¥1/百万输入Token | 性价比最高按量方案; 输出 ¥2/百万; 缓存读 1/100 价格; 1M 上下文 |
| 👍 [DeepSeek V4 Pro (API)](https://platform.deepseek.com) | ¥3/百万输入Token | V4 Flash 的 3 倍价格; 推理能力更强; 1M 上下文 |
| 👍 [Kimi K2.6 (API)](https://platform.moonshot.cn) | ¥20/百万输入Token | 支持多模态; 256K 上下文; 价格偏高但质量稳定 |
| 👍 [GLM 5.1 (API)](https://open.bigmodel.cn) | ¥10/百万输入Token | 198K 上下文; SWE-Bench Pro SOTA; 性价比好 |

### 海外 API

| 模型 | 输入价格 | 备注 |
|------|:--:|------|
| ⭐ [GPT-5.6-Sol (API)](https://platform.openai.com) | $3/百万输入Token | 输出 $12/百万; 性价比远好于 Claude API |
| ⭐ [Muse Spark 1.1 (API)](https://ai.meta.com/muse) | $1.25/百万输入Token | Meta首款付费API模型; 输出$4.25/百万; 1M上下文; Thinking/Contemplating双推理模式; 多Agent并行推理; SWE-bench Pro 58.6; MCP Atlas 88.1 |
| 👍 [Claude Opus 4.8 (API)](https://console.anthropic.com) | $15/百万输入Token | 输出 $75/百万; 昂贵但能力顶级; 缓存写 $3.75 读 $0.30 |

### API 按量 vs 包月：什么时候用哪个？

这个问题可以从"日用量"来算：

**假设你每天重度使用 Agent 编码，日均消耗约 500 万 Token**（约 50-80 次 Agent 请求）

| 方案 | 月成本 | 适用场景 |
|------|:--:|------|
| DeepSeek V4 Flash API | ~¥150 | 预算敏感、高并发需求 |
| Claude Pro ($20) | ~¥145 | 需要最强模型、能忍受 429 |
| ChatGPT Plus ($20) | ~¥145 | Codex CLI 主力、稳定优先 |
| Kimi Allegretto (¥199) | ¥199 | 国内首选、需要多模态 |
| Claude Opus API | ~$1,125 | 企业对质量要求极高、不在意成本 |

**结论**：对于绝大多数个人开发者，**包月 Coding Plan 比 API 按量计费划算 5-10 倍**。只有两种情况 API 更优：
1. 你用量极少（日均 < 50 万 Token）
2. 用 DeepSeek V4 Flash 这种超低价 API

---

## 六、选购决策树

```
你每天写代码几个小时？
├── < 2 小时 → API 按量计费（DeepSeek V4 Flash）
├── 2-6 小时 → Coding Plan 包月
│   ├── 在国内？
│   │   ├── 需要多模态？ → Kimi Allegretto ¥199
│   │   ├── 代码质量第一？ → GLM Pro ¥149
│   │   └── 预算紧张？ → MiniMax ¥49（模型较弱）
│   └── 在海外？
│       ├── 要最强模型？ → Claude Pro $20
│       ├── 要稳定体验？ → ChatGPT Plus $20
│       └── 要多模型切换？ → OpenCode Go $10
└── > 6 小时（重度）→ Coding Plan + API 双轨
    ├── 主力：Claude Pro 或 Kimi Allegretto
    └── 溢出：DeepSeek V4 Flash API 兜底
```

---

## 七、关键洞察与避坑指南

### 1. 不要只看"倍率"

额度倍率高不代表你能用到——429 限流是最大的隐性成本。Claude Pro 倍率 63.6，但实际可用额度可能只有 1/3。

### 2. Credit 体系是黑盒

任何用 credits 计费的套餐（Cursor、Copilot、CodeBuddy、Trae），你的实际 Token 获取量完全由厂商说了算。不要期望通过这些套餐"薅羊毛"。

### 3. API 缓存命中是隐藏福利

DeepSeek V4 Flash 的缓存读价格是正常价格的 1/100（其他厂商通常是 1/10）。如果你有大量重复上下文（比如固定的 system prompt），缓存命中能省 99%。

### 4. 中转商的多模型有代价

OpenCode Go $10 看起来很香，但你跑 Kimi K2.6 的 Token 量只有 Kimi 自家 Allegretto 的 22%。中转商的钱，一部分是"多模型便利费"。

### 5. 免费的不持久

NVIDIA NIM 免费不限量，但随时可能取消或限速。Ollama Free 的模型选择有限。免费白嫖可以当备用，不要当主力。

---

*数据更新：2026-07-15 · 由 [库拾创作台](https://github.com/kushishow/selfmedia-creator) 分析生成 · 参考 [awesome-coding-plan](https://github.com/mahonzhan/awesome-coding-plan)*

---

## 📊 数据说明

### 每元 Token 数 / 每亿 Token 成本

这两个指标来自 [awesome-coding-plan Issue #24](https://github.com/mahonzhan/awesome-coding-plan/issues/24) 的建议：

- **每元 Token 数** = 月度 Token 额度 ÷ 包月价格 → **越大越好**
- **每亿 Token 成本** = 包月价格 ÷ 月度 Token 额度(亿) → **越小越好**

对于 Credit/请求数计费的套餐，由于厂商不公开 1 credit = 多少 Token，无法计算这两个指标，标注为 N/A。

### 模型版本

所有模型版本数据更新至 **2026-07-15**。主要变更：
- Claude: Fable 5 (Claude Code 主力)
- ChatGPT: GPT-5.6-Sol (Codex CLI)
- Kimi: K2.7
- GLM: 5.2
- SuperGrok: Grok 4.5
- Muse Spark: 1.1

### 更新频率

每 2-4 周更新一次。发现数据过时或有新套餐上线，欢迎提 Issue 或 PR。

---

## 🤝 贡献

1. Fork 本仓库
2. 修改 `data.yaml` 中的数据
3. 运行 `python3 scripts/gen.py --data data.yaml --template README.tpl.md --output README_NEW.md`
4. 提交 PR

数据文件格式见 `data.yaml` 中的注释。

---

## 📜 协议

[CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) — 署名即可自由使用。

数据来源包含 [awesome-coding-plan](https://github.com/mahonzhan/awesome-coding-plan) 的公开数据，遵循其 CC BY 4.0 协议。

---

*本仓库由 [库拾创作台](https://github.com/justin-mc-lai/selfmedia-creator) 半自动维护 · 微信公众号：Github 库拾*
