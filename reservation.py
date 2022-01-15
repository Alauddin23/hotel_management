# Name: Md Alauddin Siddiqui
# McGill ID: 260951950

# importing the random module

import random

# importing the datetime module

import datetime

# importing Room, MONTHS, DAYS_PER_MONTH from the room module

from room import Room, MONTHS, DAYS_PER_MONTH

# creating a function which will take two integers, 1st integer represents the year number, and the 2nd integer represents
# the number of the month
# The function returns True if the month and year entered represents the month of February in a leap year and False otherwise

def helper_is_leap_year_Feb(year_integer, month_integer):
    
# First, we check whether the entered month integer represents the month of February or not 
    
    if month_integer != 2:
        
        return False
    
    else:
        
# The function then checks if the year_integer is evenly divisible by 4 or not , if not the function returns False
        
        if (year_integer % 4) != 0:
            
            return False
        
# Then the function checks whether the year which is already divisible by 4 is divisible by 100 or not, if not the function returns True
        
        else:
            
            if not ((year_integer % 100 ) == 0):
                
                return True
            
# Finally, the function checks the year which is already divisible by 4 and 100 is also divisible by 400 or not
# If yes, the function returns True and False otherwise
            
            else:
                
                if (year_integer % 400 ) == 0:
                    
                    return True
                
                else:
                    
                    return False 
    

# creating a class called Reservation which contains instance attributes that include
# booking_number (an integer), name(a string), room_reserved (a Room), check_in (a date) and check_out (a date)
# It also contains a Class attribute called booking_numbers initialized with an empty list that will contain booking numbers
# generated when reservations are made

class Reservation:
    
# creating the class attribute which by default is placed at the top just below the class header

    booking_numbers = []
    
# creating a constructor that takes as input a string, a room, two dates (representing the check in and check out respectively)
# and an optional integer representing a booking number
# if last input not provided, default value should be None

    def __init__(self, name, room_reserved, check_in, check_out, booking_number = None):
        
# The constructor raises an AssertionError if the input room is not available at the specified dates, this is checked by the
# instance method is_available which takes two date objects as input, with the first one representing the check-in date and the later one
# representing the check-out date, the method returns True if the room is available for all nights with check-in night included and
# check-out night excluded

        if not (room_reserved.is_available(check_in, check_out)):
            
            raise AssertionError ("The specified room is not available for the specified dates")
                   
# If the specified room is available for the specified dates, the constructor uses the provided inputs to initialize all the instance
# attributes acccordingly

        self.name = name
        
        self.room_reserved = room_reserved
        
        self.check_in = check_in
        
        self.check_out = check_out
        
# If the booking number is not provided, then the constructor generates a new random 13 - digit number for this reservation
# It means the number generated should not already be a part of the list of booking numbers in the class attribute
# The constructor should also update the class attribute accordingly
# We have to make sure the booking numbers cannot have leading zeros

        if booking_number == None:
            
            random_13digit_booking_number = random.randint(1000000000000, 9999999999999)
            
# The constructor continues to generate a new 13-digit random number till the random number generated is not in the list in the
# class attribute booking_numbers and the random number does not contain any leading zeros
# we create a while loop to do this task

# Since, random_13digit_booking_number is an integer we cannot slice this, however since its an integer we can convert it to string
# and then check whether the random number has a leading zero or not 

            while ((random_13digit_booking_number in Reservation.booking_numbers) or ((str(random_13digit_booking_number))[0] == 0)):
                
                random_13digit_booking_number = random.randint(1000000000000, 9999999999999)
                
# The constructor then updates the class attribute accordingly and adds the random 13-digit number after ensuring the number is
# not in the list booking_numebrs nor it has a leading zero

            Reservation.booking_numbers.append(random_13digit_booking_number)
            
            self.booking_number = random_13digit_booking_number
            
# If the booking number is provided, the constructor raises an AssertionError if such number had already been used or if it is not a
# 13 digit number 
            
        else:
            
            if len((str(booking_number))) != 13:
                raise AssertionError ("The booking number given as input is not valid as it does not contain 13 digits")
            
            if (booking_number in Reservation.booking_numbers):
                raise AssertionError ("The booking number given as input is already in use")
            
            self.booking_number = booking_number
            
# The constructor now should make sure to reserve the specified room for all nights from the check-in date (included) to check-out
# date (excluded)

