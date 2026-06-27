from collections.abc import Callable
from typing import Any


def mage_counter() -> Callable[[], int]:
    count: int = 0

    def mage_co() -> int:
        nonlocal count
        count += 1
        return count
    return mage_co


def spell_accumulator(initial_power: int) -> Callable[[int], int]:
    power: int = initial_power

    def spell_acum(added_power: int) -> int:
        nonlocal power
        power += added_power
        return power

    return spell_acum


def enchantment_factory(enchantment_type: str) -> Callable:

    def ench_factory(name: str) -> str:
        return f"{enchantment_type} {name}"
    return ench_factory


def memory_vault() -> dict[str, Callable]:
    my_dict: dict[str, Any] = {}

    def store(key: str, value: Any) -> None:
        my_dict[key] = value

    def recall(key: str) -> Any:
        try:
            return my_dict[key]
        except KeyError:
            return "Memory not found"

    return {"store": store, "recall": recall}


def main() -> None:
    initial_powers = [39, 30, 80]
    power_additions = [6, 17, 19, 17, 14]
    enchantment_types = ['Flaming', 'Radiant', 'Frozen']
    items_to_enchant = ['Ring', 'Sword', 'Shield', 'Staff']

    print("Testing mage counter...")
    counter_a = mage_counter()
    counter_b = mage_counter()
    print(f"counter_a call 1: {counter_a()}")
    print(f"counter_a call 2: {counter_a()}")
    print(f"counter_b call 1: {counter_b()}")

    print("\nTesting spell accumulator...")
    for i, j in zip(initial_powers, power_additions):
        spell = spell_accumulator(i)(j)
        print(f"Base {i}, add {j}: {spell}")

    print("\nTesting enchantment factory...")
    for k, b in zip(enchantment_types, items_to_enchant):
        print(enchantment_factory(k)(b))

    print("\nTesting memory vault...")
    print("Store 'secret' = 42")
    mem = memory_vault()
    mem["store"]("secret", 42)
    print(f"Recall 'secret': {mem['recall']('secret')}")
    print(f"Recall 'unknown': {mem['recall']('unknown')}")


if __name__ == "__main__":
    main()
