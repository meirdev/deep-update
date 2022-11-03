import copy
from typing import Any, Callable, TypeVar

T = TypeVar("T")


def deep_update(
    dict1: dict[Any, Any],
    dict2: dict[Any, Any],
    *,
    copy_fn: Callable[[T], T] = copy.deepcopy
) -> dict[Any, Any]:
    for i in dict2:
        if isinstance(dict2[i], dict) and i in dict1 and isinstance(dict1[i], dict):
            dict1[i] = deep_update(dict1[i], dict2[i])
        else:
            dict1[i] = copy_fn(dict2[i])

    return dict1
