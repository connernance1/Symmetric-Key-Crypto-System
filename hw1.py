# Conner Nance
# A01836222
# Date: 10/5/2020
# Homework 1
# Computer Security

# Main Function is at bottom of File.

import copy
import math
import itertools

from task1 import *
from task2 import *
from task3 import *
from utility import *

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

# Task 1 Outline
# 1. Gathers input from user to get


def Task1():
    keyAttributes = getKey()
    Cipher1 = colTrans(keyAttributes)
    finalCipher = getFinalCipher(Cipher1, keyAttributes)

    return {'CipherText': finalCipher, 'keyAttributes': keyAttributes}


#  Task 2 Outline
# 1. Ciphertext to binary
# 2. binary to decimal via XOR operation
# 3. dicimal through polybius square to get letters
# 4. reverse column transposition


def Task2(CipherText, keyAttributes):
    decimalArray = toDecimal(CipherText, keyAttributes['padKey'])
    plainText = decryptColTrans(decimalArray, keyAttributes['cKey'])
    return plainText


# Task 3 Outline
# 1. For possible Key Lengths 1-8
#    check all possible cipherTexts
#    for each Key until a match is found
# 2. Once Match is found ouput the Key used to find match
def Task3():
    texts = getInput()
    for length in range(1, 9):
        lists = makeLists(length)

        # Create isMatch function that returns a Key and True or false variable
        # for each item in list create a new cipher using key and compare it with
        # desired cipher, If they match then you know that Key correct.

        key = findKey(lists, texts['plainText'], texts['cipherText'], length)

        if key['isMatch']:
            return key['key']

    return 'This Plain/Cipher Text pair does not have a Valid Encryption Key'


if __name__ == '__main__':
    task1 = Task1()
    CipherText = task1['CipherText']
    keyAttributes = task1['keyAttributes']
    print('\n', 'Encrypted Message: ', CipherText, '\n')

    print('------ Task 2 ------')
    print('\n Decrypting Message...\n')

    PlainText = Task2(CipherText, keyAttributes)

    print(PlainText)

    key = Task3()
    print('\n The Key for Task 3 is:  ', key, '\n\n')
