# -*- coding: utf-8 -*-
"""
Created on Sat Dec 18 18:36:05 2021

@author: eichner
"""


class user:
    ## instance attribute
    def __init__(self, name, password, time_stamp):
        '''
        Self attributes of the class user

        Parameters
        ----------
        name : str
            username.
        password : str
            password.
        time_stamp : str
            'YYYY-MM-DD HH:MM:SS'.

        Returns
        -------
        None.

        '''
        self.name = name
        self.password = password
        self.time_stamp = time_stamp

        
class habit:
    ## instance attribute
    def __init__(self, name, description, periodicity, time_stamp, user_id):
        '''
        Self attributes of the class habit

        Parameters
        ----------
        name : str
            habit name.
        description : str
            habit description.
        periodicity : str
            'd'=daily, 'w'=weekly.
        time_stamp : str
            'YYYY-MM-DD HH:MM:SS'.
        user_id : int
            user id (foreign key).

        Returns
        -------
        None.

        '''
        self.name = name
        self.description = description
        self.periodicity = periodicity
        self.time_stamp = time_stamp
        self.user_id = user_id


class record:
    ## instance attribute
    def __init__(self, time_stamp, habit_id):
        '''
        Self attributes of the class record

        Parameters
        ----------
        time_stamp : str
            'YYYY-MM-DD HH:MM:SS'.
        habit_id : int
            habid id (foreign key).

        Returns
        -------
        None.

        '''
        self.time_stamp = time_stamp
        self.habit_id = habit_id


class color:
    ## customizing printing style
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'
