import json
import os
import random

QUESTIONS_FILE = "questions.json"
LEADERBOARD_FILE = "leaderboard.json"

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def load_json_file(filename, default_value):
    try:
        with open(filename, 'r') as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return default_value

def save_json_file(filename, data):
    try:
        with open(filename, 'w') as file:
            json.dump(data, file, indent=4)
    except IOError:
        print(f"Error: Could not save data to {filename}")

def update_leaderboard(player_name, score, total_questions):
    leaderboard = load_json_file(LEADERBOARD_FILE, [])
    percentage = round((score / total_questions) * 100, 1)
    
    new_record = {
        "name": player_name,
        "score": score,
        "total": total_questions,
        "percentage": percentage
    }
    leaderboard.append(new_record)
    leaderboard.sort(key=lambda x: (x['percentage'], x['score']), reverse=True)
    leaderboard = leaderboard[:5]
    
    save_json_file(LEADERBOARD_FILE, leaderboard)

def display_leaderboard():
    leaderboard = load_json_file(LEADERBOARD_FILE, [])
    
    print("\n==============================")
    print("      🏆 LEADERBOARD 🏆       ")
    print("==============================")
    
    if not leaderboard:
        print("No scores recorded yet. Be the first!")
    else:
        print(f"{'Rank':<5}{'Player':<15}{'Score':<10}{'Accuracy'}")
        print("-" * 40)
        for idx, record in enumerate(leaderboard, 1):
            rank_str = f"#{idx}"
            score_str = f"{record['score']}/{record['total']}"
            pct_str = f"{record['percentage']}%"
            print(f"{rank_str:<5}{record['name']:<15}{score_str:<10}{pct_str}")
    print("==============================\n")

def run_quiz():
    questions = load_json_file(QUESTIONS_FILE, [])
    
    if not questions:
        print(f"Error: No questions found in '{QUESTIONS_FILE}'. Please populate it first.")
        return

    random.shuffle(questions)
    score = 0
    total_qs = len(questions)
    
    print("\n--- Starting the Quiz! Good Luck! ---")
    
    for idx, q in enumerate(questions, 1):
        print(f"\nQuestion {idx} of {total_qs}:")
        print(q["question"])
        
        for option in q["options"]:
            print(option)
            
        valid_answers = ['A', 'B', 'C', 'D']
        while True:
            user_input = input("Your answer (A, B, C, or D): ").strip().upper()
            if user_input in valid_answers:
                break
            print("Invalid input! Please type only A, B, C, or D.")
            
        if user_input == q["answer"].upper():
            print("✅ Correct!")
            score += 1
        else:
            print(f"❌ Incorrect. The correct answer was {q['answer']}.")
            
    clear_screen()
    print("==============================")
    print("        QUIZ COMPLETE         ")
    print("==============================")
    print(f"Your final score: {score} out of {total_qs}")
    percentage = round((score / total_qs) * 100, 1)
    print(f"Accuracy Rate   : {percentage}%")
    print("==============================")
    
    player_name = input("Enter your name for the leaderboard: ").strip()
    if not player_name:
        player_name = "Anonymous"
        
    update_leaderboard(player_name, score, total_qs)
    display_leaderboard()

def main():
    while True:
        print("====== PYTHON QUIZ SYSTEM ======")
        print("1. Take the Quiz")
        print("2. View Leaderboard")
        print("3. Exit")
        print("================================")
        
        choice = input("Select an option (1-3): ").strip()
        
        if choice == '1':
            clear_screen()
            run_quiz()
        elif choice == '2':
            clear_screen()
            display_leaderboard()
        elif choice == '3':
            print("\nThanks for playing! Goodbye.")
            break
        else:
            clear_screen()
            print("⚠️ Invalid choice. Please choose a number between 1 and 3.\n")

if __name__ == "__main__":
    main()