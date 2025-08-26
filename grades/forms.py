from django import forms
from .models import Student, PrelimRecord, MidtermRecord, FinalRecord

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ["name", "course"]

class PrelimRecordForm(forms.ModelForm):
    class Meta:
        model = PrelimRecord
        fields = ["student", "prelim_exam", "quizzes", "requirements", "recitation", "absences"]
        widgets = {
            "prelim_exam": forms.NumberInput(attrs={"step": "0.01", "min": "0", "max": "100"}),
            "quizzes": forms.NumberInput(attrs={"step": "0.01", "min": "0", "max": "100"}),
            "requirements": forms.NumberInput(attrs={"step": "0.01", "min": "0", "max": "100"}),
            "recitation": forms.NumberInput(attrs={"step": "0.01", "min": "0", "max": "100"}),
            "absences": forms.NumberInput(attrs={"min": "0"}),
        }
class MidtermRecordForm(forms.ModelForm):  
    class Meta:
        model = MidtermRecord
        fields = ["student", "midterm_exam", "quizzes", "requirements", "recitation", "absences"]
        widgets = {
            "midterm_exam": forms.NumberInput(attrs={"step": "0.01", "min": "0", "max": "100"}),
            "quizzes": forms.NumberInput(attrs={"step": "0.01", "min": "0", "max": "100"}),
            "requirements": forms.NumberInput(attrs={"step": "0.01", "min": "0", "max": "100"}),
            "recitation": forms.NumberInput(attrs={"step": "0.01", "min": "0", "max": "100"}),
            "absences": forms.NumberInput(attrs={"min": "0"}),
        }

class FinalRecordForm(forms.ModelForm):  
    class Meta:
        model = FinalRecord
        fields = ["student", "final_exam", "quizzes", "requirements", "recitation", "absences"]
        widgets = {
            "final_exam": forms.NumberInput(attrs={"step": "0.01", "min": "0", "max": "100"}),
            "quizzes": forms.NumberInput(attrs={"step": "0.01", "min": "0", "max": "100"}),
            "requirements": forms.NumberInput(attrs={"step": "0.01", "min": "0", "max": "100"}),
            "recitation": forms.NumberInput(attrs={"step": "0.01", "min": "0", "max": "100"}),
            "absences": forms.NumberInput(attrs={"min": "0"}),
        }