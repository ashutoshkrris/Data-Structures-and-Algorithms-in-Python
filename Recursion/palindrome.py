def is_palindrome(strng):
    if len(strng) == 0:
        return True
    if strng[0] != strng[len(strng)-1]:
        return False
    return is_palindrome(strng[1:-1])


print(is_palindrome("awesome"))
print(is_palindrome("foobar"))
print(is_palindrome("tacocat"))
print(is_palindrome('amanaplanacanalpanama'))
print(is_palindrome('amanaplanacanalpandemonium'))
