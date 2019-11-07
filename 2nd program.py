Average=[]
no_of_students=int(input("ENTER THE NO OF STUDENTS: "))

for i in range(1,no_of_students):
    print("\nENTER THE MARKS FOR STUDENT: ",i)
    E=int(input("\nENTER THE MARKS FOR ENGLISH SUBJECT: "))
    M=int(input("\nENTER THE MARKS FOR MATHS SUBJECT: "))
    U=int(input("\nENTER THE MARKS FOR URDU SUBJECT: "))
    Sum=E+M+U;
    Average.append(i)
    Average[i]=Sum/2;
    
    
    
    

   

for j in range(1,no_of_students):
     print("\nTHE AVERAGE OF STUDENT ",i," is: ",average[i])

    
