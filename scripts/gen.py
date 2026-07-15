#!/usr/bin/env python3
"""Generate Coding Plan master markdown from structured YAML."""
import argparse
import re
import yaml
from collections import Counter


def format_name(p):
    name = p.get('name', '')
    url = p.get('subscribe_url', '')
    rank = p.get('tier_rank', 0)
    prefix = ''
    if rank == 1: prefix = '⭐ '
    elif rank == 2: prefix = '👍 '
    if url: return f'{prefix}[{name}]({url})'
    return f'{prefix}{name}'


def render_billing_matrix(plans):
    """Render unified billing rules section."""
    lines = []
    lines.append('# 计费规则统一图鉴')
    lines.append('')
    lines.append('> 所有厂商的计费套路，一个板块看透。每个厂商的[订阅页面]可点击直达。')
    lines.append('')

    # 1. 计费模式速查矩阵
    lines.append('## 计费模式速查矩阵')
    lines.append('')
    lines.append('| 厂商 | 套餐 | 计费模式 | 5h额度 | 周额度 | 月额度 | 限流机制 | 最大陷阱 |')
    lines.append('|------|------|:--:|------|------|------|------|------|')

    for p in plans:
        name = format_name(p)
        tier = p.get('tier', '')
        bt = p.get('billing_type', '')
        tiers = p.get('tiers', {})
        throttle = p.get('throttle', '')
        trap = p.get('hidden_trap', '')

        mode_map = {
            '5h_refresh': '🔄 5h刷新',
            'monthly_quota': '📦 月总量',
            'credit_blackbox': '🎲 Credit黑盒',
            'api_metered': '⚡ API按量',
            'free_limited': '🆓 限免',
            'gpu_time': '⏱️ GPU计时',
        }
        mode = mode_map.get(bt, bt)

        per_5h = tiers.get('per_5h', '-')
        per_week = tiers.get('per_week', '-')
        per_month = tiers.get('per_month', '-')

        # Truncate long fields for table
        throttle_short = throttle[:40] + '...' if len(throttle) > 40 else throttle
        trap_short = trap[:45] + '...' if len(trap) > 45 else trap

        lines.append(f'| {name} | {tier} | {mode} | {per_5h} | {per_week} | {per_month} | {throttle_short} | {trap_short} |')

    lines.append('')

    # 2. 三层闸门：5h/周/月 瓶颈分析
    lines.append('## 三层闸门深度拆解')
    lines.append('')
    lines.append('**5小时刷新制**不是"每5小时给你这么多"，而是"三层闸门每层都是上限，任何一层撞墙就停"。')
    lines.append('')

    five_h = [p for p in plans if p.get('billing_type') == '5h_refresh']
    lines.append('| 厂商 | 5h闸门 | 周闸门 | 月闸门 | 实际瓶颈在哪？ |')
    lines.append('|------|------|------|------|------|')
    for p in five_h:
        name = format_name(p)
        tiers = p.get('tiers', {})
        p5 = tiers.get('per_5h', '-')
        pw = tiers.get('per_week', '-')
        pm = tiers.get('per_month', '-')

        # Determine bottleneck
        throttle = p.get('throttle', '')
        if '3倍' in throttle:
            bottleneck = '⚠️ 高峰期3倍消耗→5h窗口秒空'
        elif '不限速' in throttle:
            bottleneck = '✅ 不限速, 5h刷新后继续'
        elif '限量' in throttle or '抢' in throttle:
            bottleneck = '⛔ 需抢库存, 抢不到=没额度'
        elif '停售' in throttle:
            bottleneck = '🚫 已停售'
        elif '毫无性价比' in throttle:
            bottleneck = '❌ 5h仅80次, 两任务见底'
        else:
            bottleneck = '5h刷新→看单次用量'

        lines.append(f'| {name} | {p5} | {pw} | {pm} | {bottleneck} |')
    lines.append('')

    # 3. 限流机制横向对比
    lines.append('## 限流机制横向对比')
    lines.append('')
    lines.append('| 厂商 | 429频率 | 触发条件 | 高峰期特殊规则 | 多Agent并发 |')
    lines.append('|------|:--:|------|------|:--:|')

    throttle_data = [
        ('Claude Pro', '🔴 极高', '正常时段也频繁', '无明显高峰规则', '❌'),
        ('ChatGPT Plus', '🟡 中等', 'Local Msg定义模糊', '无明显高峰规则', '⚠️'),
        ('Kimi Allegretto', '🟢 低', 'API不限速; CLI偶有', '无', '✅'),
        ('GLM Pro', '🔴 极高', '14-18点3倍消耗', '⛔ 高峰期3倍扣+抢购', '❌'),
        ('火山方舟', '🟡 中等', '每日00:00限量释放', '库存售完即止', '⚠️'),
        ('MiniMax', '🟢 低', '旧套餐数据; 改版后待观察', '不明显', '✅'),
        ('NVIDIA NIM', '🟡 中等', '40 rpm硬限', '无', '⚠️'),
    ]

    for name, freq, trigger, peak, concurrency in throttle_data:
        p = next((x for x in plans if x.get('name') == name), None)
        display_name = format_name(p) if p else name
        lines.append(f'| {display_name} | {freq} | {trigger} | {peak} | {concurrency} |')
    lines.append('')

    # 4. Credit 黑盒换算
    lines.append('## Credit 黑盒：你不知道 1 Credit = 多少 Token')
    lines.append('')
    lines.append('这些套餐用 credits/请求数计费，**厂商可以随时调整 credit ↔ Token 汇率而不通知你**。')
    lines.append('')

    credit_plans = [p for p in plans if p.get('billing_type') == 'credit_blackbox']
    lines.append('| 厂商 | 月费 | 月Credits | 已知换算（如果公开） | 不透明程度 |')
    lines.append('|------|:--:|:--:|------|:--:|')
    for p in credit_plans:
        name = format_name(p)
        price = p.get('price', '')
        tiers = p.get('tiers', {})
        monthly = tiers.get('per_month', '-')
        trap = p.get('hidden_trap', '')
        # Determine opacity
        if 'credit/Token汇率' in trap or '$20 API usage' in monthly:
            known = '❓ 仅标注$额, 无Token数'
            opacity = '🔴 完全不透明'
        elif 'msg/day' in monthly:
            known = '❓ msg/day, 无Token数'
            opacity = '🔴 完全不透明'
        else:
            known = '❓ 无公开换算'
            opacity = '🔴 完全不透明'
        lines.append(f'| {name} | {price} | {monthly} | {known} | {opacity} |')
    lines.append('')

    # 5. 聚合商模型倍数
    lines.append('## 聚合中转商：每个模型的折扣率不同')
    lines.append('')
    lines.append('中转商批发API→零售订阅。每个模型给的额度折扣不同，**多模型是卖点但单模型深度不如直营**。')
    lines.append('')

    agg_plans = [p for p in plans if p.get('category') == '聚合中转']
    lines.append('| 中转商 | 月费 | 可用模型数 | 单模型相对直营折扣 | 计费透明度 |')
    lines.append('|------|:--:|:--:|:--:|:--:|')
    for p in agg_plans:
        name = format_name(p)
        price = p.get('price', '')
        model = p.get('model', '')
        model_count = len([m for m in model.split('/') if m.strip()]) if '/' in model else 1
        mult = p.get('aggregator_multiplier')
        bt = p.get('billing_type', '')
        if mult:
            discount_str = f'~{int(mult*100)}%'
        elif '50x' in p.get('notes', '') or '50 倍' in p.get('notes', ''):
            discount_str = '~50x (vs Free)'
        elif bt == 'free_limited':
            discount_str = '限免, 无折扣率'
        elif bt == 'gpu_time':
            discount_str = '❓ GPU计时, 无法比较'
        else:
            discount_str = '❓ 未公开'

        if bt in ('free_limited',):
            transparency = '🟡 限免规则公开但随时变'
        elif bt == 'gpu_time':
            transparency = '🔴 完全不透明'
        else:
            transparency = '🟡 无单模型额度公开'

        lines.append(f'| {name} | {price} | ~{model_count}个 | {discount_str} | {transparency} |')
    lines.append('')

    # 6. 计费陷阱速查
    lines.append('## 计费陷阱速查：每个厂商最坑的一项')
    lines.append('')
    lines.append('| 厂商 | ⚠️ 最大陷阱 | 严重程度 |')
    lines.append('|------|------|:--:|')

    trap_severity = {
        'Claude Pro': ('429频率极高, 名义倍率63.6但实际可用1/3', '🔴'),
        'ChatGPT Plus': ('Local Messages定义模糊, 不同模式消耗不同', '🟡'),
        'GLM Coding Plan Pro': ('高峰期14-18点3倍消耗+每日限量抢, 下午干活≈白付钱', '🔴'),
        'GLM Coding Plan Lite': ('5h仅80次, ¥49买了个寂寞', '🔴'),
        'Kimi Code Allegretto': ('K2.7偶尔死循环; 新会员体系权益拆分(Code独立购买)', '🟡'),
        'Kimi Code Andante': ('¥49但额度只有Allegretto 1/20, 别买', '🔴'),
        '火山方舟 Coding Plan Lite': ('每日限量释放, 抢不到当月白等', '🔴'),
        '阿里云 Coding Plan Lite': ('已停售! 别找了; 转向更贵的Token Plan', '🔴'),
        'MiniMax Coding Plan Plus': ('数据是旧套餐的! 改版后实际额度待确认', '🟡'),
        '小米 MiMo Token Plan Pro': ('有衰减+不兼容Codex Responses API', '🟡'),
        'SuperGrok': ('免费层和付费层模型不同, Grok 4.5仅付费', '🟡'),
        'SuperGrok Heavy': ('首3月67%折扣后恢复$300, 续费时注意', '🟡'),
        '京东云 Coding Plan': ('首购价仅1次, 恢复¥40; 多模型额度分配不透明', '🟡'),
        '移动云 Coding Plan': ('仅MiniMax M2.5一个模型', '🟡'),
        '天翼云 Coding Plan': ('比智谱Lite同价但额度更低', '🟡'),
        '阶跃星辰 Step Plan': ('推广期价格不承诺长期', '🟡'),
        'NVIDIA NIM': ('免费不可持续! 随时取消/限速; 量化版影响质量', '🟡'),
        'OpenCode Go': ('单模型深度仅直营22%, 跑Kimi=1/5额度', '🔴'),
        'Ollama Pro': ('GPU时间计费完全不透明', '🔴'),
        'Fireworks Fire Pass': ('仅一个模型, 套餐随时终止', '🟡'),
        'OpenRouter': ('限免模型随时取消; 付费价不透明', '🟡'),
        'Cursor Pro': ('credit/Token汇率厂商说了算, 随时可改', '🔴'),
        'Windsurf Pro': ('msg/day不透明, 1 msg可能多次调用', '🔴'),
        'GitHub Copilot Pro': ('credits消耗规则不公开', '🔴'),
        'CodeBuddy 个人专业版': ('加赠2000有效期仅1月, 赠费用完恢复2000', '🟡'),
        'Trae Pro': ('Bonus随机送, 不承诺额度', '🟡'),
        'Kiro Pro': ('⚠️退出付款页就丢失免费资格', '🔴'),
        'Augment Code INDIE': ('40000 credits=多少Token? 无实测数据', '🟡'),
        'Zed Pro': ('$5/440万Token只是编辑器附加, 主力agent不够', '🟡'),
        'Claude Opus 4.8 (API)': ('Agent输出Token通常>输入, 实际成本按$75/百万算', '🔴'),
        'GPT-5.6-Sol (API)': ('重度使用包月$20比API月$100+便宜很多', '🟡'),
        'DeepSeek V4 Flash (API)': ('缓存命中率决定成本; 不复用prompt省不了', '🟡'),
        'DeepSeek V4 Pro (API)': ('日常coding用V4 Flash够了, 别多花钱', '🟡'),
        'Kimi K2.7 (API)': ('国内最贵API, Allegretto包月便宜10倍+', '🔴'),
        'GLM 5.2 (API)': ('Pro套餐¥149比API便宜10倍, 选套餐别用API', '🔴'),
        'Muse Spark 1.1 (API)': ('Contemplating并行agent消耗倍率未公开', '🟡'),
    }

    for p in plans:
        name = p.get('name', '')
        if name in trap_severity:
            trap_text, severity = trap_severity[name]
            display_name = format_name(p)
            lines.append(f'| {display_name} | {trap_text} | {severity} |')

    lines.append('')
    lines.append('---')
    lines.append('')
    lines.append('> **避坑核心原则**：包月套餐看瓶颈闸门(不看月总量)、Credit套餐看换算黑盒(不买不明朗的)、API按量看重度时套餐更划算(不比价就亏)。')
    lines.append('')

    return '\n'.join(lines)


