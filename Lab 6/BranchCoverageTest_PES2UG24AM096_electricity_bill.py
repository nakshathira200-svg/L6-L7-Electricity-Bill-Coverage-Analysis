
from electricity_bill import energy_charge, late_fee, subsidy


# -------------------------------
# ENERGY CHARGE TEST CASES
# -------------------------------

def test_domestic_low_usage():
    assert energy_charge(50, "domestic") == 200


def test_domestic_exactly_100():
    assert energy_charge(100, "domestic") == 350


def test_domestic_medium_usage():
    assert energy_charge(200, "domestic") == 850


def test_domestic_high_usage():
    assert energy_charge(400, "domestic") == 2150


def test_commercial_connection():
    assert energy_charge(100, "commercial") == 750


def test_invalid_connection():
    try:
        energy_charge(100, "industrial")
        assert False
    except ValueError:
        assert True


def test_negative_units():
    try:
        energy_charge(-10, "domestic")
        assert False
    except ValueError:
        assert True


# -------------------------------
# LATE FEE TEST CASES
# -------------------------------

def test_no_late_fee():
    assert late_fee(500, 0) == 0


def test_negative_days_late():
    assert late_fee(500, -5) == 0


def test_late_fee_within_15_days():
    assert late_fee(500, 10) == 50


def test_late_fee_above_15_days():
    assert late_fee(1000, 20) == 100


def test_late_fee_high_bill():
    assert late_fee(3000, 20) == 250


# -------------------------------
# SUBSIDY TEST CASES
# -------------------------------

def test_senior_citizen_low_usage():
    assert subsidy(50, True, False) == 50


def test_non_senior_low_usage():
    assert subsidy(50, False, False) == 0


def test_usage_above_100():
    assert subsidy(150, True, False) == 0


def test_solar_subsidy():
    assert subsidy(150, False, True) == 100


def test_solar_high_usage():
    assert subsidy(350, True, True) == 0
