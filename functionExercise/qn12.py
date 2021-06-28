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
message = input("-> ").lower()
active = True
status = ''
while active:
    if message == 'start':
        if status != 'start':
            status = 'start'
            print("Car started")
            message = input("-> ").lower()
        else:
            print("Car already started!")
            message = input("-> ").lower()
    elif message == 'help':
        print("start - to start the car\nstop - to stop the car\nquit - to quit the game")
        message = input("-> ").lower()
    elif message == 'stop':
        if status != 'stop':
            status = 'stop'
            print("Car stopped")
            message = input("-> ").lower()
        else:
            print("Car already stopped!")
            message = input("-> ").lower()
    elif message == "quit":
        break
    else:
        print("I don't understand this :(")
        message = input("-> ").lower()
print("Thanks for playing!")






