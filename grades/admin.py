
from django.contrib import admin
from .models import Student, PrelimRecord, MidtermRecord, FinalRecord  

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ("name", "course")
    search_fields = ("name", "course")
    ordering = ("name",)

@admin.register(PrelimRecord)
class PrelimRecordAdmin(admin.ModelAdmin):
    list_display = ("student", "prelim_exam", "quizzes", "requirements", "recitation",
        "absences", "get_attendance", "get_class_standing",
        "get_prelim_grade", "get_pass_fail",
        "get_required_75", "get_required_90", "created_at")
    
    readonly_fields = ("prelim_grade", "status")
    list_filter = ("student__course", "created_at")
    search_fields = ("student__name", "student__course")
    autocomplete_fields = ("student",)

    readonly_fields = (
        "get_attendance",
        "get_class_standing",
        "get_prelim_grade",
        "get_required_75",
        "get_required_90",
    )

    fieldsets = (
        ("Student", {"fields": ("student",)}),
        ("Components (0–100)", {
            "fields": ("prelim_exam", "quizzes", "requirements", "recitation")
        }),
        ("Attendance", {"fields": ("absences",)}),
        ("Computed", {
            "fields": (
                "get_attendance",
                "get_class_standing",
                "get_prelim_grade",
                "get_required_75",
                "get_required_90",
            )
        }),
    )

    

    @admin.display(description="Attendance Score")
    def get_attendance(self, obj):
        if not obj or obj.pk is None:
            return "-"
        return f"{obj.attendance_score():.2f}"

    @admin.display(description="Class Standing")
    def get_class_standing(self, obj):
        if not obj or obj.pk is None:
            return "-"
        return f"{obj.class_standing():.2f}"

    @admin.display(description="Prelim Grade")
    def get_prelim_grade(self, obj):
        if not obj or obj.pk is None:
            return "-"
        return f"{obj.prelim_grade():.2f}"
    
    @admin.display(description="Pass/Fail") 
    def get_pass_fail(self, obj):
        if not obj or obj.pk is None:
            return "-"
        return obj.pass_fail_status()

    @admin.display(description="Needed Each for 75% (Midterm & Final)")
    def get_required_75(self, obj):
        if not obj or obj.pk is None:
            return "-"
        val = obj.required_each_for(75.0)
        return f"{val:.2f}" if 0.0 <= val <= 100.0 else f"{val:.2f} (out of 0–100)"

    @admin.display(description="Needed Each for 90% (Midterm & Final)")
    def get_required_90(self, obj):
        if not obj or obj.pk is None:
            return "-"
        val = obj.required_each_for(90.0)
        return f"{val:.2f}" if 0.0 <= val <= 100.0 else f"{val:.2f} (out of 0–100)"
    
@admin.register(MidtermRecord)  
class MidtermRecordAdmin(admin.ModelAdmin):
    list_display = (
        "student",
        "midterm_exam",
        "quizzes",
        "requirements",
        "recitation",
        "absences",
        "get_attendance",
        "get_class_standing",
        "get_midterm_grade",
        "created_at",
    )
    list_filter = ("student__course", "created_at")
    search_fields = ("student__name", "student__course")
    autocomplete_fields = ("student",)

    readonly_fields = ("get_attendance", "get_class_standing", "get_midterm_grade")

    fieldsets = (
        ("Student", {"fields": ("student",)}),
        ("Components (0–100)", {"fields": ("midterm_exam", "quizzes", "requirements", "recitation")}),
        ("Attendance", {"fields": ("absences",)}),
        ("Computed", {"fields": ("get_attendance", "get_class_standing", "get_midterm_grade")}),
    )

    @admin.display(description="Attendance Score")
    def get_attendance(self, obj):
        if not obj or obj.pk is None:
            return "-"
        return f"{obj.attendance_score():.2f}"

    @admin.display(description="Class Standing")
    def get_class_standing(self, obj):
        if not obj or obj.pk is None:
            return "-"
        return f"{obj.class_standing():.2f}"

    @admin.display(description="Midterm Grade")
    def get_midterm_grade(self, obj):
        if not obj or obj.pk is None:
            return "-"
        return f"{obj.midterm_grade():.2f}"

@admin.register(FinalRecord)  
class FinalRecordAdmin(admin.ModelAdmin):
    list_display = (
        "student",
        "final_exam",
        "quizzes",
        "requirements",
        "recitation",
        "absences",
        "get_attendance",
        "get_class_standing",
        "get_final_grade",
        "created_at",
    )
    list_filter = ("student__course", "created_at")
    search_fields = ("student__name", "student__course")
    autocomplete_fields = ("student",)

    readonly_fields = ("get_attendance", "get_class_standing", "get_final_grade")

    fieldsets = (
        ("Student", {"fields": ("student",)}),
        ("Components (0–100)", {"fields": ("final_exam", "quizzes", "requirements", "recitation")}),
        ("Attendance", {"fields": ("absences",)}),
        ("Computed", {"fields": ("get_attendance", "get_class_standing", "get_final_grade")}),
    )

    @admin.display(description="Attendance Score")
    def get_attendance(self, obj):
        if not obj or obj.pk is None:
            return "-"
        return f"{obj.attendance_score():.2f}"

    @admin.display(description="Class Standing")
    def get_class_standing(self, obj):
        if not obj or obj.pk is None:
            return "-"
        return f"{obj.class_standing():.2f}"

    @admin.display(description="Final Grade")
    def get_final_grade(self, obj):
        if not obj or obj.pk is None:
            return "-"
        return f"{obj.final_grade():.2f}"