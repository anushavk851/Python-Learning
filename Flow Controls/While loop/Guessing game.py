#Guessing number game (lets choose 9 as the number that should be guessed to win)(you can only guess 3 times)
 secret_number=9
 guessing=0
 while guessing <3:
    guess=int(input("guess a number: "))
    guessing=guessing+1
    if guess==secret_number:
       print("congrats,you won")
       break                     
          
 else:
    print("you failed")
