def validate(rules, dictionary):
    for key, prefix, middle, suffix in rules:
        if key in dictionary:
            if dictionary[key].startswith(prefix) and dictionary[key].endswith(suffix):
                value = dictionary[key]
                if middle in value[1:-1]:
                    continue
                else:
                 return False
        else:
            return False
    return True

rules = {("key1", "", "inside", ""), ("key2", "start", "middle", "winter")}
d = {"key1": "come inside, it's too cold out", "key2": "start is middle winter"}

print(validate(rules, d))
