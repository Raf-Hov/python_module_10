from collections.abc import Callable


def spell_combiner(
        spell1: Callable[[str, int], str], spell2: Callable[[str, int], str]
        ) -> Callable[[str, int], tuple[str, str]]:

    if not callable(spell1) and callable(spell2):
        raise TypeError("Both spells must be callable")

    def combiner(torget: str, power: int) -> tuple[str, str]:
        return (spell1(torget, power), spell2(torget, power))
    return combiner


def power_amplifier(base_spell: Callable[[str, int], str], multiplier: int
                    ) -> Callable[[str, int], str]:
    if not callable(base_spell):
        raise TypeError("First spell must be callable!")

    def pow_amplifier(torget: str, power: int) -> str:
        return base_spell(torget, power * multiplier)

    return pow_amplifier


def conditional_caster(
        condition: Callable[[str, int], bool], spell: Callable[[str, int], str]
        ) -> Callable[[str, int], str]:

    if not callable(condition) and callable(spell):
        raise TypeError("Both condition and spell must be callable!")

    def condit_cast(torget: str, power: int) -> str:
        if condition(torget, power):
            return spell(torget, power)
        return "Spell fizzled"
    return condit_cast


def spell_sequence(spells: list[Callable[[str, int], str]]
                   ) -> Callable[[str, int], list[str]]:
    for i in spells:
        if not callable(i):
            raise TypeError("All items in the spells list must be callable!")

    def spel_seq(torget: str, power: int) -> list[str]:
        my_list: list[str] = []
        for i in spells:
            res = i(torget, power)
            my_list.append(res)
        return my_list

    return spel_seq


def fireball(target: str, power: int) -> str:
    return f"Fireball hits {target} for {power} damage"


def heal(target: str, power: int) -> str:
    return f"Heal restores {target} for {power} HP"


def shield(target: str, power: int) -> str:
    return f"Shield protects {target} with {power} defense rating"


def high_power_check(target: str, power: int) -> bool:
    return power > 5


def main() -> None:
    test_values = [13, 11, 6]
    test_targets = ['Dragon', 'Goblin', 'Wizard', 'Knight']

    print("\nTesting spell combiner...")
    for i, j in zip(test_targets, test_values):
        combo = ", ".join(spell_combiner(fireball, heal)(i, j))
        print("Combined spell result: "
              f"{combo}")

    print("\nTesting power amplifier...")
    for i, j in zip(test_targets, test_values):
        apli = power_amplifier(fireball, j)(i, j)
        print(f"Original: {j}, Amplified: {apli}")

    print("\nTesting conditional caster...")
    for i, j in zip(test_targets, test_values):
        condi = conditional_caster(high_power_check, shield)(i, j)
        print(condi)

    print("\nTesting spell sequence...")
    my_list = [fireball, heal, shield]
    for i, j in zip(test_targets, test_values):
        spell_seq = ",\n".join(spell_sequence(my_list)(i, j))
        print(spell_seq, end="\n\n")


if __name__ == "__main__":
    main()
