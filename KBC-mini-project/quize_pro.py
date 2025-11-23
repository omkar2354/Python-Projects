import random
import sys

# -----------------------------
# Question Bank (list of dicts)
# -----------------------------
QUESTIONS = [
    {
        "question": "What does not grow on a tree according to a popular Hindi saying?",
        "options": {"a": "Money", "b": "Flower", "c": "Leaves", "d": "Fruits"},
        "answer": "a",
        "prize": 1000
    },
    {
        "question": "Which city is known as the Pink City in India?",
        "options": {"a": "Bangalore", "b": "Mysore", "c": "Jaipur", "d": "Kochi"},
        "answer": "c",
        "prize": 3000
    },
    {
        "question": "How many states are there in India?",
        "options": {"a": "28", "b": "29", "c": "31", "d": "30"},
        "answer": "a",
        "prize": 6000
    }
]


# -----------------------------
# Simple 50-50 Lifeline
# -----------------------------
def lifeline_5050(correct_ans, options):
    wrong = [opt for opt in options if opt != correct_ans]
    random_wrong = random.choice(wrong)

    print("\n📌 50-50 Lifeline Activated!")
    print("Remaining options:")
    print(f"  {correct_ans}")
    print(f"  {random_wrong}")


# -----------------------------
# Ask a Single Question
# -----------------------------
def ask_question(q, lifeline_used):
    print("\n" + q["question"])

    # Print all options
    for key, value in q["options"].items():
        print(f"  {key}: {value}")

    # Ask user (lifeline available here)
    while True:
        user = input("\nChoose your answer (a/b/c/d) OR type 'quit' OR '5050': ").lower().strip()

        if user == "quit":
            print("Game ended. Thanks for playing!")
            sys.exit()

        # If user wants 50-50 lifeline
        if user == "5050":
            if lifeline_used:
                print("❗ You have already used 50-50 lifeline.")
            else:
                lifeline_5050(q["answer"], list(q["options"].keys()))
                return "lifeline"   # signal to main game to ask again

        # Validate answer
        elif user in q["options"].keys():
            return user
        else:
            print("Invalid input. Try again.")


# -----------------------------
# Main Game Logic
# -----------------------------
def play_game():
    print("===== WELCOME TO MINI KBC =====")

    score = 0
    lifeline_used = False

    for q in QUESTIONS:
        print("\n-----------------------------------")
        print(f"Prize for this question: Rs. {q['prize']}")
        print("-----------------------------------")

        while True:
            user_answer = ask_question(q, lifeline_used)

            # If lifeline used here
            if user_answer == "lifeline":
                lifeline_used = True
                continue  # ask again after showing reduced options

            break  # user gave a real answer

        # Check if answer is correct
        if user_answer == q["answer"]:
            score += q["prize"]
            print(f"✔ Correct! You won Rs. {q['prize']}")
        else:
            print("✘ Wrong answer!")
            break

    # Game end summary
    print("\n========== GAME OVER ==========")
    print(f"Your Total Winning Amount: Rs. {score}")

    if score == sum(q["prize"] for q in QUESTIONS):
        print("🎉 Congratulations! You won the Mini KBC!")
    else:
        print("Better luck next time!")


# -----------------------------
# Program Entry Point
# -----------------------------
if __name__ == "__main__":
    play_game()
