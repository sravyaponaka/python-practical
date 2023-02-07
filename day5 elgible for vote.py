try:
    print("enter the age")
    age=int(input("age="))
    if(age>=18):
        print("The person is for eligible for voting")
    elif(age<0):
        print("invalid input")
    else:
        print("The person is not eligible to vote until",18-age,"years")
except ValueError:
    print("enter valid input")
