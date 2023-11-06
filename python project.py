print("! ! ----------------------------WELCOME TO FEES MANAGEMENT PROGRAM------------------------------ ! ! ")
I="ENTER 1: TO VIEW STUDENTS"
II="ENTER 2: TO ADD STUDENT"
III="ENTER 3: TO SHOW FEES STRUCTURE"
IV="ENTER 4: TO DEPOSIT FEES"
V="ENTER 5: TO SHOW ANNUAL FEE"
print(I)
print(II)
print(III)
print(IV)
print(V)
command=int(input("ENTER YOUR CHOICE (1-5):"))

if command==1:
    print("STUDENT 1:-")
    print("NAME: JASPREET")
    print("ADMISSION NUMBER:3971")
    print("CLASS:11")
    print("SECTION:A")
    print("AGE:17")
    print("FATHER'S NAME: MR. KARAN SHARMA")
    print("MOTHER'S NAME: MRS. POOJA SHARMA")
    print("FATHER'S JOB: DOCTOR")
    print( )
    print("STUDENT 2:-")
    print("NAME: TANVI")
    print("ADMISSION NUMBER: 3972")
    print("CLASS: 12")
    print("SECTION:A")
    print("AGE: 18")
    print("FATHER'S NAME: MR. ANIL VERMA")
    print("MOTHER'S NAME: MRS. ANANYA VERMA")
    print("FATHER'S JOB: ENGINEER")
    print( )
    print("!------THANK YOU FOR USING-------!")

elif command==2:
    print("FOR ADDING A STUDENT, FILL THE FOLLOWING DETAILS:-")
    stud1={ }
    stud2={ }
    stud3={ }
    stud4={ }
    stud5={ }
    stud6={ }
    stud7={ }
    stud8={ }
    name="NAME"
    v1=str(input("ENTER THE NAME OF STUDENT: "))
    admn="ADMISSION NUMBER"
    v2=int(input("ENTER THE ADMISSION N0(OF 4 DIGITS): "))
    clas="CLASS"
    v3=int(input("ENTER THE CLASS:"))
    sec="SECTION"
    v4=str(input("ENTER THE SECTION IN WHICH STUDENT IS STUDYING: "))
    age="AGE OF STUDENT"
    v5=int(input("ENTER THE AGE OF STUDENT: "))
    father="FATHER'S NAME"
    v6=str(input("ENTER THE NAME OF STUDENT'S FATHER: Mr."))
    mother="MOTHER'S NAME"
    v7=str(input("ENTER THE NAME OF STUDENT'S MOTHER: Mrs."))
    job="FATHER'S JOB"
    v8=str(input("ENTER THE JOB OF STUDENT'S FATHER: "))
    stud1[name]=v1
    stud2[admn]=v2
    stud3[clas]=v3
    stud4[sec]=v4
    stud5[age]=v5
    stud6[father]=v6
    stud7[mother]=v7
    stud8[job]=v8
    print("STUDENT INFORMATION HAS BEEN ADDED")
    show= str(input("WANT TO VIEW INFORMATION ADDED(yes/no):- "))
    if show=="yes" or show=="YES":
        print(stud1)
        print(stud2)
        print(stud3)
        print(stud4)
        print(stud5)
        print(stud6)
        print(stud7)
        print(stud8)
    elif show=="no" or show== "NO":
         pass
    print("!--------THANK YOU FOR USING-------!")
elif command==3:

    import json
    fee1={ }
    fee2={ }
    fee3={ }
    fee4={ }
    fee5={ }
    clas1="CLASS 1st and 2nd"
    v1=2700
    clas2="CLASS 3rd to 5th"
    v2=3000
    clas3="CLASS 6th to 8th"
    v3=3500
    clas4="CLASS 9th and 10th"
    v4=4500
    clas5="CLASS 11th and 12th"
    v5={"PCM+HINDI": 4750,"PCM+CS": 5000,"PCMB": 6000,"PCB+HINDI": 4750,"COMMERCE+HINDI": 4250,"COMMERCE+MATHS": 5500,"ARTS":4200}
    print("=> FEES STRUCTURE FOR VARIOUS CLASSES")
    fee1[clas1]=v1
    fee1[clas2]=v2
    fee1[clas3]=v3
    fee1[clas4]=v4
    fee1[clas5]=v5
    print(json.dumps(fee1,indent=5))

