my_string = "All good things must end"

my_list = my_string.split()
print(my_list)
back_list = my_list[::-1]
print(back_list)
bad_string = str(back_list);
print(bad_string)
new_string = ""
for word in back_list:
    new_string += word + " "

print(new_string)

#for i in my_list: Doesn't change the list
#    i = i[::-1]
for i in range(len(my_list)):
    my_list[i] = my_list[i][::-1]

print(my_list)
new_string = ""
for word in my_list:
    new_string += word + " "

print(new_string)
