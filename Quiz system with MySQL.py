import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",         
    password="Saisandeep@03", 
    database="quiz_system"
)
cursor = db.cursor()


def add_question():
    q = input("Enter question: ")
    o1 = input("Option 1: ")
    o2 = input("Option 2: ")
    o3 = input("Option 3: ")
    o4 = input("Option 4: ")
    ans = int(input("Correct option (1-4): "))

    sql = "INSERT INTO questions (question, option1, option2, option3, option4, answer) VALUES (%s,%s,%s,%s,%s,%s)"
    cursor.execute(sql, (q, o1, o2, o3, o4, ans))
    db.commit()
    print("Question added!\n")

def view_questions():
    cursor.execute("SELECT * FROM questions")
    data=cursor.fetchall()
    for row in data :
        print(f"{row[0]}. {row[1]}")
        print(f"   1.{row[2]}  2.{row[3]}  3.{row[4]}  4.{row[5]}")
        print(f"   Answer: {row[6]}\n")

def delete_question():
    qid = int(input("Enter question ID to delete: "))
    cursor.execute("DELETE FROM questions WHERE qid=%s", (qid,))
    db.commit()
    print("Question deleted.\n")

def modify_question():
    qid = int(input("Enter question ID to modify: "))
    new_q = input("Enter new question: ")
    o1 = input("Option 1: ")
    o2 = input("Option 2: ")
    o3 = input("Option 3: ")
    o4 = input("Option 4: ")
    ans = int(input("Correct option (1-4): "))

    sql = """UPDATE questions 
             SET question=%s, option1=%s, option2=%s, option3=%s, option4=%s, answer=%s 
             WHERE qid=%s"""
    cursor.execute(sql, (new_q, o1, o2, o3, o4, ans, qid))
    db.commit()
    print("Question updated!\n")

def conduct_quiz(username, phone):
    cursor.execute("SELECT * FROM questions")
    questions = cursor.fetchall()

    score = 0
    total = len(questions)

    for q in questions:
        print(f"\nQ{q[0]}. {q[1]}")
        print(f"1.{q[2]}  2.{q[3]}  3.{q[4]}  4.{q[5]}")
        ans = int(input("Your answer (1-4): "))
        if ans == q[6]:
            score += 1

    print(f"\n {username}, you scored {score}/{total}")

    cursor.execute("INSERT INTO scores (username, phone, score, total) VALUES (%s,%s,%s,%s)", 
                   (username, phone, score, total))
    db.commit()

def view_scores():
    cursor.execute("SELECT * FROM scores ORDER BY quiz_date DESC")
    score=cursor.fetchall()
    for row in score:
        print(f"{row[1]} scored {row[2]}/{row[3]} on {row[4]}")
def view_top_scores():
    cursor.execute("SELECT username, score, total, quiz_date FROM scores ORDER BY score DESC, quiz_date ASC LIMIT 3")
    results = cursor.fetchall()

    print("\n Top 3 Scorers ")
    for i, row in enumerate(results, start=1):
        print(f"{i}. {row[0]} scored {row[1]}/{row[2]}")



def admin_menu():
    while True:
        print("\n--- Admin Menu ---")
        print("1. Add Question")
        print("2. View Questions")
        print("3. Modify Question")
        print("4. Delete Question")
        print("5. View Scores")
        print("6. View Top 3 Scores")
        print("7. Logout")

        choice = input("Enter choice: ")
        if choice == '1':
            add_question()
        elif choice == '2':
            view_questions()
        elif choice == '3':
            modify_question()
        elif choice == '4':
            delete_question()
        elif choice == '5':
            view_scores()
        elif choice == '6':
            view_top_scores()
        elif choice == '7':
            break
        else:
            print("Invalid choice.")

def user_menu():
    username = input("Enter your name: ")

    while True:
        phone = input("Enter your phone number (must start with 9 or 8 or 7): ")
        if phone.isdigit() and len(phone) == 10 and phone[0] in['9','8','7']:
            break
        else:
            print("Invalid phone number. It must be 10 digits and start with 987.")

    conduct_quiz(username, phone)

def main():
    while True:
        print("\n===== QUIZ SYSTEM =====")
        print("1. Admin")
        print("2. User")
        print("3. Exit")

        role = input("Enter choice: ")
        if role == '1':
            admin_menu()
        elif role == '2':
            user_menu()
        elif role == '3':
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
