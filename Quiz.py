# This may not be the best because I'm currently more used to Object Oriented Programming
# Add how many questions and answers you want without going through the trouble of constantly doing if statements

# Details
# By: Samuel Davis.
# Description: A simple question simple where you don't have to constantly right out new if and else statements


class Question:
    def __init__(self, question, answer):
        self.question = question
        self.answer = answer


questions = [
    Question("What was Minecraft coded in?", "java"),
    Question("Is MongoDB NoSQL?", "yes"),
    Question("Is Django A Framework For Java?", "no"),
    Question("Is NodeJS a Framework?", "yes"),
    Question("What's the port for HTTPS (Not HTTP)", "443"),
    Question("What's the port for HTTP", "80")
]

correct_questions = []
incorrect_questions = []

user_points = 0

# For loop
for question in questions:
    user_answer = input(f"\nQuestion: {question.question}\nEnter Answer: ")
    if user_answer.lower() == question.answer:
        user_points = user_points + 1
        print(f"Correct, you currently have {user_points} points." if user_points > 1
              else f"Correct, You have {user_points} point.")
        correct_questions.append(question.question)
    else:
        print("Incorrect")
        incorrect_questions.append(question.question)

# Tell the user what they got right and wrong, also tell then their score.
print("Thanks for testing my quiz! Here are the questions you got right.")
print(correct_questions)
print("\n")
print("Here are the questions you got incorrect")
print(incorrect_questions)
print(f"\nYou've scored: {user_points} in total. Hopefully you got the scored you wished for.")
