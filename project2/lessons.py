
import openai
import os

# Set up OpenAI API key
openai.api_key = os.getenv('web key')

# Lesson content structure
Lesson_topics = [
"Project Integration Management",
"Project Scope Management",
"Project Schedule Management",
"Project Cost Management",
"Project Quality Management",
"Project Resource Management",
"Project Communication Management",
"Project Risk Management",
"Project Procurement Management",
"Project Stakeholder Management",
"Agile & Hybrid Project Management"
]

# Generate explanation for a topic
def generate_explanation(topic):
                                prompt = f'Explain the concept of {topic} in simple terms suitable for corporate Project Management Lesson.'
                                response = openai.Completion.create(
                                engine='gpt-3.5-turbo-instruct',
                                prompt=prompt,
                                max_tokens=1400
)
                                return response.choices[0].text.strip()

# Generate a quiz question
def generate_quiz_question(topic):
                                  prompt = f'Create a multiple-choice question about {topic} for Project Management Lesson, with one correct answer and three wrong answers.'
                                  response = openai.Completion.create(
                                  engine='gpt-3.5-turbo-instruct',
                                  prompt=prompt,
                                  max_tokens=1400
)
                                  return response.choices[0].text.strip()

# Simulate a Project Integration Management scenario
def simulate_Project_Integration_Management_scenario():
                                 prompt = 'Create a simulated Project Integration Management Lesson. Include key factors a project manager should identify.'
                                 response = openai.Completion.create(
                                 engine='gpt-3.5-turbo-instruct',
                                 prompt=prompt,
                                 max_tokens=1400
)
                                 return response.choices[0].text.strip()

# Simulate a Project management plan document scenario
def simulate_Project_management_plan_document_scenario():
                                 prompt = 'Create a scenario where a project manager is required to create a Project management plan document, including tips and best practices for doing so.'
                                 response = openai.Completion.create(
                                 engine='gpt-3.5-turbo-instruct',
                                 prompt=prompt,
                                 max_tokens=1400
)
                                 return response.choices[0].text.strip()

# Simulate a Project Scope Management scenario
def simulate_Project_Scope_Management_scenario():
                                           prompt = 'Create a simulated Project Scope Management scenario for Project management Lesson, detailing how a project manager can scope management.'
                                           response = openai.Completion.create(
                                           engine='gpt-3.5-turbo-instruct',
                                           prompt=prompt,
                                           max_tokens=1400
)
                                           return response.choices[0].text.strip()

# Simulate a Project Schedule Management scenario
def simulate_Project_Schedule_Management_scenario():
                                      prompt = 'Create a scenario that outlines Project Schedule Management, including best practices of safe Project Schedule Management with examples Project Schedule Management reference links.'
                                      response = openai.Completion.create(
                                      engine='gpt-3.5-turbo-instruct',
                                      prompt=prompt,
                                      max_tokens=1400
)
                                      return response.choices[0].text.strip()

# Simulate a Project Cost Management scenario
def simulate_Project_Cost_Management_scenario():
                                       prompt = 'Create a scenario to train project managers on Project Cost Management, including best practices.'
                                       response = openai.Completion.create(
                                       engine='gpt-3.5-turbo-instruct',
                                       prompt=prompt,
                                       max_tokens=1400
)
                                       return response.choices[0].text.strip()

# Simulate a Project Quality Management scenario
def simulate_Project_Quality_Management_scenario():
                                                       prompt = 'Create a scenario to train project managers on Project Quality Management, including best practices.'
                                                       response = openai.Completion.create(
                                                       engine='gpt-3.5-turbo-instruct',
                                                       prompt=prompt,
                                                       max_tokens=1400
)
                                                       return response.choices[0].text.strip()


# Simulate Project Resource Management scenario
def simulate_Project_Resource_Management_scenario():
                                                                  prompt = 'Create a scenario to train project managers on Project Resource Management, including best practices.'
                                                                  response = openai.Completion.create(
                                                                  engine='gpt-3.5-turbo-instruct',
                                                                  prompt=prompt,
                                                                  max_tokens=1400
)
                                                                  return response.choices[0].text.strip()

