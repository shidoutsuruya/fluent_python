import sys
def log_in():
    if sys.argv[1]=='login':
        account=input('please input your account:')
        while True:
            if account not in ['abc','max']:
                print('error! account not exist, please try again')
                account=input('please input your account:')
            else:
                break
        password=input('password:')
        while True:
            if password!='123456':
                print('wrong password')
                password=input('password:')
            else:
                break
        print('hello new world')
    
def standardin():
    print('start input your content:')
    for line in sys.stdin:
        if 'q'==line.strip():
            break
        else:
            print(f'hello:{line}',end='')
def standardout(string):
    print(1+4)
    sys.stdout.write(string)
    
def exiting(age):
    if age < 18:
    # exits the program
        sys.exit("Age less than 18")    
    else:
        print("Age is not less than 18")
print(sys.getrefcount('mmmmmmnbhbbbkjbkb'))