from django.contrib import admin
from .models import Course, CourseAssignment, AvailabilitySlot, WeeklySchedule, ScheduledSlot
# Register your models here.
admin.site.register(Course)
admin.site.register(CourseAssignment)
admin.site.register(ScheduledSlot)
admin.site.register(WeeklySchedule)
admin.site.register(AvailabilitySlot)
