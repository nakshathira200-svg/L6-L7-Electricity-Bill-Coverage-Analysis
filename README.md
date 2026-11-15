# Lab 6 – Code and Branch Coverage Analysis

## Student Details

| Field | Details |
|---|---|
| Student Name | Nakshathira B |
| SRN | PES2UG24AM096 |
| Application Assigned | Electricity Bill Calculator |
| Lab | Lab 6 – Code and Branch Coverage Analysis |
| Programming Language | Python 3 |
| Testing Framework | Pytest |
| Coverage Tool | Coverage.py |

---

## 1. Project Overview

This project focuses on performing code coverage and branch coverage analysis on an Electricity Bill Calculator application using Python.

The objective is to design and execute test cases to achieve at least 90% code coverage and branch coverage.

The application contains three major functions:

- `energy_charge()` – Calculates electricity charges based on units consumed and connection type.
- `late_fee()` – Calculates late payment fees based on the number of days delayed and bill amount.
- `subsidy()` – Calculates applicable subsidies based on electricity consumption, senior citizen status and solar installation.

## 2. Technologies Used

- Python 3
- Pytest
- Coverage.py
- Git and GitHub

## 3. Test Case Implementation

Two separate test files were created:

### Code Coverage Testing

**File:** `CodeCoverageTest_PES2UG24AM096_electricity_bill.py`

This test suite verifies the execution of statements across the application's functions, including normal inputs, boundary conditions and invalid inputs.

**Execution command:**

```bash
coverage erase
coverage run --source=electricity_bill -m pytest -v CodeCoverageTest_PES2UG24AM096_electricity_bill.py
coverage report -m
```

### Branch Coverage Testing

**File:** `BranchCoverageTest_PES2UG24AM096_electricity_bill.py`

This test suite verifies the different outcomes of conditional statements and decision branches in the application.

**Execution command:**

```bash
coverage erase
coverage run --branch --source=electricity_bill -m pytest -v BranchCoverageTest_PES2UG24AM096_electricity_bill.py
coverage report -m
```

## 4. Results

### Code Coverage

| Metric | Result |
|---|---:|
| Total Statements | 32 |
| Missed Statements | 0 |
| Code Coverage | 100% |
| Test Cases Passed | 17 |

### Branch Coverage

| Metric | Result |
|---|---:|
| Total Statements | 32 |
| Missed Statements | 0 |
| Total Branches | 22 |
| Partial Branches | 0 |
| Branch Coverage | 100% |
| Test Cases Passed | 17 |

Both code coverage and branch coverage achieved 100%, exceeding the minimum requirement of 90%.

## 5. Screenshots and Documentation

The repository includes the following evidence:

- `CodeCoverage_PES2UG24AM096.png` – Code coverage execution report showing 100% coverage.
- `BranchCoverage_PES2UG24AM096.png` – Branch coverage execution report showing 22 branches and 100% coverage.
- `LAB 6_PES2UG24AM096.pdf` – Lab report containing the coverage analysis and screenshots.

## 6. Conclusion

The Electricity Bill Calculator application was successfully tested using Pytest and Coverage.py.

The test suites achieved 100% code coverage and 100% branch coverage, with all 17 test cases passing in each run.

All 32 executable statements and 22 decision branches were covered, with no missed statements or partially covered branches.

The objectives of Lab 6 were successfully achieved.

---

**Submitted by:**  
Nakshathira B  
**SRN:** PES2UG24AM096

**GitHub Repository:**  
https://github.com/nakshathira200-svg/L6-L7-Electricity-Bill-Coverage-Analysis
