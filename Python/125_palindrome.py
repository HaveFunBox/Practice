def isPalindrome(s):
    s = s.lower()
    front = 0
    back = len(s) - 1
    valid = False

    while not valid:
        if front != back and front < back:
            if s[front].isalnum():
                if s[back].isalnum():
                    if s[front] == s[back]:
                        front += 1
                        back -=1
                    else:
                        return False
                else:
                    back -=1
            else:
                front += 1
        else:
            return True
        
test = "A man, a plan, a canal: Panama"
print(isPalindrome(test))