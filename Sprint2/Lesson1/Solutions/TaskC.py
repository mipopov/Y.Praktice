firstString = str(input())
secondString = str(input())

def isSubstr(needle, haystack):
    current_pos = 0
    for c in needle:
        current_pos = haystack.find(c, current_pos) + 1
        if current_pos == 0 : return False
    return True

print(isSubstr(firstString, secondString))