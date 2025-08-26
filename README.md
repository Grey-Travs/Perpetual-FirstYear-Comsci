# Django Grading App

A web-based grading system built with Django.  
It supports Students, Prelim, Midterm, and Final records, with automatic grade calculations and requirements to pass or qualify for Dean’s List.

---

## 🚀 Features
- Add students via web form or Django Admin.
- Enter Prelim, Midterm, and Final grades with attendance, quizzes, requirements, and recitation.
- Automatic calculations:
  - Attendance score (100 – 10×absences, clamped 0–100).
  - Class standing = 40% Quizzes + 30% Requirements + 30% Recitation.
  - Prelim grade = 60% Exam + 10% Attendance + 30% Class Standing.
  - Target calculator: required Midterm/Final grades to reach 75% (pass) or 90% (Dean’s List).
- Records page shows all terms in one place.
- Clean navigation bar (Home | Grading | Records | New Student).
- Basic CSS styling for nav, buttons, and tables.

---

## 📂 Project Structure
grading_project/ # Django project settings
grades/ # App with models, views, templates, static
templates/grades/ # HTML templates
static/grades/css/ # CSS files
manage.py # Django management script
requirements.txt # Python dependencies

## 🤖 Acknowledgements
This project was developed with guidance from [ChatGPT](https://chat.openai.com/) for explanations, code scaffolding, and debugging support.  
All logic and implementation decisions were reviewed and customized by me.