# Simulate a Project Communication Management scenario
def simulate_Project_Communication_Management_scenario():
                                                       prompt = 'Create a scenario to train project managers on Project Communication Management, including best practices.'
                                                       response = openai.Completion.create(
                                                       engine='gpt-3.5-turbo-instruct',
                                                       prompt=prompt,
                                                       max_tokens=1400
)
                                                       return response.choices[0].text.strip()

# Simulate a Project Risk Management scenario
def simulate_Project_Risk_Management_scenario():
                                                       prompt = 'Create a scenario to train project managers  on Project Risk Management, including best practices .'
                                                       response = openai.Completion.create(
                                                       engine='gpt-3.5-turbo-instruct',
                                                       prompt=prompt,
                                                       max_tokens=1400
)
                                                       return response.choices[0].text.strip()

# Simulate a Project Procurement Management scenario
def simulate_Project_Procurement_Management_scenario():
                                               prompt = 'Create a scenario to train project managers on Project Procurement Management, including best practices.'
                                               response = openai.Completion.create(
                                               engine='gpt-3.5-turbo-instruct',
                                               prompt=prompt,
                                               max_tokens=1400
)
                                               return response.choices[0].text.strip()

# Simulate a Project Stakeholder Management scenario
def simulate_Project_Stakeholder_Management_scenario():
                                                       prompt = 'Create a scenario to train project managers on Project Stakeholder Management, including best practices.'
                                                       response = openai.Completion.create(
                                                       engine='gpt-3.5-turbo-instruct',
                                                       prompt=prompt,
                                                       max_tokens=1400
)
                                                       return response.choices[0].text.strip()

# Simulate an Agile & Hybrid Project Management scenario
def simulate_Agile_and_Hybrid_Project_Management_scenario():
                                                       prompt = 'Create a scenario to train project managers on Agile and Hybrid Project Management, including best practices.'
                                                       response = openai.Completion.create(
                                                       engine='gpt-3.5-turbo-instruct',
                                                       prompt=prompt,
                                                       max_tokens=1400
)
                                                       return response.choices[0].text.strip()


# Main Lesson function
def ProjectManagementLesson():
                                        prompt = 'Display objectives for Project Management Lesson.'
                                        response = openai.Completion.create(
                                        engine='gpt-3.5-turbo-instruct',
                                        prompt=prompt,
                                        max_tokens=1400
)
                                        return response.choices[0].text.strip()

for topic in Lesson_topics:
                             print(f'\n — — Lesson Topic: {topic} — -')
                             explanation = generate_explanation(topic)
                             print(f'\nExplanation:\n{explanation}\n')

                             quiz = generate_quiz_question(topic)
                             print(f'\nQuiz:\n{quiz}\n')

                             #input('Press Enter to continue to the next topic:')

                             print('\n — — Simulated Scenarios — -')
                             print('\nProject Integration Management Simulation:\n')
                             print(simulate_Project_Integration_Management_scenario())

                             print('\nProject Scope Management:\n')
                             print(simulate_Project_Scope_Management_scenario())

                             print('\nProject Schedule Management Simulation:\n')
                             print(simulate_Project_Schedule_Management_scenario())

                             print('\nProject Cost Management Simulation:\n')
                             print(simulate_Project_Cost_Management_scenario())

                             print('\nProject Quality Management Simulation:\n')
                             print(simulate_Project_Quality_Management_scenario())

                             print('\nProject Resource Management Simulation:\n')
                             print(simulate_Project_Resource_Management_scenario())

                             print('\nProject Communication Management Simulation:\n')
                             print(simulate_Project_Communication_Management_scenario())

                             print('\nProject Risk Management Simulation:\n')
                             print(simulate_Project_Risk_Management_scenario())

                             print('\nProject Procurement Management Simulation:\n')
                             print(simulate_Project_Procurement_Management_scenario())

                             print('\nProject Stakeholder Management Simulation:\n')
                             print(simulate_Project_Stakeholder_Management_scenario())

                             print('\nAgile and Hybrid Project Management Simulation:\n')
                             print(simulate_Agile_and_Hybrid_Project_Management_scenario())


# Run the Lesson program
if __name__ == '__main__':
                          ProjectManagementLesson()

