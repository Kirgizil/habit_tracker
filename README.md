# Backend Habit Tracker Application
This is my very first piece of code specifically generated for upload to github due to mandatory university classes - and there it is ;)

This exercise taught me how to implement functional and object orientated programming paradigms into a modern application backend with python. I AM proud of what I have developed within 3-4 weeks over X-mas 2021, but of course I am sure this is not the most efficient and performant code available on this topic. For the more advanced students this might even be an insult on how python code should be looking like, and I apologize deeply for this insult... Anyway, I hope at least my tutor will see the upsides on my efforts, and I will appreciate feedback from anyone to help me produce better code in the future.

# Project Description
The goal of this backend application is to ingest **USER** class, **HABIT** class, and **RECORD** class attributes by manual input. User input is sent to sqlite3 database file in which a table is provided for every class. Tables are linked via foreign key by an one-to-many (1:N) relationship (USER->HABIT->RECORD). One user can create multiple habits, and any habit is linked to exactly one user. One habit can be linked to multiple records, and any record is linked to exactly one habit. The application is designed to run outside IDLE by just executing in windows via "double click". A console will be presented to the user asking for input decisions, but also providing options for exiting prematurely. Upon starting the application, a user can be newly created and registered to the database. Existing users must initially login by their registration credentials (username and password). Usernames must be unique and at least 4 characters long. After successful login, the user is presented with several options to choose from:

**1) Registration, editing, or deleting habits:** habit names must be non-empty and unique, habit description is optional, habit periodicity must be 'd'=daily or 'w'=weekly, timestamp is generated automatically upon registration or editing. Username and password are case-sensitive.

**2) Registration, editing, or deleting of records:** a record's only attribute (except for the foreign key: habit id) is a timestamp taken either automatically or manually, in case of editing a record or doing a recording retrospectively. In the latter case you must provide a timestamp in the following ISO format: date='YYYY-MM-DD' and time='HH:MM:SS'. Records can only be edited or deleted for 14 days preceding the date of login.

**3) Reporting on existing data:** the user may print a list of all currently tracked habits, their all-time longest streaks (time passed without dropping a habit in days or weeks) and filtered by periodicity ('d'=daily, 'w'=weekly). The all-time total number of streaks and the all-time streak average (streak lengths / total number of streaks) can be displayed. I also introduced the term **Streak Performance Score** which is calculated by the ratio of longest streak vs. total number of streaks of a given period. Essentially, the number will be high if you have kept a habit for a very long time and had only very little attempts. The highest achievable value for a daily habit in a leap year would be 366 as the total number of streaks will be one and the longest streak equals 366 (366 / 1 = 366). The lowest achievable score would be (1 / 183 =) 0.0055 by dropping the habit every second day. Streak performance score can be computed for all-time, for a specific month, or for the entire year in monthly increments to see tendencies and compare. Only the recorded date ('YYYY-MM-DD') is taken into analysis, the recorded time ('HH:MM:SS') is only displayed for information purposes.

The second part of the analytics platform allows the user to immediately know what habits need to be recorded today. Based on the current timestamp, the application will calculate what habits have been recorded today ("Congratulations...."), which habits must be recorded by the end of the day/week to keep current streak, and for which habits a new streak can only be started. Based on the "current streak analysis" inspirational and motivational messages to the user will be triggered. If a user keeps to a daily habit for 3 month the following message is printed to the screen: **'MIND-BOGGLING!!!!! Three Full Month OF Keeping This Habit Makes It A Routine. Do You Feel The Increase In Life Quality?! --> GOLD'**

# How to Install and run the Project
**The appication comes with the following files:**
1. **habit_tracker.py** (main application)
2. **db_modul.py** (contains calls to the sqlite3 database)
3. **oop_modul.py** (contains all classes used within the application)
4. **productive.db** (sqlite3 database file containing one test user (Username='Timo', Password='test') and associated random example data for 5 daily and 5 weekly habits for the entire year 2021)
5. **test.py** (the most crucial parts of the application are tested here, see below of how to use this file)

**The following standard libraries are used by the project:**
1. import **sys** (Python Runtime Services)
2. import **os** (Generic Operating System Services)
3. import **re** (Text Processing Services)
4. import **random** (Generate pseudo-random numbers)
5. import **getpass** (Portable password input)
6. import **sqlite3** (DB-API 2.0 interface for SQLite databases)
7. from **datetime** import **datetime** (Basic date and time types)
8. from **operator** import **itemgetter** (Standard operators as functions)
9. from **random** import **randrange** (Generate pseudo-random numbers)

Since those are all standard libraries a healthy python 3.x installation should be able to run this code. I recommend downloading the folder 'habit_tracker' and saving this folder to a specific location. Then create a shortcut of 'habit_tracker.py' on our desktop to run the application via double clicking the shortcut. The application will be clear about the inputs needed to proceed.

# Testing
In case you want to further develop the code or want to make sure that the crucial parts of the application are running accurate, I put together a 'test.py' file which specifically looks at the following analytics functions:

1. **month_day_func:** This function is used to calculate current streak data of all habits and to only allow record logging (retrospective), editing, and deleting for a specified period.
2. **week_analytics:** This function is important for calculating the longest streak, the average streak, the total number of streaks, and the streak performance score of all weekly habits. Leap years are taken into account.
3. **calc_func_day:** This function is important to correctly calculate the length of the latest daily streak and when to check off next to keep current daily streak. Also, triggered motivational phrases up on check off are based on the result of this function.
4. **cal_func_week:** This function is important to correctly calculate the length of the latest weekly streak and when to check off next to keep current weekly streak. Also, triggered motivational phrases up on check off are based on the result of this function.
5. **daily_analytics:** This function produces data for longest daily streak, average daily streak, total number of started daily streaks, and daily streak performance score analysis.
6. **weekly_analytics:** This function produces data for longest weekly streak, average weekly streak, total number of weekly daily streaks, and weekly streak performance score analysis.
7. **weekly_analytics_from_db:** the same as weekly_analytics with the only difference that example data is directly taken from the database instead of providing them in the test.py file itself

Having said that I found it more efficient and intuitive to provide "mock data" inside 'test.py' (instead of using the random example data in productive.db), because you can make up your own scenarios and test whether the correct result is produced: Are leap years correctly implemented? Ist the sorting of data during today's status update analysis correctly executed? Are the key data longest streak, average streak, total number of streaks, and streak performance score correctly calculated?

Inside 'test.py' all possible manual entries are clearly marked and explained of what to expect. To run 'test.py' I recommend using your favorite IDLE, but you can also run command line.













