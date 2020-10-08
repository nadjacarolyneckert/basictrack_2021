names = ["Julie", "Peter", "Astrid", "Jonas", "Sam", "Fred", "Jane"]

count_up_to_Sam = 0
for name in names:
    if name == "Sam":
        break
    else:
        count_up_to_Sam += 1

print("The number of names before and not including Sam is :", count_up_to_Sam)