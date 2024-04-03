import json
s = open("en_us.json").read()
if "\\'" in s:
    s = s.replace("\\'", "\'")
# print(s)
print(json.loads(s))
