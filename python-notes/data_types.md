# Python Data Types

## Example Variables

```python
name = "Nandha"              # str
age = 30                     # int
salary = 50000.75            # float
is_employee = True           # bool
skills = ["Python", "Spark"] # list
location = ("Chennai", "TN") # tuple
ids = {101, 102, 103}        # set
details = {"id": 101}        # dict
manager = None               # NoneType
```

## Data Types Summary

| Data Type | Mutable | Ordered | Description | Example |
|------------|----------|----------|-------------|----------|
| `int` | No | N/A | Stores whole numbers | `30` |
| `float` | No | N/A | Stores decimal numbers | `50000.75` |
| `bool` | No | N/A | Stores True or False values | `True` |
| `str` | No | Yes | Stores text data | `"Nandha"` |
| `list` | Yes | Yes | Stores multiple items, allows duplicates and modifications | `["Python", "Spark"]` |
| `tuple` | No | Yes | Stores multiple items, cannot be modified after creation | `("Chennai", "TN")` |
| `set` | Yes | No | Stores unique values, removes duplicates automatically | `{101, 102, 103}` |
| `dict` | Yes | Yes | Stores data as key-value pairs | `{"id": 101}` |
| `NoneType` | No | N/A | Represents absence of a value | `None` |

## Quick Notes

### String (`str`)
- Used to store text.
- Immutable (cannot be changed directly).
- Supports indexing and slicing.

### List (`list`)
- Ordered collection.
- Mutable (can add, update, remove elements).
- Allows duplicate values.

```python
skills.append("Scala")
```

### Tuple (`tuple`)
- Ordered collection.
- Immutable (cannot be modified).
- Faster than lists for fixed data.

```python
location = ("Chennai", "TN")
```

### Set (`set`)
- Unordered collection.
- Mutable.
- Stores only unique values.

```python
numbers = {1, 2, 2, 3}
# Output: {1, 2, 3}
```

### Dictionary (`dict`)
- Stores key-value pairs.
- Mutable.
- Keys must be unique.

```python
employee = {
    "name": "Nandha",
    "age": 30
}
```

### NoneType
- Represents no value.
- Often used as a default placeholder.

```python
manager = None
```

## Interview Questions

| Question | Answer |
|-----------|---------|
| Difference between List and Tuple? | List is mutable, Tuple is immutable. |
| Difference between Set and List? | Set stores unique values and is unordered; List allows duplicates and is ordered. |
| Difference between Dict and List? | Dict stores key-value pairs; List stores indexed values. |
| Which Python collections are mutable? | List, Set, Dict |
| Which Python collections are immutable? | String, Tuple |