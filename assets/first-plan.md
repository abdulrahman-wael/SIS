
# choose and sharpen the idea

1. one-sentece pitch:
   1. This app helps students access the servces the uni offers without big confusion or latency
   2. This app helps universities easily offer their serveces and manage them without coding or paper work
   3. This app helps teachers manage there work more effectively
2. This is a learning project tell the moment
3. 5 similar apps and what I'll copy or leave from them
   1. skyward
      1. to copy: multiple interfaces: admins, parents, teachers, students
      2. to leave: most of the features won't be worth it for an MVP
   2. infinite campus
      1. to copy: demographics section
      2. to leave: notfications (for now)
   3. teachrease
      1. to copy: reporting ability for admins
      2. to leave: direct chat channels
   4. power school srs
      1. to copy: security
      2. to leave: personalized learning
   5. myu (my uni system)
      1. to copy: simple card view of services
      2. to leave: old looking interface

# Define the MVP

1. 3 interfaces: student's, admin's, and teacher's
2. student interface include: demographics view, courses grid (and grading inside), schedule view
3. admin: scheduling function (with integrated AI), courses grid, grades page (KPIs grid, details table with reporting function for both)
4. teacher interface: students, schedule, courses
5. The WOW feature: teachers can propose there (PREFERRED, NOT AVAILABLE) time slots on the schedule of the week.. then admin can see an aggregated view of there preferences and then AI can suggest the best schedule based on the this input. then the new schedule will be shown to the teachers.

# Data Model

1. class (basic info, students, schedule)
2. student (login info, demographics, courses, grades)
3. teacher (login info, schedule, courses, students)
4. admin (login info, schedule, courses)
5. courses (basic info, teachers, students, schedule)
6. schedule (teachers, classes, dates and times)

# Breaking down into tasks

1. setup, admin dashboard creation
2. one cycle over (admin interface -> student -> teacher)
   1. create a view function
   2. create the related models
   3. create the related HTML files
   4. create the related URLs in urls.py
   5. create tests
   6. deploy
3. another cycle for things left from the first cycle

# Decisions

1. SQLite
2. tailwind css
3. django-allauth
4. deployment: pythonAnyWhere
