# choose and sharpen the idea

1. one-sentece pitch:

   1. This app helps teachers suggest better "weekly work schedules for university" for the admins to create with AI without hussles
   2. all other features are delayed.
2. This is a learning project tell the moment
3. 3 similar apps and what I'll copy or leave from them

   1. skyward (scheduling feature)

      1. to copy: admin edit ability, seeing the conflicts proposed by teachers (the teacher is not available in this time slot)
      2. to leave: most of the features won't be worth it for an MVP
   2. infinite campus

      1. to copy: a progress bar for finishing the schedule (admin page)
      2. to leave: general scheduling (not only weekly schedule)
   3. Academic scheduler

      1. to copy: full admin experience (dashboard, subjects, teachers, classes, schedules)
      2. to leave: sustitution, exam timetable

# Define the MVP

1. 2 interfaces: admin's, and teacher's
2. admin: scheduling function (with integrated AI)
3. teacher interface: schedule view
4. The MAIN features:
   1. Conflict detection: teachers can propose there (NOT AVAILABLE) time slots on the schedule of the week..
   2. Aggregated availability view: admin can see an aggregated view of there preferences and then he manually choose the best schedule based on the this input. then the new schedule will be shown to the teachers.

# Data Model

* **User** — built-in: login info; role via Django Groups
* **Teacher** — user (OneToOne), courses (M2M→Course)
* **Course** — name, code, places
* **AvailabilitySlot** — teacher (FK), day_of_week [IntegerField(choices=DAY_CHOICES)], start_time, end_time
* **WeeklySchedule** — week_start, status (draft/published)
* **ScheduledSlot** — weekly_schedule (FK), teacher (FK), course (FK), place, day_of_week, start_time, end_time

# Breaking down into tasks

1. setup, admin dashboard creation
2. one cycle over (admin interface -> teacher)
   1. create the models
   2. create the related view function
   3. create the related URLs in urls.py
   4. create the related HTML files
   5. create tests
   6. deploy
3. another cycle for things left from the first cycle

# Decisions

1. SQLite
2. tailwind css
3. django built-in auth
4. deployment: pythonAnyWhere

# "done" definition

admin creates a weekly schedule for 3+ teachers and courses, respecting their unavailable slots, publishes it, teacher sees it.

# Maybe next

1. adding AI suggested plans to the UI of the admin.
2. making the tool generalizable for any scheduling of events happening inside the university
3. allowing students to vote
4. adding more features from real SISs
