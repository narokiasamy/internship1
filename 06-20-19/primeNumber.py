# given prime number, list all prime numbers before hand

number = int(input("Enter number here: "))

if (number < 1):
  for i in range (number + 1, -1):
    if (number % i == 0):
      print ("Your number is not a prime number!")
      break
    elif (i == -2):
      print ("Your number is  a prime number!")
      break
    else:
      continue
elif (number > 1):
  for i in range (2, number + 1):
    if (i == number):
      print ("Your number is a prime number!")
      break
    elif (number % i == 0):
      print ("Your number is not a prime number!")
      print ("git")
      break
    else:
      continue



