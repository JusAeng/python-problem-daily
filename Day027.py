def is_palindrome(s:str):
    if s == s[::-1]:
        return True
    return False
print(is_palindrome(input()))