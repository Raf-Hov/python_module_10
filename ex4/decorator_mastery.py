import functools
import string
import time
from typing import Any, Callable


def spell_timer(func: Callable) -> Callable:

    @functools.wraps(func)
    def wrapper(*arg: Any, **kwargs: Any) -> Callable:
        print(f"Casting {func.__name__}...")
        start = time.time()
        value = func(*arg, **kwargs)
        end = time.time()
        print(f"Spell completed in {float(end - start):.2f} seconds")
        return value
    return wrapper


def power_validator(min_power: int) -> Callable:
    def validate(func: Callable) -> Callable:

        def print_message() -> None:
            print("Insufficient power for this spell")
            return None

        @functools.wraps(func)
        def wrapper(*arg: Any, **kwargs: Any) -> Any:
            if arg[0] >= min_power:
                return func(*arg, **kwargs)
            else:
                return print_message()
        return wrapper
    return validate


def retry_spell(max_attempts: int) -> Callable:
    def retry(func: Callable) -> Callable:

        @functools.wraps(func)
        def wrapper(*arg: Any, **kwargs: Any) -> Any:
            i = 0
            while i < max_attempts:
                try:
                    return func(*arg, **kwargs)
                except Exception:
                    print(f'Spell failed, retrying... (attempt {i + 1}/'
                          f'{max_attempts})')
                    i += 1
            return f"Spell casting failed after {max_attempts} attempts"
        return wrapper
    return retry


class MageGuild:
    @staticmethod
    def validate_mage_name(name: str) -> bool:
        if not len(name) >= 3:
            return False

        for letter in name:
            if (letter not in string.ascii_letters and letter != ' '):
                return False

        return True

    def cast_spell(self, spell_name: str, power: int) -> None:

        @power_validator(min_power=10)
        def validate_power(power) -> None:
            print(f"Successfully cast {spell_name} with {power} power")
        return validate_power(power)


@spell_timer
def fireball_cast() -> str:
    return "Result: Fireball cast !"


def main() -> None:
    try:
        print('=== Testing spell timer... ===')
        print(fireball_cast())
        print('')

        print('Testing MageGuild...')
        name = 'Laurent the wisdom guardian'
        print(f'Testing name {name}: {MageGuild.validate_mage_name(name)}')
        name = '42'
        print(f'Testing name {name}: {MageGuild.validate_mage_name(name)}')
        print('')

        laurent = MageGuild()
        print('=== Working spell ===')
        laurent.cast_spell('Lightning', 15)
        print('=== Not working spell ===')
        laurent.cast_spell('Lightning', 5)
    except Exception as e:
        print(e)
        exit()


if __name__ == '__main__':
    main()
