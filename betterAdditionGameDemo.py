#Clay Kynor
#10/4/17
#betterAdditionGameDemo.py - ask addition problems till user gets 5 right

from random import randint

numCorrect=0
while numCorrect < 5:
    num1 = randint(-10,10)
    num2 = randint(-10,10)
    question = "What is " + str(num1) + '+' + str(num2) + "?"
    answer = int(input(question))
    if num1 + num2 == answer:
        print("Correct! ")
        numCorrect = numCorrect + 1
    else:
        print("The answer was", num1 + num2)

print("Congradtulaitons, your smater than Pedro")