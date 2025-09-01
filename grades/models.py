from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Student(models.Model):
    name = models.CharField(max_length=100)
    course = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name} ({self.course})"

class PrelimRecord(models.Model):

    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name="prelims")

    prelim_exam = models.FloatField(validators=[MinValueValidator(0), MaxValueValidator(100)])
    quizzes = models.FloatField(validators=[MinValueValidator(0), MaxValueValidator(100)])
    requirements = models.FloatField(validators=[MinValueValidator(0), MaxValueValidator(100)])
    recitation = models.FloatField(validators=[MinValueValidator(0), MaxValueValidator(100)])
    absences = models.PositiveIntegerField(default=0)

    created_at = models.DateTimeField(auto_now_add=True)

    def required_75(self) -> float:
        return self.required_each_for(75.0)

    def required_90(self) -> float:
        return self.required_each_for(90.0)

     # --- Calculation helpers ---
    @staticmethod
    def _clamp(x, low=0.0, high=100.0):
        return max(low, min(high, x))

    def attendance_score(self) -> float:
        absences = self.absences or 0
        return self._clamp(100.0 - 10.0 * float(absences), 0.0, 100.0)

    def class_standing(self) -> float:
        q = self.quizzes or 0.0
        r = self.requirements or 0.0
        rec = self.recitation or 0.0
        return 0.40 * q + 0.30 * r + 0.30 * rec

    def prelim_grade(self) -> float:
         exam = self.prelim_exam or 0.0
         return 0.60 * exam + 0.10 * self.attendance_score() + 0.30 * self.class_standing()

    def pass_fail_status(self):
        grade = self.prelim_grade()
        absences = self.absences or 0
        if grade >= 75 and absences < 4:
            return "PASS"
        return "FAIL"
        

    # Required Midterm/Final (assuming overall = (Prelim + Midterm + Final)/3, and Midterm=Final)
    def required_each_for(self, target_overall: float) -> float:
        prelim = self.prelim_grade()
        return (3.0 * target_overall - prelim) / 2.0


    def __str__(self):
        return f"Prelim for {self.student} on {self.created_at:%Y-%m-%d}"

class MidtermRecord(models.Model):  
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name="midterms")  
    midterm_exam = models.FloatField(validators=[MinValueValidator(0), MaxValueValidator(100)])  
    quizzes = models.FloatField(validators=[MinValueValidator(0), MaxValueValidator(100)])  
    requirements = models.FloatField(validators=[MinValueValidator(0), MaxValueValidator(100)])  
    recitation = models.FloatField(validators=[MinValueValidator(0), MaxValueValidator(100)])  
    absences = models.PositiveIntegerField(default=0)  
    created_at = models.DateTimeField(auto_now_add=True)  

    @staticmethod
    def _clamp(x, low=0.0, high=100.0):  
        return max(low, min(high, x))

    def attendance_score(self) -> float:  
        absences = self.absences or 0
        return self._clamp(100.0 - 10.0 * float(absences), 0.0, 100.0)

    def class_standing(self) -> float:  
        q = self.quizzes or 0.0
        r = self.requirements or 0.0
        rec = self.recitation or 0.0
        return 0.40 * q + 0.30 * r + 0.30 * rec

    def midterm_grade(self) -> float:  
        exam = self.midterm_exam or 0.0
        return 0.60 * exam + 0.10 * self.attendance_score() + 0.30 * self.class_standing()

    def __str__(self):
        return f"Midterm for {self.student} on {self.created_at:%Y-%m-%d}"  


class FinalRecord(models.Model):  
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name="finals")  
    final_exam = models.FloatField(validators=[MinValueValidator(0), MaxValueValidator(100)])  
    quizzes = models.FloatField(validators=[MinValueValidator(0), MaxValueValidator(100)])  
    requirements = models.FloatField(validators=[MinValueValidator(0), MaxValueValidator(100)])  
    recitation = models.FloatField(validators=[MinValueValidator(0), MaxValueValidator(100)])  
    absences = models.PositiveIntegerField(default=0)  
    created_at = models.DateTimeField(auto_now_add=True)  

    @staticmethod
    def _clamp(x, low=0.0, high=100.0):  
        return max(low, min(high, x))

    def attendance_score(self) -> float:  
        absences = self.absences or 0
        return self._clamp(100.0 - 10.0 * float(absences), 0.0, 100.0)

    def class_standing(self) -> float:  
        q = self.quizzes or 0.0
        r = self.requirements or 0.0
        rec = self.recitation or 0.0
        return 0.40 * q + 0.30 * r + 0.30 * rec

    def final_grade(self) -> float:  
        exam = self.final_exam or 0.0
        return 0.60 * exam + 0.10 * self.attendance_score() + 0.30 * self.class_standing()

    def __str__(self):
        return f"Final for {self.student} on {self.created_at:%Y-%m-%d}"  