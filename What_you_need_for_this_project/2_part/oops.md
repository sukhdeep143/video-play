--

## 🧱 1. **Think in Terms of Objects**

Ask yourself:
> What are the real-world "things" (nouns) in my program?

Example: In a school management system, you might have:
- `Student`
- `Teacher`
- `Course`

Each of these can be a class.

---

## 🧠 2. **Group Related Data and Behaviors Together**

For each class, define:
- **Attributes** (data it stores)
- **Methods** (things it can do)

```python
class Student:
    def __init__(self, name, roll_no):
        self.name = name
        self.roll_no = roll_no
        self.courses = []

    def enroll(self, course):
        self.courses.append(course)

    def show_courses(self):
        print(f"{self.name} is enrolled in: {self.courses}")
```

---

## 🧩 3. **Use One Class per Responsibility**

Apply the **Single Responsibility Principle**:
> One class should only do *one thing* well.

Don't mix logic like file saving, calculations, or UI in one class.

Example:
```python
class FileManager:
    def save_data(self, data):
        # Save to file logic

class GradeCalculator:
    def calculate_gpa(self, marks):
        # GPA logic
```

---

## 🧬 4. **Use Relationships Between Classes**

### ✅ Composition (has-a relationship):
```python
class Course:
    def __init__(self, name):
        self.name = name

class Student:
    def __init__(self, name):
        self.name = name
        self.courses = []

    def add_course(self, course):
        self.courses.append(course)

# Usage
math = Course("Math")
s1 = Student("Ravi")
s1.add_course(math)
```

### ✅ Inheritance (is-a relationship):
```python
class Person:
    def __init__(self, name):
        self.name = name

class Teacher(Person):  # Teacher is a Person
    def teach(self):
        print(f"{self.name} is teaching.")
```

---

## 🛠️ 5. **Example Project Structure**

```python
# student.py
class Student:
    ...

# teacher.py
class Teacher:
    ...

# course.py
class Course:
    ...

# main.py
from student import Student
from course import Course

s1 = Student("Aman", 101)
math = Course("Math")
s1.enroll(math)
```

---

## 🔚 Summary

| OOP Element       | What it Helps With                           |
|-------------------|----------------------------------------------|
| Classes           | Group related data + logic                   |
| `__init__`        | Initialize data when object is created       |
| Methods           | Organize functionality                       |
| Composition       | Link objects together                        |
| Inheritance       | Reuse logic and extend features              |

---
