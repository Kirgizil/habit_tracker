# -*- coding: utf-8 -*-
"""
Created on Wed Dec 22 12:14:09 2021

@author: eichner
"""


import sqlite3
from oop_modul import color


## user management
def db_user_table_creation(db_name, db_table):
    '''
    Creates a sqlite3 user table inside specified database.

    Parameters
    ----------
    db_name : str
        database name.
    db_table : str
        table name.

    Returns
    -------
    None.

    '''
    conn = sqlite3.connect(db_name)
    print("Opened database successfully");

    conn.execute(
        '''CREATE TABLE %s
        (
        USER_ID        INTEGER  PRIMARY KEY,
        NAME           TEXT        NOT NULL,
        PASSWORD       CHAR(20),
        TIME_STAMP     DATE
        );'''
        % (db_table)
        )

    print("Table created successfully");

    conn.close()


def db_user_insert(db_name, db_table, dataset):
    '''
    Insert user data into sqlite3 table.

    Parameters
    ----------
    db_name : str
        database name.
    db_table : str
        user table name.
    dataset : tup
        new user attributes (NAME, PASSWORD, TIME_STAMP)

    Returns
    -------
    None.

    '''
    conn = sqlite3.connect(db_name)

    conn.execute(
        "INSERT INTO %s(NAME, PASSWORD, TIME_STAMP) \
        VALUES %s"
        % (db_table, dataset)
        );

    conn.commit()

    conn.close()


def db_user_select(db_name, db_table):
    '''
    Select and print last user entry to the screen

    Parameters
    ----------
    db_name : str
        database name.
    db_table : str
        user table name.

    Returns
    -------
    None.

    '''
    conn = sqlite3.connect(db_name)

    cursor = conn.execute(
        "SELECT \
            USER_ID, \
            NAME, \
            PASSWORD, \
            TIME_STAMP from %s ORDER BY USER_ID DESC LIMIT 1"
        % (db_table))

    for row in cursor:
        print("USER_ID    =", row[0])
        print("NAME       =", row[1])
        print("PASSWORD   =", row[2])
        print("TIME_STAMP =", row[3]), "\n"

    conn.close()


def db_user_select_test(db_name, db_table):
    '''
    Select and print all user entries to the screen

    Parameters
    ----------
    db_name : str
        database name.
    db_table : str
        user table name.

    Returns
    -------
    None.

    '''
    conn = sqlite3.connect(db_name)

    cursor = conn.execute(
        "SELECT \
            USER_ID, \
            NAME, \
            PASSWORD, \
            TIME_STAMP from %s"
        % (db_table))

    for row in cursor:
        print("USER_ID    =", row[0])
        print("NAME       =", row[1])
        print("PASSWORD   =", row[2])
        print("TIME_STAMP =", row[3]), "\n"

    conn.close()


def db_user_select_login(db_name, db_table):
    '''
    Select all user entries and return two dictionaries: {username : password},
    {username : user id}

    Parameters
    ----------
    db_name : str
        database name.
    db_table : str
        user table name.

    Returns
    -------
    user_password : dic
        Dictionary of all current user {username : password}.
    user_id : dic
        Dictionary of all current user {username : user id}.

    '''
    conn = sqlite3.connect(db_name)

    cursor = conn.execute(
        "SELECT \
            USER_ID, \
            NAME, \
            PASSWORD, \
            TIME_STAMP from %s"
        % (db_table))

    user_ids, usernames, passwords = [], [], []
    for row in cursor:
        user_ids.append(row[0])
        usernames.append(row[1])
        passwords.append(row[2])
        
    user_password = dict(zip(usernames, passwords))
    user_id = dict(zip(usernames, user_ids))

    conn.close()

    return user_password, user_id


def db_user_update(db_name, db_table, attribute, update, user_id):
    '''
    Update a single user attribute of specific user entry.

    Parameters
    ----------
    db_name : str
        database name.
    db_table : str
        user table name.
    attribute : str
        user attribute to be changed.
    update : str
        user attribute to be change to.
    user_id : int
        user id.

    Returns
    -------
    None.

    '''
    conn = sqlite3.connect(db_name)

    conn.execute("UPDATE %s set %s = '%s' where USER_ID = %s"
                 % (db_table, attribute, update, user_id))
    conn.commit()

    conn.close()


