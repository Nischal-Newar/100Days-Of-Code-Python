#### Check if a numer is prime number ####
# function to check prime number
def prime_checker(number):
    flag = False
    if number > 1:
        for i in range(2, number):
            if number % i == 0:
                flag = True
                break
    if flag:
        print(number, "is not a prime number")
    else:
        print(number, "is a prime number")

n = int(input("Check this number: "))
prime_checker(number=n)