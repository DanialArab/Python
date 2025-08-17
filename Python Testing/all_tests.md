1. [Unit Tests](#1)
2. [Integration Tests](#2)
3. [Regression Tests](#3)
4. [System / End-to-End (E2E) Tests](#4)
5. [Integration test vs. end-to-end test](#5)
6. [Acceptance Tests](#6)
7. [Smoke & Sanity Tests](#7)
8. [Performance / Load / Stress Tests](#8)
9. [Database Testing](#9)
10. [Security Tests](#10)
11. [Exploratory Tests](#11)
12. [Python libraries for testing](#12)
    1. [Pydantic](#13)
13. [How to write tests]()
    1. [How to write unit tests ]


<a name="1"><a>
# Unit Tests

- Scope: Smallest testable part of the code (e.g., a function or method).
- Goal: Verify that individual units of code work as expected.

    Tools in Python:
    - unittest (built-in)
    - pytest (popular and more powerful)

Example: Testing if your add(a, b) function returns the correct sum.

<a name="2"><a>
# Integration Tests

- Scope: Check that different modules/components work together.
- Goal: Ensure interaction between multiple parts of the system behaves correctly.

Example: Testing if your API endpoint correctly fetches data from the database and returns JSON.

<a name="3"><a>
# Regression Tests

- Scope: Ensure that new changes don’t break old functionality.
- Goal: Prevent previously fixed bugs or working features from breaking again.

Approach: Run the existing test suite whenever code changes.

<a name="4"><a>
# System / End-to-End (E2E) Tests

- Scope: Test the system as a whole.
- Goal: Simulate real-world user scenarios.

Example: Using Selenium or Playwright to click through a web app like a real user would.


<a name="5"><a>
# Integration test vs. end-to-end test

They sound similar but actually have different scopes. Let’s break it down clearly:

**Integration Test**

- Scope: Tests that multiple modules/components of your system work correctly together.
- Focus: Integration points (how parts communicate).
- Level: Mid-level (between unit and E2E).
- Environment: Often runs in a controlled/test environment with mocked or test databases/services.

Example:
- You have a Python function that queries a database and returns results via an API endpoint. An integration test would call the endpoint and check the DB interaction, making sure data flows correctly from DB → API.

It doesn’t test the frontend UI or external dependencies (like an email service, unless mocked).

**End-to-End (E2E) Test**

- Scope: Tests the entire system from the **user’s perspective.**
- Focus: Real-world flows across all layers (frontend, backend, DB, external services).
- Level: High-level, full system.
- Environment: Usually runs in an environment close to production.

Example:
- A test script opens your website (using Selenium/Playwright), clicks “Register”, fills in a form, submits it, and checks that:
    - A record is saved in the database,
    - An email confirmation is sent,
    - The user can then log in.

That’s true end-to-end — it goes across the entire stack.

Key Differences

| Feature         | Integration Test                           | End-to-End Test                   |
| --------------- | ------------------------------------------ | --------------------------------- |
| **Scope**       | Multiple components                        | Entire system                     |
| **Goal**        | Verify modules interact correctly          | Verify user scenarios work        |
| **Speed**       | Faster (runs on partial system)            | Slower (full stack)               |
| **Reliability** | Less flaky (controlled env, mocks allowed) | More flaky (real dependencies)    |
| **Example**     | API ↔ DB works                             | User registers and receives email |

Think of it like this:
- Integration test = "Does my backend talk properly to the database?"
- E2E test = "Can a user actually sign up and log in successfully?"


<a name="6"><a>
# Acceptance Tests

- Scope: Validates against business requirements.
- Goal: Check if the system meets customer needs.

Example: “As a user, when I register, I should get a confirmation email.”

<a name="7"><a>
# Smoke & Sanity Tests

- Smoke Test: Quick check if the build is stable (basic functionality works).
- Sanity Test: Quick check after small changes (e.g., fixing a bug didn’t break anything nearby).

<a name="8"><a>
# Performance / Load / Stress Tests

- Goal: Measure how your system performs under load.
- Tools: Locust, JMeter.

<a name="9"><a>
# Database Testing

Databases can (and should) be tested:

- Unit tests with a mocked DB → Use pytest-mock, unittest.mock, or libraries like pytest-django for mocking.
- Integration tests with a real DB → Use a test database (often in-memory like SQLite, or a disposable PostgreSQL instance via Docker).

Goals:

- Verify schema (tables, indexes, constraints).
- Check stored procedures / triggers.
- Validate CRUD operations.
- Data migration tests (important in production).

<a name="10"><a>
# Security Tests

- Look for vulnerabilities (SQL injection, XSS, etc.).

<a name="11"><a>
# Exploratory Tests

- Manual, creative testing to discover unexpected issues.

So in Python (and software in general), you’ll often see a testing pyramid:

- Lots of unit tests,
- Fewer integration tests,
- Few but essential system/E2E tests.

<a name="12"><a>
# Python libraries for testing

<a name="13"><a>
## Pydantic

Pydantic sits in a special place between data validation, parsing, and testing in Python projects. Let me break it down:

### What is Pydantic?

- A Python library for data validation and settings management. 
- It uses Python type hints to define the structure of data and automatically:
    - Validates input data,
    - Parses it into proper Python types,
    - Raises clear errors if data is invalid.

Under the hood: it’s powered by type hints (str, int, list, etc.) + runtime validation.

### Where it fits in software/testing

1. Input Validation (before unit/integration tests)

- Often, bugs come from "bad data" (e.g., "42" instead of integer 42).
- Pydantic acts as a data gatekeeper: you define the schema and it guarantees correctness.

Example in an API:

    from pydantic import BaseModel
    
    class User(BaseModel):
        id: int
        name: str
        email: str
    
    user = User(id="123", name="Alice", email="alice@example.com")
    print(user.id)  # 123 (parsed into int)


If someone sends id="abc", it raises a validation error. 

2. Configuration & Settings

- Pydantic can load settings from env variables, JSON, YAML, etc.
- Great for testing with different environments (dev, test, prod).

3. Testing Companion

While not a testing framework itself, Pydantic helps tests by:

- Ensuring test data is valid before tests run.
- Making mock data creation easier (no manual type checking).
- Giving clearer errors when test inputs are malformed.

Example in integration tests:

    def test_user_model():
        user = User(id=1, name="Bob", email="bob@test.com")
        assert user.email.endswith("@test.com")

4. Commonly Used With

- FastAPI → for request/response validation.
- Databases → validating ORM models or DTOs.
- ETL/Data Pipelines → validating ingested JSON/CSV data.

In the Testing Pyramid:
- It’s not a separate "test type" like unit/integration/E2E.
- Instead, Pydantic fits at the foundation layer:
- Ensures data correctness → reduces need for extra validation logic inside unit/integration tests.

Think of it as:
- “If Pydantic says the data is valid, my tests can focus on logic instead of type-checking.”


<a name=""><a>
# How to write tests

<a name=""><a>
## How to write unit tests 
HERE 
