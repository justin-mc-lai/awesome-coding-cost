> 彻底说透：模型厂商直营 · 聚合中转商 · AI IDE · API 按量计费
> 
> 参考 [awesome-coding-plan](https://github.com/mahonzhan/awesome-coding-plan) · Issue [#24 每元 Token 数/每亿 Token 成本](https://github.com/mahonzhan/awesome-coding-plan/issues/24)
>
> {{STATS}}

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

{{OVERSEAS_TABLE}}

#### 深度解读

**Claude Pro ($20/月) — 名义上的倍率之王**

Claude Pro 的月度额度倍率高达 63.6，这意味着你花 $20 买到的计算资源，如果按 API 单价买需要 $1,273。但这是"名义"上的——Claude Pro 的 429 限流非常频繁，大量用户反映实际可用额度远低于理论值。

**ChatGPT Plus ($20/月) — 稳定但不够大方**

ChatGPT Plus 的月度额度约为 Claude Pro 的 1/3，但 GPT-5.6-Sol 在 Codex CLI 中的体验极好，且限流相对宽松。如果你用 Codex CLI 作为主力 harness，ChatGPT Plus 是更务实的选择。

### 国内四强

{{DOMESTIC_TABLE}}

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

{{AGGREGATOR_TABLE}}

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

{{IDE_TABLE}}

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

{{API_DOMESTIC_TABLE}}

### 海外 API

{{API_OVERSEAS_TABLE}}

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

*数据更新：{{LAST_UPDATED}} · 由 [库拾创作台](https://github.com/kushishow/selfmedia-creator) 分析生成 · 参考 [awesome-coding-plan](https://github.com/mahonzhan/awesome-coding-plan)*
