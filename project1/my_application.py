from flask import Flask, render_template, request, redirect, url_for
import openai
import training
import time
import os

app = Flask('my_application')

# Set your OpenAI API key
openai.api_key = os.getenv('web key')

#def generate_quiz_questions(prompt):
#    response = openai.Completion.create(
#        engine='gpt-3.5-turbo-instruct',
#        prompt=prompt,
#        max_tokens=1400
#    )
#    questions_text = response.choices[0].text.strip()
#    questions = []
#    try:
#        for q in questions_text.split('\n\n'):
#            parts = q.split('\n')
#            if len(parts) < 3:
#                print(f"Skipping improperly formatted question: {q}")
#                continue  # Skip if the question format is incorrect
#            question = parts[0]
#            options = [part.split('. ')[1] for part in parts[1:-1]]
#            answer = parts[-1].split(':')[-1].strip()
#            questions.append({"question": question, "options": options, "answer": answer})
#    except IndexError as e:
#        print(f"Error parsing question: {e}")
#    return questions

# Training content structure
training_topics = [
'Phishing Emails',
'Password Security',
'Social Engineering Attacks',
'Safe Browsing Practices',
'Device and Network Security',
'Introduction to Cloud Security',
'Understanding Shared Responsibility Model',
'Data Encryption and Protection',
'Identity and Access Management',
'Monitoring and Logging',
'Incident Response and Recovery'
]

# Generate explanation for a topic
def generate_explanation(topic):
                                prompt = f'Explain the concept of {topic} in simple terms suitable for corporate Cloud Security Training.'
                                response = openai.Completion.create(
                                engine='gpt-3.5-turbo-instruct',
                                prompt=prompt,
                                max_tokens=1400
)
                                return response.choices[0].text.strip()

# Generate a quiz question
def generate_quiz_question(topic):
                                  prompt = f'Create a multiple-choice question about {topic} for Cloud Security Training, with one correct answer and three wrong answers.'
                                  response = openai.Completion.create(
                                  engine='gpt-3.5-turbo-instruct',
                                  prompt=prompt,
                                  max_tokens=1400
)
                                  return response.choices[0].text.strip()

# Simulate a phishing scenario
def simulate_phishing_scenario():
                                 prompt = 'Create a simulated phishing email for Cloud Security Training. Include common red flags that employees should identify.'
                                 response = openai.Completion.create(
                                 engine='gpt-3.5-turbo-instruct',
                                 prompt=prompt,
                                 max_tokens=1400
)
                                 return response.choices[0].text.strip()

# Simulate a password security scenario
def simulate_password_scenario():
                                 prompt = 'Create a scenario where an employee is required to create a strong password, including tips and best practices for doing so.'
                                 response = openai.Completion.create(
                                 engine='gpt-3.5-turbo-instruct',
                                 prompt=prompt,
                                 max_tokens=1400
)
                                 return response.choices[0].text.strip()

# Simulate a social engineering attack scenario
def simulate_social_engineering_scenario():
                                           prompt = 'Create a simulated social engineering attack scenario for Cloud Security Training, detailing how an attacker might manipulate an employee.'
                                           response = openai.Completion.create(
                                           engine='gpt-3.5-turbo-instruct',
                                           prompt=prompt,
                                           max_tokens=1400
)
                                           return response.choices[0].text.strip()

# Simulate a safe browsing scenario
def simulate_safe_browsing_scenario():
                                      prompt = 'Create a scenario that highlights safe browsing practices, including identifying secure websites and avoiding malicious links.'
                                      response = openai.Completion.create(
                                      engine='gpt-3.5-turbo-instruct',
                                      prompt=prompt,
                                      max_tokens=1400
)
                                      return response.choices[0].text.strip()

# Simulate a device and network security scenario
def simulate_device_network_scenario():
                                       prompt = 'Create a scenario to train employees on securing their devices and networks, including best practices for Wi-Fi and device updates.'
                                       response = openai.Completion.create(
                                       engine='gpt-3.5-turbo-instruct',
                                       prompt=prompt,
                                       max_tokens=1400
)
                                       return response.choices[0].text.strip()

# Simulate an Introduction to Cloud Security scenario
def simulate_Introduction_to_Cloud_Security_scenario():
                                                       prompt = 'Create a scenario to train employees on Introduction to Cloud Security, including best practices.'
                                                       response = openai.Completion.create(
                                                       engine='gpt-3.5-turbo-instruct',
                                                       prompt=prompt,
                                                       max_tokens=1400
)
                                                       return response.choices[0].text.strip()


