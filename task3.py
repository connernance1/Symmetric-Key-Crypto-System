from utility import *
import copy
import math
import itertools

# Gathers User Input / Input Validation


def getInput():
    print('\n------ Task 3 ------ ')
    print('\n Copy and Paste Plain Text Suggestions: 1: "hello world"   or  2: "we confirm the delivery of the documents later" \n')
    plainText = input('Please Enter a Plain Text Message:  ')
    print('\nSuggestions: 1: "eorhllowld"   or   2: "ilwrmlyfeufesndrteetiotdmcrhvhoeoeecnta"\n ')
    cipherText = input('Please Enter a Cipher Text:  ')

    plainText = plainText.replace(" ", "")

    while len(plainText) != len(cipherText) or sorted(plainText) != sorted(cipherText):
        print('\nPlease Enter a Plain Text and CipherText that are the same Length and contain all the same characters. \n\n'
              'Suggestions: 1: "hello world"   or  2: "we confirm the delivery of the documents later" \n')
        plainText = input('Please Enter a Plain Text Message:  ')
        print('\nSuggestions: 1: "eorhllowld"   or   2: "eorhllowld" \n')
        cipherText = input('Please Enter a Cipher Text:  ')

        plainText = plainText.replace(" ", "")

    return {'plainText': plainText, 'cipherText': cipherText}

# Makes an Array of all possible Permutations for length of Key


def makeLists(length):
    template = []
    lists = []
    for i in range(length):
        template.append(i)
    combinations = list(itertools.permutations(template))
    for comb in combinations:
        lists.append(list(comb))

    return lists


# Prints an array into a string
def toString(list):
    temp = ''
    for element in list:
        temp += str(element)
    return temp

# Turns disrupted transposition into Cipher text string


def cipherToString(tempCipher, list, length):
    cipherString = ''
    ct = 0
    rowCount = 0
    while ct < length:
        for i in range(len(tempCipher)):
            hasAppended = False
            for j in range(len(list)):
                t1 = list.index(rowCount)
                max = len(tempCipher[i]) - 1
                if list.index(rowCount) <= max and hasAppended == False:
                    num = list.index(rowCount)
                    letter = tempCipher[i][list.index(rowCount)]
                    if letter != '' or letter != None:
                        cipherString += letter
                        hasAppended = True
                        ct += 1
        rowCount += 1

    return cipherString


# If the cipher string is the same as the real cipher then return the key
def isMatch(realCipher, tempCipher, list, length):
    temp = cipherToString(tempCipher, list, length)
    if realCipher == temp:
        Key = toString(list)
        return {'key': Key, 'isMatch': True}
    return {'isMatch': False}

# Checks all permutations of specified length Key to see
# if there is a match of Cipher Text


def findKey(lists, plainText, cipherText, length):

    if (length * length) > len(plainText):
        cnt = 0
        for list in lists:
            # print((cnt))
            cnt += 1
            count = 0
            rowCount = 0
            Cipher = []
            leftOver = False

            while count < len(plainText):
                for i in range(length):
                    if leftOver == False:
                        Cipher.append([])
                    rowCount += 1
                    if leftOver:
                        for j in range(len(Cipher[i]), length):
                            if count < len(plainText):
                                Cipher[i].append(plainText[count])
                                count += 1
                                # function that checks if match, if true return
                                if count == len(plainText):
                                    key = isMatch(
                                        cipherText, Cipher, list, len(plainText))
                                    if key['isMatch']:
                                        return key
                                    else:
                                        break
                    else:
                        for j in range(length):
                            max = list.index(i)
                            if j <= max and count < len(plainText):
                                Cipher[i].append(plainText[count])
                                count += 1
                                # function that checks if match, if true return
                                if count == len(plainText):
                                    key = isMatch(
                                        cipherText, Cipher, list, len(plainText))
                                    if key['isMatch']:
                                        return key
                                    else:
                                        break
                        if rowCount == length and count < len(plainText):
                            leftOver = True
    return {'isMatch': False}
