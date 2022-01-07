# -*- coding: utf-8 -*-
"""
Created on Sat Dec 18 18:34:02 2021

@author: eichner
"""

##supporting moduls
import db_modul as dbm
import sys
import os
import re
import random
import getpass

from oop_modul import user, habit, record, color
from datetime import datetime
from operator import itemgetter
from random import randrange


dic_motivation = {
    
    'If you want to achieve greatness stop asking for permission (Anonymous)',
    'Things work out best for those who make the best of how things work out'
    ' (John Wooden)',
    'To live a creative life, we must lose our fear of being wrong '
    '(Anonymous)',
    'If you are not willing to risk the usual you will have to settle for the'
    ' ordinary (Jim Rohn)',
    'Trust because you are willing to accept the risk, not because it\'s safe'
    ' or certain (Anonymous)',
    'Take up one idea. Make that one idea your life--think of it, dream of it'
    ', live on that idea. Let the brain, muscles, nerves, every part of your'
    ' body, be full of that idea, and just leave every other idea alone. This'
    ' is the way to success (Swami Vivekananda)',
    'All our dreams can come true if we have the courage to pursue them (Walt'
    ' Disney)',
    'Good things come to people who wait, but better things come to those who'
    ' go out and get them (Anonymous)',
    'If you do what you always did, you will get what you always got '
    '(Anonymous)',
    'Success is walking from failure to failure with no loss of enthusiasm '
    '(Winston Churchill)',
    'Just when the caterpillar thought the world was ending, he turned into'
    ' a butterfly (Proverb)'
    'Successful entrepreneurs are givers and not takers of positive energy '
    '(Anonymous)',
    'Whenever you see a successful person you only see the public glories, '
    'never the private sacrifices to reach them (Vaibhav)',
    'Opportunities don\'t happen, you create them (Chris Grosser)',
    'Try not to become a person of success, but rather try to become a person'
    'of value (Albert Einstein)',
    'Great minds discuss ideas; average minds discuss events; small minds '
    'discuss people (Eleanor Roosevelt)',
    'I have not failed. I\'ve just found 10,000 ways that won\'t work '
    '(Thomas A. Edison)',
    'If you don\'t value your time, neither will others. Stop giving away '
    'your time and talents--start charging for it (Kim Garst)',
    'A successful man is one who can lay a firm foundation with the bricks '
    'others have thrown at him (David Brinkley)',
    'No one can make you feel inferior without your consent '
    '(Eleanor Roosevelt)',
    'The whole secret of a successful life is to find out what is one\'s '
    'destiny to do, and then do it (Henry Ford)',
    'If you\'re going through hell keep going (Winston Churchill)',
    'The ones who are crazy enough to think they can change the world, are '
    'the ones who do (Anonymous)',
    'Don\'t raise your voice, improve your argument (Anonymous)',
    'What seems to us as bitter trials are often blessings in disguise '
    '(Oscar Wilde)',
    'The meaning of life is to find your gift. The purpose of life is to give'
    'it away (Anonymous)',
    'The distance between insanity and genius is measured only by success '
    '(Bruce Feirstein)',
    'When you stop chasing the wrong things, you give the right things a '
    'chance to catch you (Lolly Daskal)',
    'Don\'t be afraid to give up the good to go for the great (John D. '
    'Rockefeller)',
    'No masterpiece was ever created by a lazy artist (Anonymous)',
    'Happiness is a butterfly, which when pursued, is always beyond your '
    'grasp, but which, if you will sit down quietly, may alight upon you '
    '(Nathaniel Hawthorne)',
    'If you can\'t explain it simply, you don\'t understand it well enough '
    '(Albert Einstein)',
    'Blessed are those who can give without remembering and take without '
    'forgetting (Anonymous)',
    'Do one thing every day that scares you (Anonymous)',
    'What\'s the point of being alive if you don\'t at least try to do '
    'something remarkable (Anonymous)',
    'Life is not about finding yourself. Life is about creating yourself '
    '(Lolly Daskal)',
    'Nothing in the world is more common than unsuccessful people with talent'
    ' (Anonymous)',
    'Knowledge is being aware of what you can do. Wisdom is knowing when not '
    'to do it (Anonymous)',
    'Your problem isn\'t the problem. Your reaction is the problem '
    '(Anonymous)',
    'You can do anything, but not everything (Anonymous)',
    'Innovation distinguishes between a leader and a follower (Steve Jobs)',
    'There are two types of people who will tell you that you cannot make a '
    'difference in this world: those who are afraid to try and those who are '
    'afraid you will succeed. ‘ --Ray Goforth 43.  ‘Thinking should become '
    'your capital asset, no matter whatever ups and downs you come across in '
    'your life (A.P.J. Abdul Kalam)',
    'I find that the harder I work, the more luck I seem to have (Thomas '
    'Jefferson)',
    'The starting point of all achievement is desire (Napoleon Hill)',
    'Success is the sum of small efforts, repeated day-in and day-out (Robert'
    'Collier)',
    'If you want to achieve excellence, you can get there today. As of this '
    'second, quit doing less-thanexcellent work (Thomas J. Watson)',
    'All progress takes place outside the comfort zone (Michael John Bobak)',
    'You may only succeed if you desire succeeding; you may only fail if you '
    'do not mind failing (Philippos)',
    'Courage is resistance to fear, mastery of fear--not absense of fear '
    '(Mark Twain)',
    'Only put off until tomorrow what you are willing to die having left '
    'undone (Pablo Picasso)',
    'People often say that motivation doesn\'t last. Well, neither does '
    'bathing--that\'s why we recommend it daily (Zig Ziglar)',
    'We become what we think about most of the time, and that\'s the '
    'strangest secret (Earl Nightingale)',
    'The only place where success comes before work is in the dictionary '
    '(Vidal Sassoon)',
    'The best reason to start an organization is to make meaning; to create '
    'a product or service to make the world a better place (Guy Kawasaki)',
    'I find that when you have a real interest in life and a curious life, '
    'that sleep is not the most important thing (Martha Stewart)',
    'It\'s not what you look at that matters, it\'s what you see (Anonymous)',
    'The road to success and the road to failure are almost exactly the same '
    '(Colin R. Davis)',
    'The function of leadership is to produce more leaders, not more followers'
    ' (Ralph Nader)',
    'Success is liking yourself, liking what you do, and liking how you do it'
    ' (Maya Angelou)',
    'As we look ahead into the next century, leaders will be those who empower'
    ' others (Bill Gates)',
    'A real entrepreneur is somebody who has no safety net underneath them '
    '(Henry Kravis)',
    'The first step toward success is taken when you refuse to be a captive '
    'of the environment in which you first find yourself (Mark Caine)',
    'People who succeed have momentum. The more they succeed, the more they '
    'want to succeed, and the more they find a way to succeed. Similarly, '
    'when someone is failing, the tendency is to get on a downward spiral '
    'that can even become a self-fulfilling prophecy (Tony Robbins)',
    'When I dare to be powerful, to use my strength in the service of my '
    'vision, then it becomes less and less important whether I am afraid '
    '(Audre Lorde)',
    'Whenever you find yourself on the side of the majority, it is time to '
    'pause and reflect. ‘ --Mark Twain 67.  ‘The successful warrior is the '
    'average man, with laser-like focus. ‘ --Bruce Lee 68.  ‘Courage is '
    'resistance to fear, mastery of fear--not absence of fear (Mark Twain)',
    'Develop success from failures. Discouragement and failure are two of '
    'the surest stepping stones to success (Dale Carnegie)',
    'If you don\'t design your own life plan, chances are you\'ll fall into '
    'someone else\'s plan. And guess what they have planned for you? Not '
    'much (Jim Rohn)',
    'If you genuinely want something, don\'t wait for it--teach yourself to '
    'be impatient (Gurbaksh Chahal)',
    'Don\'t let the fear of losing be greater than the excitement of winning'
    ' (Robert Kiyosaki)',
    'If you want to make a permanent change, stop focusing on the size of '
    'your problems and start focusing on the size of you! (T. Harv Eker)',
    'You can\'t connect the dots looking forward; you can only connect them '
    'looking backwards. So you have to trust that the dots will somehow '
    'connect in your future. You have to trust in something--your gut, '
    'destiny, life, karma, whatever. This approach has never let me down, '
    'and it has made all the difference in my life (Steve Jobs)',
    'Successful people do what unsuccessful people are not willing to do. '
    'Don\'t wish it were easier, wish you were better (Jim Rohn)',
    'The number one reason people fail in life is because they listen to '
    'their friends, family, and neighbors (Napoleon Hill)',
    'The reason most people never reach their goals is that they don\'t '
    'define them, or ever seriously consider them as believable or achievable.'
    ' Winners can tell you where they are going, what they plan to do along '
    'the way, and who will be sharing the adventure with them (Denis Waitley)',
    'In my experience, there is only one motivation, and that is desire. No '
    'reasons or principle contain it or stand against it (Jane Smiley)',
    'Success does not consist in never making mistakes but in never making '
    'the same one a second time (George Bernard Shaw)',
    'I don\'t want to get to the end of my life and find that I lived just '
    'the length of it. I want to have lived the width of it as well '
    '(Diane Ackerman)',
    'You must expect great things of yourself before you can do them '
    '(Michael Jordan)',
    'Motivation is what gets you started. Habit is what keeps you going '
    '(Jim Ryun)',
    'People rarely succeed unless they have fun in what they are doing '
    '(Dale Carnegie)',
    'There is no chance, no destiny, no fate, that can hinder or control the '
    'firm resolve of a determined soul (Ella Wheeler Wilcox)',
    'Our greatest fear should not be of failure but of succeeding at things '
    'in life that don\'t really matter (Francis Chan)',
    'You\'ve got to get up every morning with determination if you\'re going '
    'to go to bed with satisfaction (George Lorimer)',
    'To be successful you must accept all challenges that come your way. You '
    'can\'t just accept the ones you like (Mike Gafka)',
    'Success is ... knowing your purpose in life, growing to reach your '
    'maximum potential, and sowing seeds that benefit others '
    '(John C. Maxwell)',
    'Be miserable. Or motivate yourself. Whatever has to be done, it\'s '
    'always your choice (Wayne Dyer)',
    'To accomplish great things, we must not only act, but also dream, not '
    'only plan, but also believe. ‘ -Anatole France 91.  ‘Most of the '
    'important things in the world have been accomplished by people who have '
    'kept on trying when there seemed to be no help at all (Dale Carnegie)',
    'You measure the size of the accomplishment by the obstacles you had to '
    'overcome to reach your goals (Booker T. Washington)',
    'Real difficulties can be overcome; it is only the imaginary ones that '
    'are unconquerable (Theodore N. Vail)',
    'It is better to fail in originality than to succeed in imitation '
    '(Herman Melville)',
    'Fortune sides with him who dares (Virgil)',
    'Little minds are tamed and subdued by misfortune; but great minds rise '
    'above it (Washington Irving)',
    'Failure is the condiment that gives success its flavor (Truman Capote)',
    'Don\'t let what you cannot do interfere with what you can do '
    '(John R. Wooden)',
    'You may have to fight a battle more than once to win it '
    '(Margaret Thatcher)',
    'A man can be as great as he wants to be. If you believe in yourself and '
    'have the courage, the determination, the dedication, the competitive '
    'drive and if you are willing to sacrifice the little things in life and '
    'pay the price for the things that are worthwhile, it can be done '
    '(Vince Lombardi)', 

    }


dic_daily_badges = {
    
    2 : ('Way To Go!! You Can Do It!!'),
    6 : ('Keep Going! One More Day To Obtain Your First Badge'),
    7 : ('This Is Getting Pretty AWESOME!! You Just Completed One Full Week '
         '--> PEARL'),
    13 : ('Keep Going! One More Day To Obtain Your Next Badge'),
    14 : ('FANTASTIC!! The Next Higher Badge Is Yours. You Really Deserve '
          'This --> JADE'),
    29 : ('Way To Go!! One More Day To Obtain Your Next Badge'),
    30 : ('WOW!! A Full Month Of Not Failing Once. Congratulations, The Next '
          'Higher Badge is Yours --> RUBY'),
    59 : ('Keep Going! One More Day To Obtain Your Next Badge'),
    60 : ('You Are Absolutely AMAZING!! You Just Completed Two Full Month. '
          'Be Proud Of Yourself!! --> SAPPHIRE'),
    90 : ('MIND-BOGGLING!!!!! Three Full Month OF Keeping This Habit Makes '
          'It A Routine. Do You Feel The Increase In Life Quality?! --> GOLD'),
    183 : ('NOTHING CAN STOP YOU NOW!! This Habit Became Second Nature To You '
           '--> DIAMOND'),
    365 : ('YOU ARE A HERO!! NEVER SEEN ANYTHING LIKE IT! ENJOY BEING A STAR'
           ' --> PLATINUM'),

    }


