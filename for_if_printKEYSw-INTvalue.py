student = {"name": "Colby", "age": 22, "grade": 12}
for key, value in student.items():
    if isinstance(value, int):
        print(key)