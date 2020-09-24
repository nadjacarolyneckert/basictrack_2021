#Ask the user for the time now (in hours), and ask for the number of hours to wait.
# Your program should output what the time will be on the clock when the alarm goes off.

current_time_str = input("What time is it now? (in hours 0-23)")
wait_time_str = input("How many hours do you want to wait?")

current_time = int(current_time_str)
wait_time = int(wait_time_str)

final_time = current_time + wait_time

final_answer = final_time%24

print("The alarm goes off at ", final_answer)