db=["mahee123@gmail.com",123]
email=input("Enter your email: ")
password=input("Enter your password: ")
if email=="" and password=="":
    res="please enter email and password"
elif email=="":    
    res="please enter email"
elif password=="":
    res="please enter password"
else:
    if email!=db[0] and password!=db[1]:
        res="invalid email and password"
    elif email!=db[0]:
        res="invalid email"
    elif password!=db[1]:
        res="invalid password"
    else:
        res="welcome"
print(res)

