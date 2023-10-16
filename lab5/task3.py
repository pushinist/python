n = int(input())
def towns_game(n):
    previous_towns = []
    for town in range(n):
        previous_towns.append(input())
        if len(previous_towns) == len(set(previous_towns)):
            pass
        else:
            return "REPEAT"
    new_town = input()
    if new_town not in previous_towns:
        return "OK"
    else:
        return "REPEAT"


print(towns_game(n))