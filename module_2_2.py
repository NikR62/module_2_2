first = input()
second = input()
third = input()
if first == second and second == third and third == first:
    print(3)
elif ((first == second and second != third)
    or (first != second and second == third)
    or (first == third and second != third)):
    print(2)
else:
    print(0)