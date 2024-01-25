class Time_set_0(Exception):
    pass

def S(func):
    def warper(v1,v2,time):
        a=func(v1,v2,time)
        print(f"a={a}")
        print(f"S={(a*time**2)/2}")

    return warper

@S
def a(v1, v2, time):
    try:

        a=(v2-v1)/time

    except Time_set_0:
        print("time_nepravilno")
    else:
        return a

try:
    v1=int(input())
    v2=int(input())
    time=int(input())
    if time <=0:
            raise Time_set_0('time_nepravilno')

    a(v1,v2,time)

except ValueError:
    print('nou chisla')
except Time_set_0:
    print("time<=0")




