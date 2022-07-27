import json,os
user=int(input("enter 1 if signup and 2 if login:- "))
if user==1:
    def fun():
        username=input("enter the name:- ")
        password=input("enter the password:- ")
        number="1234567890"
        upper="abcdefghijklmnopqrstuvwxyz"
        lower="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        symbol="!@#$%^&*?|"
        n,u,l,s=0,0,0,0
        p=len(password)
        i=0
        while i<p:
            if password[i] in number:
                n+=1
            if password[i] in upper:
                u+=1
            if password[i] in lower:
                l+=1
            if password[i] in symbol:
                s+=1
            i+=1
        if n>=1 and u>=1 and l>=1 and s>=1:
            print("strong password")
        else:
            print("sorry your password id too weak")
        password1=input("conferm your password:-")
        if password==password1:
            print("password comferm")
            if (os.path.isfile("myinfo.json")):
                f=open("myinfo.json","r")
                a=json.load(f)
                for i in a["user"]:
                    if i in["username"]==username:
                        print("user already exist")
                        break
                else:
                    dict={}
                    d={}
                    dict["user"]=user
                    dict["username"]=username
                    d["about yourself"]=input("anout yourself:-")
                    d["Gender"]=input("enter your gender:-")
                    d["hobbies"]=input("enter your hobbies:-")
                    d["date of birth"]=input("enter your date of birth:-")
                    d["qualification"]=input("enter your qualification:-")
                    d["current address"]=input("enter your current address:-")
                    dict["profile"]=d
                    v=a["user"]
                    v.append(dict)
                    f1=open("myinfo.json","w+")
                    json.dump(a,f1,indent=4)
                    f1.close()
                    print("succesfully signup")
            else:
                dict,l,d,dic={},[],{},{}
                dict["user"]=user
                dict["username"]=username
                d["about"] =input("write something about you:-...")
                d["gender"]=input("enter your gender:-...")
                d["hobbies"]=input("enter your hobbies:-....") 
                d["date of birth"]=input("enter your date of birth:-...")
                d["qualification"]=input("enter your qualification:-...")
                d["current address"]=input("enter your current address:-...")
                dict["profile"]=d
                l.append(dict)
                dic["user"]=l
                f2=open("myinfo.json","w+") 
                json.dump(dic,f2,indent=4)
                f2.close()
                print("succesefully signup....")
        else:
            print("password is not correct:-...")
    fun()
elif user==2:
    a=open("myinfo.json","r")
    f1=json.load(a)
    d=input("enter the user name:-..")
    v=input("enter the password:-..")
    for i in f1["user"]:
        if d==i["username"]:
            if v==i["password"]:
                print("login succeseful")
                print(i)
            else:
                print("your password is wrong....")
        else:
            print("user name is wrong....")
else:
    print("invalid...")
        