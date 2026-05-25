import functools
import operator
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


def main() -> None:
    spell_powers = [13, 45, 13, 14, 30, 42]
    operations = ['add', 'multiply', 'max', 'min']
    ops = ['Sum', 'Product', 'Max', 'Min']
    fibonacci_tests = [13, 19, 8]

    for j, i in zip(ops, operations):
        print(f"{j}:", spell_reducer(spell_powers, i))
    print(memoized_fibonacci(10))
    print(memoized_fibonacci.cache_info())  # cache_info \ lru_cache


if __name__ == "__main__":
    main()