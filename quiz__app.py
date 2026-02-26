"""
Quiz Application (CLI)

This program asks multiple programming-related questions,
validates user input, and calculates the final score.

Author: Kiran
"""


def quiz_app():
    questions = [
        {
            "question": "Which symbol is used for comments in Python?",
            "options": ["A. //", "B. <!-- -->", "C. #", "D. **"],
            "answer": "C"
        },
        {
            "question": "Which data structure stores key-value pairs in Python?",
            "options": ["A. List", "B. Tuple", "C. Dictionary", "D. Set"],
            "answer": "C"
        },
        {
            "question": "What is the correct file extension for Python files?",
            "options": ["A. .py", "B. .java", "C. .ppt", "D. .html"],
            "answer": "A"
        },
        {
            "question": "Which loop is used when the number of iterations is known?",
            "options": ["A. while loop", "B. for loop", "C. do-while loop", "D. infinite loop"],
            "answer": "B"
        },
        {
            "question": "Which function is used to take input from the user in Python?",
            "options": ["A. get()", "B. scanf()", "C. input()", "D. read()"],
            "answer": "C"
        }
    ]

    score = 0

    print("===== Welcome to the Programming Quiz =====")

    for index, q in enumerate(questions, start=1):
        print(f"\nQuestion {index}: {q['question']}")
        for option in q["options"]:
            print(option)

        # Input validation loop
        while True:
            user_answer = input("Enter your answer (A/B/C/D): ").strip().upper()
            if user_answer in ["A", "B", "C", "D"]:
                break
            else:
                print("Please enter a valid option (A, B, C, or D).")

        if user_answer == q["answer"]:
            print("Correct! ✅")
            score += 1
        else:
            print("Wrong answer ❌")
            print(f"The correct answer was: {q['answer']}")

    print("\n===== Quiz Finished =====")
    print(f"You scored {score} out of {len(questions)}")

    percentage = (score / len(questions)) * 100
    print(f"Your percentage: {percentage:.2f}%")

    if percentage >= 80:
        print("Excellent Performance! 🌟")
    elif percentage >= 50:
        print("Good Job 👍")
    else:
        print("Keep Practicing 💪")


if __name__ == "__main__":
    quiz_app()
