#Count how many even and odd numbers are present between 1 and 100
odd_count=0
even_count=0
for i in range(1,101):
    if i%2==0:
        even_count=even_count+1
    else:
        odd_count=odd_count+1
print(f' number of odd numbers present is: {odd_count} and even numbers is: {even_count}')
