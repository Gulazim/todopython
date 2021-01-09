def fizz_buzz(a):
    if a % 3 == 0:
        print("Fizz")
    elif a % 5 == 0:
        print("Buzz")
    elif a % 3 == 0 and a % 5 == 0:
        print("FizzBuzz")
    else:
        print(a)

fizz_buzz(9)
fizz_buzz(5)
fizz_buzz(23)