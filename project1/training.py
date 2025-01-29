import openai
import os

# Set up OpenAI API key
openai.api_key = os.getenv('web key')

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
                                prompt = f'Explain the concept of {topic} in simple terms suitable for corporate Cloud Security Awareness.'
                                response = openai.Completion.create(
                                engine='gpt-3.5-turbo-instruct',
                                prompt=prompt,
                                max_tokens=1400
)
                                return response.choices[0].text.strip()

# Generate a quiz question
def generate_quiz_question(topic):
                                  prompt = f'Create a multiple-choice question about {topic} for cloud Security Awareness, with one correct answer and three wrong answers.'
                                  response = openai.Completion.create(
                                  engine='gpt-3.5-turbo-instruct',
                                  prompt=prompt,
                                  max_tokens=1400
)
                                  return response.choices[0].text.strip()

# Simulate a phishing scenario
def simulate_phishing_scenario():
                                 prompt = 'Create a simulated phishing email for cloud Security Awareness. Include common red flags that employees should identify.'
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
                                           prompt = 'Create a simulated social engineering attack scenario for cloud Security Awareness, detailing how an attacker might manipulate an employee.'
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


# Run the training program
if __name__ == '__main__':
                          CloudSecurityTraining()
