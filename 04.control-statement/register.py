db=["xyz@gmail.com"]
em=input("enter your email ")
pas=input("enter your password ")
phone=input("enter phone number ")
dob=input("enter date of birth ")
if em=="":
    res="enter email"
elif pas=="":
    res="enter password"
elif phone=="":
    res="enter phone number"
elif dob=="":
    res="enter date of birth"
else:
    if em==db[0]:
        res="email already exists"
    else:
        res="registration successful"
print(res)