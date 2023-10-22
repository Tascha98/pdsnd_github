#!/usr/bin/env python
# coding: utf-8

# In[1]:


import time
import pandas as pd
import numpy as np


CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

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
        city = input("Time to select a city! Would you like to see data for Chicago, New York, or Washington? ").lower()
        #city input made case insensitive
        
        # invalid input handling for city
        if city not in ('new york city', 'chicago', 'washington'):
            print("Incorrect input. Please choose from Chicago, New York, or Washington.")
            continue
        else:
            break

    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month = input("Choose any month from January to June, type full name (all, january, february, ...): ").lower()
        # month input made case-insensitive
        
        
        # invalid input handling for month
        if month not in ('january', 'february', 'march', 'april', 'may', 
                         'june', 'all'):
            print("Incorrect input. Please choose a month within range/ensure right spelling/ or 'all'.")
            continue
        else:
            break

    # get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input("Enter a day of the week, type full name (all, monday, tuesday, ...): ").lower()
        # make entries case-insensitive and use small letters
        
        
        # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
        if day not in ('monday', 'tuesday', 'wednesday', 'thursday', 'friday',
                       'saturday', 'sunday', 'all'):
            print("Incorrect entry, please choose a valid day of the week.")
            continue
        else:
            break

    print('-'*40)
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
    # 1. read the dataframe of the selected city
    df = pd.read_csv(CITY_DATA[city])
    
    # 2. Conversion of Start Time to a datetime object to obtain your months/days/hours etc
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    
    # 3. Creating new columns that contain month and day in dataframe
    df['Month'] = df['Start Time'].dt.month
    df['Weekday'] = df['Start Time'].dt.weekday
    
    # 4. filtering of dataset, based on selections
    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        df = df[df['Month'] == month]
    
    if day != 'all':
        days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
        day = days.index(day) 
        df = df[df['Weekday'] == day]
    
    return df

def time_stats(df, city, month, day):
    """Displays statistics on the most frequent times of travel."""
    
    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # List of full month and day names in lowercase
    month_names = ['january', 'february', 'march', 'april', 'may', 'june']
    day_names = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']

    # Determine the most common month
    most_common_month = df['Month'].mode()[0]

    # TO DO: display the most common month
    if month != 'all':
        print(f"Since you selected '{month}' for the month, that will be the common month in {city.title()}.\n")
    else:
        print(f'The most common month in {city.title()} is {most_common_month}.\n')

    # Determine the most common day of the week
    most_common_day = df['Weekday'].mode()[0]

    # TO DO: display the most common day of week
    if day != 'all':
        print(f"Since you selected '{day}' for the day, that will be the common day in {city.title()}.\n")
    else:
        print(f'The most common day of the week is {most_common_day}.\n')

    # Determine the most common start hour
    df['Start Hour'] = df['Start Time'].dt.hour 
    most_common_start_hour = df['Start Hour'].mode()[0]

    # TO DO: display the most common start hour
    print(f'The most common start hour for your selection is {most_common_start_hour} o\'clock.\n')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    most_common_start_station = df['Start Station'].mode()[0]
    print('The most common start station for your selection is', most_common_start_station, '.\n\n')

    # TO DO: display most commonly used end station
    most_common_end_station = df['End Station'].mode()[0]
    print('The most commonly used end station is', most_common_end_station, '.\n\n')
    
    # calculating combination of start & end station trip by combining both in new column
    df['Station Combination'] = df['Start Station'] + ' (start) and ' + df['End Station'] + ' (end).'
    
    # TO DO: display most frequent combination of start station and end station trip
    most_common_station_combination = df['Station Combination'].mode()[0]
    print('The most common station combination for your selection is', most_common_station_combination, '\n')


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time  
    total_travel_time = df['Trip Duration'].sum()
    print('The total travel time is {} seconds'.format(total_travel_time))
    
    # TO DO: display mean travel time
    avg_travel_time = df['Trip Duration'].mean()
    print('The mean travel time is {} seconds'.format(avg_travel_time))
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df, city):
    """Displays statistics on bikeshare users. Statistics will be calculated using NumPy."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print('The user type counts in {} are as follows:\n{}'.format(city, df['User Type'].value_counts()))

    # TO DO: Display counts of gender
    if 'Gender' in df:
        gender = df['Gender'].value_counts()
        print('The gender counts in {} are as follows:\n{}'.format(city, gender))
    else:
        print('Gender data is not available for {}.\n'.format(city))

    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df:
        earliest_birth_year = df['Birth Year'].min()
        recent_birth_year = df['Birth Year'].max()
        common_birth_year = df['Birth Year'].mode()[0]

        print('The earliest birth year in {} is {}'.format(city, int(earliest_birth_year)))
        print('The most recent birth year in {} is {}'.format(city, int(recent_birth_year)))
        print('The most common year of birth in {} is {}'.format(city, int(common_birth_year)))
    else:
        print('Birth Year data is not available for {}.\n'.format(city))
    
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

# function for displaying 5 rows of data    
def raw_data(df):
    """ Displays 5 lines of raw data at a time when 'yes' is selected."""

    while True:
        rawdata = input('\nWould you like to see 5 lines of raw data? Enter yes or no.\n')
        if rawdata.lower() == 'yes':
            # Display 5 lines of raw data and increment index
            print(df.head(5))
            df = df.iloc[5:]
        else:
            break  # Exit the raw data display loop if the user enters 'no'

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        
        time_stats(df, city, month, day)
        station_stats(df)
        trip_duration_stats(df)
        
        user_stats(df, city)
        
        #function to display raw data
        raw_data(df)
        
  
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()


# In[ ]:





# In[ ]:




