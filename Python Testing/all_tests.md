Common Types of Tests
1. Unit Tests

- Scope: Smallest testable part of the code (e.g., a function or method).
- Goal: Verify that individual units of code work as expected.

    Tools in Python:
    - unittest (built-in)
    - pytest (popular and more powerful)

Example: Testing if your add(a, b) function returns the correct sum.

2. Integration Tests

- Scope: Check that different modules/components work together.
- Goal: Ensure interaction between multiple parts of the system behaves correctly.

Example: Testing if your API endpoint correctly fetches data from the database and returns JSON.

3. Regression Tests

- Scope: Ensure that new changes don’t break old functionality.
- Goal: Prevent previously fixed bugs or working features from breaking again.

Approach: Run the existing test suite whenever code changes.

4. System / End-to-End (E2E) Tests

- Scope: Test the system as a whole.
- Goal: Simulate real-world user scenarios.

Example: Using Selenium or Playwright to click through a web app like a real user would.

5. Acceptance Tests

- Scope: Validates against business requirements.
- Goal: Check if the system meets customer needs.

Example: “As a user, when I register, I should get a confirmation email.”

6. Smoke & Sanity Tests

- Smoke Test: Quick check if the build is stable (basic functionality works).
- Sanity Test: Quick check after small changes (e.g., fixing a bug didn’t break anything nearby).

7. Performance / Load / Stress Tests

- Goal: Measure how your system performs under load.
- Tools: Locust, JMeter.

8. Database Testing

Databases can (and should) be tested:

- Unit tests with a mocked DB → Use pytest-mock, unittest.mock, or libraries like pytest-django for mocking.
- Integration tests with a real DB → Use a test database (often in-memory like SQLite, or a disposable PostgreSQL instance via Docker).

Goals:

- Verify schema (tables, indexes, constraints).
- Check stored procedures / triggers.
- Validate CRUD operations.
- Data migration tests (important in production).

9. Security Tests

- Look for vulnerabilities (SQL injection, XSS, etc.).

10. Exploratory Tests

- Manual, creative testing to discover unexpected issues.

So in Python (and software in general), you’ll often see a testing pyramid:

- Lots of unit tests,
- Fewer integration tests,
- Few but essential system/E2E tests.


Integration test vs. end-to-end test

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

