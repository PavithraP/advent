import json
    
data = json.load(open('12.txt'))

def sum1(data):
    total = 0
    if isinstance(data, int):
        total += data
    elif isinstance(data, dict):
        if 'red' not in data.values():
            total += sum1(data.values()) + sum1(data.keys())
    elif isinstance(data, list):
        total += sum(sum1(x) for x in data)
    return total

print sum1(data)
