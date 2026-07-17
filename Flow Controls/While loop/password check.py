#Keep asking for password until it is correct.
password="Anu@134"
your_pass=input("enter your password: ")
while your_pass!=password:
  your_pass=input("wrong password entered,try again.  ")
  
print("logged in successfully")
