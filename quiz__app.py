# Quiz Application (CLI)
# This program asks the user a few questions and
# calculates the final score.

def quiz_app():
    questions = [
        {
            "question": "Which keyword is used to define a function in Python?",
            "options": ["A. function", "B. def", "C. define", "D. fun"],
            "answer": "B"
        },
        {
            "question": "What is the output of print(2 + 3 * 2)?",
            "options": ["A. 10", "B. 7", "C. 12", "D. 8"],
            "answer": "B"
        },
        {
            "question": "Which data type is used to store text in Python?",
            "options": ["A. int", "B. float", "C. string", "D. str"],
            "answer": "D"
        }
    ]

    score = 0

    print("Simple Quiz Application")
    print("-----------------------")

    for q in questions:
        print("\n" + q["question"])
        for option in q["options"]:
            print(option)

        user_answer = input("Enter your answer (A/B/C/D): ").strip().upper()	
	`	if user_answer not in ["A", "B", "C", "D"]:
           print("Please enter a valid option (A, B, C, or D).")
           continue

        if user_answer == q["answer"]:
           print("Correct!")
           score += 1

        else:
           print("Wrong answer.")
           print(f"The correct answer was: {q['answer']}")

    print("\nQuiz Finished")
    print(f"You scored {score} out of {len(questions)}")

if __name__ == "__main__":
    quiz_app()
