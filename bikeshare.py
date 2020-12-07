import time
import pandas as pd
import numpy as np

city_data = { 'Chicago': 'chicago.csv',
              'New York': 'new_york_city.csv',
              'Washington': 'washington.csv' }

months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

city = ''
month = ''
day = ''

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
    #Calling the global variables city, day and month to permit updates:
    global city, day, month
    
    while(True):
        city = input("Would you like to see data for New York, Chicago or Washington?\n").title()
        if city in ['New York', 'Chicago', 'Washington']:
            break
        print("!!!\nOops! Your input is invalid. Let's try again by writing only one of the 3 citis listed above!")
        
    # TO DO: get user input for month (all, january, february, ... , june)
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while(True):
        filter_by = input("Would you like to filter the date by month, day, both or not at all? Type 'none' for no time filter.\n").title()
        if filter_by not in ['Month', 'Day', 'Both', 'None']:
            print("!!!\nYour input is invalid. Let's try again by wiriting only one of the 4 options!")
            continue
        elif filter_by == 'Both':
            month = input("Which month would you like to filter by (January, February, ... , June)?\n").title()
            day = input("Which day of week would you like to filter by (Monday, Tuesdat, ... Sunday)?\n").title()
            if (month in months) and (day in days):
                break
        elif filter_by == 'Month':
            month = input("Which month would you like to filter by (January, February, ... , June)?\n").title()
            if month in months:
                break
        elif filter_by == 'Day':
            day = input("Which day of week would you like to filter by (Monday, Tuesdat, ... Sunday)?\n").title()
            if day in days:
                break
        elif filter_by == 'None':
            month = 'All'
            day = 'All'
            break
            
        print("!!!\nThe month/day you entered is incorrect. Are you sure you spelled it correctly? Let's try again!")

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
    df = pd.read_csv(city_data[city])
    # Converting the Start Time column to datetime:
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    # Extracting month and day of week from Start Time column to create two new columns:
    df['Month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # Filtering by month:
    if month != 'All':
        month = months.index(month) + 1
        # Updating/filtering the dataframe based on the chosen month:
        df = df[df['Month'] == month]

    # Filtering by day of week:
    if day != 'All':
        df = df[df['day_of_week'] == day]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    if month == 'All':
    # TO DO: display the most common month
        popular_month = df['Month'].mode()[0]
        print("Most common month: " + str(popular_month))
    
    if day == 'All':
    # TO DO: display the most common day of week
        popular_day = df['day_of_week'].mode()[0]
        print("Most common day of week: " + str(popular_day))
    
    # TO DO: display the most common start hour
    #Creating a new column to extract hour out of Start Time column:
    df['hour'] = df['Start Time'].dt.hour
    #Finding the most common hour:
    popular_hour = df['hour'].mode()[0]
    print("Most common start hour: " + str(popular_hour))
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    start_station = df['Start Station'].mode()[0]
    print("Most commonly used start station: " + str(start_station))
    
    # TO DO: display most commonly used end station
    end_station = df['End Station'].mode()[0]
    print("Most commonly used end station: " + str(end_station))

    # TO DO: display most frequent combination of start station and end station trip
    df['start_end'] = df['Start Station'] + '-' + df['End Station']
    frequent_comb = df['start_end'].mode()[0]
    print("Most frequent combination of start-end station: " + str(frequent_comb))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel = np.sum(df['Trip Duration'])
    print("Total travel time = ", total_travel)

    # TO DO: display mean travel time
    avg_travel = np.mean(df['Trip Duration'])
    print("Average travel time = ", avg_travel)
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print("User types and their counts:")
    print(user_types)
    
    if city in ['Chicago', 'New York']:
    # TO DO: Display counts of gender
        users_gender = df['Gender'].value_counts()
        print("Users' genders and their counts:")
        print(users_gender)

    # TO DO: Display earliest, most recent, and most common year of birth
        earliest_year = np.min(df['Birth Year'])
        recent_year = df['Birth Year'].iloc[-1]
        common_year = df['Birth Year'].mode()[0]
        print("The earliest registered birth year: " + str(earliest_year))
        print("The most recent registered birth year: " + str(recent_year))
        print("The most common registered birth year: " + str(common_year))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def raw_data(df):
    i = 0
    rows = df.shape[0]
    while(True):
        user_input =  input("\nWould you like to view trip data? Enter 'yes' or 'no'\n")
        if user_input.title() == 'No':
            break
        elif user_input.title() == 'Yes':
            if i+5 < rows:
                print(df.iloc[i:i+5])
                i= i+ 5
            elif i < rows:
                print(df.iloc[i:])
            else: #Displaying a message to the user when all data have been viewd
                print("\n-----We have reached the end of data!----")
        else:
            print("\nI'm sorry I didn't understand your input. Let's try again!")
            

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
