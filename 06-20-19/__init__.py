# given number, print all fibonacci numbers before

number = int(input("Enter your number here: "))

first = 1
second = 1

for i in range (1,number):
  third = (first + second)
  if (third >= number):
    break
  else:
    first = second
    second = third
    print (int(third))