elif command==4:
    clas=int(input("ENTER THE CLASS OF STUDENT: "))
    if clas<=2:
        boyfee=2700
        tutionfee=200
        sex=str(input("STUDENT IS GIRL/BOY:- "))
        if sex=="girl" or sex=="GIRL":
            print("No tuition fees for girls")
            print("Thus, fees for a girl student is", boyfee-tutionfee)
        elif sex=="boy" or sex=="BOY":
            print("fee for a boy student is",boyfee)
        else:
            print("Please enter valid option")
            pass
    elif clas>2 and clas<=5:
        boyfee=3000
        tutionfee=300
        sex=str(input("STUDENT IS GLORY/BOY:- "))
        if sex=="girl" or "GIRL":
            print("No tuition fees for girls")
            print("Thus, Fees for a girl student is",boyfee-tutionfee)
        elif sex=='boy' or sex=='boy':
            print("fee for a boy student is",boyfee)
        else:
            print("Please enter valid option")
            pass
    elif clas>5 and clas<=8:
        boyfee=3500
        tutionfee=350
        sex=str(input("STUDENT IS GIRL/BOY:- "))
        if sex=="girl" or sex=="GIRL":
            print("NO TUITION FEE")
            print("Thus, Fees for a girl student is",boyfee-tutionfee)
        elif sex=="boy" or sex=="BOY":
            print("fee for a boy student is",boyfee)
        else:
            print("please enter valid option")
            pass
    elif clas>8 and clas<=10:
        boyfee=4500
        tutionfee=400
        sex=str(input("STUDENT IS GIRL/BOY:- "))
        if sex=="girl" or sex=="GIRL":
            print("No tution fees for girls")
            print("Thus, Fees for a girl student is",boyfee-tutionfee)
        elif sex=="boy" or sex=="BOY":
            print("fee for a boy student is",boyfee)
        else:
            print("Please enter valid option")
            pass
    elif clas>10 and clas<=12:
        p=1500
        c=1500
        m=1500
        b=1500
        comm=4000
        a=4200
        cs=500
        hin=250

        sub=str(input("ENTER THE SUBJECTS(PCM+HIN,PCM=C.S,PCMB,PCB+HIN,COMM+HIN,COMM=M,A):- "))
        if sub=="PCM+HIN" or sub=="pcm+hin":
                fee=p+c+m+hin
                print("TOTAL FEES IS CALCULATED TO BE",fee)
        elif sub=="PCM+C.S" or  sub=="pcm+c.s":
            fee=p+c+m+cs
            print("TOTAL FEES IS CALCULATED TO BE",fee)
        elif sub=="PCMB" or sub=="pcmb":
            fee=p+c+m+b
            print("TOTAL FEES IS CALCULATED TO BE",fee)
        elif sub=="PCB+HIN"or sub=="pcb+hin":
            fee=p+c+b+hin
            print("TOTAL FEES IS CALCULATED TO BE",fee)
        elif sub=="COMM+HIN"or sub=="comm+hin":
            fee=comm+hin
            print("TOTAL FEES IS CALCULATED TO BE",fee)
        elif sub=="COMM+M"or sub=="comm+m":
            fee=comm+m
            print("TOTAL FEES IS CALCULATED TO BE",fee)
        elif sub=="A"or sub=="a":
            fee=a
            print("TOTAL FEES IS CALCULATED TO BE",fee)
        else:
            print("KINDLY ENTER THE VALID SUBJECTS")
    else:
        print("PLEASE ENTER VALID CLASS")
    
    print("# THE ABOVE AMOUNT CALCULATED IS TO BE DEPOSITED ONLY")
    print("ENTER THE ASKED DETAILS")
    admission=int(input("ENTER THE ADMISSION NUMBER(OF 4 DIGITS): "))
    fee=int(input("ENTER THE FEES TO BE DEPOSITED: "))
    quarter=str(input("ENTER THE QUARTER OF FEE SUBMISSION(I to IV): "))
    print("!!----------FEES DEPOSITED--------!!")
    print("!----------THANK YOU FOR USING--------!")
