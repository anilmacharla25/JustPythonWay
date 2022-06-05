def compute_lcm(n1,n2):
    if n1>n2:
        higher=n1
    else:
        higher=n2
    value=higher
    while True:
        if higher%n1==0 and higher%n2==0:
            print(f"the lcm of two nums is {higher}")
            break
        else:
            higher=higher+value

n1=int(input("enter first number"))
n2=int(input('enter second number'))
compute_lcm(n1,n2)
