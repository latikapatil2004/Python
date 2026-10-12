'''Q.7 Password Length Check
Accept a password from the user. If the password contains fewer than six characters, raise a ValueError and handle it using try-except.'''


try:
    s=input("enter password")
    if len(s)<6:
        raise ValueError("invalid password")
        
except Exception as e:
    print("Password len is invalid")