dic_weekly_badges = {
    
    2 : ('Way To Go!! You Can Do It!!'),
    3 : ('Keep Going! One More Week To Obtain Your First Badge'),
    4 : ('This Is Getting Pretty AWESOME!! You Just Completed One Full Month '
         '--> PEARL'),
    8 : ('Keep Going! One More Week To Obtain Your Next Badge'),
    9 : ('FANTASTIC!! The Next Higher Badge Is Yours. You Really Deserve '
          'This --> JADE'),
    12 : ('Way To Go!! One More Week To Obtain Your Next Badge'),
    13 : ('WOW!! Three Full Month Of Not Failing Once. Congratulations, The '
          'Next Higher Badge is Yours --> RUBY'),
    25 : ('Keep Going! One More Week To Obtain Your Next Badge'),
    26 : ('You Are Absolutely AMAZING!! You Just Completed half A Year. '
          'Be Proud Of Yourself!! --> SAPPHIRE'),
    52 : ('MIND-BOGGLING!!!!! A Full Year OF Keeping This Habit Makes '
          'It A Routine. Do You Feel The Increase In Life Quality?! --> GOLD'),
    104 : ('NOTHING CAN STOP YOU NOW!! This Habit Became Second Nature To You '
           '--> DIAMOND'),
    208 : ('YOU ARE A HERO!! NEVER SEEN ANYTHING LIKE IT! ENJOY BEING A STAR'
           ' --> PLATINUM'),
    
    }


list_noleap = ['01-31', '02-28', '03-31', '04-30', '05-31', '06-30', '07-31',
               '08-31', '09-30', '10-31', '11-30', '12-31']


list_leap = ['01-31', '02-29', '03-31', '04-30', '05-31', '06-30', '07-31',
              '08-31', '09-30', '10-31', '11-30', '12-31'] 


dic_period = {
    
    'd' : 'daily',
    'w' : 'weekly',
    
    }


dic_num_to_month = {
    
    '01': 'January',
    '02': 'February',
    '03': 'March',
    '04': 'April',
    '05': 'May',
    '06': 'June',
    '07': 'July',
    '08': 'August',
    '09': 'September',
    '10': 'October',
    '11': 'November',
    '12': 'December',
    
    }

dic_options = {

    '1': 'Add/Edit/Delete A Habit',
    '2': 'Add/Edit/Delete A Record',
    '3': 'Analytics Toolbox',
    '4': 'Check Today\'s Status',

    }


dic_habits = {

    '1': 'Add A New Habit',
    '2': 'Edit An Existing Habit',
    '3': 'Delete An Existing Habit',

    }


dic_records = {

    '1': 'Add A New Record',
    '2': 'Edit Or Delete An Existing Record',

    }


dic_analytics = {

    '1': 'See All Currently Tracked Habits',
    '2': 'See All Currently Tracked Habits With The Same Periodicity',
    '3': 'See All-Time Longest Habit Streaks',
    '4': 'See All-Time Longest Streak Of Specific Habit',
    '5': 'See All-Time Habit Streak Average',
    '6': 'See All-Time Total Number Of Started Habit Streaks',
    '7': 'See All-Time Streak Performance Scores',
    '8': 'See Monthly Streak Performance Scores',
    '9': 'See Monthly Streak Performance Scores For One Year'

    }


def current_streak_calc_sorting_func(data, timestamp, d_today, d_current,
                                     d_other, w_current, w_today, w_other, 
                                     w_soon):
    '''
    Takes as input the current timestamp, a list of tuples containing habit 
    and record attributes of one habit (tuple[0]=(habit name, 
    habid periodicity) and tuple[1:]= (record date, record time, habid id)), 
    and a range of lists in which data will be sorted depending on habit 
    status (checked today, must be checked today/this week (soon) to keep 
    current streak, no current streak available (other)).
    
    Parameters
    ----------
    data : list of tuples
        Containing record timestamps, as well as name, periodicity and id for
        one habit. tuple[0]=(habit name, habid periodicity), tuple[1:]= 
        (record date, record time, habid id).
    timestamp : str
        Current timestamp automatically assigend during login using the ISO 
        format 'YYYY-MM-DD HH:MM:SS'.
    d_today : list of lists
        Containing daily habit name, last recorded timestamp, longest habit 
        streak and its unit (day/s). Habits have been recorded today.
    d_current : list of lists
        Containing daily habit name, last recorded timestamp, longest habit 
        streak and its unit (day/s). Habits must be recorded today to 
        keep current streak.
    d_other : list of lists
        Containing daily habit name, last recorded timestamp, longest habit 
        streak and its unit (day/s). Habits w/o current streak.
    w_current : list of lists
        Containing weekly habit name, last recorded timestamp, longest habit 
        streak and its unit (week/s). Habits must be recorded today to keep 
        current streak.
    w_today : list of lists
        Containing weekly habit name, last recorded timestamp, longest habit 
        streak and its unit (week/s). Habits have been recorded today.
    w_other : list of lists
        Containing weekly habit name, last recorded timestamp, longest habit 
        streak and its unit (week/s). Habits w/o current streak.
    w_soon : list of lists
        Containing weekly habit name, last recorded timestamp, longest habit 
        streak and its unit (week/s). Habits must be recorded soon (< 7 days)
        to keep current streak.

    Returns
    -------
    d_today : list of lists
        Containing daily habit name, last recorded timestamp, longest habit 
        streak and its unit (day/s). Habits have been recorded today.
    d_current : list of lists
        Containing daily habit name, last recorded timestamp, longest habit 
        streak and its unit (day/s). Habits must be recorded today to 
        keep current streak.
    d_other : list of lists
        Containing daily habit name, last recorded timestamp, longest habit 
        streak and its unit (day/s). Habits w/o current streak.
    w_current : list of lists
        Containing weekly habit name, last recorded timestamp, longest habit 
        streak and its unit (week/s). Habits must be recorded today to keep 
        current streak.
    w_today : list of lists
        Containing weekly habit name, last recorded timestamp, longest habit 
        streak and its unit (week/s). Habits have been recorded today.
    w_other : list of lists
        Containing weekly habit name, last recorded timestamp, longest habit 
        streak and its unit (week/s). Habits w/o current streak.
    w_soon : list of lists
        Containing weekly habit name, last recorded timestamp, longest habit 
        streak and its unit (week/s). Habits must be recorded soon (< 7 days)
        to keep current streak.

    '''
    ## Get rid of dublicates and the first item in record list (habit name, 
    ## periodicity) and sort obtained list by date descending
    temp_list = list(set(data[1:]))
    
    temp_list.sort(key=itemgetter(0), reverse=True)
    
    ## Calculate current streak for all daily habits which contain records
    if data[0][1] == 'd' and temp_list:

        days = [timestamp.split(' ')[0]]

        ## generate a list of dates until reaching the date of the first 
        ## habit record
        while not list(set([temp_list[-1][0]]) & set(days)):

            days.extend(daily_countdown_func(days[-1], 1))
        
        records = [i[0] for i in temp_list]
        
        if records[0] == days[0]:
            
            d_streak = 1
            
            ## look for the first discrepancy of zipped lists --> habit break
            for a, b in zip(records[1:], days[1:]):

                if a == b:
    
                    d_streak += 1
    
                else:
                    break
        
        else:
        
            d_streak = 0
        
            for a, b in zip(records, days[1:]):
    
                if a == b:
    
                    d_streak += 1
    
                else:
                    break

        if d_streak > 1:

            unit = 'days'

        else:

            unit = 'day'
        
        ## sorting the data into appropriate list for reporting
        if records[0] == days[0]:
            
            d_today = display_analytics_func(
                
                d_today,
                data, 
                temp_list, 
                current_streak=d_streak, 
                unit=unit
                
                )
            
        elif records[0] == days[1]:
            
            d_current = display_analytics_func(
                
                d_current,
                data, 
                temp_list, 
                current_streak=d_streak, 
                unit=unit
                
                )
            
        else:

            d_other = display_analytics_func(
                
                d_other,
                data, 
                temp_list, 
                
                )
    
    ## Calculate current streak for all weekly habits which contain records
    elif data[0][1] == 'w' and temp_list:
      
        records = [i[0] for i in temp_list]                                     ## dates only list
        
        week = [timestamp.split(' ')[0]]                                        ## starting with the current timestamp

        ## does the current timestap overlap with record date list?
        if list(set(week) & set(records)):
            
            benchmark = list(set(week) & set(records))                          ## benchmark = overlap list --> current timestamp
            
            w_streak = 0                                                        ## 0 weeks assigned
            
            week = daily_countdown_func(benchmark[-1], 7)                       ## new week list, based on current timestamp

        else:
            
            w_streak = -1                                                       ## start with -1 weeks
            
            week = daily_countdown_func(timestamp.split(' ')[0], 7)
            
            if records[0] in week:                                              ## cut the generated week at the current timestamp(!)
                                                                                ## this is tricky: but it is important to generate weeks 
                week = week[:week.index(records[0]) + 1]                        ## with the correct frameshift based on the last record.

        while list(set(week) & set(records)):                                   ## overlap: generated week vs. record date list

            seven_days_gap = seven_days_upwards_func(                           ## calculating 7 days up from recognized set of records
                
                list(set(week) & set(records))[0][5:], 
                list(set(week) & set(records))[0][:4], 
                list(set(week) & set(records))[0][5:7],
                list(set(week) & set(records))[0][8:]
                
                )

            if (list(set(seven_days_gap) & set(records)) or                     ## make sure that record spacing is <7 days
                week[-1] == records[0]):                                        ## >7 days jumps are not allowed for a streak
                
                benchmark = [week[-1]]                                          ## last value in generated week --> benchmark
                
                w_streak += 1                                                   ## + 1 week due to overlap found
                
                week = daily_countdown_func(benchmark[-1], 7)                   ## generate new week based on benchmark

            else:
                break

        if w_streak == 1:

            unit = 'week'

        else:

            unit = 'weeks'

        ## sorting the data into appropriate list for reporting
        if records[0] == timestamp.split(' ')[0]:
            
            w_today = display_analytics_func(
                
                w_today,
                data, 
                temp_list, 
                current_streak=w_streak, 
                unit=unit,
                
                )
            
        ## this habit has to be checked off today to keep current streak
        elif records[0] == daily_countdown_func(
                
                timestamp.split(' ')[0], 
                7
                
                )[-1]:
            
            w_current = display_analytics_func(
                
                w_current,
                data, 
                temp_list, 
                current_streak=w_streak, 
                unit=unit,
                
                )

        ## this habit must be checked off soon or within this week (<6 days) 
        ## to keep current streak                                    
        elif records[0] in daily_countdown_func(
                
                timestamp.split(' ')[0], 
                7
                
                )[:-1]:
            
            w_soon = display_analytics_func(
                
                w_soon,
                data, 
                temp_list, 
                current_streak=w_streak, 
                unit=unit,
                
                )
        
        ## this habit has been broken and a streak must be reestablished
        else:

            w_other = display_analytics_func(
                
                w_other,
                data, 
                temp_list, 
                
                )
    
    return d_today, d_current, d_other, w_today, w_current, w_other, w_soon


def display_analytics_func(display_list, data, temp_list, current_streak=None, 
                           unit=None):
    '''
    This function generates a list of key parameter per habit used in the 
    function current_streak_calc_sorting_func --> habit name, last recorded 
    timestamp, current streak, streak unit.
    
    Parameters
    ----------
    display_list : list
        Contains habit name, last recorded timestamp, current streak, 
        streak unit per habit.
    data : list of tuples
        Containing record timestamps, as well as name, periodicity and id for
        one habit. tuple[0]=(habit name, habid periodicity), tuple[1:]= 
        (record date, record time, habid id).
    temp_list : list of lists
        Sorted (descending) list of all timestamps recorded per habit.
    current_streak : int, optional
        Current habit streak. The default is None.
    unit : str, optional
        Unit of current habit streak (day/s, week/s). The default is None.

    Returns
    -------
    display_list : list
        Contains habit name, last recorded timestamp, current streak, 
        streak unit per habit. To be printed to the screen.

    '''
    display_list.append(
                        
        [
            
            color.BOLD + color.UNDERLINE + data[0][0] + color.END,              ## habid name
            temp_list[0][0],                                                    ## last recorded date
            temp_list[0][1],                                                    ## last recorded time
            current_streak,                                                     ## current streak
            unit,                                                               ## streak unit
            
            ]
        
        )
    
    return display_list


