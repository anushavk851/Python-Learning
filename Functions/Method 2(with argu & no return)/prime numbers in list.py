#Write a function that accepts a list and prints all prime numbers present in it.
  def prime(list1):
      for i in list1:
          if i>1:
              count=0
              for j in range(1,i+1):
                  if i%j==0:
                      count=count+1
              if count==2:
                  print(i)

  number=list(map(int,input().split()))
  prime(number)
