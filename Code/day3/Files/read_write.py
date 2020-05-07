myread = open("test_file", "r")

myitems = myread.readlines()
myread.close()


myitems.insert(1, "Fluffers, Samoyed\n")

mywrite = open("test_file", "w")
mywrite.writelines(myitems)
mywrite.close()