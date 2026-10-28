from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as login_view, logout as logout_view
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import WeeklySchedule, Day

def index(request):
    return render(request, 'core/index.html')

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login_view(request, user)
            return redirect("/")
        else:
            messages.error(request, 'Invalid username or password')
    else:
        return render(request, 'core/login.html')

def logout(request):
    logout_view(request)
    return render(request, 'core/index.html')

@login_required
def schedule(request):
    active_schedule = (WeeklySchedule.objects
        .filter(status__exact='published')                     # changed: crash-safe query
        .order_by('-week_start').first())                      # changed: first() instead of latest()
    hours = [f"{h % 12 or 12} {'AM' if h < 12 else 'PM'}" for h in range(8, 17)]  # changed: 12-hour clock headers
    rows = []
    for day in range(5):
        rows.append([None] * 9)                                # changed: one blank week grid
    if active_schedule:
        for slot in active_schedule.slots.all():               # changed: slots read only when a schedule exists
            col = slot.start_time.hour - 8                     # changed: drop cols list, skip check via range guard
            if 0 <= col < 9:                                   # added: ignore out-of-grid times instead of crash
                rows[slot.day_of_week][col] = slot.course_assignment.course.name
    return render(request, 'core/schedule.html', {
        'pairs': zip(Day.labels, rows),                        # changed: day labels paired with their rows
        'hours': hours,                                        # added: hour header for the teacher
        'week': active_schedule,                               # added: template shows week dates or empty state
    })