elif command==5:
    clas=int(input("ENTER THE CLASS FOR WHICH YOU WANT TO VIEW THE ANNUAL FEES: "))
    if clas<=2:
        boyfee=2700
        tutionfee=200
        sex=str(input("STUDENT IS GIRL/BOY:- "))
        if sex=="girl" or sex=="GIRL":
            print("No tution fees for girls")
            print("Thus, annual fees for a girl student is",(boyfee-tutionfee)*12)
        elif sex=="boy" or sex=="BOY":
            print("Annual fee for a boy student is",boyfee*12)
        else:
            print("Please enter valid option")
            pass
    elif clas>2 and clas<=5:
        boyfee=3000
        tutionfee=300
        sex=str(input("STUDENT IS GIRL/BOY:- "))
        if sex=="girl" or sex=="GIRL":
            print("No tution fees for girls")
            print("Thus, annual fees for a girl student is",(boyfee-tutionfee)*12)
        elif sex=="boy" or sex=="BOY":
            print("Annual fee for a boy student is",boyfee*12)
        else:
            print("Please enter valid option")
            pass
    elif clas>5 and clas<=8:
        boyfee=3500
        tutionfee=350
        sex=str(input("STUDENT IS GIRL/BOY:- "))
        if sex=="girl" or sex=="GIRL":
            print("No tution fees for girls")
            print("Thus, annual fees for a girl student is",(boyfee-tutionfee)*12)
        elif sex=="boy" or sex=="BOY":
            print("Annual fee for a boy student is",boyfee*12)
        else:
            print("Please enter valid option")
            pass
    elif clas>8 and clas<=10:
        boyfee=4500
        tutionfee=400
        sex=str(input("STUDENT IS GIRL/BOY:- "))
        if sex=="girl" or sex=="GIRL":
            print("No tution fees for girls")
            print("Thus, annual fees for a girl student is",(boyfee-tutionfee)*12)
        elif sex=="boy" or sex=="BOY":
            print("Annual fee for a boy student is",boyfee*12)
        else:
            print("Please enter valid option")
            pass
    elif clas>10 and clas<=12:
        p=1500
        c=1500
        m=1500
        b=1500
        comm=4000
        a=4200
        cs=500
        hin=250

        sub=str(input("ENTER THE SUBJECTS(PCM+HIN,PCM=C.S,PCMB,PCB+HIN,COMM+HIN,COMM=M,A):- "))
        if sub=="PCM+HIN" or sub=="pcm+hin":
                fee=p+c+m+hin
                print("TOTAL ANNUAL FEES IS CALCULATED TO BE",fee*12)
        elif sub=="PCM+C.S" or  sub=="pcm+c.s":
            fee=p+c+m+cs
            print("TOTAL ANNUAL FEES IS CALCULATED TO BE",fee*12)
        elif sub=="PCMB" or sub=="pcmb":
            fee=p+c+m+b
            print("TOTAL ANNUAL FEES IS CALCULATED TO BE",fee*12)
        elif sub=="PCB+HIN"or sub=="pcb+hin":
            fee=p+c+b+hin
            print("TOTAL ANNUAL FEES IS CALCULATED TO BE",fee*12)
        elif sub=="COMM+HIN"or sub=="comm+hin":
            fee=comm+hin
            print("TOTAL ANNUAL FEES IS CALCULATED TO BE",fee*12)
        elif sub=="COMM+M"or sub=="comm+m":
            fee=comm+m
            print("TOTAL ANNUAL FEES IS CALCULATED TO BE",fee*12)
        elif sub=="A"or sub=="a":
            fee=a
            print("TOTAL ANNUAL FEES IS CALCULATED TO BE",fee*12)
        else:
            print("KINDLY ENTER THE VALID SUBJECTS")
    else:
        print("KINDLY ENTER THE VALID CLASS")
    print("!----------THANK YOU FOR USING--------!")
        
    
        
    
    


    
    
    
