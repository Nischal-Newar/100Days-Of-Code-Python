# Debugging leap year #

# here we have to convert the input to integer
year = input("Which year do you want to check?")

# to perform mathematical operations, year needs to be an integer
if year % 4 == 0:
  if year % 100 == 0:
    if year % 400 == 0:
      print("Leap year.")
    else:
      print("Not leap year.")
  else:
    print("Leap year.")
else:
  print("Not leap year.")