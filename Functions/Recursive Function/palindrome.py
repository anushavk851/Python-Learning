#Check palindrome number.
def reverse(n,rev=0):
    if n==0:
        return rev
     else:
        return reverse(n//10,rev*10+n%10)

def palindrome(n):
    return n==reverse(n)
num=int(input("enter a value: "))
print(palindrome(num))
