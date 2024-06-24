def logicaloprators():
    n1=int(input("Enter number one:"))
    n2=int(input("Enter number two:"))
    n3=int(input("Enter number three:"))
    x=n1==n3&n1>n2
    print("n1=n3&n1>n2:",x)
    x=n1==n3|n1>n2
    print("n1=n3|n1>n2:",x)
    x=n1==n3&n1>n2
    print("n1=n3&n1>n2&not(n2):",x)
logicaloprators()
           
