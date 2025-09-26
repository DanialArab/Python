## Core Skills to Practice for Live Coding (MLE-focused)

a) Data wrangling / manipulation

- Reading messy CSV/JSON/parquet files.
- Cleaning missing values, normalizing column names.
- Grouping, aggregating, sorting (using Python + Pandas).
- Joining datasets.
- Writing reusable functions for these.

b) Python fundamentals for clean code

- Writing modular code (functions, classes).
- Type hints (def foo(x: str) -> int:).
- Error handling (try/except, custom exceptions).
- Python standard libraries for data (csv, json, re, itertools, collections).

c) Pydantic & validation

- Define Pydantic models for structured data.
- Enforce types (e.g., email, URL, date parsing).
- Handle optional/missing fields.
- Create transformations (@field_validator).

d) Code cleanup

- Refactor a messy script into functions/classes.
- Add docstrings + comments.
- Remove redundancy.
- Add logging instead of print.

e) Mini-MLE tasks

- Compute embeddings and store them.
- Write a batch inference pipeline.
- Implement a hash/feature generator
- Serialize models (pickle, joblib, MLflow).
- Write unit tests (pytest).
- Computes word counts.
- Saves result as parquet.
