from typing import Callable


def spell_combiner(
        spell1: Callable[[str, int], str], spell2: Callable[[str, int], str]
          ) -> Callable[[str, int], tuple[str, str]]:

    if not callable(spell1) and callable(spell2):
        raise TypeError("Both spells must be callable!")

    def combine(torget: str, power: int) -> tuple[str, str]:
        res1 = spell1(torget, power)
        res2 = spell2(torget, power)
        return res1, res2

    return combine


def power_amplifier(
        base_spell: Callable[[str, int], str], multiplier: int
        ) -> Callable[[str, int], str]:

    if not callable(base_spell):
        raise TypeError("First spell must be callable!")

    def amplifier(torget: str, power: int) -> str:
        res = base_spell(torget, power * multiplier)
        return res

    return amplifier


def conditional_caster(
        condition: Callable[[str, int], bool], spell: Callable[[str, int], str]
        ) -> Callable[[str, int], str]:

    if not callable(condition) or callable(spell):
        raise TypeError("Both condition and spell must be callable!")

    def condit_cast(torget: str, pow: int) -> str:
        if condition(torget, pow):
            return spell
        return "Spell fizzled"
    return condit_cast


def spell_sequence(
        spells: list[Callable[[str, int], str]]
        ) -> Callable[[str, int], list[str]]:
    for i in spells:
        if not callable(i):
            raise TypeError("All items in the spells list must be callable!")

    def spell_caster(torget: str, pow: int) -> list[str]:
        res: list = []

        for i in spells:
            spell_res = i(torget, pow)
            res.append(spell_res)
        return res
    return spell_caster


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

    print("Testing spell combiner...")
    combo_spell = spell_combiner(fireball, heal)

    for targ, value in zip(test_targets, test_values):
        rsult = combo_spell(targ, value)
        print(f"Combined result for {targ}: {rsult}")


if __name__ == "__main__":
    main()
