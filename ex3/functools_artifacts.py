import functools
import operator
from typing import Any
from collections.abc import Callable


def spell_reducer(spells: list[int], operation: str) -> int:
    if not spells:
        return 0

    if operation in ["max", "min"]:
        get_op = getattr(__builtins__, operation)
    else:
        my_op = "mul" if operation == "multiply" else operation
        try:
            get_op = getattr(operator, my_op)
        except AttributeError:
            raise AttributeError(f"Unknown operation {operation}")
    return functools.reduce(get_op, spells)


def partial_enchanter(
        base_enchantment: Callable[[int, str, str], str]
        ) -> dict[str, Callable[[str], str]]:
    fire = functools.partial(base_enchantment, 50, "Fire")
    ice = functools.partial(base_enchantment, 50, "Ice")
    light = functools.partial(base_enchantment, 50, "Light")
    return {"Fire": fire, "Ice": ice, "Light": light}


@functools.lru_cache(maxsize=None)
def memoized_fibonacci(n: int) -> int:

    if n < 2:
        return n
    return memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2)


def spell_dispatcher() -> Callable[[Any], str]:
    @functools.singledispatch
    def cast_spell(target: Any) -> str:
        return "Unknown spell type"

    @cast_spell.register
    def _(target: str) -> str:
        return f"Enchatment: {target}"

    @cast_spell.register
    def _(target: int) -> str:
        return f"Damage spell: {target} damage"

    @cast_spell.register
    def _(target: list) -> str:
        return f"Multi-cast: {len(target)} spells"
    return cast_spell


def main() -> None:
    print("Testing spell reducer...")
    print(f"Sum: {spell_reducer([30, 40, 30], 'add')}")
    print(f"Product: {spell_reducer([100, 2400], 'mul')}")
    print(f"Max: {spell_reducer([20, 40, 4], 'max')}", end="\n\n")
    print("Testing memoized fibonacci...")
    print(f"Fib(0): {memoized_fibonacci(0)}")
    print(f"Fib(1): {memoized_fibonacci(1)}")
    print(f"Fib(10): {memoized_fibonacci(10)}")
    print(f"Fib(15): {memoized_fibonacci(15)}", end="\n\n")
    print("Testing spell dispatcher...")
    func = spell_dispatcher()
    print(func(42))
    print(func('fireball'))
    print(func([10, 20, 39]))
    print(func({"Security": 100}))


if __name__ == "__main__":
    main()
