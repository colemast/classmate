from flask import Flask, jsonify, request

app = Flask(__name__)

# Sample data
students = [
    {
        'id': 1,
        'name': 'John Doe',
        'age': 20,
        'major': 'Computer Science'
    },
    {
        'id': 2,
        'name': 'Jane Smith',
        'age': 21,
        'major': 'Mathematics'
    }
]

# Get all students
@app.route('/students', methods=['GET'])
def get_students():
    return jsonify(students)

# Get a single student
@app.route('/students/<int:student_id>', methods=['GET'])
def get_student(student_id):
    student = [student for student in students if student['id'] == student_id]
    if len(student) == 0:
        abort(404)
    return jsonify({'student': student[0]})

# Create a new student
@app.route('/students', methods=['POST'])
def create_student():
    if not request.json or not 'name' in request.json:
        abort(400)
    student = {
        'id': students[-1]['id'] + 1,
        'name': request.json['name'],
        'age': request.json.get('age', ''),
        'major': request.json.get('major', '')
    }
    students.append(student)
    return jsonify(student), 201

# Update an existing student
@app.route('/students/<int:student_id>', methods=['PUT'])
def update_student(student_id):
    student = [student for student in students if student['id'] == student_id]
    if len(student) == 0:
        abort(404)
    if not request.json:
        abort(400)
    student[0]['name'] = request.json.get('name', student[0]['name'])
    student[0]['age'] = request.json.get('age', student[0]['age'])
    student[0]['major'] = request.json.get('major', student[0]['major'])
    return jsonify(student[0])

# Delete a student
@app.route('/students/<int:student_id>', methods=['DELETE'])
def delete_student(student_id):
    student = [student for student in students if student['id'] == student_id]
    if len(student) == 0:
        abort(404)
    students.remove(student[0])
    return jsonify({'result': True})

if __name__ == '__main__':
    app.run(debug=True)
