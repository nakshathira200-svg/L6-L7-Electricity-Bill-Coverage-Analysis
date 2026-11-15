import pytest
from hypothesis import given, strategies as st, assume

from electricity_bill import units_consumed, daily_average, tariff_rate


# 1. Valid meter readings
@given(
    previous=st.integers(min_value=0, max_value=1000000),
    consumed=st.integers(min_value=0, max_value=1000000)
)
def test_units_consumed_valid(previous, consumed):
    current = previous + consumed
    assert units_consumed(f"{previous}:{current}") == consumed


# 2. Invalid data types for meter readings
@given(value=st.one_of(st.none(), st.integers()))
def test_units_consumed_invalid_type(value):
    with pytest.raises(ValueError):
        units_consumed(value)


# 3. Valid daily averages
@given(
    units=st.lists(
        st.integers(min_value=0, max_value=100000),
        min_size=1,
        max_size=50
    )
)
def test_daily_average_valid(units):
    units_csv = ",".join(map(str, units))
    expected = round(sum(units) / len(units), 2)
    assert daily_average(units_csv) == expected


# 4. Invalid data types for daily averages
@given(value=st.one_of(st.none(), st.integers()))
def test_daily_average_invalid_type(value):
    with pytest.raises(ValueError):
        daily_average(value)


# 5. Valid tariff codes
@given(
    category=st.sampled_from(["DOM", "COM", "dom", "com"]),
    slab=st.sampled_from(["A", "B", "a", "b"])
)
def test_tariff_rate_valid(category, slab):
    rates = {"DOM": 3, "COM": 6}
    slabs = {"A": 1, "B": 2}

    expected = rates[category.upper()] * slabs[slab.upper()]
    assert tariff_rate(f"{category}-{slab}") == expected


# 6. Invalid data types for tariff codes
@given(value=st.one_of(st.none(), st.integers()))
def test_tariff_rate_invalid_type(value):
    with pytest.raises(ValueError):
        tariff_rate(value)


# 7. Malformed meter readings
@given(value=st.text())
def test_units_consumed_malformed_strings(value):
    with pytest.raises(ValueError):
        units_consumed(f"{value}:not-a-number")


# 8. Malformed daily unit lists
@given(value=st.text())
def test_daily_average_malformed_strings(value):
    with pytest.raises(ValueError):
        daily_average(f"{value},not-a-number")


# 9. Invalid tariff codes
@given(value=st.text())
def test_tariff_rate_malformed_strings(value):
    with pytest.raises(ValueError):
        tariff_rate(f"{value}-INVALID")


# 10. Decreasing meter readings
@given(
    previous=st.integers(min_value=1, max_value=100000),
    current=st.integers(min_value=0, max_value=99999)
)
def test_units_consumed_rejects_decreasing_readings(previous, current):
    assume(current < previous)
    with pytest.raises(ValueError):
        units_consumed(f"{previous}:{current}")


# 11. Negative daily units
@given(
    units=st.lists(
        st.integers(min_value=-1000, max_value=-1),
        min_size=1
    )
)
def test_daily_average_rejects_negative_units(units):
    with pytest.raises(ValueError):
        daily_average(",".join(map(str, units)))
