def checkAntipalindromes(string):
    if len(string) == 0:
        return (False, 0)
    elif string != (string[::-1]):
        return (True, len(string))
    else:
        return checkAntipalindromes(string[1:])

inputString = input()
hasAntipalindrome, antipalindromeLen = checkAntipalindromes(inputString)
if hasAntipalindrome:
    print(antipalindromeLen)
else:
    print(0)
