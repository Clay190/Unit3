#Clay Kynor
#10/13/17
#quiz3.py - Quiz on Chapter 3


for i in range(-5,6):
    print(i)


i=18
while i <= 32:
    print(i)
    i = i+1
   

total = 0
for i in range(13,332,2):
    total = total + i
print(total)


total = 0 

while total<10:
    word = input("Enter a word: ")
    for ch in word:
        if 'z' in word or "Z" in word:
            total = 10
        

#I know my way isn't the cleanest, I tried to do it this following way, but it wouldn't break
"""
while True:
    word = input("Enter a word: ")
    for ch in word:
        if 'z' in word or "Z" in word:
            break
                """