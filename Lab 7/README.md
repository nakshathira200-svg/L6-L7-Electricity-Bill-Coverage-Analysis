# Lab 7 – Fuzz Testing

## Student Details

| Field | Details |
|---|---|
| Student Name | Nakshathira B |
| SRN | PES2UG24AM096 |
| Application | Electricity Bill Calculator |
| Lab | Lab 7 – Fuzz Testing |
| Programming Language | Python 3 |
| Testing Framework | Pytest |
| Fuzz Testing Library | Hypothesis |

---

## 1. Objective

The objective of this lab is to perform fuzz testing using the Hypothesis library to identify bugs and evaluate the robustness of the Electricity Bill Calculator application.

Hypothesis automatically generates different inputs, including valid values, malformed strings and invalid data types, to test the behaviour of the application.

The following three functions are tested:

- `units_consumed(reading)` – Calculates electricity consumption using previous and current meter readings.
- `daily_average(units_csv)` – Calculates the average of comma-separated daily electricity units.
- `tariff_rate(code)` – Calculates the electricity tariff rate based on the connection category and slab.

## 2. Technologies Used

- Python 3
- Pytest
- Hypothesis 6.141.1
- Git and GitHub

Install Hypothesis using:

```bash
python -m pip install hypothesis
```

## 3. Bugs Identified

During the initial fuzz-testing execution, Hypothesis generated `None` as an input for all three functions.

The original implementation attempted to call the `split()` method on these values, resulting in unexpected `AttributeError` exceptions.

Other input-validation weaknesses included:

- Incorrect meter-reading formats.
- Non-integer meter readings.
- Negative meter readings.
- Current readings smaller than previous readings.
- Empty or malformed daily-unit entries.
- Negative daily consumption values.
- Invalid tariff categories and slabs.

## 4. Bug Fixes and Improvements

Input validation was added to all three functions.

**units_consumed():**
- Validates that the input is a string.
- Checks the previous:current reading format.
- Accepts only integer meter readings.
- Rejects negative readings.
- Rejects current readings smaller than previous readings.

**daily_average():**
- Validates that the input is a string.
- Checks comma-separated integer values.
- Rejects empty entries and malformed values.
- Rejects negative electricity consumption values.

**tariff_rate():**
- Validates the tariff-code format.
- Accepts uppercase and lowercase category and slab codes.
- Rejects unsupported categories and slabs.

Invalid inputs now raise controlled `ValueError` exceptions instead of unexpected runtime errors.

## 5. Test Case Implementation

The completed test file is:

`test_electricity_bill.py`

A total of 11 Hypothesis-based test functions were implemented:

| No. | Test Case |
|---|---|
| 1 | Valid meter-reading calculations |
| 2 | Invalid data types for meter readings |
| 3 | Valid daily-average calculations |
| 4 | Invalid data types for daily averages |
| 5 | Valid tariff categories and slabs |
| 6 | Invalid data types for tariff codes |
| 7 | Malformed meter-reading strings |
| 8 | Malformed daily-unit strings |
| 9 | Invalid tariff codes |
| 10 | Decreasing meter readings |
| 11 | Negative daily consumption values |

Hypothesis automatically generates multiple input examples for each property-based test.

## 6. Execution

Run the following command from the Lab 7 directory:

```bash
python -m pytest -v test_electricity_bill.py
```

## 7. Test Results

The final execution produced the following result:

| Metric | Result |
|---|---:|
| Total test functions | 11 |
| Tests passed | 11 |
| Tests failed | 0 |
| Pass rate | 100% |

The initial fuzz-testing run exposed unhandled `AttributeError` exceptions for `None` inputs.

After implementing input validation and correcting the identified issues, all 11 tests passed successfully.

## 8. Screenshots and Documentation

The following evidence is included in this repository:

- `FuzzTesting_InitialFailure_PES2UG24AM096.png` – Initial fuzz-testing output demonstrating the input-validation failures.
- `FuzzTesting_FinalResult_PES2UG24AM096.png` – Final Pytest output showing all 11 tests passing.
- `LAB 7_PES2UG24AM096.pdf` – Lab report containing the testing approach, findings, fixes and screenshots.

## 9. Conclusion

Fuzz testing was successfully performed on the Electricity Bill Calculator using Hypothesis and Pytest.

The initial testing phase identified input-validation weaknesses in all three application functions. The source code was modified to handle invalid inputs through appropriate validation and controlled exceptions.

The final test suite achieved 11 out of 11 passing tests, demonstrating improved robustness against valid and invalid inputs.

The objectives of Lab 7 were successfully completed.

---

**Submitted by:** Nakshathira B

**SRN:** PES2UG24AM096

**GitHub Repository:**

https://github.com/nakshathira200-svg/L6-L7-Electricity-Bill-Coverage-Analysis
