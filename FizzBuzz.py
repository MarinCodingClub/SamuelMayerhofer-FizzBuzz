# Hello World program in Python
    
x = 0

while x < 101:
    x = x + 1
    if x % 5 == 0 and x % 3 == 0:
        print "FizzBuzz"
    elif x % 5 == 0:
        print "Fizz"
    elif x % 3 == 0:
        print "Buzz"
    else:
        print x
