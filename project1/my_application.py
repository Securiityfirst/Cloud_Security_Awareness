from flask import Flask, render_template, request, redirect, url_for
import openai
import training
import time

app = Flask('my_application')

# Set your OpenAI API key
openai.api_key = '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'

def generate_quiz_questions(prompt):
    response = openai.Completion.create(
        engine='gpt-3.5-turbo-instruct',
        prompt=prompt,
        max_tokens=200
    )
    questions_text = response.choices[0].text.strip()
    questions = []
    try:
        for q in questions_text.split('\n\n'):
            parts = q.split('\n')
            if len(parts) < 3:
                print(f"Skipping improperly formatted question: {q}")
                continue  # Skip if the question format is incorrect
            question = parts[0]
            options = [part.split('. ')[1] for part in parts[1:-1]]
            answer = parts[-1].split(':')[-1].strip()
            questions.append({"question": question, "options": options, "answer": answer})
    except IndexError as e:
        print(f"Error parsing question: {e}")
    return questions

@app.route('/')
def index():
    return render_template('index.html'
)

@app.route('/lessons', methods=['GET', 'POST'])
def lessons():
    if request.method == 'POST':
        lesson_title = request.form['lesson_title']
        lesson_content = request.form['lesson_content']
        training.add_lesson(lesson_title, lesson_content)
        return redirect(url_for('lessons'))
    lessons = training.get_lessons()
    return render_template('lessons.html', lessons=lessons)

@app.route('/training')
def training_view():
    return render_template('training.html')

@app.context_processor
def inject_enumerate():
    return dict(enumerate=enumerate)

@app.route('/quiz', methods=['GET', 'POST'])
def quiz_question():
    prompt = "Generate a quiz question about cloud security with options and the correct answer."
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
