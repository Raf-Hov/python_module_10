def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    return list(sorted(artifacts, key=lambda x: x['power'], reverse=True))


def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    return list(filter(lambda x: x['power'] >= min_power, mages))


def spell_transformer(spells: list) -> list:
    return list(map(lambda x: '* ' + x + ' *', spells))


def mage_stats(mages: list[dict]) -> dict:
    my_dcit: dict = {'max_power': 0, 'min_power': 0, 'avg_power': 0.0}
    my_list: list = []
    my_list = list(map(lambda x: x['power'], mages))
    my_dcit['max_power'] = max(my_list)
    my_dcit['min_power'] = min(my_list)
    my_dcit['avg_power'] = round(sum(my_list) / len(my_list), 2)
    return my_dcit


def main() -> None:
    artifacts = [{'name': 'Water Chalice', 'power': 103, 'type': 'accessory'},
                 {'name': 'Shadow Blade', 'power': 102, 'type': 'accessory'},
                 {'name': 'Ice Wand', 'power': 80, 'type': 'accessory'},
                 {'name': 'Water Chalice', 'power': 79, 'type': 'armor'}]
    mages = [{'name': 'Casey', 'power': 88, 'element': 'lightning'},
             {'name': 'Casey', 'power': 73, 'element': 'water'},
             {'name': 'Storm', 'power': 84, 'element': 'earth'},
             {'name': 'Kai', 'power': 71, 'element': 'light'},
             {'name': 'Morgan', 'power': 84, 'element': 'earth'}]
    spells = ['tsunami', 'darkness', 'meteor', 'lightning']

    print("=== Testing artifact sorter... ===")
    for item in artifact_sorter(artifacts):
        print(f"{item['name']} - {item['power']}")
    print("\n=== Testing power filter (min: 90)... ===")
    for item in power_filter(artifacts, 90):
        print(f"{item['name']} - {item['power']}")
    print("\n=== Testing spell transformer... ===")
    for item in spell_transformer(spells):
        print(item, end=" ")
    print("\n\n=== Testing mages stats... ===")
    stats = mage_stats(mages)
    print(
        f"Max power: {stats['max_power']}\n"
        f"Min power: {stats['min_power']}\n"
        f"Average power: {stats['avg_power']}"
    )
    return None


if __name__ == "__main__":
    main()
