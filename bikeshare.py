# -*- coding: utf-8 -*-
"""
Created on Sun Dec 13 20:43:36 2020

@author: hp2328
"""

import time
import datetime
import calendar
import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import traceback as tb

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
yescheck = ['yes','y','ye','ya','yah','yea','yeah','sure','ok','okay','uh huh','why not','alright','yep','yup']

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        try:
            city = str(input('Please enter which city (Chicago, New York City, Washington) you are interested in for exploring the bikeshare data: \n')).lower()
            if CITY_DATA.get(city) is not None:
                break
            print('That\'s not a valid entry, please enter one of these - Chicago, New York City, Washington - which are valid: \n')

        except:
            print('That\'s not a valid entry, please enter one of these - Chicago, New York City, Washington - which are valid: \n')

    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        try:
            # Defining the user input for the month
            month = str(input('Please enter your month of interest for exploring the bikeshare data. NOTE: valid entries are all, January, February, March, April, May, or June:  \n')).lower()
            # Setting up a list of the first six months in the year based on the given data files
            months = ['january', 'february', 'march', 'april', 'may', 'june']
            # Determining if a proper month string was entered, or if all was entered to proceed
            if (month == 'all') or (month in months):
                #breaking if the above criteria is met
                break
            # Else condition to throw an error message and have the user retry their entry again
            else:
# for testing to determine where the while loop is failing               print('boo')
                print('That\'s not a valid entry, please enter one of these - all, january, february, march, april, may, or june - which are valid:  \n') 
        # Except clause to accommodate any exceptions thrown
        except:           
            # traceback used for extra troubleshooting info
            print(tb.format_exc())
# for testing to determine where the while loop is failing            print('yah')
            print('That\'s not a valid entry, please enter one of these - all, january, february, march, april, may, or june - which are valid:  \n')


    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        try:
            # Defining the user input for the month
            day = str(input('Please enter which day of the week of interest for exploring the bikeshare data. NOTE: valid entries are all, monday, tuesday, wednesday, thursday, friday, saturday, or sunday: \n'))
            # Setting up a list of days in the week based on the given data files            
            days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
            # Determining if a proper day string was entered, or if all was entered to proceed
            if (day == 'all') or (day in days):
                #breaking if the above criteria is met
                break
            # Else condition to throw an error message and have the user retry their entry again
            else:
# for testing to determine where the while loop is failing               print('boo')
                print('That\'s not a valid entry, please enter one of these - all, january, february, march, april, may, or june - which are valid:  \n') 
        # Except clause to accommodate any exceptions thrown
        except:
            # Except clause to accommodate any exceptions thrown
            print(tb.format_exc())
# for testing to determine where the while loop is failing            print('yah')
            print('That\'s not a valid entry, please enter one of these - all, monday, tuesday, wednesday, thursday, friday, saturday, or sunday - which are valid: \n')

    # Print separator line of dashes
    print('-'*40)
    # Return the city, month, and day to the main function
    return city, month, day

def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
#    print('city is:{}\n'.format(city))
#    print('month is:{}\n'.format(month))
#    print('day is:{}\n'.format(day))
    # Load the data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])
#    print(df.head())
    # Used to view the actual dataframe    
    # Convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # Extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()
    # setting up the hour column in the dataframe using method dt.hour
    df['hour'] = df['Start Time'].dt.hour
#    print(df.head())
    # Filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        # filter by month to create the new dataframe
        df = df[df['month'] == month]
#        print(df.head())
    # filter by day of week if applicable
    if day != 'all':
#        print('day is '.format(day))
        # filter by day of week to create the new dataframe
#        daysofweek = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
#        day = daysofweek.index(day)
        df = df[df['day_of_week'] == day.title()]
#        print(df.head())
    return df

