set1 = set(input().split())
set2 = set(input().split())

def is_subset(set1, set2):
    if set1 < set2:
        return True
    else:
        return False

print(is_subset(set1, set2))