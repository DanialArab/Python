
### csv.reader()

- It allows you to read CSV (comma-separated value) files line-by-line, returning each row as a list of strings.
- Each row read from the csv file is returned as a list of strings. No automatic data type conversion is performed unless the QUOTE_NONNUMERIC format option is specified (in which case unquoted fields are transformed into floats).
- Skipping the Header Row: Often the first row is just column names.

Option 1: Use next()
 Important Concepts

Advanced: Use csv.DictReader
If you prefer accessing columns by name instead of index, use csv.DictReader:


| Feature                                | What It Does                              |
| -------------------------------------- | ----------------------------------------- |
| `csv.reader(f)`                        | Returns an iterator over rows in the file |
| `row[0]`, `row[1]`                     | Access values as strings from each row    |
| File should be opened in **text mode** | Use `'r'`, not `'rb'`                     |
| Use `encoding='utf-8'`                 | To handle all standard characters safely  |

Common Interview Gotchas

| Mistake                       | Fix                                               |
| ----------------------------- | ------------------------------------------------- |
| Forgetting to skip header     | Use `next(reader)` or `DictReader`                |
| Not converting string numbers | Use `int(row['doc_id'])`                          |
| Assuming clean input          | Always strip and lowercase text before processing |
| Using external libs           | Use only `csv` and standard library as instructed |


### csv.DictReader()

When to use DictReader:
- When column order might vary
- When readability matters (better than row[0], row[1])
- **Recommended for interviews if field names are available**



### csv.writer()
