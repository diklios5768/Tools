code_areas_simplified = []


def simplify_code_area(items, prefix=None):
    for item in items:
        code_areas_simplified[item['value']] = item['label'] if prefix is None else prefix + item['label']
        if item.get('children', False):
            simplify_code_area(item['children'], prefix=item['label'] if prefix is None else prefix + item['label'])


if __name__ == '__main__':
    simplify_code_area([])