def daily_countdown_func(timestamp, number):
    '''
    Produces a list of descending dates in daily increments from current 
    timestamp. The latter is excluded. Length of the list is user-defined. 
    Leap years are taken into account.

    Parameters
    ----------
    timestamp : str
        Current timestamp (date format 'YYYY-MM-DD' is also accepted) assigned 
        during login 'YYYY-MM-DD HH:MM:SS'. 
    number : int
        Defines the number of dates generated.

    Returns
    -------
    increment : list
        A list of descending dates 'YYYY-MM-DD' with a daily increment 
        starting one day after the current timestamp.

    '''
    ## define day, month and year from where to count back daily
    day = timestamp.split(' ')[0].split('-')[2]
    month = timestamp.split(' ')[0].split('-')[1]
    year = timestamp.split(' ')[0].split('-')[0]

    ## differentiate between normal and leap years
    dic_month_to_day = {
        
        '02' : ('31', '31'),
        '03' : ('28', '29'),                                                    ## leap year
        '04' : ('31', '31'),
        '05' : ('30', '30'),
        '06' : ('31', '31'),
        '07' : ('30', '30'),
        '08' : ('31', '31'),
        '09' : ('31', '31'),
        '10' : ('30', '30'),
        '11' : ('31', '31'),
        '12' : ('30', '30'),
        
        }
    
    increment = []
    
    for i in range(number):
        
        ## general day transition. no month/year transition
        if day != '01':
            
            day = str(int(day) - 1).zfill(2)                                    ## day - 1
            
            increment.append(
                
                year + '-' + month + '-' + day
                
                )
        
        ## month transistion. no leap yeat
        elif day == '01' and month != '01' and int(year)%4 != 0:
            
            day = dic_month_to_day[month][0]                                    ## day starts according to no leap
            month = str(int(month) - 1).zfill(2)                                ## month - 1

            increment.append(
                
                year + '-' + month + '-' + day
                
                )
        
        ## month transition. leap year
        elif (day == '01' and month != '01' and int(year)%4 == 0 and            ## leap year
              year[2:] != '00'):
            
            day = dic_month_to_day[month][1]                                    ## day starts according to leap year
            month = str(int(month) - 1).zfill(2)                                ## month - 1
            
            increment.append(
                
                year + '-' + month + '-' + day
                
                )

        ## month transition. no leap year
        elif (day == '01' and month != '01' and int(year)%400 == 0 and 
              year[2:] == '00'):
            
            day = dic_month_to_day[month][0]                                    ## day starts according to no leap
            month = str(int(month) - 1).zfill(2)                                ## month - 1
            
            increment.append(
                
                year + '-' + month + '-' + day
                
                )

        ## year transition    
        elif day == '01' and month == '01':
            
            day = '31'                                                          ## day starts at '31'
            month = '12'                                                        ## month starts at '12'
            year = str(int(year) - 1).zfill(4)                                  ## year - 1
            
            increment.append(
                
                year + '-' + month + '-' + day
                
                )

    return increment


def weekly_streak_calc_func(data, length, option):
    '''
    Calculates the length of a weekly streak per habit for all recorded data.

    Parameters
    ----------
    data : list of tuples
        Containing record timestamps, as well as name, periodicity and id for
        one habit. tuple[0]=(habit name, habid periodicity), tuple[1:]= 
        (record date, record time, habid id)
    length : int
        This is the longest habit name of all currently tracked habits. Used 
        to format the screen print.
    option : str
        Decision between calculating and printing to the screen the longest 
        streak, the streak average, the total number of streaks, or the streak
        performance ratio per habit.

    Returns
    -------
    test_value : list of lists
        Returns key data values for unittesting.
    
    w_months : list of lists
        Returns streak performance score values per habit for aggregated table
        view.

    '''
    test_value = []                                                             ## unittesting
    
    w_months, streaks = [], []

    ## Select the date from timestamp, get rid of duplicates and the first 
    ## item in record list (habit name, periodicity), and sort obtained 
    ## list by date ascending
    temp_list = list(set([i[0] for i in data[1:]]))
    temp_list.sort()

    ## no data available
    if data[0][1] == 'w' and not temp_list:
        pass

    ## only weekly habits for which recorded data is available
    elif data[0][1] == 'w' and temp_list:
    
        streak, prev = 0, []
        
        month_day = temp_list[0][5:]
        year = temp_list[0].split('-')[0]
        month = temp_list[0].split('-')[1]
        day = temp_list[0].split('-')[2]
        
        benchmark = temp_list[0]                                                ## to break habits in case of > 7 days record increments
        del temp_list[0]                                                        ## delete first item in list
        
        week = seven_days_upwards_func(                                         ## generate 7 days (1 week) based on first tuple in list
            
            month_day,
            year,
            month,
            day
            
            )
        
        ## until all items in list are deleted
        while len(temp_list) > 0:
    
            ## next item has been found in generated week
            ## "week" will be declared "previous" week to avoid duplicate 
            ## assigments for the same week
            if list(set([temp_list[0]]) & set(week)):
                
                seven_days_gap = daily_countdown_func(                          ## calculating 7 days down from recognized set of records
                    
                    list(set(week) & set([temp_list[0]]))[0],
                    7
                    
                    )

                if (list(set(seven_days_gap) & set([benchmark])) or             ## make sure that record spacing is <7 days
                    week[-1] == temp_list[0][0]):                               ## >7 days jumps are not allowed for a streak

                    benchmark = temp_list[0]                                    ## to break habits in case of > 7 days record increments
                    del temp_list[0]                                            ## delete first item in list
                    
                    prev = week                                                 ## week --> previous week
                    streak += 1
                    
                    month_day = week[-1][5:]
                    year = week[-1].split('-')[0]
                    month = week[-1].split('-')[1]
                    day = week[-1].split('-')[2]
                    
                    week = seven_days_upwards_func(                             ## next week
                        
                        month_day, 
                        year, 
                        month, 
                        day
                        
                        )
                
                else:
    
                    month_day = temp_list[0][5:]
                    year = temp_list[0].split('-')[0]
                    month = temp_list[0].split('-')[1]
                    day = temp_list[0].split('-')[2]
                    
                    benchmark = temp_list[0]                                    ## to break habits in case of > 7 days record increments
                    del temp_list[0]                                            ## delete first item in list
            
                    week = seven_days_upwards_func(                             ## next week
                        
                        month_day, 
                        year, 
                        month, 
                        day
                        
                        )
                    
                    streaks.append(streak)                                      ## collection of streaks
 
                    streak = 0                                                  ## break of habit
   
            ## next item has been found in "previous" week
            ## do not add += 1 to streak
            elif list(set([temp_list[0]]) & set(prev)):
                
                benchmark = temp_list[0]                                        ## to break habits in case of > 7 days record increments
                del temp_list[0]                                                ## delete first item in list
                
            ## next item has not been found in next week --> break in habit
            ## streak is set back to 1
            else:
    
                month_day = temp_list[0][5:]
                year = temp_list[0].split('-')[0]
                month = temp_list[0].split('-')[1]
                day = temp_list[0].split('-')[2]
                
                benchmark = temp_list[0]
                del temp_list[0]                                                ## delete first item in list
        
                week = seven_days_upwards_func(                                 ## next week
                    
                    month_day, 
                    year, 
                    month, 
                    day
                    
                    )
                
                streaks.append(streak)                                          ## collection of streaks

                streak = 0                                                      ## break of habit

        streaks.append(streak)                                                  ## completing collection of streaks
        
    ## in case of no records being available --> output will be zero
    if not streaks and data[0][1] == 'w':

        if option == 'max':
        
            print(
                
                ' {} --> {:3} weeks'
                .format(data[0][0].ljust(length), 0)
                    
                )

        elif option == 'ave':
        
            print(
                
                ' {} --> {:5} weeks'
                .format(data[0][0].ljust(length), 0.0)
                    
                )
        
        elif option == 'num':

            print(
                    
                    ' {} --> {:3} streaks'
                    .format(data[0][0].ljust(length), 0)
                        
                    )

        elif option == 'ratio':
            print(
                    
                ' {} --> {:5}'
                .format(data[0][0].ljust(length), 0.0)
                    
                )

        elif option == 'year':
            
            w_months.append(0.0)

    ## longest streak per habit is printed to the screen
    elif option == 'max' and data[0][1] == 'w':

        if max(streaks) > 1 or max(streaks) == 0:
            print(
                
                ' {} --> {:3} weeks'
                .format(data[0][0].ljust(length), max(streaks))
                
                )
        else:
            print(
                
                ' {} --> {:3} week'
                .format(data[0][0].ljust(length), max(streaks))
                
                )
            
        test_value.append(max(streaks))                                         ## for unittesting
            
    ## average streak per habit is printed to the screen
    elif option == 'ave' and data[0][1] == 'w':
        
        print(
            
            ' {} --> {:5} weeks'.format(
                
                data[0][0].ljust(length), 
                round(sum(streaks)/len(streaks), 1)
                
                )
              
              )
        
        test_value.append(round(sum(streaks)/len(streaks), 1))                  ## for unittesting
    
    ## total number of streaks per habit is printed to the screen
    elif option == 'num' and data[0][1] == 'w':
        
        print(
            
            ' {} --> {:3} streaks'.format(
                
                data[0][0].ljust(length), 
                len(streaks)
                
                )
              
              )
        
        test_value.append(len(streaks))                                         ## for unittesting
    
    ## streak performance score
    elif option == 'ratio' and data[0][1] == 'w':
        
        print(
            
            ' {} --> {:5}'.format(
                
                data[0][0].ljust(length), 
                round((max(streaks)/len(streaks)), 1)
                
                )
              
              )
        
        test_value.append(round(max(streaks)/len(streaks), 2))                  ## for unittesting
    
    ## aggregated streak performance score for table view
    elif option == 'year' and data[0][1] == 'w':
        
        w_months.append(round((max(streaks)/len(streaks)), 1))                  ## list for aggregated table view
    
    return test_value, w_months


