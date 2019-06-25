my_list = ["10.10.10.25", "10.10.24.47", "10.20.30.40"]
print (my_list)
#below is .format method
print ("I need to access IP's {}, {}, {}".format(my_list[0], my_list[2], my_list[1]))
#below is the f method
print(f"I need to access IP's {my_list[0]}, {my_list[2]}, and {my_list[1]}")
print()
print(f"I need to access IP's {my_list[0]}")

