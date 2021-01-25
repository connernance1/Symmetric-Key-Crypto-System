from utility import *
import copy
import math
import itertools

matrix = [['E', 'Y', 'O', 'P', 'D', '9'],
          ['2', 'H', 'Q', 'X', '1', 'I'],
          ['R', '3', 'A', 'J', '8', 'S'],
          ['F', '0', 'N', '4', 'G', '5'],
          ['Z', 'B', 'U', 'V', 'C', 'T'],
          ['M', '7', 'K', 'W', '6', 'L']]

alph = ['A', 'B', 'C', 'D', 'E',
        'F', 'G', 'H', 'I', 'J',
        'K', 'L', 'M', 'N', 'O',
        'P', 'Q', 'R', 'S', 'T',
        'U', 'V', 'W', 'X', 'Y', 'Z']


# Performs XOR operation on binary, returns new list of Decimal
def toDecimal(cipherText, padKey):
    decArray = []   # An array of arrays that contain the decimal pair for each letter for polybius square
    for i in range(len(cipherText)):
        if i % 2 == 0:
            dec = cipherText[i] + cipherText[i+1]
            decimal = format(int(dec), '06b')
            decArray.append(decimal)

    xor = format(int(padKey), '06b')
    for i in range(len(decArray)):
        decimal = int(xor, 2) ^ int(decArray[i], 2)
        decimal = str(decimal)
        if len(decimal) < 2:
            decimal = '0' + decimal
            decArray[i] = [int(decimal[1]), int(decimal[0])]
        else:
            decArray[i] = [int(decimal[1]), int(decimal[0])]

    return decArray


# Converts the Encrypted Decimal message back to binary
# performs XOR operation on Binary
# Turns encrpyted text cipher message back to Plain Text
def decryptColTrans(decimalArray, cKey):
    Key = []            # Array of Dictionaries of Key mapping for polybius square
    compositeKey = ""   # Text representation of Key
    orderedKey = []     # Alphabetical Column Ordering for Key
    originalKey = []    # Original Column Ordering for Key
    Cipher = []         #
    cipherMatrix = []   #
    ogKey = []          #

    # Splits the Decimal Encryption into pairs in a list
    for i in range(len(cKey)):
        if i % 2 == 0:
            temp = {}
            temp[matrix[int(cKey[i+1])][int(cKey[i])]
                 ] = {'row': cKey[i + 1], 'col': cKey[i]}
            compositeKey += matrix[int(cKey[i+1])][int(cKey[i])]
            Key.append(temp)
    for decimal in decimalArray:
        Cipher.append(matrix[decimal[0]][decimal[1]])
    for i in range(len(compositeKey)):
        og = {}
        og[compositeKey[i]] = i
        originalKey.append(og)
        ogKey.append(compositeKey[i])

    temp1 = {}
    ct = 0
    for letter in alph:
        if compositeKey.count(letter) > 1:
            for i in range(compositeKey.count(letter)):
                temp1[letter] = ct
                orderedKey.append(temp1)
                ct += 1
                temp1 = {}

        elif letter in compositeKey:
            temp1[letter] = ct
            orderedKey.append(temp1)
            ct += 1
            temp1 = {}

# Determins how many rows and columns are in matrix based on Key Size

    # Find the missing rows(rows that have one less character) by
    # getting the index of the OG row and converting
    # the index to its 'KEY' Counterpart
    # Then when you build the matrix
    # for the exception i is in the List/Dict
    # add one less character to that row.
    row = len(Key)
    col = math.ceil(len(Cipher) / len(Key))

    size = (row) * (col)
    metric = size - len(Cipher)
    remainder = False
    missingList = []
    missingValues = []
    if metric > 0:
        remainder = True
        max = len(Key) - 1
        tempKey = len(Key) - metric - 1
        missing = []
        for i in range(max, tempKey, -1):
            key = ''
            for j in range(len(originalKey)):
                key = get_key(originalKey[j], i)
                if key != None:
                    missing.append({key: i})
                    missingList.append(i)

        alphaKey = copy.copy(orderedKey)
        for i in range(len(alphaKey)):
            if i in missingList:
                missLetter = findChar(originalKey, i)
                val = findIndex(alphaKey, missLetter)
                missingValues.append(val['index'])


# Build matrix according to Dimensions
    count = 0
    for i in range(row):
        if i in missingValues and remainder:
            for j in range(col - 1):
                if count < len(Cipher):
                    if j == 0:
                        cipherMatrix.append([])
                    cipherMatrix[i].append(Cipher[count])
                    count += 1
        else:
            for j in range(col):
                if count < len(Cipher):
                    if j == 0:
                        cipherMatrix.append([])
                    cipherMatrix[i].append(Cipher[count])
                    count += 1

# Print out Plain Text using Ordering of the Key
    plainText = ''
    for i in range(len(cipherMatrix)):
        letter = get_key(orderedKey[i], i)
        cipherMatrix[i].insert(0, letter)
        temp = cipherMatrix[i]
        tempstr = ''
        for element in temp:
            tempstr += element
        # for j in range(len(cipherMatrix[i])):
        cipherMatrix[i] = {'list': tempstr, 'used': False}

    for i in range(len(originalKey)):
        for j in range(len(cipherMatrix)):
            if (cipherMatrix[i]['used'] == False and cipherMatrix[i]['list'][0:1] == (ogKey[j])[0:1]):
                if len(ogKey[j]) == 1:
                    ogKey[j] = cipherMatrix[i]['list']
                    cipherMatrix[i]['used'] = True
    for i in range(len(ogKey)):
        ogKey[i] = (ogKey[i])[1:]
    for j in range(len(ogKey[0])):
        for i in range(len(ogKey)):
            if j < len(ogKey[i]):
                plainText += ogKey[i][j]
    return plainText
