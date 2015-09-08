## 숫자 재귀(recursion)

def sumRecurrsion(inputNum):
    if inputNum == 1:
        return 1
    else:
        return inputNum + sumRecurrsion(inputNum-1)

print("합계 : ", sumRecurrsion(10))

def wordPalindrome(inputWord):
    if len(inputWord) == 1:
        return True
    else:
        if inputWord[0] == inputWord[-1]:
            return wordPalindrome(inputWord[1:-1])
        else:
            return False

print("회문인가요? ", wordPalindrome("madam"))
print("회문인가요? ", wordPalindrome("a"))
print("회문인가요? ", wordPalindrome("race car"))
print("회문인가요? ", wordPalindrome("hello"))
