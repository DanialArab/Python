
### json.load() vs json.loads():

- json.load(): Load from a file
You use this when you're reading a JSON file directly.

It expects a file-like object, such as the one you get from open(...).

json.loads(): Load from a string
You use this when you already have a JSON-formatted string (e.g., from an API response or clipboard).

It expects a string, not a file.

Rule of Thumb
Got a file → use json.load()

Got a string → use json.loads()

| Function        | Used When...                   | Input Type  | Example Use                    |
| --------------- | ------------------------------ | ----------- | ------------------------------ |
| `json.load(f)`  | Reading JSON **from a file**   | File object | `json.load(open("file.json"))` |
| `json.loads(s)` | Reading JSON **from a string** | String      | `json.loads('{"a": 1}')`       |
