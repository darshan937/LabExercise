'''7. You live 4 miles from university. The bus drives at 25mph but spends
2 minutes at each of the 10 stops on the way. How long will the bus journey take?
Alternatively, you could run to university. You jog the first mile at 7mph;
then run the next two at15mph; before jogging the last at 7mph again.
 Will this be quicker or slower than the bus?'''
distance = 4
speed = 25
stops_time = 20/60
travelledtime = distance/speed
total_timetravel = travelledtime + stops_time

print(f"the bus journey will take {total_timetravel} hours")
jog1_4 = 7 * 2
jog2_3 = 15 * 2
jogspeed = jog1_4 + jog2_3
timejog = distance/jogspeed
print(f"time taken by jogging is {timejog}")
if total_timetravel>timejog:
    print("bus will be faster than the jooging")
else:
    print("jooging will be faster than the bus ")

