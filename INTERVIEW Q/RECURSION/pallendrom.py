def isPalindrome(strng):
    if strng[0]== strng[-1]:
        return True
    elif strng[0]!= strng[-1]:
        return False
    return isPalindrome(strng[1:len(strng)-1])

print(isPalindrome('naldldn'))

# WRONG !!!!!!!!!!!!


def isPalindrome(strng):
    if len(strng)==0:
        return True
    elif strng[0]!= strng[-1]:
        return False
    return isPalindrome(strng[1:len(strng)-1])

print(isPalindrome('naldldn'))

# RIGHT {}{}{}{}{}{}{}