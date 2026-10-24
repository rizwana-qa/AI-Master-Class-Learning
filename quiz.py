#Variable and Input
name = input("What is your name? ")
print("Hello,", name)

#If-Else 
answer = input("What is the capital of Pakistan? ")
if answer.lower() == "islamabad":
    print("Correct")
else:
    print("Wrong")

#Listen loop
questions = [
    ("Capital of Pakistan?", "islamabad"),
    ("Capital of France?", "paris"),
    ("2 + 2?", "4"),
]
score = 0
for question, correct in questions:
    answer = input(question + " ")
    if answer.strip().lower() == correct:
        print("Correct")
        score += 1
    else:
        print("Wrong")
print("You scored", score, "out of", len(questions))

#Function
def ask(question, correct):
    answer = input(question + " ")
    if answer.strip().lower() == correct:
        print("Correct")
        return 1
    print("Wrong")
    return 0
 
score = 0
for question, correct in questions:
    score += ask(question, correct)
print("You scored", score, "out of", len(questions))

