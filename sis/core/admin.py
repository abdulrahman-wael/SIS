from django.contrib import admin
from .models import Course, CourseAssignment, AvailabilitySlot, WeeklySchedule, ScheduledSlot

@admin.register(AvailabilitySlot)
class AvailabilitySlotAdmin(admin.ModelAdmin):
    list_filter = ['day_of_week']

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(teacher=request.user)

    def save_model(self, request, obj, form, change):
        if not request.user.is_superuser:
            obj.teacher = request.user
        super().save_model(request, obj, form, change)

    def get_readonly_fields(self, request, obj=None):
        if request.user.is_superuser:
            return []
        return ["teacher"]

admin.site.register(Course)
admin.site.register(CourseAssignment)
admin.site.register(ScheduledSlot)
admin.site.register(WeeklySchedule)