def db_user_delete(db_name, db_table, habit_id):
    '''
    Delete specific user entry from the user table in database.

    Parameters
    ----------
    db_name : str
        database name.
    db_table : str
        user table name.
    habit_id : int
        habit id.

    Returns
    -------
    None.

    '''
    conn = sqlite3.connect(db_name)

    conn.execute("DELETE from %s where USER_ID = %s;" % (db_table, habit_id))

    conn.commit()

    conn.close()


## habit management
def db_habit_table_creation(db_name, db_table, user_id):
    '''
    Habit table creation.

    Parameters
    ----------
    db_name : str
        database name.
    db_table : str
        habit table name.
    user_id : int
        user id (foreign key).

    Returns
    -------
    None.

    '''
    conn = sqlite3.connect(db_name)
    print("Opened database successfully");

    conn.execute(
        '''CREATE TABLE %s
        (
        HABIT_ID       INTEGER     PRIMARY KEY,
        NAME           TEXT        NOT NULL,
        DESCRIPTION    TEXT,
        PERIODICITY    CHAR(1),
        TIME_STAMP     DATE,
        USER_ID        INT         NOT NULL,
        FOREIGN KEY (USER_ID)
            REFERENCES  %s (USER_ID)
        );'''
        % (db_table, user_id)
        )

    print("Table created successfully");

    conn.close()


def db_habit_insert(db_name, db_table, dataset):
    '''
    Habit registration

    Parameters
    ----------
    db_name : str
        database name.
    db_table : str
        habit table name.
    dataset : tup
        attributes to register (NAME, DESCRIPTION, PERIODICITY, TIME_STAMP, 
        USER_ID).

    Returns
    -------
    None.

    '''
    conn = sqlite3.connect(db_name)

    conn.execute(
        "INSERT INTO %s(NAME, DESCRIPTION, PERIODICITY, TIME_STAMP, USER_ID) \
        VALUES %s"
        % (db_table, dataset)
        );

    conn.commit()

    conn.close()


def db_habit_select_test(db_name, db_table):
    '''
    Select and print all habits to the screen

    Parameters
    ----------
    db_name : str
        database table.
    db_table : str
        habit table name.

    Returns
    -------
    None.

    '''
    conn = sqlite3.connect(db_name)

    cursor = conn.execute(
    "SELECT \
        HABIT_ID, \
        NAME, \
        DESCRIPTION, \
        PERIODICITY, \
        TIME_STAMP, \
        USER_ID from %s"
    % (db_table))

    for row in cursor:
        print("NAME        =", row[1])
        print("DESCRIPTION =", row[2])
        print("PERIODICITY =", row[3])
        print("TIME_STAMP  =", row[4])
        print("USER_ID     =", row[5])

    conn.close()


