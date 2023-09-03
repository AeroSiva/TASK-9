#Q1 what is the expected output of the following python code give below ;-
# data = [10,501,37,100,999,87,351]
# result = filter (lambda x:x >4, data )
# print(list(result))

[10, 501, 37, 100, 999, 87, 351]



#Q2 write a python code using lambda function to check every element of a list is an Integer or string ?

def is_int_str (lst) :
    int_str = all(map(lambda x:isinstance(x, (int,str)),lst))
    print (int_str)

lst1 = [1,'banana', 10,'apple',3.14]
lst2 = [11,'banana', 10,'apple']
is_int_str(lst1)
is_int_str(lst2)



#Q3 Using the python Lambda function create a Fibanocci series from 1 to 5o elements ?

def fib_series(s,e) :
    fib_fun = lambda n: n if n<=1 else fib_fun(n-1) + fib_fun(n-2)
    fib_lst = list(map(fib_fun, range(s,e+1)))
    return (fib_lst)
start,end =1,50
result = fib_series(start,end)
print(result)




#Q4 Write a python function to validate the Regula Expression for the following:
    # a) email Address
    # b) Mobile numer of Bangladesh
    # c) Telephone number of USA
    # d) 16 character Alpha-Numeric password composed of alphabets of Upper Case,Lower case,Special Character, Mumbers.



import re
def validation(email, ban_ph,us_tel_phone,alpha_numeric_pw):
    
    email_pat = r"^[a-zA-Z0-9._%-+]+(\.[a-zA-Z0-9._%-+]+)*@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    
    if re.match(email_pat, email):
        pass # if entered proper mail program checks for bangladesh phone number
    else:
        return (email, "is not valid")


    ban_ph_pat = r"^(?:\+?88)?01[3-9]\d{8}$"
    
    if re.match(ban_ph_pat, ban_ph):
        pass # if entered proper Bangladesh phone number program checks for proper US Telephone number
    else:
         return ("This ", ban_ph ," is not a Valid Bangladesh mobile number")


    us_tel_pat = r"^(?:\+?1[-.\s]?)?\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}$"
    
    if re.match(us_tel_pat, us_tel_phone):
        pass # if entered proper US telephone number program checks for proper password number
    else:
        return ("This ",us_tel_phone," is not a Valid USA landline number")
    

    pw_pat = r"^(?=.*[A-Z])(?=.*[a-z])(?=.*[0-9])(?=.*[!@#$%^&*()-_+=])[A-Za-z0-9!@#$%^&*()-_+=]{16}$"
    
    if re.match(pw_pat, alpha_numeric_pw):
        pass # if entered proper password program proceeds to next step.
    else:
        return ("This ",alpha_numeric_pw, "password is not valid")


email = input("Enter email id: ")
ban_ph = input("Enter bangladesh mobile number: ")
us_tel_phone = input("Enter USA  landline number:")
alpha_numeric_pw = input("Enter password:")
validation (email, ban_ph,us_tel_phone,alpha_numeric_pw)