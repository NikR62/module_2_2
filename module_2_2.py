first = input()
second = input()
third = input()
if first == second and second == third and third == first:
    print(3)
elif first == second or second == third or third == first:
    print(2)
else:
    print(0)