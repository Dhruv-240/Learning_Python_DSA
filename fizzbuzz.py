
# Complete the 'fizzBuzz' function below.
#
# The function accepts INTEGER n as parameter.
#

def fizzBuzz(n):
    # number = int(input())

    i=0
    while i!=n:
        if i%3 == 0 and i%5 ==0:
            print("FizzBuzz")
        elif i%3==0:
            print("Fizz")
        elif i%5==0:
            print("Buzz")
        else:
            print(i)
        i+=1
        

if __name__ == '__main__':
    n = int(input().strip())

    fizzBuzz(n)
