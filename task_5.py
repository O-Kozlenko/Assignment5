employees = [
    {"name": "Олена", "department": "Marketing", "salary": 25000},
    {"name": "Igor", "department": "IT", "salary": 55000},
    {"name": "Nataly", "department":"Marketing", "salary": 28000},
    {"name": "Oleg", "department": "HR", "salary": 22000},
    {"name": "Andrew", "department": "IT", "salary": 48000},
    {"name": "Mary", "department": "IT", "salary": 52000}
]

def get_department_stats(employee_list, target_dept):
    salarytot = 0
    counter = 0
    highest = 0
    for i in range(len(employees)):
        if employees[i]["department"] == target_dept:
            counter +=1
            salarytot+=employees[i]["salary"]
            if highest<employees[i]["salary"]:
                highest = employees[i]["salary"]
                bestemplo = employees[i]["name"]
    return {
        target_dept,
        salarytot/counter,
        bestemplo,
        counter,
    }
print(get_department_stats(employees,"HR"))