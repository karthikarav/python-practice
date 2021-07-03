import json
print(json.dumps({"name":"kaka","age":43}))
print(json.dumps(["kiwi","apple"]))
print(json.dumps(None))
print(json.dumps("bananas"))


import json
x = '{"name":"kaka","age":43}'
y = json.loads(x)
print(y["name"])
