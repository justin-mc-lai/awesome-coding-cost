# 💰 Awesome Coding Cost

[![License: CC BY 4.0](https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/)
[![Updated](https://img.shields.io/badge/updated-2026--07--15-green)](README.md)

> 各大模型/云厂商/聚合商/AI IDE Coding Plan 实际成本对比 — 每元能买多少 Token？
>
> 受 [awesome-coding-plan](https://github.com/mahonzhan/awesome-coding-plan) 启发，覆盖厂商直营、聚合中转、AI IDE、API 按量四大类。

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
| ⭐ [Claude Pro](https://claude.ai/upgrade) | $20/月 | 🔄 5h刷新 | 官方动态限额, 不公开固定Token | 使用上限随模型/负载变化 | 未公开固定Token月包 | 高峰期/长上下文/多Agent会更快触发限流; 官方未给固定可用Token | 不要用社区推算Token倍率当官方额度; 实际瓶颈是动态限流 |
| ⭐ [ChatGPT Plus](https://chatgpt.com/pricing) | $20/月 | 📦 月总量 | - | - | Plus订阅含动态使用限制, 不公开固定Token | Agent、Chat、Codex 等入口消耗口径不同; 高峰期和模型选择会影响可... | 官方未给固定Token额度, Agent模式和普通Chat不能直接按次数等价 |
| ⭐ [Kimi Code Allegretto](https://www.kimi.com/membership/pricing) | ¥199/月 | 📦 月总量 | 5小时/周频控以页面提示为准 | - | Kimi Code 20倍额度; Agent约150个; 额度月刷新 | 官方说明5小时及周频控以页面提示为准; 固定Token总量未公开 | 共享额度池不等于固定Token月包, Agent/Kimi Code会互相消耗同一额度 |
| [Kimi Code Andante](https://www.kimi.com/membership/pricing) | ¥49/月 | 📦 月总量 | 5小时/周频控以页面提示为准 | - | Kimi Code 1倍额度; Agent约30个; 额度月刷新 | 额度明显低于Allegretto; 固定Token总量未公开 | Kimi Code只有1倍额度, 不能按旧版社区Token估算当重度Coding包 |
| 👍 [GLM Coding Plan Pro](https://open.bigmodel.cn/glm-coding) | ¥149/月 | 🔄 5h刷新 | 400次 prompt | 2000次 | 8000次/6.4亿 | 高峰期14-18点3倍额度消耗!!! 每日10:00限量释放; Max秒售罄; ... | 高峰期3倍扣+每日限量的双重暴击, 下午干活≈1/3额度; 海外版涨价近翻倍 |
| [GLM Coding Plan Lite](https://open.bigmodel.cn/glm-coding) | ¥49/月 | 🔄 5h刷新 | 80次 | 400次 | 1600次/1.28亿 | 高峰期3倍消耗; 5h仅80次, 两个复杂任务就见底 | ¥49但5h/80次=跑两次重agent就等刷新, 性价比倒数第1 |
| 👍 [火山方舟 Coding Plan Lite](https://www.volcengine.com/activity/codingplan) | ¥40/月 | 🔄 5h刷新 | 148次/1000万Token | - | 6275次/3.2亿 | 每日00:00限量释放库存, 售完即止, 需抢 | 抢不到就当月白等; TPS 86.6最快但没库存也没用 |
| [阿里云 Coding Plan Lite](https://www.aliyun.com/benefit/scene/tokenplan) | 历史套餐(已下线) | 📦 月总量 | - | - | 已下线, 不再售卖 | 历史套餐不可新购/续费; 以百炼最新页面为准 | 已下线套餐不能继续拿旧额度做当前性价比对比 |
| ⭐ [MiniMax Coding Plan Plus](https://platform.minimaxi.com/subscribe/token-plan) | ¥49/月 | 📦 月总量 | - | - | 公开页未确认固定Token额度 | 套餐/额度可能随账号状态变化; 新旧套餐口径需登录核对 | 旧24亿Token估算未能官方确认, 不能继续当准确额度 |
| [小米 MiMo Token Plan Pro](https://platform.xiaomimimo.com/#/token-plan) | ¥329/月 | 🎲 Credit黑盒 | - | - | 380亿 Credits/月, ¥329 | 多agent并发易429; 模型稳定性待观察; 有衰减 | Credits不是Token, 折算比例和衰减规则不透明 |
| ⭐ [OpenCode Go](https://opencode.ai/go) | $10/月 (首月 $5) | 📦 月总量 | - | - | $10(首月$5) 无限制 | 多模型聚合; 不支持搜索 | 官方未公开单模型固定Token额度, 不能按直营额度等比例推算 |
| 👍 [Ollama Pro](https://ollama.com/pricing) | $20/月 | ⏱️ GPU计时 | - | - | $20 GPU时间计费(不透明) | 开源模型为主; Free版50x | GPU时间计费完全不透明, 用户不知道花$20买到了多少GPU秒 |
| 👍 [Fireworks Fire Pass](https://app.fireworks.ai/fire-pass) | $7/周 | 📦 月总量 | - | $7/周 Kimi K2.6 Turbo无限Token | - | 周付灵活但仅有Kimi K2.6 Turbo | 仅有一个模型; Fire Pass套餐可能随时终止 |
| [OpenRouter](https://openrouter.ai) | 部分模型限免 | 🆓 限免 | - | - | - | 中转聚合; 按量计费; 模型来源和稳定性依赖上游 | 限免模型随时可能取消; 付费模型按tokens计费价格不透明 |
| ⭐ [NVIDIA NIM](https://build.nvidia.com) | 免费 | 🆓 限免 | - | - | - | 免费但不限速保证; 部分模型为量化版; 首Token延迟高 | 免费不可持续! 随时取消/限速; 量化版可能模型质量低于API版 |
| 👍 [Cursor Pro](https://cursor.com/pricing) | $20/月 | 🎲 Credit黑盒 | - | - | $20 credit($20 API usage) | Usage-based; 超额按量付费 | 1 credit ≠ 固定Token数; 厂商可随时调整credit/Token汇率 |
| 👍 [Windsurf Pro](https://windsurf.com/pricing) | $20/月 (2周试用) | 🎲 Credit黑盒 | - | 日/周预算, 不公开固定Token | - | SWE-1.5不限量; Premium Model限msg数 | 预算/msg口径不等于固定Token, 一个任务可能消耗多次模型调用 |
| 👍 [GitHub Copilot Pro](https://github.com/features/copilot/plans) | $10/月 | 🎲 Credit黑盒 | - | - | 300 premium requests | IDE原生集成; 补全+Chat混合 | premium request不是Token; 不同模型/Agent调用消耗口径不同 |
| 👍 [CodeBuddy 个人标准版](https://www.codebuddy.cn/docs/ide/Account/pricing) | ¥99/月 | 🎲 Credit黑盒 | - | - | 2000基础Credits/月; 2026-09-30前每月加赠2000; 超量包3000 Credits/¥30起 | Credits消耗按模型/任务变化; 加赠有截止日期 | 旧¥59个人专业版口径已过期; 加赠Credits不是永久权益 |
| 👍 [Trae Pro](https://www.trae.ai/pricing) | $10/月 (7天免费) | 🎲 Credit黑盒 | - | - | $20 Basic + 随机Bonus | 字节出品; 补全不限量 | Bonus随机送, 不承诺额度; 有拿到$130的也有拿$5的 |
| [Kiro Pro](https://kiro.dev/pricing) | $20/月 (首月免费) | 🎲 Credit黑盒 | - | - | 1000 credits; 超量$0.04/credit | 首月免费; 退出付款页丢失免费资格! | ⚠️退出付款页就丢失免费资格! 不要试 |
| [Augment Code INDIE](https://www.augmentcode.com/pricing) | $20/月 | 🎲 Credit黑盒 | - | - | 40000 credits | 新玩家, 数据不多 | 40000 credits到底能跑多少agent? 没有实测数据 |
| [Zed Pro](https://zed.dev/pricing) | $10/月 | 🎲 Credit黑盒 | - | - | $5 included AI usage + usage-based | 编辑器原生; 补全不限 | $5 included usage不是固定Token; 主力Agent会很快进入按量付费 |
| ⭐ [DeepSeek V4 Flash (API)](https://platform.deepseek.com) | 按量计费 | ⚡ API按量 | - | - | - | TPS 50+; 1M上下文 | 价格已改为官方美元口径; 缓存命中率决定实际成本 |
| 👍 [DeepSeek V4 Pro (API)](https://platform.deepseek.com) | 按量计费 | ⚡ API按量 | - | - | - | V4 Flash的3倍价; 推理更强 | 日常coding V4 Flash够用; Pro只有硬核推理才值差价 |
| 👍 [Kimi K2.7 Code (API)](https://platform.kimi.ai) | 按量计费 | ⚡ API按量 | - | - | - | 以平台RPM/TPM为准; 缓存命中可显著降低输入成本 | 价格已改为官方美元口径; 长Agent输出多时成本主要在输出Token |
| 👍 [GLM 5.1 (API)](https://open.bigmodel.cn) | 按量计费 | ⚡ API按量 | - | - | - | 198K上下文; SWE-bench Pro SOTA | Pro套餐¥149/6.4亿比API便宜10倍, 选套餐别用API |
| 👍 [Claude Opus 4.8 (API)](https://console.anthropic.com) | 按量计费 | ⚡ API按量 | - | - | - | 输出价是输入的5倍; agent场景输出Token占比高 | Agent场景输出Token通常>输入Token; 实际成本看输出而不是只看$5输入价 |
| ⭐ [GPT-5.6-Sol (API)](https://platform.openai.com) | 按量计费 | ⚡ API按量 | - | - | - | 输出价是输入的6倍; Agent任务成本随输出Token放大 | 和ChatGPT Plus比, 重度使用包月更划算(月$20 vs API月$100+) |
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
| ⭐ [Claude Pro](https://claude.ai/upgrade) | 官方动态限额, 不公开固定Token | 使用上限随模型/负载变化 | 未公开固定Token月包 | 5h刷新→看单次用量 |
| 👍 [GLM Coding Plan Pro](https://open.bigmodel.cn/glm-coding) | 400次 prompt | 2000次 | 8000次/6.4亿 | ⚠️ 高峰期3倍消耗→5h窗口秒空 |
| [GLM Coding Plan Lite](https://open.bigmodel.cn/glm-coding) | 80次 | 400次 | 1600次/1.28亿 | ⚠️ 高峰期3倍消耗→5h窗口秒空 |
| 👍 [火山方舟 Coding Plan Lite](https://www.volcengine.com/activity/codingplan) | 148次/1000万Token | - | 6275次/3.2亿 | ⛔ 需抢库存, 抢不到=没额度 |
| [移动云 Coding Plan](https://ecloud.10086.cn/portal/act/codingplan) | 1200次 | 9000次 | 18000次 | 5h刷新→看单次用量 |
| [天翼云 Coding Plan](https://ctxirang.ctyun.cn/maas/codingPlan) | 80次 | 400次 | 1600次 | 5h刷新→看单次用量 |
| 👍 [阶跃星辰 Step Plan](https://platform.stepfun.com/subscribe) | ~100次(Mini) / ~400次(Plus) / ~1500次(Pro) | - | 全档位高速推理不加价 | 5h刷新→看单次用量 |

## 限流机制横向对比

| 厂商 | 429频率 | 触发条件 | 高峰期特殊规则 | 多Agent并发 |
|------|:--:|------|------|:--:|
| ⭐ [Claude Pro](https://claude.ai/upgrade) | 🔴 极高 | 正常时段也频繁 | 无明显高峰规则 | ❌ |
| ⭐ [ChatGPT Plus](https://chatgpt.com/pricing) | 🟡 中等 | Local Msg定义模糊 | 无明显高峰规则 | ⚠️ |
| ⭐ [Kimi Code Allegretto](https://www.kimi.com/membership/pricing) | 🟡 中等 | 共享额度池; 页面频控 | 5h/周规则以页面提示为准 | ⚠️ |
| 👍 [GLM Coding Plan Pro](https://open.bigmodel.cn/glm-coding) | 🔴 极高 | 14-18点3倍消耗 | ⛔ 高峰期3倍扣+抢购 | ❌ |
| 👍 [火山方舟 Coding Plan Lite](https://www.volcengine.com/activity/codingplan) | 🟡 中等 | 每日00:00限量释放 | 库存售完即止 | ⚠️ |
| ⭐ [MiniMax Coding Plan Plus](https://platform.minimaxi.com/subscribe/token-plan) | 🟡 待确认 | 官方额度需登录核对 | 不明显 | ⚠️ |
| ⭐ [NVIDIA NIM](https://build.nvidia.com) | 🟡 中等 | 40 rpm硬限 | 无 | ⚠️ |

## Credit 黑盒：你不知道 1 Credit = 多少 Token

这些套餐用 credits/请求数计费，**厂商可以随时调整 credit ↔ Token 汇率而不通知你**。

| 厂商 | 月费 | 月Credits | 已知换算（如果公开） | 不透明程度 |
|------|:--:|:--:|------|:--:|
| [小米 MiMo Token Plan Pro](https://platform.xiaomimimo.com/#/token-plan) | ¥329 | 380亿 Credits/月, ¥329 | ❓ 无公开换算 | 🔴 完全不透明 |
| 👍 [Cursor Pro](https://cursor.com/pricing) | $20 | $20 credit($20 API usage) | ❓ 仅标注$额, 无Token数 | 🔴 完全不透明 |
| 👍 [Windsurf Pro](https://windsurf.com/pricing) | $20 | 日/周预算, 不公开固定Token | ❓ 无公开换算 | 🔴 完全不透明 |
| 👍 [GitHub Copilot Pro](https://github.com/features/copilot/plans) | $10 | 300 premium requests | ❓ 无公开换算 | 🔴 完全不透明 |
| 👍 [CodeBuddy 个人标准版](https://www.codebuddy.cn/docs/ide/Account/pricing) | ¥99 | 2000基础Credits/月; 2026-09-30前每月加赠2000; 超量包3000 Credits/¥30起 | ❓ 无公开换算 | 🔴 完全不透明 |
| 👍 [Trae Pro](https://www.trae.ai/pricing) | $10 | $20 Basic + 随机Bonus | ❓ 无公开换算 | 🔴 完全不透明 |
| [Kiro Pro](https://kiro.dev/pricing) | $20 | 1000 credits; 超量$0.04/credit | ❓ 无公开换算 | 🔴 完全不透明 |
| [Augment Code INDIE](https://www.augmentcode.com/pricing) | $20 | 40000 credits | ❓ 无公开换算 | 🔴 完全不透明 |
| [Zed Pro](https://zed.dev/pricing) | $10 | $5 included AI usage + usage-based | ❓ 无公开换算 | 🔴 完全不透明 |

## 聚合中转商：每个模型的折扣率不同

中转商批发API→零售订阅。每个模型给的额度折扣不同，**多模型是卖点但单模型深度不如直营**。

| 中转商 | 月费 | 可用模型数 | 单模型相对直营折扣 | 计费透明度 |
|------|:--:|:--:|:--:|:--:|
| ⭐ [OpenCode Go](https://opencode.ai/go) | $10 | 动态 | ❓ 未公开 | 🟡 无单模型额度公开 |
| 👍 [Ollama Pro](https://ollama.com/pricing) | $20 | 动态 | ~50x (vs Free) | 🔴 完全不透明 |
| 👍 [Fireworks Fire Pass](https://app.fireworks.ai/fire-pass) | $7/周 | ~1个 | ❓ 未公开 | 🟡 无单模型额度公开 |
| [OpenRouter](https://openrouter.ai) | 免费 | 动态 | 限免, 无折扣率 | 🟡 限免规则公开但随时变 |
| ⭐ [NVIDIA NIM](https://build.nvidia.com) | 免费 | ~4个 | 限免, 无折扣率 | 🟡 限免规则公开但随时变 |

## 计费陷阱速查：每个厂商最坑的一项

| 厂商 | ⚠️ 最大陷阱 | 严重程度 |
|------|------|:--:|
| ⭐ [Claude Pro](https://claude.ai/upgrade) | 不要用社区推算Token倍率当官方额度; 实际瓶颈是动态限流 | 🟡 |
| ⭐ [ChatGPT Plus](https://chatgpt.com/pricing) | 官方未给固定Token额度, Agent模式和普通Chat不能直接按次数等价 | 🟡 |
| ⭐ [Kimi Code Allegretto](https://www.kimi.com/membership/pricing) | 共享额度池不等于固定Token月包, Agent/Kimi Code会互相消耗同一额度 | 🟡 |
| [Kimi Code Andante](https://www.kimi.com/membership/pricing) | Kimi Code只有1倍额度, 不能按旧版社区Token估算当重度Coding包 | 🟡 |
| 👍 [GLM Coding Plan Pro](https://open.bigmodel.cn/glm-coding) | 高峰期3倍扣+每日限量的双重暴击, 下午干活≈1/3额度; 海外版涨价近翻倍 | 🔴 |
| [GLM Coding Plan Lite](https://open.bigmodel.cn/glm-coding) | ¥49但5h/80次=跑两次重agent就等刷新, 性价比倒数第1 | 🔴 |
| 👍 [火山方舟 Coding Plan Lite](https://www.volcengine.com/activity/codingplan) | 抢不到就当月白等; TPS 86.6最快但没库存也没用 | 🔴 |
| [阿里云 Coding Plan Lite](https://www.aliyun.com/benefit/scene/tokenplan) | 已下线套餐不能继续拿旧额度做当前性价比对比 | 🔴 |
| ⭐ [MiniMax Coding Plan Plus](https://platform.minimaxi.com/subscribe/token-plan) | 旧24亿Token估算未能官方确认, 不能继续当准确额度 | 🟡 |
| [小米 MiMo Token Plan Pro](https://platform.xiaomimimo.com/#/token-plan) | Credits不是Token, 折算比例和衰减规则不透明 | 🟡 |
| ⭐ [OpenCode Go](https://opencode.ai/go) | 官方未公开单模型固定Token额度, 不能按直营额度等比例推算 | 🟡 |
| 👍 [Ollama Pro](https://ollama.com/pricing) | GPU时间计费完全不透明, 用户不知道花$20买到了多少GPU秒 | 🔴 |
| 👍 [Fireworks Fire Pass](https://app.fireworks.ai/fire-pass) | 仅有一个模型; Fire Pass套餐可能随时终止 | 🟡 |
| [OpenRouter](https://openrouter.ai) | 限免模型随时可能取消; 付费模型按tokens计费价格不透明 | 🟡 |
| ⭐ [NVIDIA NIM](https://build.nvidia.com) | 免费不可持续! 随时取消/限速; 量化版可能模型质量低于API版 | 🟡 |
| 👍 [Cursor Pro](https://cursor.com/pricing) | 1 credit ≠ 固定Token数; 厂商可随时调整credit/Token汇率 | 🔴 |
| 👍 [Windsurf Pro](https://windsurf.com/pricing) | 预算/msg口径不等于固定Token, 一个任务可能消耗多次模型调用 | 🟡 |
| 👍 [GitHub Copilot Pro](https://github.com/features/copilot/plans) | premium request不是Token; 不同模型/Agent调用消耗口径不同 | 🟡 |
| 👍 [CodeBuddy 个人标准版](https://www.codebuddy.cn/docs/ide/Account/pricing) | 旧¥59个人专业版口径已过期; 加赠Credits不是永久权益 | 🟡 |
| 👍 [Trae Pro](https://www.trae.ai/pricing) | Bonus随机送, 不承诺额度; 有拿到$130的也有拿$5的 | 🟡 |
| [Kiro Pro](https://kiro.dev/pricing) | ⚠️退出付款页就丢失免费资格! 不要试 | 🔴 |
| [Augment Code INDIE](https://www.augmentcode.com/pricing) | 40000 credits到底能跑多少agent? 没有实测数据 | 🟡 |
| [Zed Pro](https://zed.dev/pricing) | $5 included usage不是固定Token; 主力Agent会很快进入按量付费 | 🟡 |
| ⭐ [DeepSeek V4 Flash (API)](https://platform.deepseek.com) | 价格已改为官方美元口径; 缓存命中率决定实际成本 | 🟡 |
| 👍 [DeepSeek V4 Pro (API)](https://platform.deepseek.com) | 日常coding V4 Flash够用; Pro只有硬核推理才值差价 | 🟡 |
| 👍 [Kimi K2.7 Code (API)](https://platform.kimi.ai) | 价格已改为官方美元口径; 长Agent输出多时成本主要在输出Token | 🟡 |
| 👍 [GLM 5.1 (API)](https://open.bigmodel.cn) | Pro套餐¥149/6.4亿比API便宜10倍, 选套餐别用API | 🔴 |
| 👍 [Claude Opus 4.8 (API)](https://console.anthropic.com) | Agent场景输出Token通常>输入Token; 实际成本看输出而不是只看$5输入价 | 🟡 |
| ⭐ [GPT-5.6-Sol (API)](https://platform.openai.com) | 和ChatGPT Plus比, 重度使用包月更划算(月$20 vs API月$100+) | 🟡 |
| 👍 [京东云 Coding Plan](https://www.jdcloud.com/cn/pages/codingplan) | 首购¥19.9后恢复¥40; 近50款模型但每个模型额度分配不透明 | 🟡 |
| [移动云 Coding Plan](https://ecloud.10086.cn/portal/act/codingplan) | 运营商网络虽稳但模型单一; 首月¥7.9后¥40 | 🟡 |
| [天翼云 Coding Plan](https://ctxirang.ctyun.cn/maas/codingPlan) | 比智谱Lite同价但额度更低, 买之前先比GLM官网 | 🟡 |
| 👍 [阶跃星辰 Step Plan](https://platform.stepfun.com/subscribe) | 推广期价格不承诺长期; 海外$9.99比国内¥99更便宜 | 🟡 |
| ⭐ [SuperGrok](https://grok.com/supergrok) | 免费层和付费层模型可能不同(Grok 4.5仅付费) | 🟡 |
| [SuperGrok Heavy](https://grok.com/supergrok) | 首3月67%折扣后恢复$300, 注意续费时间 | 🟡 |
| ⭐ [Muse Spark 1.1 (API)](https://ai.meta.com/muse) | Contemplating模式并行agent消耗倍率未公开; 美国区可用 | 🟡 |

---

> **避坑核心原则**：包月套餐看瓶颈闸门(不看月总量)、Credit套餐看换算黑盒(不买不明朗的)、API按量看重度时套餐更划算(不比价就亏)。


---

## 核心概念

- **每元 Token 数**：花 1 元买到多少 Token → **越大越好**
- **每亿 Token 成本**：买 1 亿 Token 要多少钱 → **越小越好**
- 表格中每个套餐名点击直达订阅页面
- **核实口径**：只对官方公开固定 Token 额度的套餐计算倍率；动态限额、Credits、GPU 时间、消息数、社区估算一律标为 `N/A`，避免把推算当官方承诺

---

## 厂商直营 Coding Plan 详细数据

### 海外直营

| 套餐 | 价格 | 模型 | TPS | 月度 Token(亿) | 每元 Token 数 | 每亿 Token 成本 | 备注 |
|------|------|------|:--:|:--:|:--:|:--:|------|
| ⭐ [Claude Pro](https://claude.ai/upgrade) ($20/月) | $20 | Claude Fable 5 (Claude Code) | / | N/A | N/A | N/A | Claude Pro $20/月; Claude Code/Claude 使用上限会随模型、上下文、负载动态变化; 官方未公开固定Token月包 |
| ⭐ [ChatGPT Plus](https://chatgpt.com/pricing) ($20/月) | $20 | GPT-5.6-Sol (Codex CLI) | / | N/A | N/A | N/A | ChatGPT Plus $20/月; Codex/Agent/Chat 使用限制按官方实时规则与负载调整; 官方未公开固定Token月包 |
| ⭐ [SuperGrok](https://grok.com/supergrok) ($30/月) | $30 | Grok 4.5 (Grok Build) | / | N/A | N/A | N/A | xAI出品; Grok 4.5模型; 图文视频生成; Grok Build Agent; X实时搜索; 多Agent并发推理(Contemplating模式) |
| [SuperGrok Heavy](https://grok.com/supergrok) ($300/月) | $300 | Grok 4.5 (最高额度) | / | N/A | N/A | N/A | 16个专家模式Agent并行; 最高使用上限; 专属支持+抢先体验; 首3月67%折扣 |

### 国内直营

| 套餐 | 价格 | 模型 | TPS | 月度 Token(亿) | 每元 Token 数 | 每亿 Token 成本 | 备注 |
|------|------|------|:--:|:--:|:--:|:--:|------|
| ⭐ [Kimi Code Allegretto](https://www.kimi.com/membership/pricing) (¥199/月) | ¥199 | Kimi K2.7 Code | / | N/A | N/A | N/A | Kimi 会员Allegretto ¥199/月; Kimi Code 20倍额度; Agent用量约150个; 所有会员功能共享额度池并按Token消耗 |
| ⭐ [MiniMax Coding Plan Plus](https://platform.minimaxi.com/subscribe/token-plan) (¥49/月) | ¥49 | MiniMax M2.7 (MIT 开源, 10B 激活) | / | N/A | N/A | N/A | 旧社区数据无法从公开官方页稳定核验; 暂不采用24亿Token/月估算; 以官方订阅页/账号内额度为准 |
| 👍 [GLM Coding Plan Pro](https://open.bigmodel.cn/glm-coding) (¥149/月) | ¥149 | GLM 5.2 | 26 | 6.4 | 430万 | ¥23.3 | 代码能力国内最强; 不支持多模态; 高峰期(14-18)3倍额度; 算力紧缺需抢购; 2026年已涨3次价 |
| 👍 [火山方舟 Coding Plan Lite](https://www.volcengine.com/activity/codingplan) (¥40/月) | ¥40 | 豆包 Seed 2.0 Pro | 86 | 3.2 | 800万 | ¥12.5 | 每日00:00限量释放; TPS 86.6 最快; 倍率15.18; 国内唯一原生支持Codex Responses API |
| 👍 [京东云 Coding Plan](https://www.jdcloud.com/cn/pages/codingplan) (¥19.9/月起(首购)) | ¥19.9 | DeepSeek V4/GLM 5.2/MiniMax M2.7/Qwen3.6/Kimi K2.7 等 | / | N/A | N/A | N/A | 首购¥19.9最低价; Pro ¥99.9(90000次/月); 每天10:30开抢; 近50款模型 |
| 👍 [阶跃星辰 Step Plan](https://platform.stepfun.com/subscribe) (¥49/月起) | ¥49 | Step-3.5-Flash (196B/11B 激活) | / | N/A | N/A | N/A | 全档位高速推理不加价; 用量为同档友商2倍+; 推广期价格; 海外$9.99比国内¥99略便宜 |
| [Kimi Code Andante](https://www.kimi.com/membership/pricing) (¥49/月) | ¥49 | Kimi K2.7 Code | / | N/A | N/A | N/A | Kimi 会员Andante ¥49/月; Kimi Code 1倍额度; Agent用量约30个; 适合轻量体验 |
| [GLM Coding Plan Lite](https://open.bigmodel.cn/glm-coding) (¥49/月) | ¥49 | GLM 5.2 | 26 | 1.28 | 261万 | ¥38.3 | Pro 1/5 额度; 5h仅80次; 高峰期3倍消耗; 毫无性价比 |
| [阿里云 Coding Plan Lite](https://www.aliyun.com/benefit/scene/tokenplan) (历史套餐(已下线)) | 已下线 | Qwen 3.5 Plus | / | N/A | N/A | N/A | 历史Coding Plan Lite已停售/停续费; 后续转向百炼Token Plan/资源包; 不再参与现价比价 |
| [小米 MiMo Token Plan Pro](https://platform.xiaomimimo.com/#/token-plan) (¥329/月) | ¥329 | MiMo V2.5 Pro (1T MoE) | 46 | N/A | N/A | N/A | 官方口径为Credits/月, 不是直接Token月包; 1T MoE, 100万上下文; 多agent并发易429; 稳定性待观察 |
| [移动云 Coding Plan](https://ecloud.10086.cn/portal/act/codingplan) (¥7.9/月起(首月)) | ¥7.9 | MiniMax M2.5 | / | N/A | N/A | N/A | 运营商首家Coding Plan; 首月¥7.9后¥40; Pro ¥200; 广东另有AI融合套餐 |
| [天翼云 Coding Plan](https://ctxirang.ctyun.cn/maas/codingPlan) (¥49/月起) | ¥49 | GLM-5.2/GLM-5.1/GLM-4.7 等 | / | N/A | N/A | N/A | 电信运营商; 与智谱共享模型但额度更低; 每日10:00释放库存 |

---

## 聚合中转商

| 套餐 | 价格 | 模型 | TPS | 月度 Token(亿) | 每元 Token 数 | 每亿 Token 成本 | 备注 |
|------|------|------|:--:|:--:|:--:|:--:|------|
| ⭐ [OpenCode Go](https://opencode.ai/go) ($10/月 (首月 $5)) | $10 | 多模型聚合 | / | N/A | N/A | N/A | OpenCode Go $10/月(首月$5); 多模型聚合; 具体模型池和单模型限额可能变化 |
| ⭐ [NVIDIA NIM](https://build.nvidia.com) (免费) | 免费 | DeepSeek V4 Pro/GLM-5.2/DeepSeek V4 Flash/MiniMax M2.7 | / | N/A | 免费 🎁 | 免费 | 不限量白嫖首选; 速度无保证; 部分模型为量化版; 免费不可持续 |
| 👍 [Ollama Pro](https://ollama.com/pricing) ($20/月) | $20 | Ollama 托管模型 | / | N/A | N/A | N/A | 官方Pro $20/月; Free版50x; 开源/托管模型为主; GPU时间/额度不是Token月包 |
| 👍 [Fireworks Fire Pass](https://app.fireworks.ai/fire-pass) ($7/周) | $7/周 | Kimi K2.6 Turbo | / | N/A | N/A | N/A | Kimi K2.6 Turbo 无限 Token 调用; 周付模式灵活 |
| [OpenRouter](https://openrouter.ai) (部分模型限免) | 免费 | 多模型 (HY3-Preview/MiniMax M2.7/DeepSeek V4 Pro 等) | / | N/A | 免费 🎁 | 免费 | 中转聚合平台, 按用量计费; 部分限免模型 |

---

## AI IDE 聚合

| 套餐 | 价格 | 模型 | TPS | 月度 Token(亿) | 每元 Token 数 | 每亿 Token 成本 | 备注 |
|------|------|------|:--:|:--:|:--:|:--:|------|
| 👍 [Cursor Pro](https://cursor.com/pricing) ($20/月) | $20 | 多模型 (Auto/Composer) | / | N/A | N/A | N/A | IDE 内集成 Agent; $20 API usage; 倍率 >=1 |
| 👍 [Windsurf Pro](https://windsurf.com/pricing) ($20/月 (2周试用)) | $20 | Premium Model + SWE-1.5 无限 | / | N/A | N/A | N/A | Windsurf Pro $20/月; 官方按预算/额度展示, 不公开固定Token; 旧版msg/day口径不再作为准确额度 |
| 👍 [GitHub Copilot Pro](https://github.com/features/copilot/plans) ($10/月) | $10 | 多模型 | / | N/A | N/A | N/A | Copilot Pro $10/月; 300 premium requests/月; 付费升级为按premium requests计 |
| 👍 [CodeBuddy 个人标准版](https://www.codebuddy.cn/docs/ide/Account/pricing) (¥99/月) | ¥99 | 多模型 | / | N/A | N/A | N/A | CodeBuddy个人版2026-07-01后分标准/高级/至尊三档; 标准版¥99/月(连续包月¥70/月); 2000基础Credits/月, 2026-09-30前每月加赠2000 |
| 👍 [Trae Pro](https://www.trae.ai/pricing) ($10/月 (7天免费)) | $10 | 多模型 | / | N/A | N/A | N/A | 字节出品; Bonus 随机赠送(有收到$130); 补全不限量 |
| [Kiro Pro](https://kiro.dev/pricing) ($20/月 (首月免费)) | $20 | 多模型 | / | N/A | N/A | N/A | ⚠️退出付款页丢失免费资格; $0.04/credit 超量 |
| [Augment Code INDIE](https://www.augmentcode.com/pricing) ($20/月) | $20 | 多模型 | / | N/A | N/A | N/A | 倍率 1.25; 较新的玩家 |
| [Zed Pro](https://zed.dev/pricing) ($10/月) | $10 | 多模型 + 编辑器集成 | / | N/A | N/A | N/A | Zed Pro $10/月; 含$5 AI usage; 超出后按模型供应商价格+10%计费; 不等于固定Token月包 |

---

## API 按量计费

### 国内

| 模型 | 输入价格 | 备注 |
|------|:--:|------|
| ⭐ [DeepSeek V4 Flash (API)](https://platform.deepseek.com) | $0.14/百万输入Token | 官方API价: 输入$0.14/百万, 输出$0.28/百万; 缓存命中$0.014/百万; 1M上下文 |
| 👍 [DeepSeek V4 Pro (API)](https://platform.deepseek.com) | $0.435/百万输入Token | 官方API价: 输入$0.435/百万, 输出$0.87/百万; 推理能力更强; 1M上下文 |
| 👍 [Kimi K2.7 Code (API)](https://platform.kimi.ai) | $0.95/百万输入Token | 官方API价: 输入$0.95/百万, 输出$4/百万, 缓存命中$0.19/百万; 适合代码任务 |
| 👍 [GLM 5.1 (API)](https://open.bigmodel.cn) | ¥10/百万输入Token | 198K 上下文; SWE-Bench Pro SOTA; 性价比好 |

### 海外

| 模型 | 输入价格 | 备注 |
|------|:--:|------|
| ⭐ [GPT-5.6-Sol (API)](https://platform.openai.com) | $5/百万输入Token | 官方API价(标准短上下文): 输入$5/百万, 输出$30/百万; 缓存输入$0.50/百万; 缓存写$6.25/百万 |
| ⭐ [Muse Spark 1.1 (API)](https://ai.meta.com/muse) | $1.25/百万输入Token | Meta首款付费API模型; 输出$4.25/百万; 1M上下文; Thinking/Contemplating双推理模式; 多Agent并行推理; SWE-bench Pro 58.6; MCP Atlas 88.1 |
| 👍 [Claude Opus 4.8 (API)](https://console.anthropic.com) | $5/百万输入Token | 官方API价: 输入$5/百万, 输出$25/百万; prompt缓存写$6.25/百万, 读$0.50/百万 |

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