def time_stats(df,city,month,day,hour):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n\n')
    start_time = time.time()

    # TO DO: display the most common month
    # setting up the month counts using method value_counts for mocnt
    mocnt = df['month'].value_counts()
    # for testing to see what mocnt actually is    print(df['month'].value_counts())
    # Obtaining the maximum month value as first in the mocnt list
    maxmo = mocnt.index[0]
    if month != 'all':
        print('Your chosen month is {}. {} had {} rentals for {}.\n'.format(calendar.month_name[maxmo].title(),calendar.month_name[maxmo].title(),max(mocnt),city))
    else:
        print('The month of {} had the highest number of rentals in {} out of all months, and had {} rentals!\n'.format(calendar.month_name[maxmo].title(),city,max(mocnt)))
    

    # TO DO: display the most common day of week
    # setting up the day counts using method value_counts for dycnt
    dycnt = df['day_of_week'].value_counts()
    # for testing to see what mocnt actually is   print(dycnt)   
    maxdy = dycnt.index[0]
    if day != 'all':
        print('Your chosen day is {}. {} had {} rentals for the city of {}.\n'.format(maxdy.title(),maxdy.title(),max(dycnt),city))
    else:
        print('{} had the highest number of rentals out of all the days and had {} rentals from all {}s totaled!\n'.format(maxdy.title(),max(dycnt),maxdy.title()))
    
    # TO DO: display the most common start hour   
    # setting up the hour counts using method value_counts for hrcnt
    hrcnt = df['hour'].value_counts()
    print('Based on your choices of Month = {} and Day = {}, the top 5 rental hours with highest total rentals in {} are:'.format(month.title(),day.title(),city))
    print(df['hour'].value_counts().head(5))
    # Display the data in graphical format using pyplot for a bar graph
    df['hour'].value_counts().head(5).plot(kind='bar').legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0.)
    plt.title('Top 5 Rental Hours')
    plt.show()
    # for testing to see what mocnt actually is    
    # Obtaining the maximum month value as first in the mocnt list
    maxhr = hrcnt.index[0]
    print('\nAlso, as can be seen in the top 5 above, the {} hour had the highest number of rentals in {} and had {} total rentals for all {} hour values totaled!'.format(maxhr,city,max(hrcnt),maxhr))

    # Setting up the loop to handle user input for multiple viewings of 5 results respectively
    # Using stloc as starting point for next 5 selection if user selects to view next 5
    stloc = 5
    # Input for user selection to choose next 5 or no
    yesdat = input('\nWould you like to view 5 more rows of individual rental hour data?  Enter yes or no\n')
    while yesdat.lower() != 'no':
        # Using if statement to break out of the while loop if no is chosen, or looping back if yes
        if yesdat.lower() == 'no':
            break
            # Checking yescheck condition and, if met, printing 5 lines of the dataframe and adding 5 to stloc variable for looping back to print the next 5 lines
        elif (yesdat.lower() in yescheck):  
            print(hrcnt[stloc:stloc+5])
            stloc += 5
            # Ask if the user wants to view an additional 5 values
            yesdat = input('\nWould you like to view 5 more rows of individual rental hour data?  Enter yes or no\n')
            # Else condition to throw an error message and have the user retry their entry again
        else:
            yesdat = input('That\'s not a valid entry, please enter yes or no:\n')             

    print("\n\nThis took %s seconds." % (time.time() - start_time))
    print('-'*80)

