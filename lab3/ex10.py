def loop(mapping):
    visited = set()
    result = []
    current_key = mapping['start']

    while current_key not in visited:
        visited.add(current_key)
        result.append(current_key)
        current_key = mapping[current_key]

    return result

result = loop({'start': 'a', 'b': 'a', 'a': '6', '6': 'z', 'x': '2', 'z': '2', '2': '2', 'y': 'start'})
print(result)
