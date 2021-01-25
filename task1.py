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


def chooseKey():
    userInput = input(
        '\n Please Enter "1" for Template Key "1422555515" \n Or Enter "2" to create custom Key: ')
    if userInput != '1':
        if userInput != '2':
            userInput = input(
                'Invalid Input.\n\n Please Enter "1" for Template Key "1422555515" \n Or Enter "2" to create custom Key: ')

    cKey = ""

    if userInput == "1":
        cKey = '1422555515'
    elif userInput == "2":
        cKey = input('\n Please enter Key(Numbers Only): ')

    keyLength = 0
    while len(cKey) < 4 or (len(cKey) % 2) != 0:
        cKey = input(
            '\n Please enter Key that has\n\n 1. Even amount of Numbers \n 2. At least 4 Numbers:  ')

    return cKey


def getKey():
    print('Computer Security Assignment 1', '\n', '------ Task 1 ------')
    print('\n Suggestions: 1. "hello world"  or  2. "hello world my name is conner" \n')
    plainText = input('Enter a Plaintext message: ')
    cKey = chooseKey()

    plainText = plainText.replace(' ', '')

    # Input Validation for Plain Text
    while hasNumbers(plainText):
        print('\n Please indicate numbers with word counterpart.\n')
        plainText = ''
        plainText = input('Enter a Plaintext message: ')

    # Extract and split One-Time Pad Key from Composite Key
    # Update cKey by taking off last 2 characters
    padKey = cKey[-2:]
    cKey = cKey[:(len(cKey) - 2)]

    return {'cKey': cKey, 'padKey': padKey, 'plainText': plainText}


# Perform Columnar Transposition


def colTrans(keyAttributes):
    # Columnar Transposition to get Key

    keyList = []     # An Array with the letter representation of the cKey
    Key = ""
    keyOrder = []   # An Array of Dictionaries mapping the CKey letter with its original order
    pos = {}

    for element in range(len(keyAttributes['cKey'])):
        if element % 2 == 0:
            keyList.append(matrix[int(
                keyAttributes['cKey'][element + 1])][int(keyAttributes['cKey'][element])])
    for element in keyList:
        Key = Key + element
    for i in range(len(Key)):
        pos[Key[i]] = i
        keyOrder.append(pos)
        pos = {}

    # Create Cipher1 from plain text using Columnar Transposition
    plainTextArray = []
    plainTextMatrix = []

    for el in range(len(keyAttributes['plainText'])):
        plainTextArray.append(el)

    row = len(Key)
    col = (round(len(keyAttributes['plainText']) / len(Key)
                 ) + (len(keyAttributes['plainText']) % len(Key)))

    count = 0
    for i in range(col):
        for j in range(row):
            if count < len(keyAttributes['plainText']):
                if j == 0:
                    plainTextMatrix.append([])
                plainTextMatrix[i].append(keyAttributes['plainText'][count])
                count = count + 1
    # print(plainTextMatrix)

    temp = {}
    order = []  # An Array of Dictionaries mapping the CKey letter with its alphabetical order
    ct = 0
    for letter in alph:
        if Key.count(letter) > 1:
            for i in range(Key.count(letter)):
                temp[letter] = ct
                order.append(temp)
                ct += 1
                temp = {}

        elif letter in Key:
            temp[letter] = ct
            order.append(temp)
            ct += 1
            temp = {}

    # Loop through the matrix in the alphabetical column order and build Cipher1
    Cipher1 = ''
    for j in range(row):
        letter = findChar(order, j)
        val = findValue(keyOrder, letter)
        keyOrder = val['keyOrder']

        for i in range(len(plainTextMatrix)):
            ind = val['index']
            if (i != 0) and (len(plainTextMatrix[i]) != len(plainTextMatrix[i - 1])):
                size = len(plainTextMatrix[i])

                if ind < size:
                    Cipher1 = Cipher1 + plainTextMatrix[i][ind]
            else:
                Cipher1 = Cipher1 + plainTextMatrix[i][ind]

    return Cipher1


def convertToBinary(cipher, keyAttributes):
    temp = []
    for letter in cipher:
        for i in range(len(matrix)):
            for j in range(len(matrix)):
                if matrix[j][i] == letter.upper():
                    temp.append(int(str(i) + str(j)))

    for i in range(len(temp)):
        temp[i] = format(temp[i], '06b')

    padKey = keyAttributes['padKey']
    xorKey = format(int(padKey), '06b')
    for i in range(len(temp)):
        decimal = int(temp[i], 2) ^ int(xorKey, 2)

        if len(str(decimal)) < 2:
            temp[i] = '0' + str(decimal)
        else:
            temp[i] = str(decimal)
    return temp


def getFinalCipher(cipher, keyAttributes):
    numArray = convertToBinary(cipher, keyAttributes)

    finalCypherText = ''
    for i in numArray:
        finalCypherText += i

    return finalCypherText
