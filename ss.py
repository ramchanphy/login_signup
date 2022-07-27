import json
import os
user_input=int(input("enter 1 for sign-up and 2 for log-in:   "))
if user_input==1:
    username=input("enter your name:   ")
    def mainfun():
        global username
        password1=input("Enter your password:  ")
        password2=input("confirm  password:  ")
        l,u,p,d=0,0,0,0
        for i in password1:  
            if (i.islower()): 
                l+=1 
            if (i.isupper()): 
                u+=1			 
            if (i.isdigit()):
                d+=1
            if i.isalnum():		
                p+=1	
        if (l>=1 and u>=1 and p>=1 and d>=1 or l+p+u+d==len(password1)):
            if password1==password2:
                if len(password1)>=6 or len(password1)<=10:
                    print("password confirm")
                    if(os.path.isfile('login_signup.json')):
                        file_name=open("login_signup.json","r")
                        a=json.load(file_name)
                        for i in a["User"]:
                            if i["username"]==username:
                                print("This user is already exist")
                                break
                        else:
                                dic,d={},{}
                                dic["username"]=username
                                dic["password"]=password1
                                d["description"]=input("About: ")
                                d["Dob"]=input("Date of birth: ")
                                d["Gender"]=input("Gender: ")
                                d["Hobbies"]=input("Hobbies: ")
                                dic["Profile"]=d
                                v=a["User"]
                                v.append(dic)
                                f=open("login_signup.json","w+")
                                json.dump(a,f,indent=4)  
                                f.close()
                                print("Signup Succesfully....")
                                   
                    else:
                            
                            dic,li,d,di={},[],{},{}
                            dic["username"]=username
                            dic["password"]=password1
                            d["description"]=input("About:- ")
                            d["Dob"]=input("Date of birth:- ")
                            d["Gender"]=input("Gender:- ")
                            d["Hobbies"]=input("Hobbies:- ")
                            dic["Profile"]=d
                            li.append(dic)
                            di["User"]=li
                            f=open("login_signup.json","w+")
                            json.dump(di,f ,indent=4)
                            f.close()
                            print("Signup Succesfully....")

                else:
                    print("password must be more than 6 characters")
            else:
                print("both password are not match :(")
        else:
            print("must have atleast a digit, an uppercase and a special characters")
    mainfun()

                            

elif user_input==2:
    a=open("login_signup.json","r")
    f=json.load(a)
    d=input("Enter your user name:- ")
    v=input("Enter your password:-  ")
    for i in f["User"]:
        if i["username"]==d:
            if d==i['username']:
                if v==i['password']:
                    print("Login successful :) .......")
                    print(i)
                    break
                else:
                    print("wrong  password :( .....")
                    break
            else:
                print("wrong username :( ....")
                break
        else:
            print("this username doesn't exist")
            break
else:
    print("Your enter wrong input :( ....")