#Car Stimulation( if user input help print-[(start-to start the car)(stop-to stop the car)(exit-to quit)] 
  # if the user input something else print "i dont understand that"
  #if we type start=car  started...ready to go!
  #stop=car stopped.
  #if it is quit terminate the program

while True:
        command=input(">").lower()
        if command=="help":
            print('''
            stop-to stop the car
            start-to start the car
            quit-exit the game 
                ''')   
        elif command=="start":
            print("Car started.....ready to go ")
        elif command=="stop":
            print("car stopped.")
        elif command=="quit":
            break
        else:
            print("i dont understand ...")
            
