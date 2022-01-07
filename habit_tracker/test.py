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
from habit_tracker import (daily_countdown_func, 
                           weekly_streak_calc_func, 
                           current_streak_calc_sorting_func, 
                           daily_streak_calc_func,
                           seven_days_upwards_func,
                           )


class SolutionTest(unittest.TestCase):

    def test_daily_countdown_func(self):
        """
        Testing if the correct date list is returned and and that the numbers 
        for year, month and day are in the allowed range. The function takes a 
        timestamp and returns a specified number of preceding days as a list 
        in daily increments and descending order ('YYYY-MM-DD'). This function
        is used to calculate current streak data of all habits and to only 
        allow record logging (retrospective), editing, and deleting for a 
        specified period.  
        """
        ## suppress printing to screen
        suppress_text = io.StringIO()
        sys.stdout = suppress_text
        
        ## mock up data  - change for different scenarios
        time_stamp = '2022-01-31'
        number = 365
      
        
        ## first string value in list
        self.assertEqual(
            
            daily_countdown_func(
                
                time_stamp, number
                
                )
            
            [0], '2022-01-30'  ## change to first expected string value in list here
            
            )
        
        ## last string value in list
        self.assertEqual(
            
            daily_countdown_func(
                
                time_stamp,
                number
                
                )
            
            [-1], '2021-01-31'  ## change to last expected string value in list here
            
            )
        
        ## number of returned string values
        self.assertEqual(
            
            len(
                
                daily_countdown_func(
                    
                    time_stamp, number
                    
                    )
                
                ), 365  ## change to number of expected string values in list here
            
            )

        ## checking year, month, and day are in valid range
        for i in range(number):
            ## day > 0
            self.assertGreater(
                
                    int(
                        
                        daily_countdown_func(
                            
                            time_stamp, number
                    
                        )
                
                    [i][-2:]
                    
                    ), 0
                
                )
            
            ## day < 32
            self.assertLess(
                
                    int(
                        
                        daily_countdown_func(
                            
                            time_stamp, number
                    
                        )
                
                    [i][-2:]
                    
                    ), 32
                
                )
        
            ## month > 0
            self.assertGreater(
                
                    int(
                        
                        daily_countdown_func(
                            
                            time_stamp, number
                    
                        )
                
                    [i][5:7]
                    
                    ), 0
                
                )
            
            ## month < 13
            self.assertLess(
                
                    int(
                        
                        daily_countdown_func(
                            
                            time_stamp, number
                    
                        )
                
                    [i][5:7]
                    
                    ), 13
                
                )
        
            ## year > 999
            self.assertGreater(
                
                    int(
                        
                        daily_countdown_func(
                            
                            time_stamp, number
                    
                        )
                
                    [i][:4]
                    
                    ), 999
                
                )
            
            ## month < 3000
            self.assertLess(
                
                    int(
                        
                        daily_countdown_func(
                            
                            time_stamp, number
                    
                        )
                
                    [i][:4]
                    
                    ), 3000
                
                )
        
    def test_seven_days_upwards_func(self):
        """
        Testing if the correct sequence of following seven days in a list 
        based on the input is calculated correctly and that the numbers for 
        year, month and day are in the allowed range. This function is 
        important for calculating the longest streak, the average streak, 
        the total number of streaks, and the streak performance score of all 
        weekly habits. Leap years are taken into account.

        """
        ## mock up data  - change for different scenarios
        date = '2020-02-28'  ## e.g., testing leap year functionality
        date2 = '2020-12-31'  ## e.g., testing year transition
        
        month_day = date[5:]
        year = date[:4]
        month = date[5:7]
        day = date[8:]
        
        month_day2 = date2[5:]
        year2 = date2[:4]
        month2 = date2[5:7]
        day2 = date2[8:]

        self.assertEqual(
            
            seven_days_upwards_func(
                
                month_day, year, month, day
                
                )[0], '2020-02-29'  ## change to first expected string value in list here
            
            )
        
        self.assertEqual(
            
            seven_days_upwards_func(
                
                month_day, year, month, day
                
                )[-1], '2020-03-06'  ## change to last expected string value in list here
            
            )
    
        self.assertEqual(
            
            seven_days_upwards_func(
                
                month_day2, year2, month2, day2
                
                )[0], '2021-01-01'  ## change to first expected string value in list here
            
            )
        
        self.assertEqual(
            
            seven_days_upwards_func(
                
                month_day2, year2, month2, day2
                
                )[-1], '2021-01-07'  ## change to last expected string value in list here
            
            )
        
        
        ## checking year, month, and day are in valid range
        for i in range(7):
            ## day > 0
            self.assertGreater(
                
                int(
                    
                    seven_days_upwards_func(
                    
                        month_day, year, month, day
                    
                        )[i][-2:]
                    
                    ), 0
                
                )
            
            ## day < 32
            self.assertLess(
                
                int(
                    
                    seven_days_upwards_func(
                    
                        month_day, year, month, day
                    
                        )[i][-2:]
                    
                    ), 32
                
                )
            
            ## month > 0
            self.assertGreater(
                
                int(
                    
                    seven_days_upwards_func(
                    
                        month_day, year, month, day
                    
                        )[i][5:7]
                    
                    ), 0
                
                )
            
            ## month < 13
            self.assertLess(
                
                int(
                    
                    seven_days_upwards_func(
                    
                        month_day, year, month, day
                    
                        )[i][5:7]
                    
                    ), 13
                
                )
    
            ## month > 999
            self.assertGreater(
                
                int(
                    
                    seven_days_upwards_func(
                    
                        month_day, year, month, day
                    
                        )[i][:4]
                    
                    ), 999
                
                )
            
            ## month < 3000
            self.assertLess(
                
                int(
                    
                    seven_days_upwards_func(
                    
                        month_day, year, month, day
                    
                        )[i][:4]
                    
                    ), 3000
                
                )
    
    def test_current_streak_calc_sorting_func_day(self):
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
            ('2022-01-31', '', 1), 
            ('2022-02-01', '', 1),
            ('2022-02-02', '', 1), 
            ('2022-02-03', '', 1), 
            ('2022-02-04', '', 1), 
            ('2022-02-06', '', 1), 
            ('2022-02-07', '', 1), 
            ('2022-02-08', '', 1), 
            ('2022-02-09', '', 1), 
            ('2022-03-30', '', 1), 
            ('2022-03-31', '', 1), 
            ('2022-04-01', '', 1), ## break --> +9 days --> current streak = 3
            ('2022-04-10', '', 1), ## 3 days
            ('2022-04-11', '', 1), ## 2 days
            ('2022-04-12', '', 1), ## 1 day
            
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
            
            current_streak_calc_sorting_func(
                
                data, today, d_today, d_current, d_other, 
                w_current, w_today, w_other, w_soon
                
                )
            
            [0][0]
            
            )
        
        ## the data will be populated in this list if check off needs to 
        ## happen today to keep current streak
        self.assertTrue(
            
            current_streak_calc_sorting_func(
                
                data, current, d_today, d_current, d_other, 
                w_current, w_today, w_other, w_soon
                
                )
            
            [1][0]
            
            )
        
        ## the data will be populated in this list if no current streak is 
        ## available the habit has not been checked off for > 1 day
        self.assertTrue(
            
            current_streak_calc_sorting_func(
                
                data, other, d_today, d_current, d_other, 
                w_current, w_today, w_other, w_soon
                
                )
            
            [2][0]
            
            )
        
        ## The resulting number inside the generated list should reflect 
        ## the current streak as highlighted above
        self.assertEqual(
            
            current_streak_calc_sorting_func(
                
                data, today, d_today, d_current, d_other, 
                w_current, w_today, w_other, w_soon
                
                )
            
            [0][0][3], 3  ## change to expected current streak
            
            ) 

        ## The resulting number inside the generated list should reflect 
        ## the current streak as highlighted above
        self.assertEqual(
            
            current_streak_calc_sorting_func(
                
                data, current, d_today, d_current, d_other, 
                w_current, w_today, w_other, w_soon
                
                )
            
            [1][0][3], 3  ## change to expected current streak
            
            )        
        
    
    def test_current_streak_calc_sorting_func_week(self):
        """
        Testing if weekly habit data is correctly sorted into the corresponding 
        list to fuel status update functionality. This function is important 
        to correctly calculate the length of the latest streak and when to 
        check off next to keep current streak. Also, triggered motivational 
        phrases up on check off are based on the result of this function.
        """
        d_today, d_current, d_other = [], [], []
        w_today, w_current, w_other, w_soon = [], [], [], []
        
        ## mock up data - change for different scenarios
        data = [
            
            ('Unittesting', 'w'), 
            ('2022-01-01', '', 1),
            ('2022-01-08', '', 1),
            ('2022-01-15', '', 1),
            ('2022-01-22', '', 1),
            ('2022-01-30', '', 1),
            ('2022-02-06', '', 1), 
            ('2022-02-19', '', 1), ## break --> +8 --> current streak = 3 
#            ('2022-02-21', '', 1), ## 3 weeks
#            ('2022-02-22', '', 1), ## 3 weeks
#            ('2022-02-23', '', 1), ## 3 weeks
#            ('2022-02-24', '', 1), ## 3 weeks
#            ('2022-02-25', '', 1), ## 3 weeks
#            ('2022-02-26', '', 1), ## 3 weeks
            ('2022-02-27', '', 1), ## 3 weeks
#            ('2022-02-28', '', 1), ## 2 weeks
#            ('2022-03-01', '', 1), ## 2 weeks
#            ('2022-03-02', '', 1), ## 2 weeks
#            ('2022-03-03', '', 1), ## 2 weeks
#            ('2022-03-04', '', 1), ## 2 weeks
#            ('2022-03-05', '', 1), ## 2 weeks
            ('2022-03-06', '', 1), ## 2 weeks
#            ('2022-03-07', '', 1), ## 1 week
#            ('2022-03-08', '', 1), ## 1 weeks
#            ('2022-03-09', '', 1), ## 1 weeks
#            ('2022-03-10', '', 1), ## 1 weeks
#            ('2022-03-11', '', 1), ## 1 weeks
#            ('2022-03-12', '', 1), ## 1 weeks
            ('2022-03-13', '', 1), ## 1 weeks
            ('2022-03-14', '', 1), ## 0 weeks
            
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
            
            current_streak_calc_sorting_func(
                
                data, today, d_today, d_current, d_other, 
                w_current, w_today, w_other, w_soon
                
                )
            
            [3][0]
            
            )
               
        ## the data will be populated in this list if check off needs to 
        ## happen today to keep current streak. Last check off was 7 days ago.
        self.assertTrue(
            
            current_streak_calc_sorting_func(
                
                data, current, d_today, d_current, d_other, 
                w_today, w_current, w_other, w_soon
                
                )
            
            [4][0]
            
            ) 

        ## the data will be populated in this list if no current streak is 
        ## available the habit has not been checked off for > 7 days.
        self.assertTrue(
            
            current_streak_calc_sorting_func(
                
                data, other, d_today, d_current, d_other, 
                w_today, w_current, w_other, w_soon
                
                )
            
            [5][0]
            
            )

        ## the data will be populated in this list if the habit has not been 
        ## checked off for the last 1-6 days. Here: 6 days
        self.assertTrue(
            
            current_streak_calc_sorting_func(
                
                data, soon6, d_today, d_current, d_other, 
                w_today, w_current, w_other, w_soon
                
                )
            
            [6][0]
            
            )

        ## the data will be populated in this list if the habit has not been 
        ## checked off for the last 1-6 days. Here: 3 days
        self.assertTrue(
            
            current_streak_calc_sorting_func(
                
                data, soon3, d_today, d_current, d_other, 
                w_today, w_current, w_other, w_soon
                
                )
            
            [6][0]
            
            )

        ## the data will be populated in this list if the habit has not been 
        ## checked off for the last 1-6 days. Here: 1 day
        self.assertTrue(
            
            current_streak_calc_sorting_func(
               
                data, soon1, d_today, d_current, d_other, 
                w_today, w_current, w_other, w_soon
               
                )
            
            [6][0]
            
            )
        
        ## The resulting number inside the generated list should reflect 
        ## the current streak as highlighted above
        self.assertEqual(
            
            current_streak_calc_sorting_func(
                
                data, today, d_today, d_current, d_other, 
                w_today, w_current, w_other, w_soon
                
                )
            
            [3][0][3], 3  ##  change to expected current streak
            
            )
        
        ## The resulting number inside the generated list should reflect 
        ## the current streak as highlighted above
        self.assertEqual(
            
            current_streak_calc_sorting_func(
                
                data, current, d_today, d_current, d_other, 
                w_today, w_current, w_other, w_soon
                
                )
            
            [4][0][3], 3  ##  change to expected current streak
            
            )
        
        ## The resulting number inside the generated list should reflect 
        ## the current streak as highlighted above
        self.assertEqual(
            
            current_streak_calc_sorting_func(
                
                data, soon6, d_today, d_current, d_other, 
                w_today, w_current, w_other, w_soon
                
                )
            
            [6][0][3], 3  ##  change to expected current streak
            
            )


    def test_daily_streak_calc_func(self):
        """
        Testing if the values for longest streak, average streak, total number
        of started streaks, and streak performance are calculated correctly 
        for all daily habits. This function is heavily used during Analytics 
        Toolbox execution.
        """

        ## mock up data - change for different scenarios
        data = [
            
            ('Unittesting', 'd'), 
            ('2021-01-01', '', 1), ## 1 day
            ('2022-01-31', '', 1), ## break --> 1 day
            ('2022-02-01', '', 1), ## 2 days
            ('2022-02-02', '', 1), ## 3 days
            ('2022-02-03', '', 1), ## 4 days
            ('2022-02-04', '', 1), ## 5 days
            ('2022-02-06', '', 1), ## break --> 1 day
            ('2022-02-07', '', 1), ## 2 days
            ('2022-02-08', '', 1), ## 3 days
            ('2022-02-09', '', 1), ## 4 days
            ('2022-03-30', '', 1), ## break --> 1 day
            ('2022-03-31', '', 1), ## 2 days
            ('2022-04-01', '', 1), ## 3 days --> current streak
            
            ]
 
        long_streak = 5  ## change to expected longest streak
        num_streak = 4  ## change to the total number of streaks
        ave_streak = round(((1 + 5 + 4 + 3) / num_streak), 1) ## change to the sum of streak length divided by the total number of streaks
        ratio = round((long_streak / num_streak), 2)  ## change to the ratio between the longes streak and the total number of streaks
        
        ## the result should be the longest streak in the data in days
        self.assertEqual(
            daily_streak_calc_func(
                
                data, 1, 'max'
                
                )[0][0], long_streak
            
            )

        ## the result should be the average streak (sum of all streak lengths 
        ## divided by the total number of streaks) in the data in days
        self.assertEqual(
            
            daily_streak_calc_func(
                
                data, 1, 'ave'
                
                )[0][0], ave_streak
            
            )

        ## the result should be the total number of streaks in the data
        self.assertEqual(
            
            daily_streak_calc_func(
                
                data, 1, 'num'
                
                )[0][0], num_streak
            
            )

        ## the result should be the ratio between longest streak and 
        ## divided by the total number of streaks) in the data
        self.assertEqual(
            
            daily_streak_calc_func(
                
                data, 1, 'ratio'
                
                )[0][0], ratio
            
            )

    
    def test_weekly_streak_calc_func(self):
        """
        Testing if the values for longest streak, average streak, total number
        of started streaks, and streak performance are calculated correctly 
        for all weekly habits. This function is heavily used during Analytics 
        Toolbox execution.
        """
        ## mock up data - change for different scenarios
        data = [
            
            ('Unittesting', 'w'), 
            ('2021-12-31', '', 1), ## 0 weeks
#            ('2022-01-01', '', 1), ## 0 weeks
#            ('2022-01-02', '', 1), ## 0 weeks
            ('2022-01-03', '', 1), ## 0 weeks
            ('2022-01-04', '', 1), ## 0 weeks
#            ('2022-01-05', '', 1), ## 0 weeks
#            ('2022-01-06', '', 1), ## 0 weeks
            ('2022-01-07', '', 1), ## 1 week
#            ('2022-01-08', '', 1), ## 1 week
#            ('2022-01-09', '', 1), ## 1 week
#            ('2022-01-10', '', 1), ## 1 week
            ('2022-01-11', '', 1), ## 1 week
#            ('2022-01-12', '', 1), ## 1 week
#            ('2022-01-13', '', 1), ## 1 week
            ('2022-01-14', '', 1), ## 2 weeks
            ('2022-01-15', '', 1), ## 2 weeks
#            ('2022-01-16', '', 1), ## 2 weeks
#            ('2022-01-17', '', 1), ## 2 weeks
            ('2022-01-18', '', 1), ## 2 weeks
#            ('2022-01-19', '', 1), ## 2 weeks
#            ('2022-01-20', '', 1), ## 2 weeks
            ('2022-01-21', '', 1), ## 3 weeks --> longest streak (=3)
#            ('2022-01-28', '', 1), ## 4 weeks
            ('2022-02-04', '', 1), ## break --> 0 weeks
            
            ]

        long_streak = 3  ## change to expected longest streak
        num_streak = 2  ## change to the total number of streaks
        ave_streak = round(((3 + 0) / num_streak), 1)  ## change to the sum of streak length divided by the total number of streaks
        ratio = round((long_streak / num_streak), 2)  ## change to the ratio between the longes streak and the total number of streaks
        
        ## the result should be the longest streak in the data in weeks
        self.assertEqual(
            
            weekly_streak_calc_func(
                
                data, 1, 'max'
                
                )[0][0], long_streak
            
            )

        ## the result should be the average streak (sum of all streak lengths 
        ## divided by the total number of streaks) in the data in weeks
        self.assertEqual(
            
            weekly_streak_calc_func(
                
                data, 1, 'ave'
                
                )[0][0], ave_streak
            
            )

        ## the result should be the total number of streaks in the data
        self.assertEqual(
            
            weekly_streak_calc_func(
                
                data, 1, 'num'
                
                )[0][0], num_streak
            
            )

        ## the result should be the ratio between longest streak and 
        ## divided by the total number of streaks) in the data
        self.assertEqual(
            
            weekly_streak_calc_func(
                
                data, 1, 'ratio'
                
                )[0][0], ratio
            
            )
        

    def test_weekly_streak_calc_func_db(self):
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
            
            weekly_streak_calc_func(
                
                temp, 1, 'max'
                
                )[0][0], 6
            
            )

        ## Average streak in Q1 2021 for 'Calling My Parents' is 3.0 weeks 
        ## (6, 2, and 1 week --> (6 + 2 + 1) / 3 = 3)
        self.assertEqual(
            
            weekly_streak_calc_func(
                
                temp, 1, 'ave'
                
                )[0][0], 3.0
            
            )
        
        ## total number of streaks in in Q1 2021 for 'Calling My Parents' is 3 
        ##(6, 2, and 1 week)
        self.assertEqual(
            
            weekly_streak_calc_func(
                
                temp, 1, 'num'
                
                )[0][0], 3
            
            )
        
        ## streak performance score in Q1 2021 for 'Calling My Parents' is 2.0 
        ## (6, 2, and 1 week --> 6 / 3 = 2)
        self.assertEqual(
            
            weekly_streak_calc_func(
                
                temp, 1, 'ratio'
                
                )[0][0], 2.0
            
            )


if __name__ == '__main__':
    
    unittest.main()
    