# The constructor now considers the fact when the check-in month and check-out month are in the same month and they are in the same year

        if ((check_in.year),(check_in.month)) == ((check_out.year),(check_out.month)):
            
            day_of_check_in_month = check_in.day
            
            room_reserved.reserve_room(datetime.date(check_in.year, check_in.month, day_of_check_in_month))
            
            day_of_check_in_month += 1
            
# The constructor uses a while loop to make for each night from check-in night to the night before check-out, the room is reserved 
            
            while ( day_of_check_in_month != check_out.day):
                
                room_reserved.reserve_room(datetime.date(check_in.year, check_in.month, day_of_check_in_month))
                
                day_of_check_in_month += 1
                
# Now, the constructor checks for the situation when the check-in (year,month) is different from check-out (year, month)         
        
        else:
            
# The constructor first reserves the rooms for the check-in month
# Since, we have already made sure the rooms are available for all the specified nights, we can directly work with the list in the
# value of the dictionary in the availability attribute of Room objects

            day_of_check_in_month = check_in.day
            
            room_reserved.reserve_room(datetime.date(check_in.year, check_in.month, day_of_check_in_month))
            
            day_of_check_in_month += 1
            
            counter = 0 
            
            while ( counter < len(room_reserved.availability[((check_in.year),(check_in.month))][(check_in.day + 1):])):
                
                room_reserved.reserve_room(datetime.date(check_in.year, check_in.month, day_of_check_in_month))
                
                day_of_check_in_month += 1
                
                counter += 1
                
# The constructor now takes into consideration the months between the check-in month and the check-out month as they are both accounted
# seperately

            month = check_in.month
            
            year = check_in.year
            
            if month == 12:
                
                month = 1
                year += 1
                
            else:
                
                month +=1
                    
            while ((year),(month)) != ((check_out.year),(check_out.month)):
                
                day = 1
                
                room_reserved.reserve_room(datetime.date(year, month, day))
                
                day += 1
                
                counter1 = 0
                
# Here, we make sure that the while loop is iterated 2 less times than the entire length of the list in the value of the dictionary
# in the availability attribute of the room object as in the length both the 1st element None and the second element is taken into
# consideration, however we have to exclude them as we already taken them into account 
                
                while (counter1 < (len(room_reserved.availability[((year),(month))]) - 2)):
                       
                    room_reserved.reserve_room(datetime.date(year, month, day))
                       
                    day += 1
                       
                    counter1 += 1
                    
                if month == 12:
                    
                    month = 1
                    year += 1
                    
                else:
                    
                    month += 1
                    
# The constructor now reserves room for every night in the check-out month before the check-out
# However, the check-out day can also be the first day of the month and thus we also take that into consideration

            if (not(check_out.day == 1)):
    
                check_out_month_day = 1
        
                room_reserved.reserve_room(datetime.date(check_out.year, check_out.month, check_out_month_day))
        
                check_out_month_day += 1
        
# Iterating the while loop in a way the room is being reserved for all night before the check-out day 
        
                while (check_out_month_day != check_out.day):
            
                    room_reserved.reserve_room(datetime.date(check_out.year, check_out.month, check_out_month_day))
            
                    check_out_month_day += 1
                
                
# Now we add the __str__ method to the class, which will return a string representation
# of a reservation containing the booking number, name on the reservation, room reserved and check-in and out dates
# with each piece of information in the string in a new line

    def __str__(self):
        
# The new line character is introduced, as we want to show each piece of information in a new line
        
        return ("Booking number: " + str(self.booking_number) + "\n" + "Name: " + self.name + "\n" + "Room reserved: " + str(self.room_reserved) + "\n" + "Check-in date: " + str(self.check_in) + "\n" + "Check-out date: " + str(self.check_out))
    

# Creating an instance method which takes no input, and returns a string containing the booking number and name on the reservation
# seperated by two hyphens

    def to_short_string(self):
        
        return ((str(self.booking_number)) + "--" + (self.name))
    
    
# Now, we create a class method that takes as input a string of the same format as the one returned by the to_short_string method,
# two date objects representing the check-in and check-out dates and a room object
# The method creates and returns an object of type Reservation for a stay in the specified room

    @classmethod
    
    def from_short_string(cls, short_string, check_in, check_out, room_reserved):
        
# Using the split method on short_string and "--" as a delimiter to get a list with booking number as its 1st element and
# name on the reservation as its second

        name_booking_number_list = short_string.split("--")

# The class method finally returns an object of type Reservation for a stay in the specified room

        return cls(name_booking_number_list[1], room_reserved, check_in, check_out, int(name_booking_number_list[0]))
    
    
