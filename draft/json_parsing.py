import json

string_as_json_format = '{"web":"abc", "api":"qwe"}'
obj = json.loads(string_as_json_format)

key = "api"

if key in obj:
    print(obj[key])
else:
    print(f"Ключа {key} в JSON нет")