def daily_streak_calc_func(data, length, option):
    '''
    Calculates streak length per daily habit for all recorded data starting 
    from the first day of recording the data.

    Parameters
    ----------
    data : list of tuples
        Containing record timestamps, as well as name, periodicity and id for
        one habit. tuple[0]=(habit name, habid periodicity), tuple[1:]= 
        (record date, record time, habid id).
    length : int
        This is the longest habit name of all currently tracked habits. Used 
        to format the screen print.
    option : str
        Decision between calculating and printing to the screen the longest 
        streak, the streak average, the total number of streaks, or the streak
        performance ratio per habit.

    Returns
    -------
    test_value : list of lists
        Returns key data values for unittesting.
    
    d_months : list of lists
        Returns streak performance score values per habit for aggregated table
        view.

    '''
    test_value = []                                                             ## unittesting
    
    d_months = []
    
    ## Select the date from timestamp, get rid of duplicates and the first 
    ## item in record list (habit name, periodicity), and sort obtained 
    ## list by date ascending
    temp_list = list(set([i[0] for i in data[1:]]))
    temp_list.sort()
    
    ## no data available
    if data[0][1] == 'd' and not temp_list:
        pass
    
    ## only daily habits with available data
    if data[0][1] == 'd' and temp_list:
        
        streak, streaks = 1, []
        
        benchmark = temp_list[0]                                                ## starting date
    
        for date in temp_list[1:]:

            ## yearly transition
            if (
                    
                    int(date.split('-')[0]) ==
                    int(benchmark.split('-')[0]) + 1 and
                    date[5:] == '01-01' and
                    benchmark[5:] == '12-31'
                    
                    ):
     
                streak += 1
                benchmark = date
    
            ## no leap month transition
            elif (
                    
                    int(date.split('-')[2]) == 1 and 
                    benchmark[5:] in list_noleap and
                    int(date[:4])%4 != 0
                    
                    ):
                
                streak += 1
                benchmark = date
    
            ## leap month transition
            elif (
                    
                    int(date.split('-')[2]) == 1 and 
                    benchmark[5:] in list_noleap and
                    int(date[:4])%4 == 0 and
                    date[2:4] != '00'
                    
                    ):
                
                streak += 1
                benchmark = date
            
            ## no leap month transition
            elif (
                    
                    int(date.split('-')[2]) == 1 and 
                    benchmark[5:] in list_noleap and
                    int(date[:4])%400 == 0 and
                    date[2:4] == '00'
                    
                    ):
                
                streak += 1
                benchmark = date
            
            ## general daily transition
            elif (
                    
                    int(date.split('-')[2]) ==
                    int(benchmark.split('-')[2]) + 1
                    
                    ):
    
                streak += 1
                benchmark = date
            
            ## break of habit
            else:
    
                streaks.append(streak)                                          ## list of streaks per period
                streak = 1
                benchmark = date
        
        streaks.append(streak)                                                  ## completing list of streaks
        
        ## longest streak per habit is printed to the screen
        if not streaks:
            
            if option == 'max':
                
                print(
                    
                    ' {} --> {:3} days'
                    .format(data[0][0].ljust(length), 0)
                      
                      )
                
            elif option =='ave':
                
                print(
                    
                    ' {} --> {:5} days'
                    .format(data[0][0].ljust(length), 0.0)
                      
                      )
                
            elif option =='num':
                
                print(
                    
                    ' {} --> {:3} days'
                    .format(data[0][0].ljust(length), 0)
                      
                      )
                
            elif option =='ratio':
                
                print(
                    
                    ' {} --> {:5} days'
                    .format(data[0][0].ljust(length), 0.0)
                      
                      )
                
            elif option =='year':
                
                d_months.append(0.0)
        
        ## longest streak per habit is printed to the screen
        elif option == 'max':
        
            if max(streaks) > 1 or max(streaks) == 0:
                print(
                    
                    ' {} --> {:3} days'
                    .format(data[0][0].ljust(length), max(streaks))
                      
                      )
            else:
                print(
                    
                    ' {} --> {:3} day'
                    .format(data[0][0].ljust(length), max(streaks))
                    
                    )
            
            test_value.append(max(streaks))                                     ## for unittesting
        
        ## average streak per habit is printed to the screen
        elif option == 'ave' and streaks:
            
            print(
                
                ' {} --> {:5} days'
                .format(
                    
                    data[0][0].ljust(length), 
                    round(sum(streaks)/len(streaks),1)
                    
                    )

                 )
            
            test_value.append(round(sum(streaks)/len(streaks),1))               ## for unittesting
        
        ## total number of streaks per habit is printed to the screen
        elif option == 'num':
            
            print(
                
                ' {} --> {:3} streaks'
                .format(
                    
                    data[0][0].ljust(length),
                    len(streaks)
                    
                    )
                  
                )
            
            test_value.append(len(streaks))                                     ## for unittesting
        
        ## streak performance score
        elif option == 'ratio':
            
            print(
                
                ' {} --> {:5}'
                .format(
                    
                    data[0][0].ljust(length),
                    round((max(streaks)/len(streaks)), 1)
                    
                    )
                
                )
            
            test_value.append(round((max(streaks)/len(streaks)), 2))            ## for unittesting
        
        ## aggregated streak performance score for table view
        elif option == 'year':
            
            d_months.append(round((max(streaks)/len(streaks)), 1))              ## for aggregated table view

    return test_value, d_months


def seven_days_upwards_func(month_day, year, month, day):
    '''
    Generates a list of seven dates 'YYYY-MM-DD' in daily increments (1 week) 
    ascending. Leap years are taken into account. Provided starting date is 
    excluded.

    Parameters
    ----------
    month_day : str
        'MM-DD' string based on the starting date which is excluded from the 
        resulting list.
    year : str
        'YYYY' string based on the starting date which is excluded from the 
        resulting list.
    month : str
        'MM' string based on the starting date which is excluded from the 
        resulting list.
    day : str
        'DD' string based on the starting date which is excluded from the 
        resulting list.

    Returns
    -------
    week : list
        List of ascending dates ('YYYY-MM-DD') in daily increments starting 
        one day after the provided date.

    '''
    week = []
    for z in range(7):

        ## not end of the month --> day + 1 (no leap year)
        if (month_day not in list_noleap and
            int(year)%4 != 0):
            
            day = str(int(day) + 1).zfill(2)                                    ## day + 1
            month_day = month + '-' + day
            
            week.append(
                
                year + '-' + month + '-' + day
                
                )
        
        ## not end of the month --> day + 1 (leap year)
        elif (month_day not in list_leap and
              int(year)%4 == 0 and
              year[2:] != '00'):
            
            day = str(int(day) + 1).zfill(2)                                    ## day + 1
            month_day = month + '-' + day
            
            week.append(
                
                year + '-' + month + '-' + day
                
                )
        
        ## not end of the month --> day + 1 (no leap year)
        elif (month_day not in list_noleap and
              int(year)%400 == 0 and
              year[2:] == '00'):
            
            day = str(int(day) + 1).zfill(2)                                    ## day + 1
            month_day = month + '-' + day
            
            week.append(
                
                year + '-' + month + '-' + day
                
                )
        ## month/year transition
        else:
            
            ## month transition
            if month != '12':
                
                day = '01'                                                      ## start new month with day == '01'
                month = str(int(month) + 1).zfill(2)                            ## month + 1
                month_day = month + '-' + day
                
                week.append(
                    
                    year + '-' + month + '-' + day
                
                )

            ## year transition
            else:

                day = '01'                                                      ## start new month with day == '01'
                month = '01'                                                    ## start new year with month == '01'
                year = str(int(year) + 1).zfill(4)                              ## year + 1
                month_day = month + '-' + day

                week.append(
                    
                    year + '-' + month + '-' + day
                
                )
                
    return week


def example_record_data(db_name, db_record_table, habit_id, p):
    '''
    Generates test record data for the year 2021 ('2021-MM-DD HH:MM:SS'). For 
    admin use only.

    Parameters
    ----------
    db_name : str
        Defines database name in which record data should be written.
    db_record_table : str
        Defines table name in which record data should be written.
    habit_id : int
        Defines habit id for which record data should be written.
    p : float
        Probability to generate a record per day. Reasonable values for weekly 
        habits are between 0.05-0.25. Reasonable values for daily habits are 
        between 0.75-0.95.

    Returns
    -------
    None.

    '''
    dataset = []
    for i in range(1, 13):
        if i in [1, 3, 5, 7, 8, 10, 12]:
            for j in range(1, 32):
                if (random.random() < p) == True:
                    dataset.append(('2021-{:2}-{:2} {:2}:{:2}:{:2}'.format(
                        
                        str(i).zfill(2),
                        str(j).zfill(2),
                        str(randrange(25)).zfill(2),
                        str(randrange(60)).zfill(2),
                        str(randrange(60)).zfill(2),
                        
                        ), habit_id))

        elif i in [2]:
            for j in range(1, 29):
                if (random.random() < p) == True:
                    dataset.append(('2021-{:2}-{:2} {:2}:{:2}:{:2}'.format(
                        
                        str(i).zfill(2),
                        str(j).zfill(2),
                        str(randrange(25)).zfill(2),
                        str(randrange(60)).zfill(2),
                        str(randrange(60)).zfill(2),
                        
                        ), habit_id))
        else:
            for j in range(1, 31):
                if (random.random() < p) == True:
                    dataset.append(('2021-{:2}-{:2} {:2}:{:2}:{:2}'.format(
                        
                        str(i).zfill(2), 
                        str(j).zfill(2),
                        str(randrange(25)).zfill(2),
                        str(randrange(60)).zfill(2),
                        str(randrange(60)).zfill(2),
                        
                        ), habit_id))
    
    for i in dataset:
        dbm.db_record_insert(db_name, db_record_table, i)        


def example_habit_data(db_name, db_habit_table):
    '''
    Generates test habit data of 10 predefined habits - 5 daily and 5 weekly 
    habits. Habit attributes (name, description, periodicity, time stamp, and 
    user id) are predefined. For admin use only.

    Parameters
    ----------
    db_name : str
        Defines database name in which habit data should be written.
    db_habit_table : str
        Defines table name in which habit data should be written.

    Returns
    -------
    None.

    '''
    habit_names = [
        
        'Daily Yoga Session',
        'Weekly Jogging Distance (>20K)',
        'Drinking 1L Water Every Day',
        'Cleaning The House Every Week',
        'Going To Bed Early',
        'Reflection On The Working Week',
        'Complimenting My Wife',
        'Going To The Gym',
        'Using Dental Floss',
        'Calling My Parents',
        
        ]

    habit_description = [
        
        'Test Data',
        'Test Data',
        'Test Data',
        'Test Data',
        'Test Data', 
        'Test Data',
        'Test Data',
        'Test Data',
        'Test Data',
        'Test Data',
        
        ]

    habit_periodicity = [
        
        'd',
        'w',
        'd',
        'w',
        'd',
        'w',
        'd',
        'w',
        'd',
        'w',
        
        ]
    
    time_stamp = [
        
        '2021-01-01 00:00:00',
        '2021-01-01 00:00:00',
        '2021-01-01 00:00:00',
        '2021-01-01 00:00:00',
        '2021-01-01 00:00:00',
        '2021-01-01 00:00:00',
        '2021-01-01 00:00:00',
        '2021-01-01 00:00:00',
        '2021-01-01 00:00:00',
        '2021-01-01 00:00:00',
        
        ]
    
    user_id = [
        
        '1',
        '1',
        '1',
        '1',
        '1',
        '1',
        '1',
        '1',
        '1',
        '1',
        
        ]

    for i in zip(
            
            habit_names,
            habit_description,
            habit_periodicity, 
            time_stamp, 
            user_id
            
            ):
        
        dbm.db_habit_insert(db_name, db_habit_table, i)


def decision_process(name):
    '''
    Streamlining nested navigation for the first two decision points of the 
    application.

    Parameters
    ----------
    name : dic
        Dictionary of options to choose from for the different functionalities 
        of the application.

    Returns
    -------
    decision : str
        Recognition string to trigger desired functionality of the application.

    '''
    print(
        
        '\n\n You Want To...\n'
        
        )

    for i in name:

        print('{:4}'.format(int(i)), '-->',  name[i])

    print(
        
        'x'.rjust(4), '-->', 'Exit'
        
        )
    
    decision = input(
        
        '\n Please Choose Appropriate Index From the Menu Above --> '
        
        )

    screen_clear()

    if decision == 'x':

        input(
            
            '\n\n Press <Enter> To Exit...'
            
            )

        sys.exit()

    ## handle invalid input
    while decision not in [i for i in name]:

        print(
        
        '\n\n You Presented The Systen With Invalid Input...\n'
        
        )

        for i in name:
    
            print('{:4}'.format(int(i)), '-->',  name[i])
    
        print(
            
            'x'.rjust(4), '-->', 'Exit'
            
            )
        
        decision = input(
            
            '\n Please Try Again And Choose Appropriate Left Index From the Menu Above: '
            
            )
    
        screen_clear()
        
        if decision == 'x':

            input(
                
                '\n\n Press <Enter> To Exit...'
                
                )

            sys.exit()

    return decision


def program_exit():
    '''
    Printing the confirmation to the screen that nothing has been deleted by
    exiting prematurely.

    Returns
    -------
    None.

    '''
    screen_clear()

    print(
        
        '\n\n Record Has Not Been Deleted'
        
        )

    input(
        
        '\n\n Press <Enter> To Exit...'
        
        )

    sys.exit()


def screen_clear():
    '''
    Clears the print screen for better user experience. Distinguishes between 
    different operating systems.

    Returns
    -------
    None.

    '''
    ## for mac and linux(here, os.name is 'posix')
    if os.name == 'posix':
      _ = os.system('clear')

    else:
      ## for windows platfrom
      _ = os.system('cls')