# creating a static method that takes as input a room object and a list of tuples
# In the list, each tuple will contain the year (integer), month(string), and day (integer), and the fourth element will be
# a string in the same format as that returned by the to_short_string method
# the last element of the tuple will be an empty string if no reservation has yet been made
# The method should return a dictionary where each key is a booking number and each value is the reservation object for that booking
# number

    @staticmethod
    
    def get_reservations_from_row(room_reserved, list_of_tuples):
        
# creating an empty list which will contain all the booking numbers that will be keys of the output dictionary
# Since, they will be keys we will only take the unique booking numbers

        booking_number_list = [] 

        for elem in list_of_tuples:
            
            if len(elem[3]) != 0: # This is done to make sure, the reservation has been made, otherwise no reservation object
                
# The string which matches the same format as that returned by the to_short_string method is broken down into 2 elements and stored in
# a list with the first element being the booking number while the second element being the name 
        
                list_of_booking_number_and_name = (elem[3]).split("--")
                
# We check, whether the booking numbers are already in the list booking_numer_list or not, if not we add them
# and if yes we dont as this will be keys of the output dictionary and they have to be unique 
                
                if (list_of_booking_number_and_name[0]) not in booking_number_list:
                    
                    booking_number_list.append(list_of_booking_number_and_name[0])
                    
# The method now iterates through all the elements of the list booking_numer_list, and then iterates through all the
# tuples in the input list to check which tuples have the same booking number as the booking number being iterated
# This is done to get the two dates corresponding to this booking numbers and check which one is check-in date and which is check-out date
# and create the appropriate Reservation objects

# creating an empty dictionary which will given as output

        reservation_dictionary = {}

        for elem in booking_number_list:
            
# creating an empty list which will contain the 4 th element of the tuple whose booking number matches our booking number
# all the elements of this list would be identical

            short_string_list = [] 
            
# creating an empty list which will contain the date objects

            date_object_list = [] 
            
            for tuples in list_of_tuples:
                
                if elem == (tuples[3][:13]): # The booking number is the first 13 digit in the string which is the 4 element of the tuple
                    
# Before creating the date object, we convert the month from string to its corresponding integer value                    
                    
                    month_integer = (MONTHS.index(tuples[1])) + 1 
                     
                    date_object = datetime.date(tuples[0], month_integer, tuples[2])
                    
# We now add the each date objects to the list date_object_list
                    
                    date_object_list.append(date_object)
                    
                    short_string_list.append(tuples[3])
                    
# Since, only two date objects will be added to the list date_object_list, the smaller date i.e earlier date will be check-in date
# and the larger date i.e later date will be the last date of booking 

            check_in = min(date_object_list)
            
            one_day_before_check_out = max(date_object_list)
            
# Now, the one_day_before_check_out date object obtained shows us the last day of the booking made by the user
# The user will check out on the next day, and thus we increase the day by 1
# However, if it is the last day of the month or the year, we change the month and year accordingly and also keeping in the mind
# obtaining the year, month, date of the last date of booking

            year = one_day_before_check_out.year

            month = one_day_before_check_out.month
            
            day = one_day_before_check_out.day
            
            if helper_is_leap_year_Feb(year, month):
                
                if day == 29: # last day of february during leap year
                    
                    day = 1
                    
                    month += 1
                    
                else:
                    
                    day += 1
                    
            else:
                
                if month == 12:
                    
                    if day == 31: # last day of December
                        
                        day = 1
                        
                        month = 1
                        
                        year += 1
                        
                    else:
                        
                        day += 1
                        
                else:
                    
# First we calculate the number of days of that month

                    number_of_days_month = DAYS_PER_MONTH[month - 1]
                    
                    if day == number_of_days_month:
                        
                        day = 1
                        
                        month += 1
                        
                    else:
                        
                        day += 1
                        
# Finally we create the check_out date

            check_out = datetime.date(year, month, day)
            
            
# The method now creates the Reservation object using the class method from_short_string

            reservation_object = Reservation.from_short_string(short_string_list[0], check_in, check_out, room_reserved)
            
# The method finally creates and returns the dictionary where each key is a booking number and each value is the reservation object
# for that booking number

            reservation_dictionary[int(elem)] = reservation_object
            
        return reservation_dictionary
            
            
            
        


                    
                    
                    
                    
                    
                
                
            
            
        
         
                
                       
                       
                
                
                
                
                
                
            
            
            
                
                
            
            
            
            
            
                
                
            
            
            
            

            


            
            

    
    
    