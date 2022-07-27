import json,os
def function():
    user=input("Login or Sign_up:-")
    if user=="signup":
        ur_name=input("enter your name:")
        password=input("enter the password")
        p=len(password)
        symbol="@#$!%&"
        number="1234567890"
        upper="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        lower="abcdefghijklmnopqrstuvwxyz"
        s,n,u,l=0,0,0,0
        i=0
        while i<len(password):
            if password[i] in symbol:
                s+=1
            if password[i] in number:
                n+=1
            if password[i] in upper:
                u+=1
            if password[i] in lower:
                l+=1
            i+=1
        if p>6:
            if s>=1 and n>=1 and u>=1 and l>=1:
                print("strong password")
            else:
                print("invalid")
        else:
            print("no")
        password1=input("re-enter the password:- ")
        if password1==password:
            print("your password is a match")
            if (os.path.isfile("userdetails.json")):
                op=open("userdetails.json","r")
                a=json.load(op)
                for i in a["user"]:
                    if i["username"]==ur_name:
                        print("already exist")
                        dict={}
                        d={}
                        dict["username"]=ur_name
                        dict["password"]=password1
                        d["discription"]=input("enter the discription:-")
                        d["D.O.B"]=input("enter your date of birth:/")
                        d["Age"]=int(input("enter your age:-"))
                        d["Gender"]=input("Female/Male:-")
                        d["Hobbies"]=input("enter your hobbie:-")
                        d["Home Address"]=input("enter your home address:-")
                        d["Current Address"]=input("enter the current address:-")
                        dict["profile"]=d        
                        v=a["user"]
                        v.append(dict)
                        f=open("userdetails.json","w+")
                        json.dump(a,f,indent=4)
                        f.close()
                        print("signup succesfully")
                        break
            else:
                dict={}
                l=[]
                d={}
                dict["username"]=ur_name
                dict["password"]=password1
                d["discription"]=input("enter your discription:-")
                d["D.O.B"]=input("enter your date of birth:-")
                d["Gender"]=input("male/female:-")
                d["Hobbies"]=input("enter your hobbies")
                d["Home Address"]=input("enter your home address:-")
                d["Current Address"]=input("enter your current address:-")
                dict["Profile"]=d
                v=a["user"]
                v.append(dict)
                f=open("userdetails.json","w+")
                json.dump(a,f,indent=4)
                f.close()
                print("signup succesfully")
        else:
            print("password is incorrect")
    elif user=="login":
        a=open("userdetails.json","r")
        f=json.load(a)
        d=input("enter your user name:-")
        v=input("enter your user password:-")
        for i in f["user"]:
            if d==i["username"]:
                if v==i["password"]:
                    print("login succesful")
                    print(i)
                    break
                else:
                    print("check your user")
            else:
                print("check your user name")
    else:
        print("invalid")    
function()        
        