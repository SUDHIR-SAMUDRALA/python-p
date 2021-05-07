def func():
    #x, y = 12,0
    x= float(input("Enter num value:"))
    y= float(input("Enter denom value:"))
    print(x/y)

try:
    func()
except(ZeroDivisionError):
    print("This Is a Zero division error!")
finally:
    print("**END**")