def db_habit_select(db_name, db_table, select=None, display=None, 
                    habit_id=None, user_id = None, periodicity=None):
    '''
    Select, print and return habit data selectively based on optional 
    attributes. 

    Parameters
    ----------
    db_name : str
        database name.
    db_table : str
        habit table name.
    select : str, optional
        specific SELECT options. The default is None.
    display : str, optional
        specific PRINT options. The default is None.
    habit_id : int, optional
        Selects habit data based on HABIT_ID. The default is None.
    user_id : int, optional
        Selects habit data based on USER_ID. The default is None.
    periodicity : str, optional
        Selects habit data based on PERIODICITY. The default is None.

    Returns
    -------
    habit_name : str
        specific habit name for printing to the screen.
    habit_ids : list
        list of habit ids [habid_id].
    habit_id_lookup : dic
        dictionary {habit_name : habit_id}.

    '''

    conn = sqlite3.connect(db_name)

    if select == 'limit_1':
        cursor = conn.execute(
        "SELECT \
            HABIT_ID, \
            NAME, \
            DESCRIPTION, \
            PERIODICITY, \
            TIME_STAMP, \
            USER_ID from %s ORDER BY HABIT_ID DESC LIMIT 1"
        % (db_table))

    elif select == 'habit_id':
        cursor = conn.execute(
        "SELECT \
            HABIT_ID, \
            NAME, \
            DESCRIPTION, \
            PERIODICITY, \
            TIME_STAMP, \
            USER_ID from %s where HABIT_ID = %s"
        % (db_table, habit_id))

    elif select == 'periodicity':
        cursor = conn.execute(
        "SELECT \
            HABIT_ID, \
            NAME, \
            DESCRIPTION, \
            PERIODICITY, \
            TIME_STAMP, \
            USER_ID from %s where USER_ID = '%s' AND PERIODICITY = '%s'"
        % (db_table, user_id, periodicity))
    
    else:
        cursor = conn.execute(
        "SELECT \
            HABIT_ID, \
            NAME, \
            DESCRIPTION, \
            PERIODICITY, \
            TIME_STAMP, \
            USER_ID from %s where USER_ID = '%s'"
        % (db_table, user_id))

    if display == 'habit_name':
        count, habit_name, habit_ids, habit_names = 0, '', [], []
        for row in cursor:
            count+=1
            habit_ids.append(row[0])
            habit_name = color.UNDERLINE + color.BOLD + row[1] + color.END
            print('{:4}'.format(row[0]), '-->', row[1]), "\n"

    elif display == 'limit_1':
        count, habit_name, habit_names, habit_ids = 0, '', [], []
        for row in cursor:
            count+=1
            habit_ids.append(row[0])
            habit_names.append(row[1])
            habit_name = row[1]
    
    elif display == 'record':
        count, habit_name, habit_names, habit_ids = 0, '', [], []
        for row in cursor:
            count+=1
            habit_ids.append(row[0])
            habit_names.append(row[1])
            habit_name = color.UNDERLINE + color.BOLD + row[1] + color.END

    elif display == 'list':
        count, habit_name, habit_ids, habit_names = 0, '', [], []
        for row in cursor:
            count+=1
            habit_ids.append(row[0])
            habit_name = color.UNDERLINE + color.BOLD + row[1] + color.END
            print('-->', row[1]), "\n"
    
    elif display == 'analytics':
        habit_name, habit_ids, habit_names = '', [], []
        for row in cursor:
            habit_ids.append(row[0])
            habit_names.append((row[1], row[3]))
    
    else:
        habit_name, habit_ids, habit_names = '', [], []
        for row in cursor:
            habit_name = color.UNDERLINE + color.BOLD + row[1] + color.END
            habit_ids.append(row[0])
            print(" NAME        =", row[1])
            print(" DESCRIPTION =", row[2])
            print(" PERIODICITY =", row[3])
            print(" TIME_STAMP  =", row[4])

    habit_id_lookup = dict(zip(habit_names, habit_ids))

    conn.close()

    return habit_name, habit_ids, habit_id_lookup


def db_habit_update(db_name, db_table, attribute, update, habit_id):
    '''
    Update specific habit data entries in database table

    Parameters
    ----------
    db_name : str
        database name.
    db_table : str
        habit table name.
    attribute : str
        attribute to be changed.
    update : str
        attribute to be changed to.
    habit_id : int
        habit id.

    Returns
    -------
    None.

    '''
    conn = sqlite3.connect(db_name)

    conn.execute("UPDATE %s set %s = '%s' where HABIT_ID = %s"
                 % (db_table, attribute, update, habit_id))
    conn.commit()

    conn.close()


