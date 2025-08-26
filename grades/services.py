def clamp(x, low=0.0, high=100.0):
    return max(low, min(high, x))

def attendance_score(absences: int) -> float:
    return clamp(100 - 10 * absences, 0, 100)

def class_standing(quizzes: float, requirements: float, recitation: float) -> float:
    return 0.40 * quizzes + 0.30 * requirements + 0.30 * recitation

def prelim_grade(prelim_exam: float, attendance: float, cls: float) -> float:
    return 0.60 * prelim_exam + 0.10 * attendance + 0.30 * cls

def needed_midterm_final_equal(prelim: float, target_overall: float) -> float:
    # Overall = (Prelim + Midterm + Final)/3, with Midterm = Final
    return (3 * target_overall - prelim) / 2
