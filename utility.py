def get_key(dict, val):
    for key, value in dict.items():
        if val == value:
            return key


def findValue(list, letter):
    # once return value, pop off from array
    ct = 0
    for item in list:
        if letter in item:
            temp = list.pop(ct)
            return {'index': temp[letter], 'keyOrder': list}
        ct += 1


def findIndex(list, letter):
    # once return value, pop off from array
    ct = 0
    for item in list:
        if letter in item:
            temp = list.pop(ct)
            return {'index': temp[letter], 'keyOrder': list}
        ct += 1


def findChar(list, j):
    for item in list:
        temp = get_key(item, j)
        if temp != None:
            if item[temp] == j:
                return temp


def hasNumbers(inputString):
    return any(char.isdigit() for char in inputString)