def db_habit_delete(db_name, db_table, habit_id):
    '''
    Delete specific habit from database table

    Parameters
    ----------
    db_name : str
        database name.
    db_table : str
        habit table name.
    habit_id : int
        habit id.

    Returns
    -------
    None.

    '''
    conn = sqlite3.connect(db_name)

    cursor = conn.execute(
        "SELECT \
            HABIT_ID, \
            NAME, \
            DESCRIPTION, \
            PERIODICITY, \
            TIME_STAMP, \
            USER_ID from %s where HABIT_ID = %s" % (db_table, habit_id))

    print(
        
        ' This Entry Has Been Irreversibly Deleted:\n'
        
        );

    for row in cursor:
        print(" NAME        =", row[1])
        print(" DESCRIPTION =", row[2])
        print(" PERIODICITY =", row[3])
        print(" TIME_STAMP  =", row[4])

    conn.execute("DELETE from %s where HABIT_ID = %s;" % (db_table, habit_id))

    conn.commit()

    conn.close()


def db_record_table_creation(db_name, db_table, habit_id):
    '''
    Creating a record table with specific attributes

    Parameters
    ----------
    db_name : str
        database name.
    db_table : str
        record table name.
    habit_id : int
        habit id (foreign key).

    Returns
    -------
    None.

    '''
    conn = sqlite3.connect(db_name)
    print("Opened database successfully");

    conn.execute(
            '''CREATE TABLE %s
            (
            RECORD_ID      INTEGER     PRIMARY KEY,
            TIME_STAMP     DATE,
            HABIT_ID       INT         NOT NULL,
            FOREIGN KEY (HABIT_ID)
                REFERENCES  %s (HABIT_ID)
            );'''
            % (db_table, habit_id)
            )

    print("Table created successfully");

    conn.close()


def db_record_insert(db_name, db_table, dataset):
    '''
    Inserting record data into specific database table

    Parameters
    ----------
    db_name : str
        database name.
    db_table : str
        record table name.
    dataset : tup
        record attributes in tuple (TIME_STAMP, HABIT_ID).

    Returns
    -------
    None.

    '''
    conn = sqlite3.connect(db_name)

    conn.execute(
        "INSERT INTO %s(TIME_STAMP, HABIT_ID) \
        VALUES %s"
        % (db_table, dataset)
        );

    conn.commit()

    conn.close()


def db_record_select(db_name, db_table, select=None, att_id=None, display=None,
                     dates=None):
    '''
    Select, print and return record data selectively based on optional 
    attributes.

    Parameters
    ----------
    db_name : str
        database name.
    db_table : str
        record table name.
    select : str, optional
        specific SELECT options. The default is None.
    att_id : int, optional
        habit id or record id to select by. The default is None.
    display : str, optional
        specific PRINT options. The default is None.
    dates : tup, optional
        tuple of date strings 'YYYY-MM-DD' to select by. The default is None.

    Returns
    -------
    record_name : TYPE
        DESCRIPTION.
    record_ids : TYPE
        DESCRIPTION.

    '''
    conn = sqlite3.connect(db_name)

    if select == 'limit_1':
        cursor = conn.execute(
            "SELECT \
                RECORD_ID, \
                TIME_STAMP, \
                HABIT_ID from %s ORDER BY RECORD_ID DESC LIMIT 1"
            % (db_table))

    elif select == 'habit_id':
        cursor = conn.execute(
        "SELECT \
            RECORD_ID, \
            TIME_STAMP, \
            HABIT_ID from %s where HABIT_ID = %s"
        % (db_table, att_id))

    elif select == 'habit_id_lim14':
        cursor = conn.execute(
        "SELECT \
            RECORD_ID, \
            TIME_STAMP, \
            HABIT_ID from %s where HABIT_ID = %s \
                             ORDER BY TIME_STAMP DESC LIMIT 14"
        % (db_table, att_id))
    
    elif select == 'habit_id_lim14_date':
        cursor = conn.execute(
        "SELECT \
            RECORD_ID, \
            TIME_STAMP, \
            HABIT_ID from %s where HABIT_ID = %s AND \
                             substr(TIME_STAMP,0,11) in %s  \
                             ORDER BY TIME_STAMP DESC"
        % (db_table, att_id, dates))
    
    elif select == 'habit_id_unittest':
        cursor = conn.execute(
        "SELECT \
            RECORD_ID, \
            TIME_STAMP, \
            HABIT_ID from %s where HABIT_ID = %s AND \
                             substr(TIME_STAMP,0,8) in %s  \
                             ORDER BY TIME_STAMP DESC"
        % (db_table, att_id, dates))
    
    elif select == 'habit_id_ratio':
        cursor = conn.execute(
        "SELECT \
            RECORD_ID, \
            TIME_STAMP, \
            HABIT_ID from %s where HABIT_ID = %s AND \
                             substr(TIME_STAMP,0,8) = '%s'  \
                             ORDER BY TIME_STAMP DESC"
        % (db_table, att_id, dates))
    
    elif select == 'record_id':
        cursor = conn.execute(
        "SELECT \
            RECORD_ID, \
            TIME_STAMP, \
            HABIT_ID from %s where RECORD_ID = %s"
        % (db_table, att_id))

    else:
        cursor = conn.execute(
            "SELECT \
                RECORD_ID, \
                TIME_STAMP, \
                HABIT_ID from %s"
            % (db_table))

    if display == 'analytics':
        record_name, record_ids = [], []
        for row in cursor:
            record_name.append((row[1].split(' ')[0], row[1].split(' ')[1], 
                                row[2]))
            record_ids.append(row[0])
        
    elif display == 'record_id':
        record_name, record_ids = '', []
        for row in cursor:
            record_name = color.UNDERLINE + color.BOLD + row[1] + color.END
            record_ids.append(row[0])
    
    elif display == 'limit_1':
        record_name, record_ids = '', []
        for row in cursor:
            record_name = color.UNDERLINE + color.BOLD + row[1] + color.END
            record_ids.append(row[0])
            print(' -->', row[1]), "\n"
    
    else:
        record_name, record_ids = '', []
        for row in cursor:
            record_name = color.UNDERLINE + color.BOLD + row[1] + color.END
            record_ids.append(row[0])
            print('{:4}'.format(row[0]), '-->', row[1]), "\n"

    conn.close()
    
    return record_name, record_ids


