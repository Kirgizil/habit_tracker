# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a unittest file.
"""

import db_modul as dbm
import unittest
import sys
import io

from operator import itemgetter
from habit_tracker_V12 import (month_day_func, 
                               weekly_analytics, 
                               calc_func, 
                               daily_analytics,
                               week_analytics,
                               )


class SolutionTest(unittest.TestCase):

    def test_month_day_func(self):
        """
        Testing if the correct date list is returned. The function takes a 
        time stamp and returns a specified number of preceeding days as a list 
        in daily increments and descending order ('YYYY-MM-DD'). This function
        is used to calculate current streak data of all habits and to only 
        allow record logging (retrospective), editing, and deleting for a 
        specified period.  
        """
        ## suppress printing to screen
        suppress_text = io.StringIO()
        sys.stdout = suppress_text
        
        ## mock up data  - change for different scenarios
        time_stamp = '2021-01-31'
        number = 31
      
        ## first string value in list
        self.assertEqual(
            
            month_day_func(
                
                time_stamp, number
                
                )
            
            [0], '2021-01-30'  ## change to first expected string value in list here
            
            )
        
        ## last string value in list
        self.assertEqual(
            
            month_day_func(
                
                time_stamp,
                number
                
                )
            
            [-1], '2020-12-31'  ## change to last expected string value in list here
            
            )
        
        ## number of returned string values
        self.assertEqual(
            
            len(
                
                month_day_func(
                    
                    time_stamp, number
                    
                    )
                
                ), 31  ## change to number of expected string values in list here
            
            )


    def test_week_analytics(self):
        """
        Testing if the correct sequence of preceding seven days in a list 
        based on the input is calculated correctly. This function is important
        for calculating the longest streak, the average streak, the total 
        number of streaks, and the streak performance score of all weekly 
        habits. Leap years are taken into accout.

        """
        ## mock up data  - change for different scenarios
        date = '2020-02-28'  ## e.g., testing leap year functionality
        
        month_day = date[5:]
        year = date[:4]
        month = date[5:7]
        day = date[8:]

        self.assertEqual(
            
            week_analytics(
                
                month_day, year, month, day
                
                )[0], '2020-02-29'  ## change to first expected string value in list here
            
            )
        
        self.assertEqual(
            
            week_analytics(
                
                month_day, year, month, day
                
                )[-1], '2020-03-06'  ## change to last expected string value in list here
            
            )
    
    
    def test_calc_func_day(self):
        """
        Testing if daily habit data is correctly sorted into the corresponding 
        list to fuel status update functionality. This function is important 
        to correctly calculate the length of the latest streak and when to 
        check off next to keep current streak. Also, triggered motivational 
        phrases up on check off are based on the result of this function.
        """
        d_today, d_current, d_other = [], [], []
        w_current, w_today, w_other, w_soon = [], [], [], []
        
        ## mock up data - change for different scenarios
        data = [
            
            ('Unittesting', 'd'), 
            ('2022-01-31', '', 1), ## 1 day
            ('2022-02-01', '', 1), ## 2 days
            ('2022-02-02', '', 1), ## 3 days
            ('2022-02-03', '', 1), ## 4 days
            ('2022-02-04', '', 1), ## 5 days
            ('2022-02-06', '', 1), ## break --> 1 day
            ('2022-02-07', '', 1), ## 2 days
            ('2022-02-08', '', 1), ## 3 days
            ('2022-02-09', '', 1), ## 4 days --> current streak
            
            ]

        ## the same day as last check off --> the habit has been checked off 
        ## today
        today = data[-1][0]
        
        ## + 1 day on last check-off --> must be checked off today to keep 
        ## current streak
        current = data[-1][0][:8] + str(int(data[-1][0][-2:]) + 1).zfill(2)  
        
        ## >1 day on last check-off --> no current streak
        other = data[-1][0][:8] + str(int(data[-1][0][-2:]) + 2).zfill(2)    

        
        ## the data will be populated in this list if checked off today
        self.assertTrue(
            
            calc_func(
                
                data, today, d_today, d_current, d_other, 
                w_current, w_today, w_other, w_soon
                
                )
            
            [0][0]
            
            )
        
        ## the data will be populated in this list if check off needs to 
        ## happen today to keep current streak
        self.assertTrue(
            
            calc_func(
                
                data, current, d_today, d_current, d_other, 
                w_current, w_today, w_other, w_soon
                
                )
            
            [1][0]
            
            )
        
        ## the data will be populated in this list if no current streak is 
        ## available the habit has not been checked off for > 1 day
        self.assertTrue(
            
            calc_func(
                
                data, other, d_today, d_current, d_other, 
                w_current, w_today, w_other, w_soon
                
                )
            
            [2][0]
            
            )
        
        ## The resulting number inside the generated list should reflect 
        ## the current streak as highlighted above
        self.assertEqual(
            
            calc_func(
                
                data, today, d_today, d_current, d_other, 
                w_current, w_today, w_other, w_soon
                
                )
            
            [0][0][3], 4  ## change to expected current streak
            
            ) 

        ## The resulting number inside the generated list should reflect 
        ## the current streak as highlighted above
        self.assertEqual(
            
            calc_func(
                
                data, current, d_today, d_current, d_other, 
                w_current, w_today, w_other, w_soon
                
                )
            
            [1][0][3], 4  ## change to expected current streak
            
            )        
        
    
    def test_calc_func_week(self):
        """
        Testing if weekly habit data is correctly sorted into the corresponding 
        list to fuel status update functionality. This function is important 
        to correctly calculate the length of the latest streak and when to 
        check off next to keep current streak. Also, triggered motivational 
        phrases up on check off are based on the result of this function.
        """
        d_today, d_current, d_other = [], [], []
        w_current, w_today, w_other, w_soon = [], [], [], []
        
        ## mock up data - change for different scenarios
        data = [
            
            ('Unittesting', 'w'), 
            ('2022-01-01', '', 1), ## 0 weeks
            ('2022-01-08', '', 1), ## 1 week
            ('2022-01-15', '', 1), ## 2 weeks
            ('2022-01-22', '', 1), ## 3 weeks
            ('2022-01-30', '', 1), ## break --> 0 weeks (+ 8 days)
            ('2022-02-06', '', 1), ## 1 week
            ('2022-02-13', '', 1), ## 2 weeks --> current streak
            
            ]

        ## the same day as last check off --> the habit has been checked off 
        ## today
        today = data[-1][0]     
        
        ## + 7 days on last check-off --> must be check off today to keep 
        ## current streak
        current = data[-1][0][:8] + str(int(data[-1][0][-2:]) + 7).zfill(2)  
        
        ## >7 days on last check-off --> no current streak
        other = data[-1][0][:8] + str(int(data[-1][0][-2:]) + 8).zfill(2)    
        
        ## 1-6 days on last ckeck-off --> must be checked off within the next 
        ## couple of days to keep current streak
        soon6 = data[-1][0][:8] + str(int(data[-1][0][-2:]) + 6).zfill(2)
        soon3 = data[-1][0][:8] + str(int(data[-1][0][-2:]) + 3).zfill(2)
        soon1 = data[-1][0][:8] + str(int(data[-1][0][-2:]) + 1).zfill(2)


        ## the data will end up in this list if checked off today
        self.assertTrue(
            
            calc_func(
                
                data, today, d_today, d_current, d_other, 
                w_current, w_today, w_other, w_soon
                
                )
            
            [3][0]
            
            )
               
        ## the data will be populated in this list if check off needs to 
        ## happen today to keep current streak. Last check off was 7 days ago.
        self.assertTrue(
            
            calc_func(
                
                data, current, d_today, d_current, d_other, 
                w_current, w_today, w_other, w_soon
                
                )
            
            [4][0]
            
            ) 

        ## the data will be populated in this list if no current streak is 
        ## available the habit has not been checked off for > 7 days.
        self.assertTrue(
            
            calc_func(
                
                data, other, d_today, d_current, d_other, 
                w_current, w_today, w_other, w_soon
                
                )
            
            [5][0]
            
            )

        ## the data will be populated in this list if the habit has not been 
        ## checked off for the last 1-6 days. Here: 6 days
        self.assertTrue(
            
            calc_func(
                
                data, soon6, d_today, d_current, d_other, 
                w_current, w_today, w_other, w_soon
                
                )
            
            [6][0]
            
            )

        ## the data will be populated in this list if the habit has not been 
        ## checked off for the last 1-6 days. Here: 3 days
        self.assertTrue(
            
            calc_func(
                
                data, soon3, d_today, d_current, d_other, 
                w_current, w_today, w_other, w_soon
                
                )
            
            [6][0]
            
            )

        ## the data will be populated in this list if the habit has not been 
        ## checked off for the last 1-6 days. Here: 1 day
        self.assertTrue(
            
            calc_func(
                
                data, soon1, d_today, d_current, d_other, 
                w_current, w_today, w_other, w_soon
                
                )
            
            [6][0]
            
            )
        
        ## The resulting number inside the generated list should reflect 
        ## the current streak as highlighted above
        self.assertEqual(
            
            calc_func(
                
                data, today, d_today, d_current, d_other, 
                w_current, w_today, w_other, w_soon
                
                )
            
            [3][0][3], 2  ##  change to expected current streak
            
            )
        
        ## The resulting number inside the generated list should reflect 
        ## the current streak as highlighted above
        self.assertEqual(
            
            calc_func(
                
                data, current, d_today, d_current, d_other, 
                w_current, w_today, w_other, w_soon
                
                )
            
            [4][0][3], 2  ##  change to expected current streak
            
            )
        
        ## The resulting number inside the generated list should reflect 
        ## the current streak as highlighted above
        self.assertTrue(
            
            calc_func(
                
                data, soon6, d_today, d_current, d_other, 
                w_current, w_today, w_other, w_soon
                
                )
            
            [6][0][3], 2  ##  change to expected current streak
            
            )


    def test_daily_analytics(self):
        """
        Testing if the values for longest streak, average streak, total number
        of started streaks, and streak performance are calculated correctly 
        for all daily habits. This function is heavily used during Analytics 
        Toolbox execution.
        """

        ## mock up data - change for different scenarios
        data = [
            
            ('Unittesting', 'd'), 
            ('2022-01-01', '', 1), ## 1 day
            ('2022-01-02', '', 1), ## 2 days
            ('2022-01-03', '', 1), ## 3 days
            ('2022-01-04', '', 1), ## 4 days --> longest streak = 4
            ('2022-01-06', '', 1), ## break --> 1 day (+ 2 days)
            ('2022-02-07', '', 1), ## 2 days
            ('2022-02-08', '', 1), ## 3 days --> 2 streaks in total (4 + 3)
            
            ]
 
        long_streak = 4  ## change to expected longest streak
        ave_streak = round(((4 + 3) / 2), 1) ## change to the sum of streak length divided by the total number of streaks
        num_streak = 2  ## change to the total number of streaks
        ratio = round((4 / 2), 2)  ## change to the ratio between the longes streak and the total number of streaks
        
        ## the result should be the longest streak in the data in days
        self.assertEqual(
            daily_analytics(
                
                data, 1, 'max'
                
                )[0][0], long_streak
            
            )

        ## the result should be the average streak (sum of all streak lengths 
        ## divided by the total number of streaks) in the data in days
        self.assertEqual(
            
            daily_analytics(
                
                data, 1, 'ave'
                
                )[0][0], ave_streak
            
            )

        ## the result should be the total number of streaks in the data
        self.assertEqual(
            
            daily_analytics(
                
                data, 1, 'num'
                
                )[0][0], num_streak
            
            )

        ## the result should be the ratio between longest streak and 
        ## divided by the total number of streaks) in the data
        self.assertEqual(
            
            daily_analytics(
                
                data, 1, 'ratio'
                
                )[0][0], ratio
            
            )

    
    def test_weekly_analytics(self):
        """
        Testing if the values for longest streak, average streak, total number
        of started streaks, and streak performance are calculated correctly 
        for all weekly habits. This function is heavily used during Analytics 
        Toolbox execution.
        """
        ## mock up data - change for different scenarios
        data = [
            
            ('Unittesting', 'w'), 
            ('2022-01-01', '', 1), ## 0 weeks
            ('2022-01-08', '', 1), ## 1 week
            ('2022-01-15', '', 1), ## 2 weeks
            ('2022-01-22', '', 1), ## 3 weeks --> longest streak = 3
            ('2022-01-30', '', 1), ## break --> 0 weeks (+8 days)
            ('2022-02-06', '', 1), ## 1 week
            ('2022-02-13', '', 1), ## 2 week --> 2 streaks in total (3 + 2)
            
            ]

        long_streak = 3  ## change to expected longest streak
        ave_streak = round(((3 + 2) / 2), 1)  ## change to the sum of streak length divided by the total number of streaks
        num_streak = 2  ## change to the total number of streaks
        ratio = round((3 / 2), 2)  ## change to the ratio between the longes streak and the total number of streaks
        
        ## the result should be the longest streak in the data in weeks
        self.assertEqual(
            
            weekly_analytics(
                
                data, 1, 'max'
                
                )[0][0], long_streak
            
            )

        ## the result should be the average streak (sum of all streak lengths 
        ## divided by the total number of streaks) in the data in weeks
        self.assertEqual(
            
            weekly_analytics(
                
                data, 1, 'ave'
                
                )[0][0], ave_streak
            
            )

        ## the result should be the total number of streaks in the data
        self.assertEqual(
            
            weekly_analytics(
                
                data, 1, 'num'
                
                )[0][0], num_streak
            
            )

        ## the result should be the ratio between longest streak and 
        ## divided by the total number of streaks) in the data
        self.assertEqual(
            
            weekly_analytics(
                
                data, 1, 'ratio'
                
                )[0][0], ratio
            
            )
        

    def test_weekly_analytics_from_db(self):
        """
        Test that the correct longest and avearge streak for weekly habits is 
        returned.
        """
        ## selecting test habit data from database (Calling My Parents)
        (
            
            habit_name, 
            habit_ids, 
            habit_id_lookup
            
            ) = dbm.db_habit_select(
                
                'productive.db', 
                'habit_table', 
                select='habit_id',
                display='analytics',
                habit_id=10,
                
                )
        
        
        ## selecting test record data from database for Q1 2021 (Calling My Parents)
        (
            
            temp, 
            record_ids
            
            ) = dbm.db_record_select(
                
                'productive.db', 
                'record_table', 
                select='habit_id_unittest',
                display='analytics', 
                att_id=10, 
                dates=('2021-01', '2021-02', '2021-03')
                
                )        
        
        ## sorting and formating the data selected to be used for testing
        temp.sort(key=itemgetter(0))
        temp.insert(0 , list(habit_id_lookup.keys())[0])
        
        ## longest streak in Q1 2021 for 'Calling My Parents' is 6 weeks
        self.assertEqual(
            
            weekly_analytics(
                
                temp, 1, 'max'
                
                )[0][0], 6
            
            )

        ## Average streak in Q1 2021 for 'Calling My Parents' is 3.0 weeks 
        ## (6, 2, and 1 week --> (6 + 2 + 1) / 3 = 3)
        self.assertEqual(
            
            weekly_analytics(
                
                temp, 1, 'ave'
                
                )[0][0], 3.0
            
            )
        
        ## total number of streaks in in Q1 2021 for 'Calling My Parents' is 3 
        ##(6, 2, and 1 week)
        self.assertEqual(
            
            weekly_analytics(
                
                temp, 1, 'num'
                
                )[0][0], 3
            
            )
        
        ## streak performance score in Q1 2021 for 'Calling My Parents' is 2.0 
        ## (6, 2, and 1 week --> 6 / 3 = 2)
        self.assertEqual(
            
            weekly_analytics(
                
                temp, 1, 'ratio'
                
                )[0][0], 2.0
            
            )


if __name__ == '__main__':
    
    unittest.main()
    