def render_table(plans, category_filter, sub_category_filter=None):
    filtered = [p for p in plans if p.get('category') == category_filter]
    if sub_category_filter:
        filtered = [p for p in filtered if p.get('sub_category') == sub_category_filter]
    filtered.sort(key=lambda p: p.get('tier_rank', 99))

    lines = [
        '| 套餐 | 价格 | 模型 | TPS | 月度 Token(亿) | 每元 Token 数 | 每亿 Token 成本 | 备注 |',
        '|------|------|------|:--:|:--:|:--:|:--:|------|',
    ]

    for p in filtered:
        name = format_name(p)
        tier_text = p.get('tier', '')
        if tier_text: name += f' ({tier_text})'
        price = p.get('price', '')
        model = p.get('model', '')
        tps = p.get('tps')
        tokens_val = p.get('tokens_per_month')
        tps_str = str(int(tps)) if tps is not None else '/'

        if tokens_val is not None and price not in ('免费', ''):
            m = re.search(r'[\d.]+', str(price))
            if m:
                price_num = float(m.group())
                tokens_per_yuan = (float(tokens_val) * 100_000_000) / price_num
                per_yuan_str = f'{tokens_per_yuan/10_000:.0f}万' if tokens_per_yuan >= 10_000 else f'{tokens_per_yuan:.0f}'
                cost_per_100m = price_num / float(tokens_val)
                sym = '¥' if p.get('currency') == 'cny' else '$'
                cost_str = f'{sym}{cost_per_100m:.1f}'
                tokens_display = str(tokens_val)
            else:
                per_yuan_str = 'N/A'; cost_str = 'N/A'; tokens_display = 'N/A'
        elif price in ('免费', '部分模型限免'):
            per_yuan_str = '免费 🎁'; cost_str = '免费'
            tokens_display = str(tokens_val) if tokens_val else 'N/A'
        else:
            per_yuan_str = 'N/A'; cost_str = 'N/A'; tokens_display = 'N/A'

        lines.append(f'| {name} | {price} | {model} | {tps_str} | {tokens_display} | {per_yuan_str} | {cost_str} | {p.get("notes","")} |')
    return '\n'.join(lines)


