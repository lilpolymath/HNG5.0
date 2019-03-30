def FizzBuzz():
     for i in range(101):
          if i%21 == 0:
               print("FizzBuzzWoof")
          elif i%15 == 0:
               print("FizzBuzz")
          elif i%5 == 0:
               print("Buzz")
          elif i%3 == 0:
               print("Fizz")
          elif i%7 == 0:
               print("Woof")
          else:
              print(i)

FizzBuzz()
