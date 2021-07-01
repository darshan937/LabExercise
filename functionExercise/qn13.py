'''
  Building the car game ::
  CAR GAME:
        > help
          start - to start the car
          stop - to stop the car
          quit - to exit
        > asd
          I don't understand this
        > start
          Car started... Ready to go!!
        > stop
          Car stopped..
        > quit
'''
print ("This is a car game")

string = ""
start = False
while True:
    string = input("input your choice: (help/start/stop/quit) :--->").lower()

    if string == "help":
        print("start - to start the car\nstop - to stop the car\nquit - to quit the game")

    elif string == "start":
        if start:
            print("car already started")
        else:
            start = True
            print("Car started... Ready to go!!")

    elif string == "stop":
        if not start:
            print("car already stopped")
        else:
            start = False
            print("car stopped")

    elif string == "quit":
        break

    else:
        print("sorry i don,t get uh ")



