# Debugging fizzbuzz #
for number in range(1, 101):
  if number % 3 == 0 or number % 5 == 0:
    print("FizzBuzz")
# here we have to use elif to avoid printing FizzBuzz and Fizz both
  if number % 3 == 0:
    print("Fizz")
# here we have to use elif to avoid printing FizzBuzz and Buzz both
  if number % 5 == 0:
    print("Buzz")
# here we have to remove the square bracket
  else:
    print([number])