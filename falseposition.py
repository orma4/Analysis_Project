from math import sin
def f(x):
    "Returns a desired function"
    x=float("%.4f" %x)
    return sin(x)
i=1
def regulaFalsi(a, b,maxiteration,i):
    "Prints root of f(x) in interval [a, b]"
    if f(a) * f(b) >= 0:
        print("You have not assumed right a and b")
        return -1

    c = maxiteration  #Initialize result

    if  maxiteration>=0:
        # Find the point that touches x axis
        c = (a * f(b) - b * f(a)) / (f(b) - f(a))
        if maxiteration == 0:
            print("The value of root is : ", '%.4f' % c)
            return -1
        print('c=',c)
        print('iteration',i,':','f(a)=',f(a),'f(c)=' ,f(c),'f(b)=', f(b))
        #Check if the above found point is root
        if f(c) == 0:
            print("The value of root is : ", '%.4f' % c)
            return -1
        #Decide the side to repeat the steps
        elif f(c) * f(a) < 0:
            b = c
        else:
            a = c
        return regulaFalsi(a,b,maxiteration-1,i+1)
    else:
        return -1
regulaFalsi(2,4,4,i)
