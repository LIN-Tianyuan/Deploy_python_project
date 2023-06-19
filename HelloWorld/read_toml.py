import toml
import sys

"""
Usage:
>> python read_toml.py pyproject.toml project.author.name
>> LIN
"""
def get_value(keys, i, setting):
    string = setting.get(keys[i])
    if isinstance(string, dict):
        if i+1 < len(keys):
            return get_value(keys, i+1, string)
    return string


if len(sys.argv) == 3:
    filename = sys.argv[1]
    getvalue = sys.argv[2]
    with open(filename, mode="r") as fp:
        config = toml.load(fp)
    toml_keys = getvalue.split(".")
    print(get_value(toml_keys, 0, config))
else:
    print("Arguments Error!")