# Simulate Understanding Shared Responsibility Model scenario
def simulate_Understanding_Shared_Responsibility_Model_scenario():
                                                                  prompt = 'Create a scenario to train employees on Shared Responsibility Model, including best practices.'
                                                                  response = openai.Completion.create(
                                                                  engine='gpt-3.5-turbo-instruct',
                                                                  prompt=prompt,
                                                                  max_tokens=1400
)
                                                                  return response.choices[0].text.strip()

# Simulate a Data Encryption and Protection scenario
def simulate_Data_Encryption_and_Protection_scenario():
                                                       prompt = 'Create a scenario to train employees on Data Encryption and Protection, including best practices.'
                                                       response = openai.Completion.create(
                                                       engine='gpt-3.5-turbo-instruct',
                                                       prompt=prompt,
                                                       max_tokens=1400
)
                                                       return response.choices[0].text.strip()

# Simulate an Identity and Access Management scenario
def simulate_Identity_and_Access_Management_scenario():
                                                       prompt = 'Create a scenario to train employees on securing their devices and networks, including best practices for Wi-Fi and device updates.'
                                                       response = openai.Completion.create(
                                                       engine='gpt-3.5-turbo-instruct',
                                                       prompt=prompt,
                                                       max_tokens=1400
)
                                                       return response.choices[0].text.strip()

# Simulate a Monitoring and Logging scenario
def simulate_Monitoring_and_Logging_scenario():
                                               prompt = 'Create a scenario to train employees on Monitoring and Logging, including best practices.'
                                               response = openai.Completion.create(
                                               engine='gpt-3.5-turbo-instruct',
                                               prompt=prompt,
                                               max_tokens=1400
)
                                               return response.choices[0].text.strip()

# Simulate an Incident Response and Recovery scenario
def simulate_Incident_Response_and_Recovery_scenario():
                                                       prompt = 'Create a scenario to train employees on Incident Response and Recovery, including best practices.'
                                                       response = openai.Completion.create(
                                                       engine='gpt-3.5-turbo-instruct',
                                                       prompt=prompt,
                                                       max_tokens=1400
)
                                                       return response.choices[0].text.strip()

# Main training function
def CloudSecurityTraining():
                                        prompt = 'Display objectives for Cloud Security Training.'
                                        response = openai.Completion.create(
                                        engine='gpt-3.5-turbo-instruct',
                                        prompt=prompt,
                                        max_tokens=1400
)
                                        return response.choices[0].text.strip()

for topic in training_topics:
                             print(f'\n — — Training Topic: {topic} — -')
                             explanation = generate_explanation(topic)
                             print(f'\nExplanation:\n{explanation}\n')

                             quiz = generate_quiz_question(topic)
                             print(f'\nQuiz:\n{quiz}\n')

                             #input('Press Enter to continue to the next topic:')

                             print('\n — — Simulated Scenarios — -')
                             print('\nPhishing Email Simulation:\n')
                             print(simulate_phishing_scenario())

                             print('\nPassword Security Simulation:\n')
                             print(simulate_password_scenario())

                             print('\nSocial Engineering Simulation:\n')
                             print(simulate_social_engineering_scenario())

                             print('\nSafe Browsing Simulation:\n')
                             print(simulate_safe_browsing_scenario())

                             print('\nDevice and Network Security Simulation:\n')
                             print(simulate_device_network_scenario())

                             print('\nIntroduction to Cloud Security Simulation:\n')
                             print(simulate_Introduction_to_Cloud_Security_scenario())

                             print('\nUnderstanding Shared Responsibility Model Simulation:\n')
                             print(simulate_Understanding_Shared_Responsibility_Model_scenario())

                             print('\nData Encryption and Protection Simulation:\n')
                             print(simulate_Data_Encryption_and_Protection_scenario())

                             print('\nIdentity and Access Management Simulation:\n')
                             print(simulate_Identity_and_Access_Management_scenario())

                             print('\nMonitoring and Logging Simulation:\n')
                             print(simulate_Monitoring_and_Logging_scenario())

                             print('\nIncident Response and Recovery Simulation:\n')
                             print(simulate_Incident_Response_and_Recovery_scenario())

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
    prompt = "Generate a quiz question about cloud security with four options and one correct answer."
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
                            CloudSecurityTraining() 
