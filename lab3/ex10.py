def ex10(map):
    visited = set()
    result = []
    currentKey = map['start']

    while currentKey not in visited:
        visited.add(currentKey)
        result.append(currentKey)
        currentKey = map[currentKey]

    return result

print(ex10({'start': 'a', 'b': 'a', 'a': '6', '6': 'z', 'x': '2', 'z': '2', '2': '2', 'y': 'start'}))