def db_record_update(db_name, db_table, attribute, update, record_id):
    '''
    Update specific record table attributes

    Parameters
    ----------
    db_name : str
        database name.
    db_table : TYPE
        record table name.
    attribute : str
        attribute to be changed.
    update : str
        attribute to be change to.
    record_id : int
        record id.

    Returns
    -------
    None.

    '''
    conn = sqlite3.connect(db_name)

    conn.execute("UPDATE %s set %s = '%s' where RECORD_ID = %s"
                 % (db_table, attribute, update, record_id))
    conn.commit()

    conn.close()


def db_record_delete(db_name, db_table, record_id, db_habit_table, habit_id):
    '''
    Specifically delete record entry from database table

    Parameters
    ----------
    db_name : str
        database name.
    db_table : str
        record table name.
    record_id : int
        record id.
    db_habit_table : str
        habit table name.
    habit_id : TYPE
        habid id.

    Returns
    -------
    None.

    '''
    conn = sqlite3.connect(db_name)

    cursor = conn.execute(
        "SELECT \
            RECORD_ID, \
            TIME_STAMP, \
            HABIT_ID from %s where RECORD_ID = %s"
        % (db_table, record_id))

    print("This Entry Has Been Irreversibly Deleted:\n");
    
    print(
        
        db_habit_select(
            
            db_name,
            db_habit_table,
            select='habit_id',
            display='record',
            habit_id=habit_id,
            
            )[0] + ':'
        
        )
    
    for row in cursor:
        print("RECORD_ID  =", row[0])
        print("TIME_STAMP =", row[1])
        print("HABIT_ID   =", row[2]), "\n"

    conn.execute("DELETE from %s where RECORD_ID = %s;"
                 % (db_table, record_id))

    conn.commit()

    conn.close()


def table_delete(db_name, db_table):
    '''
    Specifically deleting any database table from the database

    Parameters
    ----------
    db_name : str
        database name.
    db_table : TYPE
        table name.

    Returns
    -------
    None.

    '''
    conn = sqlite3.connect(db_name)

    cursor = conn.cursor()
    
    cursor.execute("DROP TABLE {}".format(db_table))
    print("Table dropped... ")
    
    conn.commit()
    
    conn.close()