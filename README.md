# Backend Habit Tracker Application
This is my very first piece of code specifically generated due to mandatory unversity classes for upload to github - and there it is ;)

This exercise taught me how to implement functional and object orientated programming paradigms into a modern application backend with python. I AM proud of what I have developed within 3-4 weeks over X-mas 2021, but of course I am sure this is not the most efficient and performant code available on this topic. For the more advanced students this might even be an insult on how python code should be looking like, and I apologize deeply for this insult... Anyway, I hope at least my tutor will see the upsides on my efforts, and I will appreciate feedback from anyone to help me produce better code in the future.

# Project Description
The goal of this backend application is to ingest **USER** class, **HABIT** class, and **RECORD** class attributes by manual input. User input is send to sqlite3 database file in which a table is provided for every class. Tables are linked via foreign key by an one-to-many (1:N) relationship (USER->HABIT->RECORD). One user can create multiple habits, and any habit is linked to exactly one user. One habit can be linked to multiple records, and any record is linked to exactly one habit. The application is designed to run outside IDLE by just executing in windows via "double click". A console will be presented to the user asking for input decisions, but also providing options for exiting prematurely. Upon starting the application, a user can be newly created and registered to the database. Existing users must initially login by their registration credentials (username and password). Usernames must be unique and at least 4 characters long. After successful login, the user is presented with several options to choose from:

**1) Registration, editing, or deleting habits:** habit names must be non-empty and unique, habit description is optional, habit periodicity must be 'd'=daily or 'w'=weekly, timestamp is generated automatically upon registration or editing. Username and password are case-sensitive.

**2) Registration, editing, or deleting of records:** a records only attribute (except for the foreign key: habit id) is a timestamp taken either automatically or manually, in case of editing a record or doing a recording retrospectively. In the latter case you must provide a timestamp in the following ISO format: date='YYYY-MM-DD' and time='HH:MM:SS'. Records can only be edited or deleted for 14 days preceding the date of login.

**3) Reporting on existing data:** the user may print a list of all currently tracked habits, their all-time longest streaks (time passed without dropping a habit in days or weeks), and filtered by perodicity ('d'=daily, 'w'=weekly). The all-time total number of streaks and the all-time streak average (streak legths / total number of streaks) can be displayed. I also introduced the term **Streak Performance Score** which is calculated by the ratio of longest streak vs. total number of streaks of a given period. Essentially, the number will be high if you have kept a habit for a very long time and had only very little attempts. The highest achievable value for a daily habit in a leap year would be 366 as the total number of streaks will be one and the longest streak equals 366 (366 / 1 = 366). The lowest achievable score would be (1 / 183 =) 0.0055 by dropping the habit every second day. Streak performance score can be computed for all-time, for a specific month, or for the entire year in monthly increments to see tendencies and compare. Only the recorded date ('YYYY-MM-DD') is taken into analysis, the recorded time ('HH:MM:SS') is only displayed for information purposes.

The second part of the analytics platform allows the user to immediately know what habits need to be recorded today. Based on the current timestamp, the application will calculate what habits have been recorded today ("Congratulations...."), which habits must be recorded by the end of the day/week to keep current streak, and for which habits a new streak can only be started. Based on the "current streak analysis" inspirational and motivationaö messages to the user will be triggered. If a user keeps to a daily habit for 3 month the following message is printed to the screen: **'MIND-BOGGLING!!!!! Three Full Month OF Keeping This Habit Makes It A Routine. Do You Feel The Increase In Life Quality?! --> GOLD'**

# How to Install and run the Project
test





# How to Use the Project
test

# Include Credits
to the community stackoverflow and others

# Include Tests
test.py
