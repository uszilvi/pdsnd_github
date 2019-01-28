#corrected version, Szilvia Ujvarosi, 01/08/2019
import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york': 'new_york_city.csv',
              'washington': 'washington.csv'}

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        #(str) city - name of the city to analyze
        #(str) month - name of the month to filter by, or "all" to apply no month filter
        #(str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (Chicago, New York, Washington).
    while True:
        city= input('Would you like to see data for Chicago, New York, or Washington?:\n').lower()
        if city not in ('chicago', 'new york', 'washington'):
            print('Please correct your input. Enter: Chicago, New York, or Washington')
            continue
        else:
            break

    # get user input for month
    while True:
        month= input('Which month would you like to filter the data by? \nJanuary, February, March, April, May or June. Please type all if you do not wish to filter the data by a specific month:\n').lower()
        if month not in ('january', 'february', 'march', 'april', 'may', 'june', 'all'):
            print('Please correct your input.')
            continue
        else:
            break

    # get user input for day of week
    while True:
        day= input("Which day would you like to filter the data by (e.g., Sunday) ? \nPlease type all if you don't want to filter the data by a specific day:\n").lower()
        if day not in ('monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all'):
            print('Please correct your input.')
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
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        df = df[df['month'] == month]

    if day != 'all':
        df = df[df['day_of_week'] == day.title()]

    return df

def time_stats_3filters(df):
    """Displays statistics on the most frequent times of travel -filters: city, month, day"""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    Common_hour = df['hour'].mode()[0]
    print("Most Common Start Hour is: {}".format(Common_hour))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def time_stats_2filtersm(df):
    """Displays statistics on the most frequent times of travel -filters: city, month, day=all."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common day of week
    Common_day = df['day_of_week'].mode()[0]
    print("Most Common Day of Week: {}".format(Common_day))

    # display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    Common_hour = df['hour'].mode()[0]
    print("Most Common Start Hour: {}".format(Common_hour))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def time_stats_2filtersd(df):
    """Displays statistics on the most frequent times of travel -filters: city, month=all, day."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

     # display the most common month
    Common_month = df['month'].mode()[0]
    print("Most Common Month: {}".format(Common_month))

    # display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    Common_hour = df['hour'].mode()[0]
    print("Most Common Start Hour: {}".format(Common_hour))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def time_stats_1filter(df):
    """Displays statistics on the most frequent times of travel -filters: city, month=all, day=all."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    Common_month = df['month'].mode()[0]
    print("Most Common Month: {}".format(Common_month))

    # display the most common day of week
    Common_day = df['day_of_week'].mode()[0]
    print("Most Common Day of Week: {}".format(Common_day))

    # display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    Common_hour = df['hour'].mode()[0]
    print("Most Common Start Hour: {}".format(Common_hour))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    Common_start_station = df['Start Station'].mode()[0]
    print("Most Commonly used start station is: {}".format(Common_start_station))

    # display most commonly used end station
    Common_end_station = df['End Station'].mode()[0]
    print("Most Commonly used end station is: {}".format(Common_end_station))

    # display most frequent combination of start station and end station trip
    df ['Start_end_station'] = df['Start Station'] + df['End Station']
    Common_startend_station = df['Start_end_station'].mode()[0]
    print("Most frequent combination of start station and end station is: {}".format(Common_startend_station))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    Total_travel_time = sum(df['Trip Duration'])
    Count_travels = df.shape[0]

    print("The total travel time is: {} seconds, Count : {}".format(Total_travel_time, Count_travels))

    # display mean travel time
    Mean_travel_time = sum(df['Trip Duration'])/len(df['Trip Duration'])
    print("The mean travel time is: {} seconds/trip".format(Mean_travel_time))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # display counts of user types
    User_types = df['User Type'].value_counts()
    print(User_types)

    # display counts of gender
    Male_or_female = df['Gender'].value_counts()
    print(Male_or_female)

    # display earliest, most recent, and most common year of birth
    Earliest_year = int(min(df['Birth Year']))
    print("The earliest year of birth is: {}".format(Earliest_year))
    Most_recent_year = int(max(df['Birth Year']))
    print("The most recent year of birth is: {}".format(Most_recent_year))
    Common_year = int(df['Birth Year'].mode()[0])
    print("Most common year of birth is: {}".format(Common_year))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def user_stats_type(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # display counts of user types
    User_types = df['User Type'].value_counts()
    print(User_types)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        #display the first 5 rows of data to the user if they say yes
        raw_data = input('\nWould you like to see the first 5 lines of raw data? Enter yes or no.\n')

        if raw_data.lower() == 'yes':
            print(df.head())

        #display 5 rows of data to the user till they say no
            if len(df) % 5 == 0:
                blocknr = len(df) // 5
            else:
                blocknr = int(len(df) // 5) + 1

            for i in range(1, blocknr):
                raw_data2 = input('\nWould you like to see 5 more lines of raw data? Enter yes or no.\n')

                if raw_data2.lower() == 'yes':
                    print( df.iloc[i*5:min(len(df), (i+1)*5)].head())
                    i += 1
                else:
                    break
        else:
            pass

        if month != 'all' and day != 'all':
            time_stats_3filters(df)
        elif month != 'all' and day == 'all':
            time_stats_2filtersm(df)
        elif month == 'all' and day != 'all':
            time_stats_2filtersd(df)
        else:
            time_stats_1filter(df)

        station_stats(df)
        trip_duration_stats(df)

        if city == 'washington':
            user_stats_type(df)
            print("Age and gender information are not available for Washington.")
        else:
            user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break

if __name__ == "__main__":
	main()
