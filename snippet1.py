#Code Snippet 1:
db = open("output.txt", "a")
a = "Hello" + "1"
b = "How do you do?"
db.write(a+", "+b+"\n")
db.close()