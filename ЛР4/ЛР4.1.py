import json


def task() -> float:
    with open('input.json', 'r') as file:
        data = json.load(file)
    summ = 0
    for dict_ in data:
        summ += dict_["score"] * dict_["weight"]
        value = round(summ, 3)
    return summ


print(task())
