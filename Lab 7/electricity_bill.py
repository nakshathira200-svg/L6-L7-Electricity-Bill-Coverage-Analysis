RATES = {"DOM": 3, "COM": 6}

SLAB = {"A": 1, "B": 2}


def units_consumed(reading):
    if not isinstance(reading, str):
        raise ValueError("Reading must be a string")

    parts = reading.split(':')
    if len(parts) != 2:
        raise ValueError("Reading must contain previous:current")

    try:
        previous, current = map(int, parts)
    except ValueError:
        raise ValueError("Meter readings must be integers")

    if previous < 0 or current < 0:
        raise ValueError("Meter readings cannot be negative")

    if current < previous:
        raise ValueError("Current reading cannot be less than previous reading")

    return current - previous


def daily_average(units_csv):
    if not isinstance(units_csv, str):
        raise ValueError("Daily units must be a string")

    parts = units_csv.split(',')
    if not parts or any(not part.strip() for part in parts):
        raise ValueError("Daily units must contain comma-separated numbers")

    try:
        units = [int(u.strip()) for u in parts]
    except ValueError:
        raise ValueError("Daily units must be integers")

    if any(u < 0 for u in units):
        raise ValueError("Daily units cannot be negative")

    return round(sum(units) / len(units), 2)


def tariff_rate(code):
    if not isinstance(code, str):
        raise ValueError("Tariff code must be a string")

    parts = code.split('-')
    if len(parts) != 2:
        raise ValueError("Tariff code must have the format CATEGORY-SLAB")

    category, slab = (part.strip().upper() for part in parts)

    if category not in RATES:
        raise ValueError("Unknown tariff category")

    if slab not in SLAB:
        raise ValueError("Unknown tariff slab")

    return RATES[category] * SLAB[slab]


def main():
    print("==== Running units_consumed ====")
    user_input = input("Enter meter readings as previous:current (e.g. 1200:1350): ")
    result = units_consumed(user_input)
    print("Units Consumed:", result)

    print("\n==== Running daily_average ====")
    user_input = input("Enter daily units as CSV (e.g. 5,7,6): ")
    result = daily_average(user_input)
    print("Daily Average:", result)

    print("\n==== Running tariff_rate ====")
    user_input = input("Enter a tariff code (e.g. DOM-A): ")
    result = tariff_rate(user_input)
    print("Rate per Unit:", result)


if __name__ == "__main__":
    main()
