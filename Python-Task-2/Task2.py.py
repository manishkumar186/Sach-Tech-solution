while True:
    accno = input("enter account number");
    fs = accno[:-3];
    ss = accno[-3:];
    m= len(accno)
    if(m<10):
        print("please enter 10 digit account number");
    elif(accno.isnumeric()==False):
        print("Account number must be digit not a alphanumeric");
    else:
        for i in fs:
            print("*",end="")
        print(ss);
        break;
