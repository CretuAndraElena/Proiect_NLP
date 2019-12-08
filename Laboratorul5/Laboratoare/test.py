import json
lst = ["asa",[("name", "value"), ("name2", "value2")],[("name", "value"), ("name2", "value2")]]
rs = json.dumps(dict(lst))
print(rs)