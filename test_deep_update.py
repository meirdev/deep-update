from deep_update import deep_update


def test_deep_update_1():
    dict1 = {"a": {"b": {"c": 1}}}
    dict2 = {"a": {"b": {"d": 2}}}
    deep_update(dict1, dict2)
    assert dict1 == {"a": {"b": {"c": 1, "d": 2}}}


def test_deep_update_2():
    dict1 = {"a": {"b": {"c": 1}}, "d": 2, "e": 3}
    dict2 = {"a": {"b": {"c": 2}}, "d": 3, "f": 4}
    deep_update(dict1, dict2)
    assert dict1 == {"a": {"b": {"c": 2}}, "d": 3, "e": 3, "f": 4}
