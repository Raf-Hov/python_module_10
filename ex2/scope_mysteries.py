from collections.abc import Callable


def mage_counter() -> Callable[[], int]:
    count: int = 0

    def mage_co() -> int:
        nonlocal count
        print()
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


def enchantment_factory(enchantment_type: str) -> Callable[[str], str]:

    def ench_factory(name: str) -> str:
        return f"{enchantment_type} {name}"
    return ench_factory



def main() -> None:
    ench = enchantment_factory("Flaming")
    print(ench("Shield"))


if __name__ == "__main__":
    main()
