import sys
import random

ans = True

while ans:
    question = input("Ask the magic 8 ball a question: (press enter to quit)")

    choice = random.randint(0, 7)
    answers = {
        0: "It is certain",
        1: "Outlook good",
        2: "You may rely on it",
        3: "Ask again later",
        4: "Concentrate and ask again",
        5: "Reply hazy, try again",
        6: "Hell no string bean",
        7: "Sources say no"
    }

    if question == "":
        sys.exit()
    else:
        print(answers[choice])