def habit_registration(dic_period, db_name, db_habit_table, user_id, text=''):
    '''
    Facilitates interactive registration and editing of habit data.

    Parameters
    ----------
    period : dic
        Habit attribute PERIODICITY ('d'=daily, 'w'=weekly).
    db_name : str
        Defines database name in which habit data should be written.
    db_habit_table : str
        Defines table name in which habit data should be written.
    user_id : int
        Habit attribute USER_ID.
    text : str, optional
        Habit attribute DESCRIPTION. The default is ''.

    Returns
    -------
    habit_name : str
        Habit attribute NAME (non-empty, unique).
    habit_description : str
        Habit attribute DESCRIPTION.
    habit_periodicity : str
        Habit attribute PERIODICITY ('d'=daily, 'w'=weekly).

    '''
    habit_name = input(
        
        "\n\n Name Of The {}Habit OR Exit (x): --> ".format(text)
        
        )

    screen_clear()

    if habit_name == 'x':

        input(
            
            '\n\n Press <Enter> To Exit...'
            
            )

        sys.exit()     
    
    habit_lookup = dbm.db_habit_select(
        
        db_name,
        db_habit_table,
        display='record',
        user_id=user_id,
        
        )[2]

    habit_name = unique_func(
        
        habit_lookup,
        db_name,
        db_habit_table,
        habit_name,
        'Habit',
        
        )

    ## handle invalid (empty string) input
    while not habit_name:

        print(
            
            '\n\n Habit Name Can\'t Be Empty'
            
            )

        habit_name = input(
            
            '\n\n Try Again Or Exit (x): --> '
            
            )

        screen_clear()

        if habit_name == 'x':
            input(
                
                '\n\n Press <Enter> To Exit...'
                
                )

            sys.exit()

    habit_description = input(
        
        '\n\n Description Of The {}Habit: --> '.format(text)
        
        )

    screen_clear()

    ## transfrom empty string '' to 'none'
    if not habit_description:

        habit_description = 'none'

    habit_periodicity = input(
        
        '\n\n Periodicity Of The {}Habit (d=daily, w=weekly) Or Exit (x): --> '
        .format(text)
        
        )

    screen_clear()

    if habit_periodicity == 'x':

        input(
            
            '\n\n Press <Enter> To Exit...'
            
            )

        sys.exit()
    
    ## handle invalid input
    while habit_periodicity not in dic_period.keys():
 
        print(
            
            '\n\n For Periodicity Only \'d\' (daily) Or \'w\' (weekly) Is '
            'Allowed\n'
            
            )

        habit_periodicity = input(
            
            '\n\n Try Again Or Exit (x): --> '
            
            )

        screen_clear()

        if habit_periodicity == 'x':

            input(
                
                '\n\n Press <Enter> To Exit...'
                
                )

            sys.exit()

    return habit_name, habit_description, habit_periodicity


def unique_func(lookup, db_name, db_table, name, domain):
    '''
    Streamlining functionality to only allow unique user- and habit names in 
    the database.

    Parameters
    ----------
    lookup : dic
        Dictionary of currently registered habits {habit_name : habit_id}.
    db_name : str
        Defines database name in which data should be written.
    db_table : str
        Defines table name in which data should be written.
    name : str
        Defines the name with which the data should be written into the 
        database. The name will be compared to what is already registered.
    domain : str
        Defines the domain ('Username', 'Habit') in which the data should be 
        written into the database for printing to the screen.

    Returns
    -------
    name : str
        Unique user- or habit name provided by user input.

    '''
    ## stay in this loop while the name provided by the user is already 
    ## registered to the database
    while name in lookup.keys():

        print(
            
            '\n\n The {} \'{}\' Already Exists!'.format(
                
                domain,
                color.UNDERLINE + color.BOLD + name + color.END,
                
                )
            )

        name = input(
            
            '\n\n Please Try A Different Name OR Exit (x): --> '
            
            )

        screen_clear()

        if name == 'x':

            input(
                
                '\n\n Press <Enter> To Exit...'
                
                )

            sys.exit()
    
    return name


def main():
    '''
    Main function of the application. When started the application will ask 
    for user credentials prior further registration, editing, and deleting 
    functionalities (habits, records) and analytics.

    Returns
    -------
    None.

    '''
    ## Initiation of database tables (for admin only)
#    dbm.db_user_table_creation("productive.db","user_table")
#    dbm.db_habit_table_creation("productive.db","habit_table", "user_table")
#    dbm.db_record_table_creation("productive.db", "record_table", "habit_table")


    ## global variable time stamp and allowed input formats (regex)
    time_stamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    date_format = ('^[1-2][0-9][0-9][0-9]-(0[1-9]|1[0-2])-'
                   '(0[1-9]|1[0-9]|2[0-9]|3[0-1])$')
    time_format = ('^(0[0-9]|1[0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9]$')
    year_month_format = ('^[1-2][0-9][0-9][0-9]-(0[1-9]|1[0-2])$')
    year_format = ('^[1-2][0-9][0-9][0-9]$')

    ## database name and tables
    db_name = 'productive.db'
    db_user_table = 'user_table'
    db_habit_table = 'habit_table'
    db_record_table = 'record_table'

    ## Writing example data into the database for testing the application 
    ##(for admin only)
#    example_habit_data(db_name, db_habit_table)
    ## weekly data
#    example_record_data(db_name, db_record_table, 10, 0.25)
    ## daily data
#    example_record_data(db_name, db_record_table, 9, 0.95)
#    sys.exit()

    ## Drop Tables for admin only
