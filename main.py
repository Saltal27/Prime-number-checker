def prime_checker(number):
    prime_number = True
    for num in range(1, number):
        if num != 1 and number % num == 0:
            prime_number = False
    if prime_number == True:
        print("It's a prime number.")
    else:
        print("It's not a prime number.")
            
n = int(input("Check this number: "))
prime_checker(number=n)


