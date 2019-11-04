print('''
@%%%%%%%%%%%%%%%%%%%%%@
Press 1 for Red colour
Press 2 for Green colour
Press 3 for Blue colour
@%%%%%%%%%%%%%%%%%%%%@
''')

while 1:
    colour1 = int(input("Enter your 1st colour"))
    colour2 = int(input("Enter your 2nd COlour"))
    if (colour1==1 and colour2==2):
        print('''
    \tCONGRATULATIONS
    You have created violet colour
''')
    elif colour1==2 and colour2==3:
        print('''
\tCONGRATULATIONS
you have created orange colour''')
    elif colour1==3 and colour2==1:
        print('''
\tCONGRATULATIONS
You have created Purple colour
''')
    else:
        print('''
\tERROR
Incorrect combination
''')
        break
    