def station_stats(df,city,month,day):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    # Printing the top 5 most common starting stations based on input using value_counts() function
    print('Based on your choices of Month = {} and Day = {}, the top 5 most common starting stations with highest total rentals in {} are:'.format(month.title(),day.title(),city))
    # Assigning variables stst the value_counts() based on input and reading the top one in ststmax
    stst = df['Start Station'].value_counts()
    ststmax = stst.index[0]
    print(stst.head(5))
    # Display the data in graphical format using pyplot for a bar graph
    stst.head(5).plot(kind='bar').legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0.)
    plt.title('Top 5 Most Common Starting Stations')
    plt.show()

    # Setting up the loop to handle user input for multiple viewings of 5 results respectively
    # Using stloc as starting point for next 5 selection if user selects to view next 5
    stloc = 5
    # Input for user selection to choose next 5 or no
    yesdat = input('\nWould you like to view 5 more rows of individual Starting Station rental data?  Enter yes or no\n')
    while yesdat.lower() != 'no':
        # Using if statement to break out of the while loop if no is chosen, or looping back if yes
        if yesdat.lower() == 'no':
            break
            # Checking yescheck condition and, if met, printing 5 lines of the dataframe and adding 5 to stloc variable for looping back to print the next 5 lines
        elif (yesdat.lower() in yescheck):  
            print(stst[stloc:stloc+5])
            stloc += 5
            # Ask if the user wants to view an additional 5 values
            yesdat = input('\nWould you like to view 5 more rows of individual Starting Station rental data?  Enter yes or no\n')
            # Else condition to throw an error message and have the user retry their entry again
        else:
            yesdat = input('That\'s not a valid entry, please enter yes or no:\n')             


    # Using if/elif/else statements to consider all the possibilities for whether month and day are all or not
    if month != 'all' and day != 'all':
        print("\nFor all {}'s for the month of {}, {} was the most common starting station for riders with {} rentals in {}.\n".format(day.title(),month.title(),ststmax,max(stst),city))
    elif month != 'all':
        print("\nFor all days in the month of {}, {} was the most common starting station for riders with {} rentals in {}.\n".format(month.title(),ststmax,max(stst),city))
    elif day != 'all':
        print("\nFor all {}'s from January to June, {} was the most common starting station for riders with {} rentals in {}.\n".format(day.title(),ststmax,max(stst),city))
    else:
        print("\nFor all days from January to June, {} was the most common starting station for riders with {} rentals in {}.\n".format(ststmax,max(stst),city))
        

    # TO DO: display most commonly used end station
    # Printing the top 5 most common ending stations based on input using value_counts() function
    print('Based on your choices of Month = {} and Day = {}, the top 5 most common ending stations with highest total rentals in {} are:'.format(month.title(),day.title(),city))
    # Assigning variables endst the value_counts() based on input and reading the top one in endstmax
    endst = df['End Station'].value_counts()
    endstmax = endst.index[0]
    print(endst.head(5))
    # Display the data in graphical format using pyplot for a bar graph
    endst.head(5).plot(kind='bar').legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0.)
    plt.title('Top 5 Most Common Ending Stations')
    plt.show()

    # Setting up the loop to handle user input for multiple viewings of 5 results respectively
    # Using stloc as starting point for next 5 selection if user selects to view next 5
    stloc = 5
    # Input for user selection to choose next 5 or no
    yesdat = input('\nWould you like to view 5 more rows of individual Ending Station rental data?  Enter yes or no\n')
    while yesdat.lower() != 'no':
        # Using if statement to break out of the while loop if no is chosen, or looping back if yes
        if yesdat.lower() == 'no':
            break
            # Checking yescheck condition and, if met, printing 5 lines of the dataframe and adding 5 to stloc variable for looping back to print the next 5 lines
        elif (yesdat.lower() in yescheck):  
            print(endst[stloc:stloc+5])
            stloc += 5
            # Ask if the user wants to view an additional 5 values
            yesdat = input('\nWould you like to view 5 more rows of individual Ending Station rental data?  Enter yes or no\n')
            # Else condition to throw an error message and have the user retry their entry again
        else:
            yesdat = input('That\'s not a valid entry, please enter yes or no:\n')             

    # Using if/elif/else statements to consider all the possibilities for whether month and day are all or not
    if month != 'all' and day != 'all':
        print("\nFor all {}'s for the month of {}, {} was the most common ending station for riders with {} rentals in {}.\n".format(day.title(),month.title(),endstmax,max(endst),city))
    elif month != 'all':
        print("\nFor all days in the month of {}, {} was the most common ending station for riders with {} rentals in {}.\n".format(month.title(),endstmax,max(endst),city))
    elif day != 'all':
        print("\nFor all {}'s from January to June, {} was the most common ending station for riders with {} rentals in {}.\n".format(day.title(),endstmax,max(endst),city))
    else:
        print("\nFor all days from January to June, {} was the most common ending station for riders with {} rentals in {}.\n".format(endstmax,max(endst),city))


    # TO DO: display most frequent combination of start station and end station trip
    # Setting options to better view the dataframe contents
    # pd.set_option('display.max_rows', None)
    # pd.set_option('display.max_columns', 20)
    # pd.set_option('display.max_colwidth', 10)
    # pd.set_option('display.width', None)
    # Combining Start and End Stations in one unique column to count all and find the most common pairing
    df['stendcombo'] = df['Start Station'] +',' + df['End Station']
    # Assigning variables stendcombocnt the value_counts() based on input and reading the top one in stendcombomax
    stendcombocnt = df['stendcombo'].value_counts()
    # Printing the first 4 listings in stendcombocnt to see results - print(stendcombocnt.head(4))
    stendcombomax = stendcombocnt.index[0]
    # Printing stendcombomax to verify results - print(stendcombomax)
    # Finding the number of rows in the df - print('Number of rows in Dataframe : ', len(df.index))
    # Printing the first 20 to see results - print(df['stendcombo'].value_counts().head(20))
    # Using split parts of stendcombomax to show the most used combo of Start and End Stations
    print('\nBased on the selections, the most commonly used Start and End Station combination consists of these two Stations:')
    print('Start Station: {}'.format(stendcombomax.split(',')[0]))
    print('End Station: {}'.format(stendcombomax.split(',')[1]))
    print('Having {} total round trips!'.format(stendcombocnt[0]))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*80)

