exam_results =[
    {"student_name": "Анна", "score":91},
    {"student_name": "Богдан", "score": 58},
    {"student_name": "Вікторія", "score": 75},
    {"student_name": "Григорій", "score": 45}
]
passing_score = 60 # Прохідний бал

for i in range(len(exam_results)):
    if exam_results[i]["score"] >= passing_score:
        exam_results[i]["passed"] = True
    else:
        exam_results[i]["passed"] = False
    print(exam_results[i])