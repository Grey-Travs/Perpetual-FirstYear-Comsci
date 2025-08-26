from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib import messages
from .forms import (
    StudentForm, PrelimRecordForm, MidtermRecordForm, FinalRecordForm
)
from .models import PrelimRecord, MidtermRecord, FinalRecord


def student_create(request):
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("student_create")  
    else:
        form = StudentForm()
    return render(request, "grades/student_create.html", {"form": form})


def prelim_create(request):
    """Page to enter prelim components and immediately save the record."""
    if request.method == "POST":
        form = PrelimRecordForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("prelim_list")
    else:
        form = PrelimRecordForm()
    return render(request, "grades/prelim_create.html", {"form": form})


def midterm_create(request):
    if request.method == "POST":
        form = MidtermRecordForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("prelim_list")
    else:
        form = MidtermRecordForm()
    return render(request, "grades/midterm_create.html", {"form": form})


def final_create(request):
    if request.method == "POST":
        form = FinalRecordForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("prelim_list")
    else:
        form = FinalRecordForm()
    return render(request, "grades/final_create.html", {"form": form})


def prelim_list(request):
    records = PrelimRecord.objects.select_related("student").order_by("-created_at")
    midterm_records = MidtermRecord.objects.select_related("student").order_by("-created_at")
    final_records = FinalRecord.objects.select_related("student").order_by("-created_at")

    return render(
        request,
        "grades/prelim_list.html",
        {
            "records": records,             
            "midterm_records": midterm_records,
            "final_records": final_records,
        },
    )


def midterm_list(request):  
    return redirect("prelim_list")


def final_list(request):  
    return redirect("prelim_list")


def grading(request):
    """
    Unified Grading page with a term dropdown (prelim/midterm/final).
    - On POST success → redirect to Records so you can confirm the new row.
    - On invalid → re-render form with clear errors.
    """
    term = request.GET.get("term") or request.POST.get("term") or "prelim"

    form_map = {
        "prelim":  (PrelimRecordForm, "Prelim"),
        "midterm": (MidtermRecordForm, "Midterm"),
        "final":   (FinalRecordForm, "Finals"),
    }
    if term not in form_map:
        term = "prelim"

    FormClass, term_label = form_map[term]
    context = {"term": term, "term_label": term_label}

    if request.method == "POST":
        form = FormClass(request.POST)
        if form.is_valid():
            obj = form.save()
            messages.success(request, f"{term_label} saved for {obj.student}.")
            return redirect("prelim_list")
        else:
            context["form"] = form
            return render(request, "grades/grading.html", context)

    # GET → blank form
    context["form"] = FormClass()
    return render(request, "grades/grading.html", context)
def home(request):  
    return render(request, "grades/home.html")