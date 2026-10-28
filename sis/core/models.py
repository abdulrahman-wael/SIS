from django.db import models
from django.contrib.auth.models import User

class Day(models.IntegerChoices):
    SUN = 0, "Sun"; MON = 1, "Mon"; TUE = 2, "Tue"; WED = 3, "Wed"; THU = 4, "Thu"

class Course(models.Model):
    name = models.CharField(max_length=30)
    code = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return self.name


class CourseAssignment(models.Model):
    teacher = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    hours_per_week = models.IntegerField()

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields = ['teacher', 'course'],
                 name = 'unique_teacher_course'
            )
        ]

    def __str__(self):
        return str(self.teacher) + '_' + str(self.course)

class AvailabilitySlot(models.Model):
    teacher = models.ForeignKey(User, on_delete=models.CASCADE)
    day_of_week = models.PositiveSmallIntegerField(choices=Day.choices)
    start_time = models.TimeField()
    end_time = models.TimeField()

    def __str__(self):
        return str(self.teacher) + '_' + str(self.day_of_week)

class WeeklySchedule(models.Model):
    CATEGORY_CHOICES = [
        ('published', 'Published'),
        ('draft', 'Draft')
    ]

    week_start = models.DateField()
    status = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='draft')
    conflict_count = models.IntegerField(default=0)
    candidate_group = models.PositiveSmallIntegerField(null=True, blank=True)

class ScheduledSlot(models.Model):
    weekly_schedule = models.ForeignKey(WeeklySchedule, on_delete=models.CASCADE, related_name='slots')
    course_assignment = models.ForeignKey(CourseAssignment, on_delete=models.PROTECT)
    day_of_week = models.PositiveSmallIntegerField(choices=Day.choices)
    start_time = models.TimeField()
    end_time = models.TimeField()

    class Meta:
        ordering = ['day_of_week', 'start_time']
