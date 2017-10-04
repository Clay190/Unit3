#Clay Kynor
#10/4/17
#stringLoopDemo.py - how to loop through a string

word = input("Enter a word ")

for ch in word:
    if ch=="a" or ch=="e" or ch=="i" or ch=="o" or ch=="u":
        print (ch.upper())
    else:
        print(ch)