def render_api_table(plans, sub_category_filter=None):
    filtered = [p for p in plans if p.get('category') == 'API 按量']
    if sub_category_filter:
        filtered = [p for p in filtered if p.get('sub_category') == sub_category_filter]
    filtered.sort(key=lambda p: p.get('tier_rank', 99))
    lines = ['| 模型 | 输入价格 | 备注 |', '|------|:--:|------|']
    for p in filtered:
        name = format_name(p)
        price = p.get('price', '')
        notes = p.get('notes', '')
        lines.append(f'| {name} | {price} | {notes} |')
    return '\n'.join(lines)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--data', required=True)
    parser.add_argument('--template', required=True)
    parser.add_argument('--output', required=True)
    args = parser.parse_args()

    with open(args.data) as f:
        data = yaml.safe_load(f)
    plans = data['plans']

    cats = Counter(p.get('category', 'other') for p in plans)
    stats = f"共收录 **{len(plans)}** 个套餐：厂商直营 {cats.get('厂商直营',0)} | 聚合中转 {cats.get('聚合中转',0)} | AI IDE {cats.get('AI IDE',0)} | API 按量 {cats.get('API 按量',0)}"

    with open(args.template) as f:
        template = f.read()

    output = template
    output = output.replace('{{STATS}}', stats)
    output = output.replace('{{BILLING_MATRIX}}', render_billing_matrix(plans))
    output = output.replace('{{DOMESTIC_TABLE}}', render_table(plans, '厂商直营', '国内'))
    output = output.replace('{{OVERSEAS_TABLE}}', render_table(plans, '厂商直营', '海外'))
    output = output.replace('{{AGGREGATOR_TABLE}}', render_table(plans, '聚合中转'))
    output = output.replace('{{IDE_TABLE}}', render_table(plans, 'AI IDE'))
    output = output.replace('{{API_DOMESTIC_TABLE}}', render_api_table(plans, '国内'))
    output = output.replace('{{API_OVERSEAS_TABLE}}', render_api_table(plans, '海外'))
    output = output.replace('{{LAST_UPDATED}}', data['last_updated'])

    with open(args.output, 'w') as f:
        f.write(output)
    print(f'✅ ({len(plans)} plans): {args.output}')


if __name__ == '__main__':
    main()
