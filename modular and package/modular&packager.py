import datetime
import random
import math
import time
import uuid
from fileoperations import file_menu

print("---------------------------\n")
print("Welcome to Multi-Utility Toolkit\n")
print("---------------------------\n")

while True:
    print("1. Datetime and time operations")
    print("2. Mathemetical Operations")
    print("3. Random Data Generation")
    print("4. Generate Unique Identifiers (UUID)")
    print("5. File Operation (Custom Module)")
    print("6. Explore Module Attributes (dir())")
    print("7. Exit")
    print()

    choice=int(input("Enter your choice: "))
    print()

    if choice<=0 or choice>7:
        print("Enter the Valid Choice from mention above\n")
    
    else:
        
        if choice==1:
            while True:
                print("Datetime and Time Operations:")
                print("1. Display Current Date and Time")
                print("2. Calculate Difference Between Two Date/Time")
                print("3. Format Date into Custom Format")
                print("4. Stopwatch")
                print("5. Countdown Timer")
                print("6. Back to Main menu")

                choice1=int(input("Enter the Choice: "))
                print()

                if choice1<=0 or choice1>6:
                    print("Enter the Valid Choice from mention above\n")

                else:
                    if choice1==1:
                        a=datetime.datetime.now()
                        print(a)
                        print()

                    elif choice1==2:
                        print("1. Difference Between Two Dates")
                        print("2. Difference Between Two Times")
                        print()

                        choose=int(input("Enter your choice: "))
                        print()

                        if choose==1:
                            date1=input("Enter the First Date(DD-MM-YYYY): ")
                            date2=input("Enter the Second Date(DD-MM-YYYY): ")
                            date1=datetime.datetime.strptime(date1, "%d-%m-%Y")
                            date2=datetime.datetime.strptime(date2, "%d-%m-%Y")
                            print()
                            d=date1-date2
                            diff=abs(d)
                            print(f"Difference Between {date1.date()} and {date2.date()} is {diff}\n")

                        elif choose==2:
                            time1=input("Enter the First time (HH:MM:SS)(am/pm): ")
                            time2=input("Enter the second time (HH:MM:SS)(am/pm): ")

                            time1=datetime.datetime.strptime(time1,"%H:%M:%S %p")
                            time2=datetime.datetime.strptime(time2,"%H:%M:%S %p")

                            d=time1-time2
                            diff=abs(d)

                            print(f"Difference Between {time1.time()} and {time2.time()} is {diff}")

                    elif choice1==3:
                        format=input("Enter the Format (e.g. = DD-MM-YYYY): ")
                        format=format.lower()

                        if format=="dd-mm-yyyy":
                            date=datetime.datetime.now()
                            print(date.strftime("%d-%m-%Y"))

                        elif format=="mm-dd-yyyy":
                            date=datetime.datetime.now()
                            print(date.strftime("%m-%d-%Y"))

                        elif format=="yyyy-dd-mm":
                            date=datetime.datetime.now()
                            print(date.strftime("%Y-%d-%m"))

                        elif format=="yyyy-mm-dd":
                            date=datetime.datetime.now()
                            print(date.strftime("%Y-%m-%d"))

                        else:
                            print("Invalid Format\n")

                    elif choice1==4:
                        running=False
                        elap=0
                        start=None

                        while True:

                            print("Write start to Start stopwatch")
                            print("Write stop to Stop stopwatch")
                            print("Write reset to Reset stopwatch")
                            print("Write display to display stopwatch")
                            print("press 0 for exit")

                            write=input("Enter the Word: ")
                            write=write.lower()

                            if write=="start":
                                if not running:
                                    start=time.time()-elap
                                    running=True
                                    print("Stopwatch Started\n")
                                else:
                                    print("Stopwatch is Sunning\n")

                            elif write=="stop":
                                    elap=time.time()-start
                                    running=False
                                    print(f"Stopwatch Duration is {elap} seconds\n")

                            elif write=="reset":
                                running=False
                                elap=0
                                start=None
                                print("Stopwatch Reset Done\n")

                            elif write=="display":
                                if running:
                                    current=time.time()-start
                                    print(f"Duration time is: {current} seconds\n")
                                else:
                                    current=elap
                                    print(f"Duration time is: {current} seconds\n")

                            elif write=="0":
                                print("Exiting Stopwatch\n")
                                break

                    elif choice1==5:
                        a=int(input("Enter the Timer in Seconds: "))

                        for i in range(a,0,-1):
                            print(i)
                            time.sleep(1)

                        print("0")
                        print()

                    elif choice1==6:
                        print("Back to main menu\n")
                        break

        elif choice==2:
            while True:
                    
                print("Mathematical Operations:")
                print("1. Calculate Factorial")
                print("2. Solve Compound Interest")
                print("3. Trignometric Calculation")
                print("4. Area of Geometric Shapes")
                print("5. Back to Main Menu")
    
                choice2=int(input("Enter your Choice: "))
    
                if choice2<=0 or choice2>5:
                    print("Enter the Valid Choice from mention above\n")
    
                elif choice2==1:
                    num=int(input("Enter the Number for Factorial: "))
                    print()
    
                    if num<=0:
                        print("Factorial is not defined for negative numbers\n")
                    else:
                        fac=math.factorial(num)
                        print(f"The Factorial of {num} is: {fac}\n")
                            
                elif choice2==2:
                    prin=float(input("Enter the Principal Amount: "))
                    rate=float(input("Enter the Rate of Interest: "))
                    year=int(input("Enter the Number of years: "))
    
                    if prin<=0 or rate<=0 or year<=0:
                        print("Values should not be in Negative\n")
                    else:
                        rate=rate/100
                        ci=prin*(1+rate)**year
    
                    print(f"Principal Amount is: {prin}\nRate of Interest is: {rate}\nNumber of years is: {year}\nCompound Interest is: {ci}\n")
                
                elif choice2==3:
                    degree=int(input("Enter Degree to Convert: "))
                    print("1. Sin method")
                    print("2. Cos method")
                    print("3. Tan method")
                    
                    a=int(input("Enter your Choice: "))
                    
                    if a<=0 or a>3:
                        print("Enter the Valid Choice from mention above\n")
                    else:
                        if a==1:
                            print(math.sin(degree))
                        elif a==2:
                            print(math.cos(degree))
                        elif a==3:
                            print(math.tan(degree))
                
                elif choice2==4:
                    while True:
                        print("1. Area of Square")
                        print("2. Area of Circle")
                        print("3. Area of Triangle")
                        print("4. Area of Rectangle")
                        print("5. Area of Parallelogram")
                        print("6. Area of Trapezium")
                        print("7. Area of Ellipse")
                        print("8. Exit")
    
                        find=int(input("Enter your choice: "))
    
                        if find<=0 or find>8:
                            print("Enter the Valid Choice from mention above\n")
                        
                        else:
                            if find==1:
                                a=float(input("Enter the Length of side: "))
                                print()
                                if a<=0:
                                    print("Finding Area is not defined for negative numbers\n")
                                else:
                                    asq=a**2
                                    print(f"Area of Square is: {asq}\n")
                            
                            elif find ==2:
                                r=float(input("Enter the Radius of Circle: "))
                                print()
    
                                if r<=0:
                                    print("Finding Area is not defined for negative numbers\n")
                                else:
                                    ac=math.pi*r*r
                                    print(f"Area of Circle is: {ac}\n")
                            
                            elif find==3:
                                base=float(input("Enter the Base of Triangle: "))
                                height=float(input("Enter the Height of Triangle: "))
                                print()
    
                                if base<=0 or height<=0:
                                    print("Finding Area is not defined for negative numbers\n")
                                    
                                else:
                                    tri=0.5*base*height
                                    print(f"Area of Triangle is: {tri}\n")
                            
                            elif find==4:
                                length=float(input("Enter the Length of Rectangle: "))
                                width=float(input("Enter the Width of Rectangle: "))
                                print()
    
                                if length<=0 or width<=0:
                                    print("Finding Area is not defined for negative numbers\n")
                                else:
                                    rec=length*width
                                    print(f"Area of Rectangle is: {rec}\n")
    
                            elif find==5:
                                base=float(input("Enter the Base of Parallelogram: "))
                                height=float(input("Enter the Height of Parallelogram: "))
                                print()
    
                                if base<=0 or height<=0:
                                    print("Finding Area is not defined for negative numbers\n")
                                else:
                                    para=base*height
                                    print(f"Area of Parallelogram is: {para}\n")
    
                            elif find==6:
                                a=float(input("Enter the First side of Trapezium: "))
                                b=float(input("Enter the Second side of Trapezium: "))
                                h=float(input("Enter the Height of Trapezium: "))
                                print()
    
                                if a<=0 or b<=0 or h<=0:
                                    print("Finding Area is not defined for negative numbers\n")
                                else:                            
                                    at=0.5*(a+b)*h
                                    print(f"Area of Trapezium is: {at}\n")
    
                            elif find==7:
                                r1=float(input("Enter the Radius of minor axis: "))
                                r2=float(input("Enter the Radius of major axis: "))
    
                                if r1<=0 or r2<=0:
                                    print("Finding Area is not defined for negative numbers\n")
                                else:
                                    ae=math.pi*r1*r2
                                    print(f"Area of Ellipse is: {ae}\n")
    
                            elif find==8:
                                print("Exiting")
                                break
                elif choice2==5:
                    print("Exiting\n")
                    break    

        elif choice==3:
            while True:
                print("Random Data Generation:")
                print("1. Generate Random Number")
                print("2. Generate Random List")
                print("3. Create Random Password")
                print("4. Generate Random OTP")
                print("5. Back to Menu")

                choose1=int(input("Enter the Choice: "))

                if choose1<=0 or choose1>5:
                    print("Enter the Valid Choice from mention above\n")
                
                else:
                    if choose1==1:
                        r=random.randint(1,100)
                        print(f"Random Number: {r}\n")
                    
                    elif choose1==2:
                        l=[]
                        for i in range(1,7):
                            r=random.sample(range(1,100),6)
                            l.append(r)
                        b=random.choice(l)
                        print(f"Random List is: {b}\n")
                    
                    elif choose1==3:
                        l = ["A8$dKp#z1Q","m@3Xv9*TgH","pR#7d!zM5K","qW1*T@kL8b","Z$6gXp#4Vr","nM@5T!pK7Q","Y9#xqW2*Ld","B@4pL7!XmT","K6#vQm8T!Z","X@3nW5*LpR"]
                        b=random.choice(l)
                        print(f"Random Passward is: {b}\n")

                    elif choose1==4:
                        r=random.randint(000000,999999)
                        print(f"Random OTP is: {r}\n")

                    elif choose1==5:
                        print("Exiting\n")
                        break


        elif choice==4:
            while True:
                print("1. Generate UUID1 (based on timestamp and MAC address")
                print("2. Generate UUID4 (random base)")
                print("3. Back to Main Menu")
                
                choice3=int(input("Enter your Choice: "))
                
                if choice3<=0 or choice3>3:
                    print("Enter the Valid Choice from mention above\n")
                
                else:
                    if choice3==1:
                        r=uuid.uuid1()
                        print(f"UUID Based on Timestamp and MAC Address is: {r}\n")
                    
                    elif choice3==2:
                        r=uuid.uuid4()
                        print(f"Random UUID is: {r}\n")
                    
                    elif choice3==3:
                        print("Exiting\n")
                        break
        elif choice==5:
            file_menu()

        elif choice==6:
            while True:
                print("\n--- Explore Module Attributes ---")
                print("1. Explore math module")
                print("2. Explore random module")
                print("3. Explore datetime module")
                print("4. Back to Main Menu")

                choice = int(input("Enter your choice: \n"))
                
                if choice == 1:
                    print("Attributes in math module:\n")
                    import math
                    print(dir(math))
                elif choice == 2:
                    print("Attributes in random module:\n")
                    import random
                    print(dir(random))
                elif choice == 3:
                    print("Attributes in datetime module:\n")
                    import datetime
                    print(dir(datetime))
                elif choice == 4:
                    break
                else:
                    print("Invalid choice. Please try again.\n")

        elif choice==7:
            print("Exiting Toolkit, Thankyou")
            break