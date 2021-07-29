def reverse(strng):
    if len(strng) <= 1:
        return strng
    return strng[len(strng)-1] + reverse(strng[:len(strng)-1])


print(reverse("Ashutosh"))
print(reverse("P"))
print(reverse("nohtyP"))
