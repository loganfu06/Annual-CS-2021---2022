f = open("reverse_me.txt")
contents = f.read()
f.close()
reverse = contents.split("\n")
for i in reversed(reverse):
    print(i)