#    dbm.table_delete(db_name, db_habit_table)
#    dbm.db_user_select_test(db_name, db_user_table)
#    dbm.db_habit_select_test(db_name, db_habit_table)
#    sys.exit()

    ## User Management
    login = input(
        
        '\n\n Enter Username Or New Registration (new) --> '
        
        )
    
    screen_clear()

    ## Generation of new user credentials
    if login == 'new':

        print(
            
            '\n\n Please Provide Username (At Least 4 Characters)'
            ' Or Exit (x):'
            
            )
        
        username = input(
            
            '\n\n Username: --> '
            
            )

        screen_clear()

        if username == 'x':

            input(
                
                '\n\n Press <Enter> To Exit...'
                
                )

            sys.exit()
        
        ## 4 characters are mandatory
        while len(username) < 4:
            
            print(
                
                '\n\n Please Provide At Least 4 Characters Or Exit (x):'
            
            )
            
            username = input(
            
            '\n\n Username: --> '
            
            )

            screen_clear()
            
            if username == 'x':

                input(
                    
                    '\n\n Press <Enter> To Exit...'
                    
                    )
    
                sys.exit()
        
        
        password_lookup = dbm.db_user_select_login(
            
            db_name,
            db_user_table,
            
            )[0]

        unique_func(
            
            password_lookup,
            db_name,
            db_user_table,
            username,
            'Username',
            
            )

        print(
            
            '\n\n Please Provide Password (At Least 4 Characters) Or Exit (x):'
            
            )
        
        password = getpass.getpass(
            
            '\n\n Password: --> '
            
            )

        screen_clear()
        
        if password == 'x':

            input(
                
                '\n\n Press <Enter> To Exit...'
                
                )

            sys.exit()

        ## 4 characters are mandatory
        while len(password) < 4:
            
            print(
                
                '\n\n Please Provide At Least 4 Characters Or Exit (x):'
            
            )
            
            password = getpass.getpass(
            
            '\n\n Password: --> '
            
            )

            screen_clear()
            
            if password == 'x':

                input(
                    
                    '\n\n Press <Enter> To Exit...'
                    
                    )
    
                sys.exit()
        
        repeat = getpass.getpass(
            
            '\n\n\n\n Repeat Password: --> '
            
            )

        screen_clear()

        ## Matching password and repeat prior registration
        if password != repeat:

            print(
                
                '\n\n Password Input Does Not Match. Please contact the '
                'administrator for help.'
                
                )

            input(
                
                '\n\n Press <Enter> To Exit...'
                
                )

            sys.exit()

        else:

            new_user = user(
                
                username,
                password,
                time_stamp,
                
                )

            dataset = (
                
                new_user.name,
                new_user.password,
                new_user.time_stamp,
                
                )
            
            
            dbm.db_user_insert(
                
                db_name,
                db_user_table,
                dataset,
                
                )

            print(
                
                '\n\n New User Has Been Registered To The Database:\n'
                
                )

            dbm.db_user_select(
                
                db_name,
                db_user_table,
                
                )

            input(
                
                '\n Press <Enter> To Exit...'
                
                )

            sys.exit()

    ## User credentials are available
    else:

        username = login
        
        screen_clear()
    
        password = getpass.getpass(
            
            '\n\n Password: --> '
            
            )
    
        screen_clear()
    
        (
            
            password_lookup,
            id_lookup,
            
            ) = dbm.db_user_select_login(
                
                db_name,
                db_user_table,
            
                )
        
        ## Exit application prematurely in case of wrong user credentials
        if username in password_lookup.keys():

            if password_lookup[username] == password:
    
                user_id = id_lookup[username]
                
                print(
                    
                    '\n\n Welcome Back {}!'.format(username)
                    
                    )
    
            else:
    
                print(
                    
                    '\n\n Password Does Not Match the Username'
                    
                    )
    
                input(
                    
                    '\n\n Press <Enter> To Exit...'
                    
                    )
    
                sys.exit()
    
        else:
    
            print(
                
                '\n\n Username Does Not Exist'
                
                )
    
            input(
                
                '\n\n Press <Enter> To Exit...'
                
                )
    
            sys.exit()

    ## Initial decision matrix to generate the tuple variable 'code'
    decision1 = decision_process(
        
        dic_options,
        
        )

    if decision1 == '1':

        decision2 = decision_process(
            
            dic_habits,
            
            )

    elif decision1 == '2':

        decision2 = decision_process(
            
            dic_records,
            
            )

    elif decision1 == '3':

        decision2 = decision_process(
            
            dic_analytics,
            
            )

    elif decision1 == '4':

        decision2 = '1'

    code = (int(decision1), int(decision2))                                     ## result of initial decision matrix

    ## Decision loop based on generated tuple variable 'code' from above
    if code == (1, 1):
        ## Add a new habit
        (
        
            habit_name,
            habit_description,
            habit_periodicity,
            
            ) = habit_registration(
                
                dic_period,
                db_name,
                db_habit_table,
                user_id,
                text='New ',
                
                )

        new_habit = habit(
            
            habit_name,
            habit_description,
            habit_periodicity,
            time_stamp,
            user_id,
            
            )

        dataset = (
            
            new_habit.name,
            new_habit.description,
            new_habit.periodicity,
            new_habit.time_stamp,
            new_habit.user_id,
            
            )

        dbm.db_habit_insert(
            
            db_name,
            db_habit_table,
            dataset,
            
            )

        print(
            
            '\n\n New Habit Has Been Registered To The Database:\n'
            
            )

        dbm.db_habit_select(
            
            db_name,
            db_habit_table,
            select='limit_1',
            
            )

        input(
            
            '\n Press <Enter> To Exit...'
            
            )

        sys.exit()

    elif code == (1, 2):
        ## Edit existing habit
        
        print('\n\n')
        
        habit_ids = dbm.db_habit_select(
            
            db_name,
            db_habit_table,
            display='habit_name',
            user_id=user_id,
            
            )[1]

        if not habit_ids:

            print(
                
                '\n\n No Habit Data Available'
                
                )

            input(
                
                '\n\n Press <Enter> To Exit...'
                
                )

            sys.exit()

        else:

            print(
                
                'x'.rjust(4), '-->', 'Exit'
                
                )

        habit_id = input(
            
            '\n\n Please Provide Index Of The Habit You Want To Edit: '
            
            )

        screen_clear()

        if habit_id == 'x':

            input(
                
                '\n\n Press <Enter> To Exit...'
                
                )

            sys.exit()

        ## handle invalid input
        while habit_id not in [str(i) for i in habit_ids]:

            print('\n\n')
            
            habit_ids = dbm.db_habit_select(
                
                db_name,
                db_habit_table,
                display='habit_name',
                user_id=user_id,
                
                )[1]

            print(
                
                'x'.rjust(4), '-->', 'Exit'
                
                )

            habit_id = input(
                
                '\n\n Please Try Again And Choose Appropriate Left Index From '
                'the Menu Above Or Exit (x): --> '
                
                )

            screen_clear()
            
            if habit_id == 'x':

                input(
                    
                    '\n\n Press <Enter> To Exit...'
                    
                    )

                sys.exit()

        (
            
            habit_name,
            habit_description,
            habit_periodicity,
            
            ) = habit_registration(
                
                dic_period,
                db_name,
                db_habit_table,
                user_id,
                
                )

        ## updating database attributes with collected user values
        attributes = ['NAME', 'DESCRIPTION', 'PERIODICITY', 'TIME_STAMP']
        values = [habit_name, habit_description, habit_periodicity, time_stamp]

        for i, j in zip(attributes, values):
            
            dbm.db_habit_update(
                
                db_name,
                db_habit_table,
                i,
                j,
                habit_id,
                
                )

        print(
            
            '\n\n Habit Details Have Been Changed To...\n'
            
            )

        dbm.db_habit_select(
            
            db_name,
            db_habit_table,
            habit_id=habit_id,
            select='habit_id',
            
            )
        
        input(
            
            '\n Press <Enter> To Exit...'
            
            )

    elif code == (1, 3):
        ## Delete existing habit
        
        print('\n\n')
        
        (
            
            habit_name,
            habit_ids,
            habit_id_lookup,
            
            ) = dbm.db_habit_select(
                
                db_name,
                db_habit_table,
                display='habit_name',
                user_id=user_id,
                
                )

        if not habit_name:

            print(
                
                '\n\n No Habit Data Available'
                
                )

            input(
                
                '\n\n Press <Enter> To Exit...'
                
                )

            sys.exit()

        else:

            print(
                
                'x'.rjust(4), '-->', 'Exit'
                
                )

        habit_id = input(
            
            '\n\n Please Provide Index Of The Habit You Want To Delete: '
            
            )

        screen_clear()

        if habit_id == 'x':

                input(
                    
                    '\n\n Press <Enter> To Exit...'
                    
                    )

                sys.exit()
        
        ## handle invalid input
        while habit_id not in [str(i) for i in habit_ids]:

            habit_ids = dbm.db_habit_select(
                
                db_name,
                db_habit_table,
                display='habit_name',
                user_id=user_id,
                
                )[1]

            print(
                
                'x'.rjust(4), '-->', 'Exit'
                
                )

            habit_id = input(
                
                '\n\n Please Try Again And Choose Appropriate Left Index From '
                'the Menu Above Or Exit (x): --> '
                
                )

            screen_clear()

            if habit_id == 'x':

                input(
                    
                    '\n\n Press <Enter> To Exit...'
                    
                    )

                sys.exit()

        if habit_id == 'x':

            input(
                
                '\n\nPress <Enter> To Exit...'
                
                )

            program_exit()

        elif habit_id:

            print(
                
                '\n\n Are You Sure You Want To {} \'{}\' (y) OR Exit (x)?\n'
                .format(
                    
                    color.RED + "DELETE" + color.END,
                    habit_name,
                    
                    )
                
                )

            habit_name = dbm.db_habit_select(
                
                db_name,
                db_habit_table,
                habit_id=habit_id,
                select='habit_id',
                                
                )[0]
            
            delete = input('\n--> ')
            
            screen_clear()

            if delete == 'y':

                print('\n')
                
                dbm.db_habit_delete(
                    
                    db_name,
                    db_habit_table,
                    habit_id,
                    
                    )

                input(
                    
                    '\n Press <Enter> To Exit...'
                    
                    )

                sys.exit()
                
            else:

                program_exit()

    elif code == (2, 1):
        ## Add new record
        
        print('\n\n')
        
        (
            
            habit_name,
            habit_ids,
            habit_id_lookup,
            
            ) = dbm.db_habit_select(
                
                db_name,
                db_habit_table,
                display='habit_name',
                user_id=user_id,
                
                )

        if not habit_name:

            print(
                
                '\n\n No Habit Data Available'
                
                )

            input(
                
                '\n\n Press Enter To Exit'
                
                )

            sys.exit()

        else:

            print(
                
                'x'.rjust(4), '-->', 'Exit\n'
                
                )
    
        habit_id = input(
            
            ' Please Provide Index Of The Habit You Want To Record: --> '
            
            )

        screen_clear()

        if habit_id == 'x':

            input(
                
                '\n\n Press <Enter> To Exit...'
                
                )

            sys.exit()

        ## handle invalid input
        while habit_id not in [str(i) for i in habit_ids]:

            print('\n\n')
            
            habit_ids = dbm.db_habit_select(
                
                db_name,
                db_habit_table,
                display='habit_name',
                user_id=user_id,
                
                )[1]

            print('x'.rjust(4), '-->', 'Exit')

            habit_id = input(
                
                '\n Please Try Again And Choose Appropriate Left Index From '
                'the Menu Above Or Exit (x): --> '
                
                )

            screen_clear()
            
            if habit_id == 'x':

                input(
                    
                    '\n\n Press <Enter> To Exit...'
                    
                    )

                sys.exit()

        if habit_id == 'x':

            input(
                
                '\n\n Press <Enter> To Exit...'
                
                )

            program_exit()

        elif habit_id:

            retrospective = input(
                
                '\n\n Do You Want To Record Now (<Enter>) Or Retrospectively '
                '(r) Or Exit (x) --> '
                
                )

            screen_clear()
            
            if retrospective == 'x':

                input(
                    
                    '\n\n Press <Enter> To Exit...'
                    
                    )

                sys.exit()
            
            ## handle invalid input
            while retrospective not in ['', 'r']:

                retrospective = input(
                
                '\n\n Press <Enter> To Record Current Date And Time, \'r\' '
                'To Record Retrospectively OR Exit (x) '
                '--> '
                
                )
                
                screen_clear()
                
                if retrospective == 'x':
                    
                    input(
                        
                        '\n\n Press <Enter> To Exit...'
                        
                        )
                    
                    sys.exit()
            
            if retrospective == 'r':

                date = input(
                    
                    '\n\n Please Provide DATE in ISO Format (YYYY-MM-DD): --> '
                    
                    )

                screen_clear()
                
                ## handle invalid input (timestamp format)
                while not re.search(date_format, date):

                    date = input(
                        
                        '\n\n The DATE Must Follow ISO Format (YYYY-MM-DD). '
                        'Try Again Or Exit (x): --> '
                        
                        )

                    screen_clear()

                    if date == 'x':

                        input(
                            
                            '\n\n Press <Enter> To Exit...'
                            
                            )

                        sys.exit()

                ## Generate a 2 weeks (14 days) list of dates descending in 
                ## daily increments (w/o current date)
                fourteen_day_increment = daily_countdown_func(time_stamp, 14)
                
                ## add current date to the list
                fourteen_day_increment.insert(0, time_stamp.split(' ')[0])
                
                ## handle invalid input (last fourteen days plus today)
                while not list(set([date]) & set(fourteen_day_increment)):

                    date = input(
                        
                        '\n\n The DATE Must Be Today OR Within The Last 14 '
                        'Days. Try Again Or Exit (x): --> '
                        
                        )

                    screen_clear()

                    if date == 'x':

                        input(
                            
                            '\n\n Press <Enter> To Exit...'
                            
                            )

                        sys.exit()

                time = input(
                    
                    '\n\n Please Provide TIME in ISO Format (HH:MM:SS): --> '
                    
                    )

                screen_clear()
                
                ## handle invalid input (timestamp format)
                while not re.search(time_format, time):

                    time = input(
                        
                        '\n\n The TIME Must Follow ISO Format (HH:MM:SS). '
                        'Try Again Or Exit (x): --> '
                        
                        )

                    screen_clear()

                    if time == 'x':

                        input(
                            
                            '\n\n Press <Enter> To Exit...'
                            
                            )

                        sys.exit()
                
                time_stamp = date + ' ' + time

            new_record = record(
                
                time_stamp,
                habit_id,
                
                )

            dataset = (
                
                new_record.time_stamp,
                new_record.habit_id,
                
                )

            dbm.db_record_insert(
                
                db_name,
                db_record_table,
                dataset,
                
                )

            print(
                
                '\n\n New Record Has Been Registered To The Database:\n'
                
                )

            print(
                
                '',
                dbm.db_habit_select(
                    
                    db_name,
                    db_habit_table,
                    select='habit_id',
                    display='limit_1',
                    habit_id=habit_id,
                    
                    )[0], 
                end=''
                
                )

            dbm.db_record_select(
                
                db_name,
                db_record_table,
                select='limit_1',
                display='limit_1',
                
                )

            ## Motivation feature: badge and general motivation phrases
            ## Find out about current streaks and trigger phrases accordingly
            
            (
            
            habit_name,
            habit_ids,
            habit_id_lookup,
            
            ) = dbm.db_habit_select(
                
                db_name,
                db_habit_table,
                select='habit_id',
                display='analytics',
                user_id=user_id,
                habit_id=habit_id,
                
                )
    
            masterlist = []
    
            for i,j in habit_id_lookup.items():
                
                (
                    
                    record_name,
                    record_ids,
                    
                    ) = dbm.db_record_select(
                    
                        db_name,
                        db_record_table,
                        select='habit_id',
                        display='analytics',
                        att_id=j,
                
                        )
    
                record_name.insert(0, i)
                
                masterlist.append(record_name)                                  ## masterlist = list of tuples:
                                                                                ## tuple[0]=(habit name, habid periodicity), 
            (                                                                   ## tuple[1:]= (record date, record time, habid id)
                
                d_today,
                d_current,
                d_other,
                w_current,
                w_today,
                w_other,
                w_soon,
                
                ) = [], [], [], [], [], [], []
        
            ## Calculate current streak data
            for i in masterlist:
                
                (
                    d_today,
                    d_current,
                    d_other,
                    w_today,
                    w_current,
                    w_other,
                    w_soon,
                    
                    ) = current_streak_calc_sorting_func(
                        
                        i, 
                        time_stamp,
                        d_today, 
                        d_current, 
                        d_other, 
                        w_today,
                        w_current,
                        w_other, 
                        w_soon
                        
                        )
     
            ## print motivational phrases based on current streak data to 
            ## the screen
            for i in [
                    
                    d_current, 
                    d_other, 
                    d_today, 
                    w_current, 
                    w_other, 
                    w_today, 
                    w_soon
                    
                    ]:
                
                try:
                    
                    if len(i[0]) == 5:
                        
                        if i[0][4] == 'weeks':
                            
                            if i[0][3] in dic_weekly_badges.keys():
                                
                                print(
                                    
                                    '\n\n '+ color.BOLD +                                    
                                    '"' + dic_weekly_badges[i[0][3]] + '"' +
                                    color.END
                                    
                                    )
                            
                            else:
                                
                                print(
                                
                                    '\n\n '+ color.BOLD + 
                                    '"' + random.sample(dic_motivation, 1)[0] + 
                                    '"' + color.END
                                    
                                    )
                            
                        
                        elif i[0][4] == 'days':
                            
                            if i[0][3] in dic_daily_badges.keys():
                                
                                print(
                                    
                                    '\n\n '+ color.BOLD +                                    
                                    '"' + dic_daily_badges[i[0][3]] + '"' + 
                                    color.END
                                    
                                    )
                                
                            else:
                                
                                print(
                                
                                    '\n\n '+ color.BOLD + 
                                    '"' + random.sample(dic_motivation, 1)[0] + 
                                    '"' + color.END
                                    
                                    )
                        
                        else:
                            
                            print(
                                
                                '\n\n '+ color.BOLD + 
                                '"' + random.sample(dic_motivation, 1)[0] + 
                                '"' + color.END
                                
                                )
                            
                except:
                    pass

            input(
                
                '\n\n Press <Enter> To Exit...'
                
                )

            sys.exit()

    elif code == (2, 2):
        ## Correct existing record
        
        dates = [time_stamp.split(' ')[0]]
        dates.extend(daily_countdown_func(time_stamp, 14))
        dates = tuple(dates)

        print('\n\n')
        
        (
            
            habit_name,
            habit_ids,
            habit_id_lookup,
            
            ) = dbm.db_habit_select(
                
                db_name,
                db_habit_table,
                display='habit_name',
                user_id=user_id,
                
                )

        if not habit_name:

            print(
                
                '\n\n No Habit Data Available'
                
                )

            input(
                
                '\n\n Press <Enter> To Exit...'
                
                )

            sys.exit()

        else:
            print(
                
                'x'.rjust(4), '-->', 'Exit'
                
                )
    
        habit_id = input(
            
            '\n Please Provide Index Of The Habit You Want To Correct Or '
            'Delete A Record Of: '
            
            )

        screen_clear()

        ## handle invalid input
        while habit_id not in [str(i) for i in habit_ids]:

            print('\n\n')
            
            habit_ids = dbm.db_habit_select(
                
                db_name,
                db_habit_table,
                display='habit_name',
                user_id=user_id,
                
                )[1]

            print(
                
                'x'.rjust(4), '-->', 'Exit'
                
                )

            habit_id = input(
                
                '\n Please Try Again And Choose Appropriate Left Index From '
                'the Menu Above Or Exit (x): --> '
                
                )

            screen_clear()

            if habit_id == 'x':

                input(
                    
                    '\n\n Press <Enter> To Exit...'
                    
                    )

                sys.exit()

        if habit_id == 'x':

            input(
                
                '\n\n Press <Enter> To Exit...'
                
                )

            program_exit()

        elif habit_id:

            print('\n\n')
            
            print(
                
                dbm.db_habit_select(
                    
                    db_name,
                    db_habit_table,
                    select='habit_id',
                    display='record',
                    habit_id=habit_id,
                    
                    )[0] + ':\n'
                
                )

            record_ids = dbm.db_record_select(
                
                db_name,
                db_record_table,
                select='habit_id_lim14_date',
                att_id=habit_id,
                dates=dates
                
                )[1]

            if not record_ids:

                print(
                    
                    '\n\n No Record Data Available'
                    
                    )

                input(
                    
                    '\n\n Press <Enter> To Exit...'
                    
                    )

                sys.exit()

            else:

                print(
                    
                    'x'.rjust(4), '-->', 'Exit\n'
                    
                    )

            record_id = input(
                
                'Please Provide Index Of The Record Which Should Be Changed '
                'OR Deleted: '
                
                )

            screen_clear()

            if record_id == 'x':

                input(
                    
                    '\n\n Press <Enter> To Exit...'
                    
                    )

                sys.exit()

            ## handle invalid input
            while str(record_id) not in [str(i) for i in record_ids]:

                print('\n\n')
            
                print(
                    
                    dbm.db_habit_select(
                        
                        db_name,
                        db_habit_table,
                        select='habit_id',
                        display='record',
                        habit_id=habit_id,
                        
                        )[0] + ':\n'
                    
                    )
    
                record_ids = dbm.db_record_select(
                    
                    db_name,
                    db_record_table,
                    select='habit_id_lim14',
                    att_id=habit_id,
                    
                    )[1]

                print(
                    
                    'x'.rjust(4), '-->', 'Exit'
                    
                    )

                record_id = input(
                    
                    '\n Please Try Again And Choose Appropriate Left Index '
                    'From the Menu Above Or Exit (x): --> '
                    
                    )

                screen_clear()

                if record_id == 'x':

                    input(
                        
                        '\n\n Press <Enter> To Exit...'
                        
                        )

                    sys.exit()

            print(
                
                '\n\n Do You Want To Change (x) OR Delete (del) This Record?\n'
                
                )
            
            print(
                    
                    dbm.db_habit_select(
                        
                        db_name,
                        db_habit_table,
                        select='habit_id',
                        display='record',
                        habit_id=habit_id,
                        
                        )[0] + ':', end=''
                    
                    )
            
            dbm.db_record_select(
                
                db_name,
                db_record_table,
                select='record_id',
                att_id=record_id,
                
                )

            x_del = input(
                
                '\n --> '
                
                )

            screen_clear()

            ## editing a record
            if x_del == 'x':

                date = input(
                    
                    '\n\n Please Provide DATE In ISO Format (YYYY-MM-DD): --> '
                    
                    )

                screen_clear()

                while not re.search(date_format, date):

                    date = input(
                        
                        '\n\n The DATE Must Follow ISO Format (YYYY-MM-DD). '
                        'Try Again Or Exit (x): --> '
                        
                        )

                    screen_clear()

                    if date == 'x':

                        input(
                            
                            '\n\n Press <Enter> To Exit...'
                            
                            )

                        sys.exit()

                ## Generate a 2 weeks (14 days) list of dates descending in 
                ## daily increments (w/o current date) 
                fourteen_day_increment = daily_countdown_func(time_stamp, 14)

                ## add current date to the list
                fourteen_day_increment.insert(0, time_stamp.split(' ')[0])
                
                ## handle invalid input (last fourteen days plus today)
                while not list(set([date]) & set(fourteen_day_increment)):

                    date = input(
                        
                        '\n\n The DATE Must Be Today OR Within The Last 14 '
                        'Days. Try Again Or Exit (x): --> '
                        
                        )

                    screen_clear()

                    if date == 'x':

                        input(
                            
                            '\n\n Press <Enter> To Exit...'
                            
                            )

                        sys.exit()

                time = input(
                    
                    '\n\n Please Provide TIME In ISO Format (HH:MM:SS): --> '
                    
                    )

                screen_clear()

                ## handle invalid input (timestamp format)
                while not re.search(time_format, time):

                    time = input(
                        
                        '\n\n The TIME Must Follow ISO Format (HH:MM:SS). '
                        'Try Again Or Exit (x): --> '
                        
                        )

                    screen_clear()

                    if time == 'x':

                        input(
                            
                            '\n\n Press <Enter> To Exit...'
                            
                            )

                        sys.exit()
                
                time_stamp = date + ' ' + time

                print(
                    
                    '\n\n The Record Has Been Changed From...'
                    
                    )

                dbm.db_record_select(
                    
                    db_name,
                    db_record_table,
                    select='record_id',
                    att_id=record_id,
                    
                    )
                
                dbm.db_record_update(
                    
                    db_name,
                    db_record_table,
                    'TIME_STAMP',
                    time_stamp,
                    record_id,
                    
                    )
                
                print("\n To...")
                dbm.db_record_select(
                    
                    db_name,
                    db_record_table,
                    select='record_id',
                    att_id=record_id,
                    
                    )
                
                input(
                    
                    '\n\n Press <Enter> To Exit...'
                    
                    )

                sys.exit()

            elif x_del == 'del':

                habit_name = dbm.db_habit_select(
                    
                    db_name,
                    db_habit_table,
                    select='habit_id',
                    display='record',
                    habit_id=habit_id,
                    
                    )[0] + ':'

                record_name = dbm.db_record_select(
                    
                    db_name,
                    db_record_table,
                    att_id=record_id,
                    select='record_id',
                    display='record_id',
                    
                    )[0]

                delete = input(
                    
                    '\n\n Are You Sure You Want To {} {} \'{}\' (y) Or Exit '
                    '(x)? '.format(
                        
                        color.RED + 'DELETE' + color.END,
                        habit_name,
                        record_name,
                        
                        )
                    
                    )

                if delete == 'y':

                    screen_clear()

                    print('\n\n')
                    
                    dbm.db_record_delete(
                        
                        db_name,
                        db_record_table,
                        record_id,
                        db_habit_table,
                        habit_id
                        
                        )
                   
                    input(
                        
                        '\n\n Press <Enter> To Exit...'
                        
                        )

                    sys.exit()
                
                else:

                    program_exit()
            else:

                print(
                    
                    '\n\n Record Has Not Been Changed Or Deleted'
                    
                    )
                
                input(
                    
                    '\n\n Press <Enter> to Exit...'
                    
                    )

    elif code == (3, 1):
        ## List of habits
        
        print(color.BOLD + color.UNDERLINE + 
              '\n\n List Of Currently Tracked Habits:' + color.END + '\n')
        
        habit_ids = dbm.db_habit_select(
            
            db_name,
            db_habit_table,
            display='list',
            user_id=user_id,
            
            )[1]
       
        if not habit_ids:

            print(
                
                '\n\n No Habit Data Available'
                
                )

            input(
                
                '\n\n Press <Enter> To Exit...'
                
                )

            sys.exit()
        
        input(
                
                '\n\nPress <Enter> To Exit...'
                
                )
        
        sys.exit()

    elif code == (3, 2):
        ## List of habits with same periodicity
        
        periodicity = input(
            
            '\n\n Which Periodicity Do You Want To See (d=daily, w=weekly)? --> '
            
            )

        screen_clear()

        ## handle invalid input
        while periodicity not in dic_period:
            
            periodicity = input(
                
                '\n\n Invalid Input. You Must Choose Between d=daily And '
                'w=weekly --> '
                
                )

            screen_clear()

        
        print(
            
            '\n\n ' + color.UNDERLINE + color.BOLD +
            'List Of {} Habits:'.format(dic_period[periodicity].upper()) + 
            color.END + '\n'
            
            )

        
        ## database call based on PERIODICITY
        habit_ids = dbm.db_habit_select(
            
            db_name,
            db_habit_table,
            select='periodicity',
            display='list',
            user_id=user_id,
            periodicity=periodicity,
            
            )[1]

        if not habit_ids:

            print(
                
                '\n\n No Habit Data Available'
                
                )

            input(
                
                '\n\n Press <Enter> To Exit...'
                
                )

            sys.exit()
        
        input(
            
            '\n\n Press <Enter> To Exit...'
            
            )

    elif code == (3, 3):
        ## Longest streaks for current habits
        (
            
            habit_name,
            habit_ids,
            habit_id_lookup,
            
            ) = dbm.db_habit_select(
                
                db_name,
                db_habit_table,
                display='analytics',
                user_id=user_id,
                
                )
    
        masterlist = []

        for i,j in habit_id_lookup.items():
            
            (
                
                record_name,
                record_ids,
                
                ) = dbm.db_record_select(
                
                    db_name,
                    db_record_table,
                    select='habit_id',
                    display='analytics',
                    att_id=j,
            
                    )

            record_name.insert(0, i)
            
            masterlist.append(record_name)
            
        print(
            
            color.UNDERLINE + color.BOLD + '\n\n All-Time Longest Habit '
            'Streak:\n' + color.END
            
            )
            
        ## calculate the longest habit name (printing to screen purpose)
        length = len(max([i[0][0] for i in masterlist]))
        
        ## generate longest streak data for currently tracked habits
        for i in masterlist:
            
            daily_streak_calc_func(i, length, 'max')
            weekly_streak_calc_func(i, length, 'max')
            
        input(
            
            '\n\n Press <Enter> To Exit...'
            
            )

    elif code == (3, 4):
        ## Longest Streak of specific habit
        (
            
            habit_name,
            habit_ids,
            habit_id_lookup,
            
            ) = dbm.db_habit_select(
                
                db_name,
                db_habit_table,
                display='analytics',
                user_id=user_id,
                
                )
    
        masterlist = []

        for i,j in habit_id_lookup.items():
            
            (
                
                record_name,
                record_ids,
                
                ) = dbm.db_record_select(
                
                    db_name,
                    db_record_table,
                    select='habit_id',
                    display='analytics',
                    att_id=j,
            
                    )

            record_name.insert(0, i)
            
            masterlist.append(record_name)
        
        print(
            
            '\n\n ' + color.UNDERLINE + color.BOLD + 'Choose A Habit...'
            '\n' + color.END
            
            )
        
        for i in masterlist:
            
            print(
                
                '{:4}'.format(i[1][2]) + ' --> ' + str(i[0][0])
                
                )
            
        print(
            
            'x'.rjust(4), '-->', 'Exit'
            
            )

        
        habit_id = input(
            
            '\n Please Provice Index Of Habit You Want To See The Longest '
            'Streak Of --> '
            
            )
        
        screen_clear()

        ## handle invalid input
        while habit_id not in [str(habit_id_lookup[i[0]]) for i in masterlist]:

            print('\n\n')
            
            for i in masterlist:
            
                print(
                    
                    '{:4}'.format(i[1][2]) + ' --> ' + str(i[0][0])
                    
                    )
                
            print(
                
                'x'.rjust(4), '-->', 'Exit'
                
                )
            
            habit_id = input(
                
                '\n Please Try Again And Choose Appropriate Left Index '
                    'From the Menu Above Or Exit (x): --> '
                    
                    )

            screen_clear()

            if record_id == 'x':

                input(
                    
                    '\n\n Press <Enter> To Exit...'
                    
                    )
                
                sys.exit()
        
        if habit_id == 'x':

            input(
                    
                '\n\n Press <Enter> To Exit...'
                    
                )

            sys.exit()

        print(
            
            '\n\n ' + color.UNDERLINE + color.BOLD + 'All-Time Longest Habit '
            'Streak For...\n' + color.END
            
            )
        
        ## calculate the longest habit name (printing to screen purpose)
        length = len(max([i[0][0] for i in masterlist]))
        
        ## generate longest streak data for specific habit
        for i in masterlist:

            if str(i[1][2]) == habit_id:
                
                daily_streak_calc_func(i, length, 'max')
                weekly_streak_calc_func(i, length, 'max')
        
        input(
            
            '\n\n Press <Enter> To Exit...'
            
            )

    elif code == (3, 5):
        ## Average streaks for current habits
        (
            
            habit_name,
            habit_ids,
            habit_id_lookup,
            
            ) = dbm.db_habit_select(
                
                db_name,
                db_habit_table,
                display='analytics',
                user_id=user_id,
                
                )
    
        masterlist = []

        for i,j in habit_id_lookup.items():
            
            (
                
                record_name,
                record_ids,
                
                ) = dbm.db_record_select(
                
                    db_name,
                    db_record_table,
                    select='habit_id',
                    display='analytics',
                    att_id=j,
            
                    )

            record_name.insert(0, i)
            
            masterlist.append(record_name)
            
        print(
            
            color.UNDERLINE + color.BOLD + '\n\n All-Time Average Habit Streak'
            ':\n' + color.END
            
            )
            
        ## calculate the longest habit name (printing to screen purpose)
        length = len(max([i[0][0] for i in masterlist]))
        
        ## generate average streak data for currently tracked habits
        for i in masterlist:
            
            daily_streak_calc_func(i, length, 'ave')
            weekly_streak_calc_func(i, length, 'ave')
            
        input(
            
            '\n\n Press <Enter> To Exit...'
            
            )
        
    elif code == (3, 6):
        ## Total number of streaks for current habits
        (
            
            habit_name,
            habit_ids,
            habit_id_lookup,
            
            ) = dbm.db_habit_select(
                
                db_name,
                db_habit_table,
                display='analytics',
                user_id=user_id,
                
                )
    
        masterlist = []

        for i,j in habit_id_lookup.items():
            
            (
                
                record_name,
                record_ids,
                
                ) = dbm.db_record_select(
                
                    db_name,
                    db_record_table,
                    select='habit_id',
                    display='analytics',
                    att_id=j,
            
                    )

            record_name.insert(0, i)
            
            masterlist.append(record_name)
            
        print(
            
            color.UNDERLINE + color.BOLD + '\n\n All-time '
            'Total Number Of Started Habit Streaks:\n' + color.END
            
            )
            
        ## calculate the longest habit name (printing to screen purpose)
        length = len(max([i[0][0] for i in masterlist]))
        
        ## generate average streak data for currently tracked habits
        for i in masterlist:
            
            daily_streak_calc_func(i, length, 'num')
            weekly_streak_calc_func(i, length, 'num')
            
        input(
            
            '\n\n Press <Enter> To Exit...'
            
            )
    
    elif code == (3, 7):
        ## All-time Performance Score for all current habits
        (
            
            habit_name,
            habit_ids,
            habit_id_lookup,
            
            ) = dbm.db_habit_select(
                
                db_name,
                db_habit_table,
                display='analytics',
                user_id=user_id,
                
                )
    
        masterlist = []

        for i,j in habit_id_lookup.items():
            
            (
                
                record_name,
                record_ids,
                
                ) = dbm.db_record_select(
                
                    db_name,
                    db_record_table,
                    select='habit_id',
                    display='analytics',
                    att_id=j,
            
                    )

            record_name.insert(0, i)
            
            masterlist.append(record_name)
            
        print(
            
            color.UNDERLINE + color.BOLD + '\n\n All-Time '
            'Longest Streak Vs. Number Of Started Streaks Ratio:\n' 
            + color.END
            
            )
            
        ## calculate the longest habit name (printing to screen purpose)
        length = len(max([i[0][0] for i in masterlist]))
        
        ## generate average streak data for currently tracked habits
        for i in masterlist:
            
            daily_streak_calc_func(i, length, 'ratio')
            weekly_streak_calc_func(i, length, 'ratio')
            
        input(
            
            '\n\n Press <Enter> To Exit...'
            
            )
    
    elif code == (3, 8):
        ## Performance Score for a specific month for all current habits
        
        yyyy_mm = input(
            
            'Please provide year and month you want to analyse (YYYY-MM) OR '
            'Exit (x): --> '
            
            )
        
        ## check if input is ok
        screen_clear()
            
        if yyyy_mm == 'x':

            input(
                
                '\n\n Press <Enter> To Exit...'
                
                )

            sys.exit()
    
        ## handle invalid input (year_month_format)
        while not re.search(year_month_format, yyyy_mm):

            yyyy_mm = input(
                
                '\n\n The DATE Must Follow ISO Format (YYYY-MM). '
                'Try Again Or Exit (x): --> '
                
                )

            screen_clear()

            if yyyy_mm == 'x':

                input(
                    
                    '\n\n Press <Enter> To Exit...'
                    
                    )

                sys.exit()

        (
            
            habit_name,
            habit_ids,
            habit_id_lookup,
            
            ) = dbm.db_habit_select(
                
                db_name,
                db_habit_table,
                display='analytics',
                user_id=user_id,
                
                )
    
        masterlist = []

        for i,j in habit_id_lookup.items():
            
            (
                
                record_name,
                record_ids,
                
                ) = dbm.db_record_select(
                
                    db_name,
                    db_record_table,
                    select='habit_id_ratio',
                    display='analytics',
                    dates=yyyy_mm,
                    att_id=j,
            
                    )

            record_name.insert(0, i)
            
            masterlist.append(record_name)
            
        print(
            
            color.UNDERLINE + color.BOLD + '\n\n Longest Streak'
            ' Vs. Number Of Started Streaks Ratio In {} {}:\n'
            .format(dic_num_to_month[yyyy_mm[-2:]], yyyy_mm[:4]) + color.END
            
            )
            
        ## calculate the longest habit name (printing to screen purpose)
        length = len(max([i[0][0] for i in masterlist]))
        
        ## generate average streak data for currently tracked habits
        for i in masterlist:
            
            daily_streak_calc_func(i, length, 'ratio')
            weekly_streak_calc_func(i, length, 'ratio')
            
        input(
            
            '\n\n Press <Enter> To Exit...'
            
            )
    
    elif code == (3, 9):
        ## Performance Score for a specific year in monthly increments for all current habits
        
        yyyy = input(
            
            'Please Provide Year Of Analyses (YYYY) OR '
            'Exit (x): --> '
            
            )
        
        screen_clear()
            
        if yyyy == 'x':

            input(
                
                '\n\n Press <Enter> To Exit...'
                
                )

            sys.exit()
    
        ## handle invalid input (year_month_format)
        while not re.search(year_format, yyyy):

            yyyy = input(
                
                '\n\n The DATE Must Follow ISO Format (YYYY). '
                'Try Again Or Exit (x): --> '
                
                )

            screen_clear()

            if yyyy == 'x':

                input(
                    
                    '\n\n Press <Enter> To Exit...'
                    
                    )

                sys.exit()

        print(
                
                color.UNDERLINE + color.BOLD + '\n\n Monthly '
                'Longest Streak Vs. Number Of Started Streaks Ratios In {} :\n'
                .format(yyyy) + color.END
                
                )
        
        master = []
        for i in range(1, 13):
            
            mm = str(i).zfill(2)
            
            yyyy_mm = yyyy + '-' + mm
        
            (
                
                habit_name,
                habit_ids,
                habit_id_lookup,
                
                ) = dbm.db_habit_select(
                    
                    db_name,
                    db_habit_table,
                    display='analytics',
                    user_id=user_id,
                    
                    )
        
            masterlist = []
    
            for i,j in habit_id_lookup.items():
                
                (
                    
                    record_name,
                    record_ids,
                    
                    ) = dbm.db_record_select(
                    
                        db_name,
                        db_record_table,
                        select='habit_id_ratio',
                        display='analytics',
                        dates=yyyy_mm,
                        att_id=j,
                
                        )
    
                record_name.insert(0, i)
                
                masterlist.append(record_name)
                
            
                
            ## calculate the longest habit name (printing to screen purpose)
            length = len(max([i[0][0] for i in masterlist]))
            
            ## generate average streak data for currently tracked habits
            months, names_habits = [], []

            for i in masterlist:
                
                if daily_streak_calc_func(
                        
                        i, 
                        length, 
                        'year'
                        
                        )[1]:
                    
                    months.append(
                        
                        daily_streak_calc_func(
                            
                            i, 
                            length, 
                            'year'
                        
                            )[1][0]
                        
                        )
                
                elif weekly_streak_calc_func(
                        
                        i, 
                        length,
                        'year'
                        
                        )[1]:
                
                    months.append(
                        
                        weekly_streak_calc_func(
                            
                            i,
                            length,
                            'year'
                            
                            )[1][0]
                        
                        )
                
            master.append(months)
            
        names_habits = [(' ' + i[0][0]) for i in masterlist]
        
        h_length = max([len(i) for i in names_habits])

        master.insert(0, names_habits)

        master = list(map(list, zip(*master)))

        master.insert(0, [' Month','Jan', 'Feb', 'Mar', 'Apr', 'Mai', 'Jun', 
                          'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
        
        for h in master:
            
            print(
                
                h[0].ljust(h_length),
                ' --> ',
                str(h[1]).rjust(4), 
                str(h[2]).rjust(4), 
                str(h[3]).rjust(4), 
                str(h[4]).rjust(4), 
                str(h[5]).rjust(4), 
                str(h[6]).rjust(4),
                str(h[7]).rjust(4), 
                str(h[8]).rjust(4), 
                str(h[9]).rjust(4), 
                str(h[10]).rjust(4), 
                str(h[11]).rjust(4), 
                str(h[12]).rjust(4),
                  
                  )

        input(
            
            '\n\n Press <Enter> To Exit...'
            
            )
    
    elif code == (4, 1):
        ## Status Update
        
        (
            
            habit_name,
            habit_ids,
            habit_id_lookup,
            
            ) = dbm.db_habit_select(
                
                db_name,
                db_habit_table,
                display='analytics',
                user_id=user_id,
                
                )
    
        masterlist = []

        for i,j in habit_id_lookup.items():
            
            (
                
                record_name,
                record_ids,
                
                ) = dbm.db_record_select(
                
                    db_name,
                    db_record_table,
                    select='habit_id',
                    display='analytics',
                    att_id=j,
            
                    )

            record_name.insert(0, i)
            
            masterlist.append(record_name)                                      ## masterlist = list of tuples:
                                                                                ## tuple[0]=(habit name, habid periodicity), 
        (                                                                       ## tuple[1:]= (record date, record time, habid id)
                
            d_today,
            d_current,
            d_other,
            w_current,
            w_today,
            w_other,
            w_soon,
            
            ) = [], [], [], [], [], [], []
    
        ## Calculate current streak data
        for i in masterlist:
            
            (
                d_today,
                d_current,
                d_other,
                w_today,
                w_current,
                w_other,
                w_soon,
                
                ) = current_streak_calc_sorting_func(
                    
                    i, 
                    time_stamp,
                    d_today, 
                    d_current, 
                    d_other, 
                    w_today,
                    w_current,
                    w_other, 
                    w_soon
                    
                    )
        
        print(
            
            color.BOLD + color.UNDERLINE + '\n\n Daily Habits:' + color.END
            
            )
        
        if not d_today and not d_current and not d_other:
            
            print(
                
                '\n\n No Data Available...'
                
                )
        
        for i in d_today:
            
            print(
                        
                '\n Congratulations! You Have Checked Off \'{}\' Today --> '
                'Current Streak: {} {}'.format(
                    
                    i[0],
                    i[3],
                    i[4]
                    
                    )
                
                )
                    
        for i in d_current:
            
            print(
                        
                '\n Record \'{}\' By The End Of The Day To Extend '
                'Current Streak ({} {}) --> Last Check Off: {} {}'.format(
                    
                    i[0],
                    i[3],
                    i[4],
                    i[1],
                    i[2],
                    
                    )
                
                )
                    
        for i in d_other:

            print(
                        
                '\n Start New Streak For \'{}\' --> Last Check Off: {} {}'
                .format(
                    
                    i[0], 
                    i[1],
                    i[2],
                    
                    )
                
                )
        
        print(
            
            color.BOLD + color.UNDERLINE + '\n\n Weekly Habits:' + color.END
            
            )
        
        if not w_today and not w_current and not w_other and not w_soon:
            
            print(
                
                '\n\n No Data Available...'
                
                )
        
        for i in w_today:
            
            print(
                        
                '\n Congratulations! You Have Checked Off \'{}\' Today --> '
                'Current Streak: {} {}'.format(
                    
                    i[0],
                    i[3],
                    i[4]
                    
                    )
                
                )
            
        for i in w_current:
            
            print(
                        
                '\n Record \'{}\' By The End Of The Day To Extend '
                'Current Streak ({} {}) --> Last Check Off: {} {}'.format(
                    
                    i[0],
                    i[3],
                    i[4],
                    i[1],
                    i[2],
                    
                    )
                
                )
        
        for i in w_soon:
            
            print(
                        
                '\n Record \'{}\' Soon To Keep Current Streak ({} {})'
                ' --> Last Check Off: {} {}'.format(
                    
                    i[0],
                    i[3],
                    i[4],
                    i[1],
                    i[2],
                    
                    )
                
                )
                    
        for i in w_other:
            
            print(
                        
                '\n Start New Streak For \'{}\' --> Last Check Off: {} {}'
                .format(
                    
                    i[0], 
                    i[1],
                    i[2],
                    
                    )
                
                )

        input('\n\n Press <Enter> to Exit...')


if __name__ == '__main__':

    main()