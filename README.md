# 💰 Awesome Coding Cost

[![License: CC BY 4.0](https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/)
[![Plans Tracked](https://img.shields.io/badge/plans-36-blue)](README.md)
[![Updated](https://img.shields.io/badge/updated-2026--07--15-green)](README.md)

> 各大模型/云厂商/聚合商/AI IDE Coding Plan 实际成本对比 — **一个板块看透所有计费套路**。每个套餐名点击直达订阅页面。
>
> 受 [awesome-coding-plan](https://github.com/mahonzhan/awesome-coding-plan) 启发，采纳其 [Issue #24](https://github.com/mahonzhan/awesome-coding-plan/issues/24) 的「每元 Token 数 / 每亿 Token 成本」量化方案。

---

# 🚀 2026 大模型 Coding Plan 比价指南

> 彻底说透：模型厂商直营 · 聚合中转商 · AI IDE · API 按量计费
>
> 参考 [awesome-coding-plan](https://github.com/mahonzhan/awesome-coding-plan) · Issue [#24 每元 Token 数/每亿 Token 成本](https://github.com/mahonzhan/awesome-coding-plan/issues/24)
>
> 共收录 **36** 个套餐：厂商直营 16 | 聚合中转 5 | AI IDE 8 | API 按量 7

---

# 计费规则统一图鉴

> 所有厂商的计费套路，一个板块看透。每个厂商的[订阅页面]可点击直达。

## 计费模式速查矩阵

| 厂商 | 套餐 | 计费模式 | 5h额度 | 周额度 | 月额度 | 限流机制 | 最大陷阱 |
|------|------|:--:|------|------|------|------|------|
| ⭐ [Claude Pro](https://claude.ai/upgrade) | $20/月 | 🔄 5h刷新 | 359次/3966万Token | 3590次/3.97亿(2026.5-7 +50%) | 14360次/15.88亿 | 429频繁; 实际可用额度远低于理论值; 高峰期尤其严重 | 倍率63.6是名义值, 实际429后可用额度≈1/3 |
| ⭐ [ChatGPT Plus](https://chatgpt.com/pricing) | $20/月 | 🔄 5h刷新 | 45-225次 Local Messages | 2190次/1.54亿 | 8760次/6.16亿 | 限流比Claude宽松; 但Local Messages定义不透明 | Local Messages定义模糊, Agent模式 vs Chat模式消耗不同 |
| ⭐ [Kimi Code Allegretto](https://www.kimi.com/membership/pricing) | ¥159-199/月 | 🔄 5h刷新 | 刷新1307次/6500万Token | 9073次/3.57亿 | 36292次/14.28亿 | API不限速!!! 多agent并发不弹429; Kimi Code自研CLI偶... | K2.7升级后偶尔死循环; 149/199新会员体系权益拆分(Code权益独立购买) |
| [Kimi Code Andante](https://www.kimi.com/membership/pricing) | ¥39-49/月 | 🔄 5h刷新 | 刷新359次/1500万Token | 639次/2100万 | 2556次/8400万 | Allegretto 1/20额度; ¥49毫无性价比 | 这档位的Token量跑几个agent就干, 仅适合体验到门外 |
| 👍 [GLM Coding Plan Pro](https://open.bigmodel.cn/glm-coding) | ¥149/月 | 🔄 5h刷新 | 400次 prompt | 2000次 | 8000次/6.4亿 | 高峰期14-18点3倍额度消耗!!! 每日10:00限量释放; Max秒售罄; ... | 高峰期3倍扣+每日限量的双重暴击, 下午干活≈1/3额度; 海外版涨价近翻倍 |
| [GLM Coding Plan Lite](https://open.bigmodel.cn/glm-coding) | ¥49/月 | 🔄 5h刷新 | 80次 | 400次 | 1600次/1.28亿 | 高峰期3倍消耗; 5h仅80次, 两个复杂任务就见底 | ¥49但5h/80次=跑两次重agent就等刷新, 性价比倒数第1 |
| 👍 [火山方舟 Coding Plan Lite](https://www.volcengine.com/activity/codingplan) | ¥40/月 | 🔄 5h刷新 | 148次/1000万Token | - | 6275次/3.2亿 | 每日00:00限量释放库存, 售完即止, 需抢 | 抢不到就当月白等; TPS 86.6最快但没库存也没用 |
| [阿里云 Coding Plan Lite](https://www.aliyun.com/benefit/scene/tokenplan) | ¥40/月 (已下线) | 🔄 5h刷新 | 1200次/4000万Token | 9000次 | 18000次/6亿 | 已停售(2026.3.20停购, 4.13停续费) | 已停售! 转向Token Plan(更贵); Qwen Code免费层1000→100次/... |
| ⭐ [MiniMax Coding Plan Plus](https://platform.minimaxi.com/subscribe/token-plan) | ¥49/月 | 🔄 5h刷新 | 1360次/6000万Token(老数据) | - | 54400次/24亿 | 旧套餐已改版, 新套餐数据待确认; 模型代码能力偏弱 | 数据是旧的! 已改套餐后实际额度可能变化; 模型只适合量大的场景 |
| [小米 MiMo Token Plan Pro](https://platform.xiaomimimo.com/#/token-plan) | ¥329/月 | 📦 月总量 | - | - | 380亿 Credits/月, ¥329 | 多agent并发易429; 模型稳定性待观察; 有衰减 | 便宜但有衰减; 不兼容Codex Responses API |
| ⭐ [OpenCode Go](https://opencode.ai/go) | $10/月 (首月 $5) | 📦 月总量 | - | - | $10(首月$5) 无限制 | 多模型聚合; 不支持搜索 | 单模型深度只有直营22%; 跑Kimi=Kimi直营的1/5额度 |
| 👍 [Ollama Pro](https://ollama.com/pricing) | $20/月 | ⏱️ GPU计时 | - | - | $20 GPU时间计费(不透明) | 开源模型为主; Free版50x | GPU时间计费完全不透明, 用户不知道花$20买到了多少GPU秒 |
| 👍 [Fireworks Fire Pass](https://app.fireworks.ai/fire-pass) | $7/周 | 📦 月总量 | - | $7/周 Kimi K2.6 Turbo无限Token | - | 周付灵活但仅有Kimi K2.6 Turbo | 仅有一个模型; Fire Pass套餐可能随时终止 |
| [OpenRouter](https://openrouter.ai) | 部分模型限免 | 🆓 限免 | - | - | - | 中转聚合; 按量计费; 模型来源和稳定性依赖上游 | 限免模型随时可能取消; 付费模型按tokens计费价格不透明 |
| ⭐ [NVIDIA NIM](https://build.nvidia.com) | 免费 | 🆓 限免 | - | - | - | 免费但不限速保证; 部分模型为量化版; 首Token延迟高 | 免费不可持续! 随时取消/限速; 量化版可能模型质量低于API版 |
| 👍 [Cursor Pro](https://cursor.com/pricing) | $20/月 | 🎲 Credit黑盒 | - | - | $20 credit($20 API usage) | Usage-based; 超额按量付费 | 1 credit ≠ 固定Token数; 厂商可随时调整credit/Token汇率 |
| 👍 [Windsurf Pro](https://windsurf.com/pricing) | $20/月 (2周试用) | 🎲 Credit黑盒 | - | 日/周预算 | - | SWE-1.5不限量; Premium Model限msg数 | msg/day不透明; 一个msg可能消耗多次模型调用 |
| 👍 [GitHub Copilot Pro](https://github.com/features/copilot/plans) | $10/月 | 🎲 Credit黑盒 | - | - | $15 monthly credits | IDE原生集成; 补全+Chat混合 | credits消耗规则不公开; 补全和Chat消耗不同 |
| 👍 [CodeBuddy 个人专业版](https://www.codebuddy.cn/pricing) | ¥59/月 | 🎲 Credit黑盒 | - | - | 2000 Credits(含体验500); 限时加赠2000 | 阿里出品; 国产IDE首选 | 加赠2000有效期仅1个月; 赠费用完恢复2000 |
| 👍 [Trae Pro](https://www.trae.ai/pricing) | $10/月 (7天免费) | 🎲 Credit黑盒 | - | - | $20 Basic + 随机Bonus | 字节出品; 补全不限量 | Bonus随机送, 不承诺额度; 有拿到$130的也有拿$5的 |
| [Kiro Pro](https://kiro.dev/pricing) | $20/月 (首月免费) | 🎲 Credit黑盒 | - | - | 1000 credits; 超量$0.04/credit | 首月免费; 退出付款页丢失免费资格! | ⚠️退出付款页就丢失免费资格! 不要试 |
| [Augment Code INDIE](https://www.augmentcode.com/pricing) | $20/月 | 🎲 Credit黑盒 | - | - | 40000 credits | 新玩家, 数据不多 | 40000 credits到底能跑多少agent? 没有实测数据 |
| [Zed Pro](https://zed.dev/pricing) | $10/月 | 🎲 Credit黑盒 | - | - | $5 tokens(440万Claude Sonnet 4.6) + usage-based | 编辑器原生; 补全不限 | $5/440万Token只是编辑器附加, 主力agent不够用 |
| ⭐ [DeepSeek V4 Flash (API)](https://platform.deepseek.com) | 按量计费 | ⚡ API按量 | - | - | - | TPS 50+; 1M上下文 | 缓存命中率决定实际成本; system prompt复用可省99% |
| 👍 [DeepSeek V4 Pro (API)](https://platform.deepseek.com) | 按量计费 | ⚡ API按量 | - | - | - | V4 Flash的3倍价; 推理更强 | 日常coding V4 Flash够用; Pro只有硬核推理才值差价 |
| 👍 [Kimi K2.6 (API)](https://platform.moonshot.cn) | 按量计费 | ⚡ API按量 | - | - | - | 256K上下文; 多模态支持 | 价格是国内API最高的; Allegretto包月¥199比API便宜10倍+ |
| 👍 [GLM 5.1 (API)](https://open.bigmodel.cn) | 按量计费 | ⚡ API按量 | - | - | - | 198K上下文; SWE-bench Pro SOTA | Pro套餐¥149/6.4亿比API便宜10倍, 选套餐别用API |
| 👍 [Claude Opus 4.8 (API)](https://console.anthropic.com) | 按量计费 | ⚡ API按量 | - | - | - | 输出$75是输入的5倍; agent场景输出Token占比高 | Agent场景输出Token通常>输入Token; $75输出价实际成本远超$15输入价 |
| ⭐ [GPT-5.6-Sol (API)](https://platform.openai.com) | 按量计费 | ⚡ API按量 | - | - | - | 性价比远好于Claude API | 和ChatGPT Plus比, 重度使用包月更划算(月$20 vs API月$100+) |
| 👍 [京东云 Coding Plan](https://www.jdcloud.com/cn/pages/codingplan) | ¥19.9/月起(首购) | 📦 月总量 | - | - | Lite 18000次/月, Pro 90000次/月 | 每天10:30开抢; 首购价仅1次 | 首购¥19.9后恢复¥40; 近50款模型但每个模型额度分配不透明 |
| [移动云 Coding Plan](https://ecloud.10086.cn/portal/act/codingplan) | ¥7.9/月起(首月) | 🔄 5h刷新 | 1200次 | 9000次 | 18000次 | 仅MiniMax M2.5模型 | 运营商网络虽稳但模型单一; 首月¥7.9后¥40 |
| [天翼云 Coding Plan](https://ctxirang.ctyun.cn/maas/codingPlan) | ¥49/月起 | 🔄 5h刷新 | 80次 | 400次 | 1600次 | 与智谱共享模型但额度更低; 每日10:00释放库存 | 比智谱Lite同价但额度更低, 买之前先比GLM官网 |
| 👍 [阶跃星辰 Step Plan](https://platform.stepfun.com/subscribe) | ¥49/月起 | 🔄 5h刷新 | ~100次(Mini) / ~400次(Plus) / ~1500次(Pro) | - | 全档位高速推理不加价 | 推广期价格, 可能随时调整 | 推广期价格不承诺长期; 海外$9.99比国内¥99更便宜 |
| ⭐ [SuperGrok](https://grok.com/supergrok) | $30/月 | 📦 月总量 | - | - | 月付$30, rate-limited | Grok Build Agent不限速; 图文视频生成有独立限制 | 免费层和付费层模型可能不同(Grok 4.5仅付费) |
| [SuperGrok Heavy](https://grok.com/supergrok) | $300/月 | 📦 月总量 | - | - | 16个并发Agent, $300/月 | 无公开限流数据 | 首3月67%折扣后恢复$300, 注意续费时间 |
| ⭐ [Muse Spark 1.1 (API)](https://ai.meta.com/muse) | 按量计费 | ⚡ API按量 | - | - | - | Meta首款付费API; 1M上下文; Thinking/Contemplati... | Contemplating模式并行agent消耗倍率未公开; 美国区可用 |

## 三层闸门深度拆解

**5小时刷新制**不是"每5小时给你这么多"，而是"三层闸门每层都是上限，任何一层撞墙就停"。

| 厂商 | 5h闸门 | 周闸门 | 月闸门 | 实际瓶颈在哪？ |
|------|------|------|------|------|
| ⭐ [Claude Pro](https://claude.ai/upgrade) | 359次/3966万Token | 3590次/3.97亿(2026.5-7 +50%) | 14360次/15.88亿 | 5h刷新→看单次用量 |
| ⭐ [ChatGPT Plus](https://chatgpt.com/pricing) | 45-225次 Local Messages | 2190次/1.54亿 | 8760次/6.16亿 | 5h刷新→看单次用量 |
| ⭐ [Kimi Code Allegretto](https://www.kimi.com/membership/pricing) | 刷新1307次/6500万Token | 9073次/3.57亿 | 36292次/14.28亿 | ✅ 不限速, 5h刷新后继续 |
| [Kimi Code Andante](https://www.kimi.com/membership/pricing) | 刷新359次/1500万Token | 639次/2100万 | 2556次/8400万 | ❌ 5h仅80次, 两任务见底 |
| 👍 [GLM Coding Plan Pro](https://open.bigmodel.cn/glm-coding) | 400次 prompt | 2000次 | 8000次/6.4亿 | ⚠️ 高峰期3倍消耗→5h窗口秒空 |
| [GLM Coding Plan Lite](https://open.bigmodel.cn/glm-coding) | 80次 | 400次 | 1600次/1.28亿 | ⚠️ 高峰期3倍消耗→5h窗口秒空 |
| 👍 [火山方舟 Coding Plan Lite](https://www.volcengine.com/activity/codingplan) | 148次/1000万Token | - | 6275次/3.2亿 | ⛔ 需抢库存, 抢不到=没额度 |
| [阿里云 Coding Plan Lite](https://www.aliyun.com/benefit/scene/tokenplan) | 1200次/4000万Token | 9000次 | 18000次/6亿 | 🚫 已停售 |
| ⭐ [MiniMax Coding Plan Plus](https://platform.minimaxi.com/subscribe/token-plan) | 1360次/6000万Token(老数据) | - | 54400次/24亿 | 5h刷新→看单次用量 |
| [移动云 Coding Plan](https://ecloud.10086.cn/portal/act/codingplan) | 1200次 | 9000次 | 18000次 | 5h刷新→看单次用量 |
| [天翼云 Coding Plan](https://ctxirang.ctyun.cn/maas/codingPlan) | 80次 | 400次 | 1600次 | 5h刷新→看单次用量 |
| 👍 [阶跃星辰 Step Plan](https://platform.stepfun.com/subscribe) | ~100次(Mini) / ~400次(Plus) / ~1500次(Pro) | - | 全档位高速推理不加价 | 5h刷新→看单次用量 |

## 限流机制横向对比

| 厂商 | 429频率 | 触发条件 | 高峰期特殊规则 | 多Agent并发 |
|------|:--:|------|------|:--:|
| ⭐ [Claude Pro](https://claude.ai/upgrade) | 🔴 极高 | 正常时段也频繁 | 无明显高峰规则 | ❌ |
| ⭐ [ChatGPT Plus](https://chatgpt.com/pricing) | 🟡 中等 | Local Msg定义模糊 | 无明显高峰规则 | ⚠️ |
| Kimi Allegretto | 🟢 低 | API不限速; CLI偶有 | 无 | ✅ |
| GLM Pro | 🔴 极高 | 14-18点3倍消耗 | ⛔ 高峰期3倍扣+抢购 | ❌ |
| 火山方舟 | 🟡 中等 | 每日00:00限量释放 | 库存售完即止 | ⚠️ |
| MiniMax | 🟢 低 | 旧套餐数据; 改版后待观察 | 不明显 | ✅ |
| ⭐ [NVIDIA NIM](https://build.nvidia.com) | 🟡 中等 | 40 rpm硬限 | 无 | ⚠️ |

## Credit 黑盒：你不知道 1 Credit = 多少 Token

这些套餐用 credits/请求数计费，**厂商可以随时调整 credit ↔ Token 汇率而不通知你**。

| 厂商 | 月费 | 月Credits | 已知换算（如果公开） | 不透明程度 |
|------|:--:|:--:|------|:--:|
| 👍 [Cursor Pro](https://cursor.com/pricing) | $20 | $20 credit($20 API usage) | ❓ 仅标注$额, 无Token数 | 🔴 完全不透明 |
| 👍 [Windsurf Pro](https://windsurf.com/pricing) | $20 | - | ❓ 无公开换算 | 🔴 完全不透明 |
| 👍 [GitHub Copilot Pro](https://github.com/features/copilot/plans) | $10 | $15 monthly credits | ❓ 无公开换算 | 🔴 完全不透明 |
| 👍 [CodeBuddy 个人专业版](https://www.codebuddy.cn/pricing) | ¥59 | 2000 Credits(含体验500); 限时加赠2000 | ❓ 无公开换算 | 🔴 完全不透明 |
| 👍 [Trae Pro](https://www.trae.ai/pricing) | $10 | $20 Basic + 随机Bonus | ❓ 无公开换算 | 🔴 完全不透明 |
| [Kiro Pro](https://kiro.dev/pricing) | $20 | 1000 credits; 超量$0.04/credit | ❓ 无公开换算 | 🔴 完全不透明 |
| [Augment Code INDIE](https://www.augmentcode.com/pricing) | $20 | 40000 credits | ❓ 无公开换算 | 🔴 完全不透明 |
| [Zed Pro](https://zed.dev/pricing) | $10 | $5 tokens(440万Claude Sonnet 4.6) + usage-based | ❓ 无公开换算 | 🔴 完全不透明 |

## 聚合中转商：每个模型的折扣率不同

中转商批发API→零售订阅。每个模型给的额度折扣不同，**多模型是卖点但单模型深度不如直营**。

| 中转商 | 月费 | 可用模型数 | 单模型相对直营折扣 | 计费透明度 |
|------|:--:|:--:|:--:|:--:|
| ⭐ [OpenCode Go](https://opencode.ai/go) | $10 | ~5个 | ~22% | 🟡 无单模型额度公开 |
| 👍 [Ollama Pro](https://ollama.com/pricing) | $20 | ~4个 | ~50x (vs Free) | 🔴 完全不透明 |
| 👍 [Fireworks Fire Pass](https://app.fireworks.ai/fire-pass) | $7/周 | ~1个 | ❓ 未公开 | 🟡 无单模型额度公开 |
| [OpenRouter](https://openrouter.ai) | 免费 | ~3个 | 限免, 无折扣率 | 🟡 限免规则公开但随时变 |
| ⭐ [NVIDIA NIM](https://build.nvidia.com) | 免费 | ~4个 | 限免, 无折扣率 | 🟡 限免规则公开但随时变 |

## 计费陷阱速查：每个厂商最坑的一项

| 厂商 | ⚠️ 最大陷阱 | 严重程度 |
|------|------|:--:|
| ⭐ [Claude Pro](https://claude.ai/upgrade) | 429频率极高, 名义倍率63.6但实际可用1/3 | 🔴 |
| ⭐ [ChatGPT Plus](https://chatgpt.com/pricing) | Local Messages定义模糊, 不同模式消耗不同 | 🟡 |
| ⭐ [Kimi Code Allegretto](https://www.kimi.com/membership/pricing) | K2.7偶尔死循环; 新会员体系权益拆分(Code独立购买) | 🟡 |
| [Kimi Code Andante](https://www.kimi.com/membership/pricing) | ¥49但额度只有Allegretto 1/20, 别买 | 🔴 |
| 👍 [GLM Coding Plan Pro](https://open.bigmodel.cn/glm-coding) | 高峰期14-18点3倍消耗+每日限量抢, 下午干活≈白付钱 | 🔴 |
| [GLM Coding Plan Lite](https://open.bigmodel.cn/glm-coding) | 5h仅80次, ¥49买了个寂寞 | 🔴 |
| 👍 [火山方舟 Coding Plan Lite](https://www.volcengine.com/activity/codingplan) | 每日限量释放, 抢不到当月白等 | 🔴 |
| [阿里云 Coding Plan Lite](https://www.aliyun.com/benefit/scene/tokenplan) | 已停售! 别找了; 转向更贵的Token Plan | 🔴 |
| ⭐ [MiniMax Coding Plan Plus](https://platform.minimaxi.com/subscribe/token-plan) | 数据是旧套餐的! 改版后实际额度待确认 | 🟡 |
| [小米 MiMo Token Plan Pro](https://platform.xiaomimimo.com/#/token-plan) | 有衰减+不兼容Codex Responses API | 🟡 |
| ⭐ [OpenCode Go](https://opencode.ai/go) | 单模型深度仅直营22%, 跑Kimi=1/5额度 | 🔴 |
| 👍 [Ollama Pro](https://ollama.com/pricing) | GPU时间计费完全不透明 | 🔴 |
| 👍 [Fireworks Fire Pass](https://app.fireworks.ai/fire-pass) | 仅一个模型, 套餐随时终止 | 🟡 |
| [OpenRouter](https://openrouter.ai) | 限免模型随时取消; 付费价不透明 | 🟡 |
| ⭐ [NVIDIA NIM](https://build.nvidia.com) | 免费不可持续! 随时取消/限速; 量化版影响质量 | 🟡 |
| 👍 [Cursor Pro](https://cursor.com/pricing) | credit/Token汇率厂商说了算, 随时可改 | 🔴 |
| 👍 [Windsurf Pro](https://windsurf.com/pricing) | msg/day不透明, 1 msg可能多次调用 | 🔴 |
| 👍 [GitHub Copilot Pro](https://github.com/features/copilot/plans) | credits消耗规则不公开 | 🔴 |
| 👍 [CodeBuddy 个人专业版](https://www.codebuddy.cn/pricing) | 加赠2000有效期仅1月, 赠费用完恢复2000 | 🟡 |
| 👍 [Trae Pro](https://www.trae.ai/pricing) | Bonus随机送, 不承诺额度 | 🟡 |
| [Kiro Pro](https://kiro.dev/pricing) | ⚠️退出付款页就丢失免费资格 | 🔴 |
| [Augment Code INDIE](https://www.augmentcode.com/pricing) | 40000 credits=多少Token? 无实测数据 | 🟡 |
| [Zed Pro](https://zed.dev/pricing) | $5/440万Token只是编辑器附加, 主力agent不够 | 🟡 |
| ⭐ [DeepSeek V4 Flash (API)](https://platform.deepseek.com) | 缓存命中率决定成本; 不复用prompt省不了 | 🟡 |
| 👍 [DeepSeek V4 Pro (API)](https://platform.deepseek.com) | 日常coding用V4 Flash够了, 别多花钱 | 🟡 |
| 👍 [Claude Opus 4.8 (API)](https://console.anthropic.com) | Agent输出Token通常>输入, 实际成本按$75/百万算 | 🔴 |
| ⭐ [GPT-5.6-Sol (API)](https://platform.openai.com) | 重度使用包月$20比API月$100+便宜很多 | 🟡 |
| 👍 [京东云 Coding Plan](https://www.jdcloud.com/cn/pages/codingplan) | 首购价仅1次, 恢复¥40; 多模型额度分配不透明 | 🟡 |
| [移动云 Coding Plan](https://ecloud.10086.cn/portal/act/codingplan) | 仅MiniMax M2.5一个模型 | 🟡 |
| [天翼云 Coding Plan](https://ctxirang.ctyun.cn/maas/codingPlan) | 比智谱Lite同价但额度更低 | 🟡 |
| 👍 [阶跃星辰 Step Plan](https://platform.stepfun.com/subscribe) | 推广期价格不承诺长期 | 🟡 |
| ⭐ [SuperGrok](https://grok.com/supergrok) | 免费层和付费层模型不同, Grok 4.5仅付费 | 🟡 |
| [SuperGrok Heavy](https://grok.com/supergrok) | 首3月67%折扣后恢复$300, 续费时注意 | 🟡 |
| ⭐ [Muse Spark 1.1 (API)](https://ai.meta.com/muse) | Contemplating并行agent消耗倍率未公开 | 🟡 |

---

> **避坑核心原则**：包月套餐看瓶颈闸门(不看月总量)、Credit套餐看换算黑盒(不买不明朗的)、API按量看重度时套餐更划算(不比价就亏)。


---

## 核心概念

- **每元 Token 数**：花 1 元买到多少 Token → **越大越好**
- **每亿 Token 成本**：买 1 亿 Token 要多少钱 → **越小越好**
- 表格中每个套餐名点击直达订阅页面

---

## 厂商直营 Coding Plan 详细数据

### 海外直营

| 套餐 | 价格 | 模型 | TPS | 月度 Token(亿) | 每元 Token 数 | 每亿 Token 成本 | 备注 |
|------|------|------|:--:|:--:|:--:|:--:|------|
| ⭐ [Claude Pro](https://claude.ai/upgrade) ($20/月) | $20 | Claude Fable 5 (Claude Code) | / | 15.88 | 7940万 | $1.3 | 2026.7 最新模型 Fable 5; 5h刷新359次/3966万Token; 周额度+50%; 倍率63.6碾压全场; 429频繁 |
| ⭐ [ChatGPT Plus](https://chatgpt.com/pricing) ($20/月) | $20 | GPT-5.6-Sol (Codex CLI) | / | 6.16 | 3080万 | $3.2 | GPT-5.6-Sol 最新旗舰; 45-225次/5h; 周2190次/1.54亿; 倍率21.8; 限流比Claude宽松 |
| ⭐ [SuperGrok](https://grok.com/supergrok) ($30/月) | $30 | Grok 4.5 (Grok Build) | / | N/A | N/A | N/A | xAI出品; Grok 4.5模型; 图文视频生成; Grok Build Agent; X实时搜索; 多Agent并发推理(Contemplating模式) |
| [SuperGrok Heavy](https://grok.com/supergrok) ($300/月) | $300 | Grok 4.5 (最高额度) | / | N/A | N/A | N/A | 16个专家模式Agent并行; 最高使用上限; 专属支持+抢先体验; 首3月67%折扣 |

### 国内直营

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

---

## 聚合中转商

| 套餐 | 价格 | 模型 | TPS | 月度 Token(亿) | 每元 Token 数 | 每亿 Token 成本 | 备注 |
|------|------|------|:--:|:--:|:--:|:--:|------|
| ⭐ [OpenCode Go](https://opencode.ai/go) ($10/月 (首月 $5)) | $10 | GLM-5.2/Kimi K2.7/DeepSeek V4 Pro/Qwen3.6/MiniMax M2.7 等 | / | 3.22 | 3220万 | $3.1 | 多模型聚合; 倍率 6; 支持多种 Agent harness |
| ⭐ [NVIDIA NIM](https://build.nvidia.com) (免费) | 免费 | DeepSeek V4 Pro/GLM-5.2/DeepSeek V4 Flash/MiniMax M2.7 | / | N/A | 免费 🎁 | 免费 | 不限量白嫖首选; 速度无保证; 部分模型为量化版; 免费不可持续 |
| 👍 [Ollama Pro](https://ollama.com/pricing) ($20/月) | $20 | GLM-5.2/MiniMax M2.7/Qwen3.6/DeepSeek V4 Flash 等 | / | 11.12 | 5560万 | $1.8 | Free 版 50x; 开源模型为主; 估值为近似值 |
| 👍 [Fireworks Fire Pass](https://app.fireworks.ai/fire-pass) ($7/周) | $7/周 | Kimi K2.6 Turbo | / | N/A | N/A | N/A | Kimi K2.6 Turbo 无限 Token 调用; 周付模式灵活 |
| [OpenRouter](https://openrouter.ai) (部分模型限免) | 免费 | 多模型 (HY3-Preview/MiniMax M2.7/DeepSeek V4 Pro 等) | / | N/A | 免费 🎁 | 免费 | 中转聚合平台, 按用量计费; 部分限免模型 |

---

## AI IDE 聚合

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

---

## API 按量计费

### 国内

| 模型 | 输入价格 | 备注 |
|------|:--:|------|
| ⭐ [DeepSeek V4 Flash (API)](https://platform.deepseek.com) | ¥1/百万输入Token | 性价比最高按量方案; 输出 ¥2/百万; 缓存读 1/100 价格; 1M 上下文 |
| 👍 [DeepSeek V4 Pro (API)](https://platform.deepseek.com) | ¥3/百万输入Token | V4 Flash 的 3 倍价格; 推理能力更强; 1M 上下文 |
| 👍 [Kimi K2.6 (API)](https://platform.moonshot.cn) | ¥20/百万输入Token | 支持多模态; 256K 上下文; 价格偏高但质量稳定 |
| 👍 [GLM 5.1 (API)](https://open.bigmodel.cn) | ¥10/百万输入Token | 198K 上下文; SWE-Bench Pro SOTA; 性价比好 |

### 海外

| 模型 | 输入价格 | 备注 |
|------|:--:|------|
| ⭐ [GPT-5.6-Sol (API)](https://platform.openai.com) | $3/百万输入Token | 输出 $12/百万; 性价比远好于 Claude API |
| ⭐ [Muse Spark 1.1 (API)](https://ai.meta.com/muse) | $1.25/百万输入Token | Meta首款付费API模型; 输出$4.25/百万; 1M上下文; Thinking/Contemplating双推理模式; 多Agent并行推理; SWE-bench Pro 58.6; MCP Atlas 88.1 |
| 👍 [Claude Opus 4.8 (API)](https://console.anthropic.com) | $15/百万输入Token | 输出 $75/百万; 昂贵但能力顶级; 缓存写 $3.75 读 $0.30 |

---

## 选购决策树

```
你每天写代码几个小时？
├── < 2 小时 → API 按量计费（DeepSeek V4 Flash）
├── 2-6 小时 → Coding Plan 包月
│   ├── 在国内？
│   │   ├── 不怕抢 → GLM Pro ¥149（代码最强）
│   │   ├── 要多模态+不限速 → Kimi Allegretto ¥159-199
│   │   ├── 极致省钱 → MiniMax ¥49（模型较弱+数据旧）
│   │   └── 运营商省心 → 京东云 ¥19.9（首购）/ 移动云 ¥7.9（首月）
│   └── 在海外？
│       ├── 最强模型 → Claude Pro $20（忍429）
│       ├── 稳定体验 → ChatGPT Plus $20
│       └── 多模型切换 → OpenCode Go $10
└── > 6 小时（重度）→ Coding Plan + API 双轨
    ├── 主力：Claude Pro 或 Kimi Allegretto
    └── 溢出：DeepSeek V4 Flash API 兜底
```

---

*数据更新：2026-07-15 · 由 [awesome-coding-cost](https://github.com/justin-mc-lai/awesome-coding-cost) 分析生成 · 参考 [awesome-coding-plan](https://github.com/mahonzhan/awesome-coding-plan)*

---

## 📊 数据说明

### 计费规则统一图鉴

本次更新重构了对比结构，新增 6 个子板块统一呈现所有厂商的计费套路：

1. **计费模式速查矩阵** — 36个套餐的计费模式+额度+限流+陷阱一表打尽
2. **三层闸门深度拆解** — 5h/周/月哪层是实际瓶颈
3. **限流机制横向对比** — 429频率+高峰期规则+多Agent并发
4. **Credit 黑盒换算** — 列出所有用积分/credits 计费的套餐
5. **聚合商模型倍数** — 每个中转商的折扣率 vs 直营
6. **计费陷阱速查** — 每个厂商最坑的一个设计+严重程度

### 每元 Token 数 / 每亿 Token 成本

来自 [awesome-coding-plan Issue #24](https://github.com/mahonzhan/awesome-coding-plan/issues/24)：
- **每元 Token 数** = 月度 Token 额度 ÷ 包月价格 → 越大越好
- **每亿 Token 成本** = 包月价格 ÷ 月度 Token 额度(亿) → 越小越好

Credit/请求数计费套餐无法计算，标注 N/A。

### 模型版本

更新至 **2026-07-15**：Claude Fable 5, Kimi K2.7, GLM 5.2, GPT-5.6-Sol, Grok 4.5, Muse Spark 1.1。

### 更新频率

每 2-4 周更新。发现数据过时或新套餐，欢迎提 Issue/PR。

---

## 🤝 贡献

1. Fork 本仓库
2. 修改 `data.yaml`
3. 运行 `python3 scripts/gen.py --data data.yaml --template README.tpl.md --output README_NEW.md`
4. 提交 PR

---

## 📜 协议

[CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)

数据来源包含 [awesome-coding-plan](https://github.com/mahonzhan/awesome-coding-plan) 的公开数据，遵循其 CC BY 4.0 协议。

---

*本仓库由 [库拾创作台](https://github.com/justin-mc-lai/selfmedia-creator) 半自动维护 · 微信公众号：Github 库拾*
