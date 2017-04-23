
def calc_fib(n):
    a,b=0.0,1.0
    for i in range(n):
        a,b=b,a+b
    return a
def main():
    n=int(input('input n s.t. fib(n): '))
    res=calc_fib(n)
    print(res)
if __name__ == '__main__':
    main()