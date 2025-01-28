# List of lessons
lessons = [
    "Lesson 1: Introduction to Cloud Security",
    "Lesson 2: Understanding Shared Responsibility Model",
    "Lesson 3: Data Encryption and Protection",
    "Lesson 4: Identity and Access Management",
    "Lesson 5: Monitoring and Logging",
    "Lesson 6: Incident Response and Recovery"
]

# List of questions and answers
questions = [
    {
        "question": "What is the shared responsibility model?",
        "options": ["A) A model where cloud provider is responsible for everything",
                    "B) A model where both cloud provider and customer share responsibilities",
                    "C) A model where customer is responsible for everything"],
        "answer": "B"
    },
    {
        "question": "Why is data encryption important?",
        "options": ["A) To make data readable",
                    "B) To protect data from unauthorized access",
                    "C) To delete data"],
        "answer": "B"
    },
    {
        "question": "What does IAM stand for?",
        "options": ["A) Identity and Access Management",
                    "B) Internet Access Management",
                    "C) Internal Access Management"],
        "answer": "A"
    }
]

def display_lessons():
    print("Cloud Security Awareness Lessons:")
    for lesson in lessons:
        print(lesson)
    print("\n")

def conduct_test():
    score = 0
    print("Cloud Security Awareness Test:")
    for i, q in enumerate(questions):
        print(f"Q{i+1}: {q['question']}")
        for option in q['options']:
            print(option)
        answer = input("Your answer (A/B/C): ").strip().upper()
        if answer == q['answer']:
            score += 1
    return score

def display_score(score):
    total_questions = len(questions)
    print(f"\nYour Score: {score}/{total_questions}")
    if score == total_questions:
        print("Excellent! You have a strong understanding of cloud security.")
    elif score >= total_questions / 2:
        print("Good job! But there's room for improvement.")
    else:
        print("You need to work more on your cloud security knowledge.")

if __name__ == "__main__":
    display_lessons()
    score = conduct_test()
    display_score(score)
