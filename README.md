# Deep update

Deep update to dictionary.

_Note: The original dictionary (`dict1`) is modified._

## Example

```python
from deep_update import deep_update

a = {
    "a": 1,
    "b": {
        "c": 2,
        "d": 3,
    },
    "e": 4,
}

b = {
    "b": {
        "c": 5,
    },
    "e": 6,
}

deep_update(a, b)

print(a)

# {'a': 1, 'b': {'c': 5, 'd': 3}, 'e': 6}
```
