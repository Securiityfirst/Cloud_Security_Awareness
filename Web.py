from flask import Flask, render_template, request, redirect, url_for
import openai
import os

app = Flask('Web')
import openai

# Set up OpenAI API key
openai.api_key = os.getenv('web key')

lessons = []

def generate_quiz_questions(prompt):
    try:
        response = openai.Completion.create(
            engine='gpt-3.5-turbo-instruct',
            prompt=prompt,
            max_tokens=1400
        )
        questions_text = response.choices[0].text.strip()
        questions = []
        for q in questions_text.split('\n\n'):
            parts = q.split('\n')
            if len(parts) < 3:
                print(f"Skipping improperly formatted question: {q}")
                continue  # Skip if the question format is incorrect
            question = parts[0]
            options = []
            for part in parts[1:-1]:
                if '. ' in part:
                    options.append(part.split('. ', 1)[1])
                else:
                    print(f"Skipping improperly formatted option: {part}")
            answer = parts[-1].split(':')[-1].strip()
            questions.append({"question": question, "options": options, "answer": answer})
    except IndexError as e:
        print(f"Error parsing question: {e}")
    except Exception as e:
        print(f"Error generating quiz questions: {e}")
        questions = []
    return questions

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/lessons', methods=['GET', 'POST'])
def lessons_view():
    if request.method == 'POST':
        lesson_title = request.form['lesson_title']
        lesson_content = request.form['lesson_content']
        lessons.append({"title": lesson_title, "content": lesson_content})
        return redirect(url_for('lessons_view'))
    return render_template('lessons.html', lessons=lessons)

@app.context_processor
def inject_enumerate():
    return dict(enumerate=enumerate)

@app.route('/quiz', methods=['GET', 'POST'])
def quiz_question():
    prompt = "Generate a quiz question about cloud security with 16 quiz questions 4 answer options and one correct answer."
    quiz_questions = generate_quiz_questions(prompt)

    if request.method == 'POST':
        score = 0
        for i, q in enumerate(quiz_questions):
            answer = request.form.get(f'question-{i}')
            if answer == q['answer']:
                score += 1
        return render_template('results.html', score=score, total=len(quiz_questions))

    return render_template('quiz.html', quiz=quiz_questions)

if __name__ == '__main__':
                          app.run(host='0.0.0.0', port=8080, debug=True)
