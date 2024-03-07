def isPalindrome(s):
    s = [char.lower() for char in s if char.isalnum()]
    return s == s[::-1]

test = "A man, a plan, a canal: Panama"
print(isPalindrome(test))