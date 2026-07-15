#!/usr/bin/env python3
"""Generate Coding Plan master markdown from structured YAML."""
import argparse
import re
import yaml


def render_table(plans, category_filter, sub_category_filter=None):
    filtered = [p for p in plans if p.get('category') == category_filter]
    if sub_category_filter:
        filtered = [p for p in filtered if p.get('sub_category') == sub_category_filter]
    filtered.sort(key=lambda p: p.get('tier_rank', 99))

    lines = [
        '| 套餐 | 价格 | 模型 | TPS | 月度 Token(亿) | 每元 Token 数 | 每亿 Token 成本 | 额度倍率 | 备注 |',
        '|------|------|------|:--:|:--:|:--:|:--:|:--:|------|',
    ]

    for p in filtered:
        name = p.get('name', '')
        if p.get('tier'):
            name = f'{name} ({p["tier"]})'

        price = p.get('price', '')
        model = p.get('model', '')
        tps = p.get('tps')
        tokens_val = p.get('tokens_per_month')

        rank = p.get('tier_rank', 0)
        if rank == 1:
            name = f'⭐ {name}'
        elif rank == 2:
            name = f'👍 {name}'

        tps_str = str(int(tps)) if tps is not None else '/'

        if tokens_val is not None and price not in ('免费', ''):
            m = re.search(r'[\d.]+', str(price))
            if m:
                price_num = float(m.group())
                currency = p.get('currency', 'cny')
                tokens_per_yuan = (float(tokens_val) * 100_000_000) / price_num
                if tokens_per_yuan >= 10_000:
                    per_yuan_str = f'{tokens_per_yuan/10_000:.0f}万'
                else:
                    per_yuan_str = f'{tokens_per_yuan:.0f}'
                cost_per_100m = price_num / float(tokens_val)
                sym = '¥' if currency == 'cny' else '$'
                cost_str = f'{sym}{cost_per_100m:.1f}'
                multiplier_str = 'N/A'
                tokens_display = str(tokens_val)
            else:
                per_yuan_str = 'N/A'
                cost_str = 'N/A'
                multiplier_str = 'N/A'
                tokens_display = 'N/A'
        elif price in ('免费', '部分模型限免'):
            per_yuan_str = '免费 🎁'
            cost_str = '免费'
            multiplier_str = '免费'
            tokens_display = str(tokens_val) if tokens_val else 'N/A'
        else:
            per_yuan_str = 'N/A'
            cost_str = 'N/A'
            multiplier_str = 'N/A'
            tokens_display = 'N/A'

        notes = p.get('notes', '')
        lines.append(
            f'| {name} | {price} | {model} | {tps_str} | {tokens_display} | {per_yuan_str} | {cost_str} | {multiplier_str} | {notes} |'
        )

    return '\n'.join(lines)


def render_api_table(plans, sub_category_filter=None):
    filtered = [p for p in plans if p.get('category') == 'API 按量']
    if sub_category_filter:
        filtered = [p for p in filtered if p.get('sub_category') == sub_category_filter]
    filtered.sort(key=lambda p: p.get('tier_rank', 99))

    lines = [
        '| 模型 | 输入价格 | 输出价格 | 缓存价格 | 上下文 | 备注 |',
        '|------|:--:|:--:|:--:|:--:|------|',
    ]

    for p in filtered:
        name = p.get('name', '')
        price = p.get('price', '')
        model = p.get('model', '')
        notes = p.get('notes', '')
        rank = p.get('tier_rank', 0)
        prefix = '⭐ ' if rank == 1 else ('👍 ' if rank == 2 else '')
        lines.append(f'| {prefix}{name} | {price} | - | - | - | {notes} |')

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

    # Category stats
    cats = {}
    for p in plans:
        c = p.get('category', 'other')
        cats[c] = cats.get(c, 0) + 1

    stats = f"共收录 **{len(plans)}** 个套餐：厂商直营 {cats.get('厂商直营',0)} | 聚合中转 {cats.get('聚合中转',0)} | AI IDE {cats.get('AI IDE',0)} | API 按量 {cats.get('API 按量',0)}"

    with open(args.template) as f:
        template = f.read()

    output = template
    output = output.replace('{{STATS}}', stats)
    output = output.replace('{{DOMESTIC_TABLE}}', render_table(plans, '厂商直营', '国内'))
    output = output.replace('{{OVERSEAS_TABLE}}', render_table(plans, '厂商直营', '海外'))
    output = output.replace('{{AGGREGATOR_TABLE}}', render_table(plans, '聚合中转'))
    output = output.replace('{{IDE_TABLE}}', render_table(plans, 'AI IDE'))
    output = output.replace('{{API_DOMESTIC_TABLE}}', render_api_table(plans, '国内'))
    output = output.replace('{{API_OVERSEAS_TABLE}}', render_api_table(plans, '海外'))
    output = output.replace('{{LAST_UPDATED}}', data['last_updated'])

    with open(args.output, 'w') as f:
        f.write(output)

    print(f'✅ 母版已生成 ({len(plans)} plans): {args.output}')


if __name__ == '__main__':
    main()