def convert(seconds):
    return time.strftime("%d:%H:%M:%S", time.gmtime(seconds)) 

def trip_duration_stats(df,day,month,city):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    # Calculate total travel time for all trips based on user selections using the sum() function on the Trip Duration column in the dataset
    travtime = df['Trip Duration'].sum()
    # Using if/elif/else statements to consider all the possibilities for whether month and day are all or not
    if month != 'all' and day != 'all':
        print("\nFor all {}'s for the month of {}, the total travel time for all rentals was {} (dd,hh,mm,ss) in {}.\n".format(day.title(),month.title(),convert(travtime),city))
    elif month != 'all':
        print("\nFor all days in the month of {}, the total travel time for all rentals was {} (dd,hh,mm,ss) in {}.\n".format(month.title(),convert(travtime),city))
    elif day != 'all':
        print("\nFor all {}'s from January to June, the total travel time for all rentals was {} (dd,hh,mm,ss) in {}.\n".format(day.title(),convert(travtime),city))
    else:
        print("\nFor all days from January to June, the total travel time for all rentals was {} (dd,hh,mm,ss) in {}.\n".format(convert(travtime),city))


    # TO DO: display mean travel time
    # Calculate mean travel time for all trips based on user selections using the mean() function on the Trip Duration column in the dataset
    meantime = df['Trip Duration'].mean()
    # Using if/elif/else statements to consider all the possibilities for whether month and day are all or not
    if month != 'all' and day != 'all':
        print("\nFor all {}'s for the month of {}, the mean travel time for all rentals was {} (dd,hh,mm,ss) in {}.\n".format(day.title(),month.title(),convert(meantime),city))
    elif month != 'all':
        print("\nFor all days in the month of {}, the mean travel time for all rentals was {} (dd,hh,mm,ss) in {}.\n".format(month.title(),convert(meantime),city))
    elif day != 'all':
        print("\nFor all {}'s from January to June, the mean travel time for all rentals was {} (dd,hh,mm,ss) in {}.\n".format(day.title(),convert(meantime),city))
    else:
        print("\nFor all days from January to June, the mean travel time for all rentals was {} (dd,hh,mm,ss) in {}.\n".format(convert(meantime),city))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df,day,month,city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    # Assigning variable usertype the value_counts()
    usertype = df['User Type'].value_counts()
    # Using if/elif/else statements to consider all the possibilities for whether month and day are all or not
    if month != 'all' and day != 'all':
        print("\nFor all {}'s for the month of {}, these are the User Types and rental counts below for {}:".format(day.title(),month.title(),city))
        print(usertype)
    elif month != 'all':
        print("\nFor all days in the month of {}, these are the User Types and rental counts below for {}:".format(month.title(),city))
        print(usertype)
    elif day != 'all':
        print("\nFor all {}'s from January to June, these are the User Types and rental counts below for {}:".format(day.title(),city))
        print(usertype)
    else:
        print("\nFor all days from January to June, these are the User Types and rental counts below for {}:".format(city))
        print(usertype)


    # TO DO: Display counts of gender
    
    while True: 
        try:
            # Assigning variable gender the value_counts()
            gender = df['Gender'].value_counts()
            # Using if/elif/else statements to consider all the possibilities for whether month and day are all or not
            if month != 'all' and day != 'all':
                print("\nFor all {}'s for the month of {}, these are the Genders of renters and rental counts below for {}:".format(day.title(),month.title(),city))
                print(gender)
                break
            elif month != 'all':
                print("\nFor all days in the month of {}, these are the Genders of renters and rental counts below for {}:".format(month.title(),city))
                print(gender)
                break
            elif day != 'all':
                print("\nFor all {}'s from January to June, these are the Genders of renters and rental counts below for {}:".format(day.title(),city))
                print(gender)
                break
            else:
                print("\nFor all days from January to June, these are the Genders of renters and rental counts below for {}:".format(city))
                print(gender)
                break
        except:
            print('\n{} has no Gender data. Moving to next set of info.\n'.format(city.title()))
            break


    # TO DO: Display earliest, most recent, and most common year of birth
    # Assigning variable eyear for min() value, lyear for max() value, and maxyear for the max() of the value_counts()
    while True:
        try:
            eyear = df['Birth Year'].min()
            lyear = df['Birth Year'].max()
            maxyear = df['Birth Year'].value_counts().index[0]
            # Using if/elif/else statements to consider all the possibilities for whether month and day are all or not
            if month != 'all' and day != 'all':
                print("\nFor all {}'s for the month of {}, these are the earliest, most recent, and most common year of birth for {}:".format(day.title(),month.title(),city))
                print('Earliest Birth Year of riders: {}'.format(eyear))
                print('Most Recent Birth Year of riders: {}'.format(lyear))
                print('Most Common Birth Year of riders: {}'.format(maxyear))
                break
            elif month != 'all':
                print("\nFor all days in the month of {}, these are the earliest, most recent, and most common year of birth for {}:".format(month.title(),city))
                print('Earliest Birth Year of riders: {}'.format(eyear))
                print('Most Recent Birth Year of riders: {}'.format(lyear))
                print('Most Common Birth Year of riders: {}'.format(maxyear))
                break
            elif day != 'all':
                print("\nFor all {}'s from January to June, these are the earliest, most recent, and most common year of birth for {}:".format(day.title(),city))
                print('Earliest Birth Year of riders: {}'.format(eyear))
                print('Most Recent Birth Year of riders: {}'.format(lyear))
                print('Most Common Birth Year of riders: {}'.format(maxyear))
                break
            else:
                print("\nFor all days from January to June, these are the earliest, most recent, and most common year of birth for {}:".format(city))
                print('Earliest Birth Year of riders: {}'.format(eyear))
                print('Most Recent Birth Year of riders: {}'.format(lyear))
                print('Most Common Birth Year of riders: {}'.format(maxyear))
                break
        except:
            print('{} has no Birth Year data.\n'.format(city.title()))
            break


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_data(df):
    stloc=0
    yesdat=input('Would you like to display 5 rows of raw data? Please enter yes or no:\n').lower()
    while yesdat.lower() != 'no':
        # Using if statement to break out of the while loop if no is chosen, or possibly looping back if yes
        if yesdat.lower() == 'no':
            break
            # Checking yescheck condition and, if met, printing 5 lines of the dataframe and adding 5 to stloc variable for looping back to print the next 5 lines
        elif (yesdat.lower() in yescheck):            
            # Setting options to better view the dataframe contents
            pd.set_option('display.max_columns', 20)
            pd.set_option('display.max_colwidth', 40)
            print(df.iloc[stloc:stloc+5])
            stloc += 5
            # Asking if the user wants to view an additional 5 values
            yesdat = input('\nWould you like to view 5 more rows of raw data? Please enter yes or no:\n')
            # Else condition to throw an error message and have the user retry their entry again
        else:
            yesdat = input('That\'s not a valid entry, please enter yes or no:\n') 

            
def main():
    while True:

        # Obtaining the city, month, and day of interest based on the user input in the get_filters function
        city, month, day = get_filters()

        # Building the dataframe based on the returned values of city, month, and day based on the user input
        df = load_data(city, month, day)
        # for testing to check the dataframe       print(df.head())
        hour = df['hour']
        # Obtaining the required time stats to meet the rubric using the time_stats function
        time_stats(df,city,month,day,hour)
        
        # Obtaining the required station stats to meet the rubric using the station_stats function
        station_stats(df,city,month,day)
        
        # Obtaining the trip duration stats to meet the rubric using the trip_duration_stats function
        trip_duration_stats(df,day,month,city)
        
        # Obtaining the user stats to meet the rubric using the user_stats function
        user_stats(df,day,month,city)
        
        # Sending the dataframe to ask the user if they would like to see 5 lines of raw data at a time
        display_data(df)
        
        restart = input('\nWould you like to investigate the bikeshare data further? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break

if __name__ == "__main__":
    main()