
def check_language(word, language):
    """Check whether a string belongs to the selected language."""

    if language == "a*b*":
        # All a's must come before all b's
        return all(
            word[i] <= word[i + 1]
            for i in range(len(word) - 1)
        )

    elif language == "a^n b^n":
        # Number of a's must equal number of b's
        count_a = word.count("a")
        count_b = word.count("b")

        return (
            word == "a" * count_a + "b" * count_b
            and count_a == count_b
        )

    return False


def generate_strings(language, p):
    """Generate candidate strings of length at least p."""

    strings = []

    if language == "a*b*":
        for a in range(p + 1):
            for b in range(p + 1):
                word = "a" * a + "b" * b

                if len(word) >= p:
                    strings.append(word)

    elif language == "a^n b^n":
        for n in range(1, p + 3):
            word = "a" * n + "b" * n

            if len(word) >= p:
                strings.append(word)

    return strings


def generate_splits(word, p):
    """Generate all valid x, y, z decompositions."""

    splits = []

    for x_end in range(min(p, len(word)) + 1):
        for y_end in range(x_end + 1, len(word) + 1):

            x = word[:x_end]
            y = word[x_end:y_end]
            z = word[y_end:]

            if len(x + y) <= p and len(y) > 0:
                splits.append((x, y, z))

    return splits


def pump_string(x, y, z, i):
    """Generate xy^iz."""

    return x + (y * i) + z


def verify_conditions(word, x, y, z, p, language):
    condition_1 = len(x + y) <= p
    condition_2 = len(y) > 0

    return {
        "Condition 1: |xy| <= p": condition_1,
        "Condition 2: |y| > 0": condition_2,
        "Condition 3: Original string belongs to L":
            check_language(word, language)
    }
