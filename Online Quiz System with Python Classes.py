#Create a Python program for an online quiz system. Implement classes forquizzes, questions, and users. Include methods for taking quizzes, scoring, anddisplaying results.
class Question:
    def __init__(self, text, options, correct_option):
        self.text = text
        self.options = options
        self.correct_option = correct_option

    def display_question(self):
        print(self.text)
        for i, option in enumerate(self.options, start=1):
            print(f"{i}. {option}")

    def is_correct(self, user_answer):
        return user_answer == self.correct_option


class Quiz:
    def __init__(self, name):
        self.name = name
        self.questions = []

    def add_question(self, question):
        self.questions.append(question)

    def take_quiz(self):
        score = 0
        for question in self.questions:
            question.display_question()
            user_answer = input("Your answer (enter the option number): ")
            if question.is_correct(int(user_answer)):
                print("Correct!")
                score += 1
            else:
                print(f"Incorrect! The correct answer is {question.correct_option}")

        print(f"\nQuiz completed! Your score: {score}/{len(self.questions)}")


class User:
    def __init__(self, username):
        self.username = username

# Example usage with user input:

# Create a user
username = input("Enter your username: ")
user = User(username)

# Create a quiz
quiz_name = input("Enter the quiz name: ")
quiz = Quiz(quiz_name)

# Add questions to the quiz
num_questions = int(input("Enter the number of questions in the quiz: "))
for _ in range(num_questions):
    question_text = input("Enter the question: ")
    options = [input(f"Enter option {i}: ") for i in range(1, 4)]
    correct_option = int(input("Enter the correct option number: "))
    question = Question(question_text, options, correct_option)
    quiz.add_question(question)

# Take the quiz
print(f"\nWelcome, {user.username}! You are about to take the {quiz.name} quiz.")
quiz.take_quiz()
