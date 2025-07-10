import colorama

def init_colors() -> None:
    """Fixes Windows console color compatibility."""
    colorama.just_fix_windows_console()


def multiprint(strings: list) -> None:
    """Concatinate a given list of string and print it."""
    final_string = strings[0]

    for string in strings[1:]:
        final_string += string

    print(final_string)
