processed_results = [
    {'student_name': 'Анна', 'score': 91, 'passed': True},
    {'student_name': 'Богдан', 'score': 58, 'passed': False},
    {'student_name': 'Вікторія', 'score': 75, 'passed': True},
    {'student_name': 'Григорій', 'score': 45, 'passed': False},
]
successful_students = []

for i in range(len(processed_results)):
    if processed_results[i]["passed"] == True:
        successful_students.append(processed_results[i])
print(successful_students)