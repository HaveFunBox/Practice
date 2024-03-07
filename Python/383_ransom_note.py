def canConstruct(ransomNote, magazine):
    mag = {}
    for letter in magazine:
        if letter in mag:
            mag[letter] += 1
        else:
            mag[letter] = 1
    
    for letter in ransomNote:
        if letter in mag and mag[letter] != 0:
            mag[letter] -= 1
        else:
            return False
    return True

print(canConstruct('a', 'ab'))