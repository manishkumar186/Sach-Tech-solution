import random;

a = 1234;
b = 4321;
data = [];
whole_data = {};

print("Press 1: To Create Account");
print("Press 2: To Check Balance");
print("Press 3: To Deposit");
print("Press 4: To Withdraw");
print("Press 0: To Exit");
print("press 5: To Admin");
print("********************************************************************************");

while True:
    choice = input("Enter choice: ");
    if(choice.isdigit() == True):
        if(choice == "1"):
            user_name = input("Enter Name: ");
            inital_amount = int(input("Enter Initial Amount: "));
            gen_acc_no = random.randint(a,b);
            print("Your Account Created Successfully \nHere is your Acc No: {}\n".format(gen_acc_no));
            data.append(user_name);
            data.append(inital_amount);
            new_data = data.copy();
            whole_data[gen_acc_no] = new_data
            data.clear();
            
        elif(choice == "2"):
            view_acc_no = int(input("Enter Account Number: "));
            if(view_acc_no in whole_data):
                print("Weicome {}".format(whole_data[view_acc_no][0]));
                print("Here is your balance: Rs. {}/-\n".format(whole_data[view_acc_no][1]));
                
        elif(choice == "3"):
            deposit_acc_no = int(input("Enter Your Account Number: "));
            if(deposit_acc_no in whole_data):
                print("welcome {}".format(whole_data[deposit_acc_no][0]))
                deposit = int(input("Enter Amount to deposit: "));
                new_data = whole_data[deposit_acc_no][1]+deposit
                whole_data[deposit_acc_no][1] = new_data
                print("Your account credited with {}\nCurrent balance Rs. {}/-\n".format(deposit, new_data));
            else:
                 print("Please Enter Valid Account Number!!! ")
                 
        elif(choice == "4"):
            withdraw_acc_no = int(input("Enter Your Account Number: "));
            if(withdraw_acc_no in whole_data):
                print("welcome {}".format(whole_data[withdraw_acc_no][0]));
                withdraw = int(input("Enter Amount to withdraw: "));
                if(whole_data[withdraw_acc_no][1] >= withdraw):
                    new_data = whole_data[withdraw_acc_no][1]-withdraw
                    whole_data[withdraw_acc_no][1] = new_data
                    print("Your account debited with {}\nCurrent balance Rs. {}/-\n".format(withdraw, new_data));
                else:
                    print("You have no sufficent balance in your account !!!\n");
            else:
                print("Please Enter Valid Account Number!!!\n");
                
        elif(choice == "5"):
            password = input("Enter Password: ");
            if(password == "manish"):
                print(whole_data,"\n");
            else:
                print("Please Enter Valid Password !!!\n");
                
        elif(choice == "0"):
            break;

    else:
        print("Choose correct option!!!!\n");