#Write a program to calculates the time it takes to get somewhere using
#different modes of travel

distance_str = input("How many kilometers is it to your destination?")
mode_of_transport_str = input("How fast is your mode of transport? Please answer in km/h ")
additional_time_str = input("Is there any additional time you need, e.g. parking, scratch ice? Please answer in minutes")

distance = int(distance_str)
mode_of_transport = int(mode_of_transport_str)
additional_time = int(additional_time_str)

travel_time = distance/mode_of_transport + additional_time/60

print(" You need ", travel_time, "hours to reach your destination.")
