# Name: Md Alauddin Siddiqui
# McGill ID: 260951950

# importing the datetime module

import datetime

# importing the random module

import random

# importing the copy module

import copy

# importing the os module

import os

# from room module we import Room, MONTHS, DAYS_PER_MONTH

from room import Room, MONTHS, DAYS_PER_MONTH

# from reservation module we import Reservation

from reservation import Reservation


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
    

# creating a class called Hotel with the following instance attributes
# name (a string), rooms (a list of Room objects), reservations
# (a dictionary mapping integers, i.e. booking numbers, to Reservation objects)

class Hotel:
    
# creating a constructor that takes as input a string, a list of Room objects, and a dictionary mapping integers to Reservation objects
# default values for the last two inputs should be an empty list and an empty dictionary respectively
# The constructor uses the provided inputs to initialize all the instance attributes accordingly
# The list of rooms and dictionary of reservations should be deep copied

    def __init__(self, name, rooms = [], reservations = {}):
        
        self.name = name
        
        self.rooms = (copy.deepcopy(rooms))
        
        self.reservations = (copy.deepcopy(reservations))
        
        
# The instance method takes as input two strings representing the name of the person reserving and the type of room desired respectively
# as well as two date objects with one representing the check in date, and the other representing the check out date
# If a room of the specified type is available at the hotel for the dates indicated, then the method
# creates a reservation for the first available room of that type and returns the booking number of
# the reservation

    def make_reservation(self, name, room_type, check_in, check_out):
        
# The method first checks whether the specified room is available at the hotel or not for the dates indicated
# This is done using the static method find_available_room which takes as input a list of objects of type room,
# a string representing room type and two date objects representing check-in date and check-out date
# The method returns the first Room object from the list which is of correct type and is available for the specified dates
# Otherwise, the method returns None

# When the method find_available_room does not return None, it means there is a room in the list of room objects which is an instance
# attribute in hotel object which is of correct type and is available for specified dates

        if (Room.find_available_room(self.rooms, room_type, check_in, check_out)) != None:
            
# If a room is available and is of correct type, the method creates reservation for the 1st available room of that type and returns
# booking number of that reservation

            first_available_room = Room.find_available_room(self.rooms, room_type, check_in, check_out)
            
# creating the Reservation for this room object

            reservation_object = Reservation(name, first_available_room, check_in, check_out)
            
# Now the method updates the attribute storing all the hotel reservations accordingly
# Since, here we are dealing with only one Room object and only one Reservation object is formed, we can directly add it to the
# dictionary 

            self.reservations[reservation_object.booking_number] = reservation_object
            
# The function finally returns the booking number of the reservation

            return (reservation_object.booking_number)

# If the room is not available for the specified dates, the method raises an AssertionError 
            
        else:
            
            raise AssertionError ("The room is not available for the specified dates")
        
        
# Creating an instance method which takes as input a list of integers representing booking numbers
# The method returns a float indicating the amount of money a user should pay the hotel for these reservations
# If the booking number refers to a reservation that was not made for this hotel, then the method simply ignores it

    def get_receipt(self, list_of_booking_numbers):
        
# The method now iterates through the list_of_booking_numbers, each of this booking numbers are keys in the dictionary stored inside
# the instance attribute in Hotel objects called reservations and their corresponding values are the Reservation objects which
# correspond to this booking numbers

        amount_of_money = 0 # This variable will contain the total amount of money
        
        for elem in list_of_booking_numbers:
            
# If the booking number refers to reservation that was not made for this hotel, the method simply ignores it

            if elem in self.reservations:
                
# First, we get the reservation object corresponding to the booking number being iterated 
                
                reservation_object = self.reservations[elem]
                
# Then from the reservation object, we obtain the check-in and check-out date
                
                check_in_date = reservation_object.check_in
                
                check_out_date = reservation_object.check_out
                
# Since, both of these objects are date objects, we can easily calculate how many days apart this two dates are

                difference_in_days = check_out_date - check_in_date
                
# Now, from the reservation object corresponding to the booking number, we obtain a Room object which is stored in the instance
# attribute room_reserved

                room_object = reservation_object.room_reserved
                
# from the room_object, we obtain the price of the selected room per night which is stored in the instance attribute price
# which is then multiplied with the number of days in between check-in and check-out date to calculate the total price
# corresponding to the booking number being iterated

                total_price = (room_object.price) * (difference_in_days.days)
                
# Finally, at the end of each iteration, the total_price is added to the already being accumulated total amount of money 
                
                amount_of_money += total_price
                
# The method finally returns a float indicating the amount of money the user should pay the hotel for these reservations 
                
        return amount_of_money
    
    
# The instance method takes as input a booking number (an integer) and returns a reservation object with given number or None if
# no reservations were found

    def get_reservation_for_booking_number(self, booking_number):
        
# The method returns the corresponding value in the dictionary stored in instance attribute of hotel called reservations which has the
# key of booking_number 
        
        if booking_number in self.reservations:
            
            return (self.reservations[booking_number])
        
        else: 
            
            return None # Otherwise, the method returns None
        
        
# Creating an instance method which takes as input an integer representing a booking number
# The method does not return any value, but cancels the reservation with the specified booking number

    def cancel_reservation(self, booking_number):
        
# If the booking number does not refer to a reservation at the hotel, then the method does not do anything
        
        if (self.get_reservation_for_booking_number(booking_number)) != None:
            
# First, we obtain the reservation object which matches our input booking number integer 
            
            reservation_object = self.get_reservation_for_booking_number(booking_number)
            
# Then, we obtain the check-in and check-out date of the user which is stored in the instance attribute of our reservation object

            check_in_date = reservation_object.check_in
            
            check_out_date = reservation_object.check_out
            
            day = check_in_date.day
            
            month = check_in_date.month
            
            year = check_in_date.year
            
# Now, we consider the situation when the check-in and check-out are on the same month of the same year

            if ((check_in_date.year),(check_in_date.month)) == ((check_out_date.year),(check_out_date.month)):
                
# The method now makes the room object stored as an instance attribute in the reservation object available using the instance method
# make_available
                
                (reservation_object.room_reserved).make_available(check_in_date)
                
# After this, a while loop is created which iterates till the day of the check-out has been reached
# As the check-out day is not included and thus we will not make it available

                day += 1
                
                while (day != check_out_date.day):
                    
                    (reservation_object.room_reserved).make_available(datetime.date(year, month, day))
                    
                    day += 1
                    
# Now, we consider the situation when the check-in (year, month) and check-out (year, month) are not same

            else:
                
                (reservation_object.room_reserved).make_available(check_in_date)
                
                day += 1
                
# Now, we iterate till the last day of the check-in month and year and cancel reservation for the entire check-in month
# We will also make sure to consider the additional day for the leap year in the month of February

                if helper_is_leap_year_Feb(check_in_date.year, check_in_date.month):
                    
                    while (day != 30): # as 29 days are there in a leap year February
                        
                        (reservation_object.room_reserved).make_available(datetime.date(year, month, day))
                        
                        day += 1
                        
                else:
                    
# First we get the number of days of the check-in month

                    number_of_days = DAYS_PER_MONTH[ month - 1] # 1 is subtracted as months starts from 1 while index start from 0 
                    
# This ensures the entire month from the check-in night to the last month of night, reservation is canclled                   
                    
                    while (day != (number_of_days + 1)):
                        
                        (reservation_object.room_reserved).make_available(datetime.date(year, month, day))
                        
                        day += 1
                        
# Now as we go to the next month, we make sure if this is the last month of the year, we increase the year value by 1 and change the
# month value to 1, and if it is not the last month of the year, we increase the value of month by 1
                        
                if month == 12:
                    
                    month = 1
                    year += 1
                    
                else:
                    
                    month += 1
                        
# Now we consider the situation for the months between the check-in and check-out month
# we iterate using the while loop in a such a way that the loop will keep iterating till we reach the check-out (year, month)
# as that month is accounted seperately 

                while ((year), (month)) != ((check_out_date.year),(check_out_date.month)):
                    
                    day_of_month_iterated = 1 # The first day of every month 
                    
                    (reservation_object.room_reserved).make_available(datetime.date(year, month, day_of_month_iterated))
                    
                    day_of_month_iterated += 1
                    
                    
                    if helper_is_leap_year_Feb(year, month):
                        
                        while (day_of_month_iterated != 30): # 29 days of a leap year 
                            
                            (reservation_object.room_reserved).make_available(datetime.date(year, month, day_of_month_iterated))
                            
                            day_of_month_iterated += 1
                            
# If the (year, month) being iterated is not a leap year, we first calculate the number of days of the month and iterate in a way
# reservations of all the days of month is cancelled 
                            
                    else:
                        
                        number_of_days_in_month = DAYS_PER_MONTH[month - 1]
                        
                        while (day_of_month_iterated != (number_of_days_in_month + 1)):
                            
                            (reservation_object.room_reserved).make_available(datetime.date(year, month, day_of_month_iterated))
                            
                            day_of_month_iterated += 1
                            
# Finally, at the end of the outer while loop, we check whether the month is the last month of the year or not
# If yes, month is assigned a value 1 while year has been increased by 1, else month is increased by 1
                            
                    if month == 12:
                        
                        month = 1
                        
                        year += 1
                        
                    else:
                        
                        month += 1
                        
# Finally, we take into account the check-out month and cancel reservation for all days till the night before the check-out

                day_of_check_out_month = 1
                
                (reservation_object.room_reserved).make_available(datetime.date(check_out_date.year, check_out_date.month, day_of_check_out_month))
                
                day_of_check_out_month += 1
                
# Here, we stop the iteration as soon as the check-out day is reached as that day is excluded from reservation
# Here we are directly using check out day and thus we do not need to take consideration of the leap year 
                
                while (day_of_check_out_month != check_out_date.day):
                    
                    (reservation_object.room_reserved).make_available(datetime.date(check_out_date.year, check_out_date.month, day_of_check_out_month))
                    
                    day_of_check_out_month += 1
                

# The method finally removes the reservation from the reservations attribute of the hotel object 
            
            del (self.reservations[booking_number])
            
            
# Creating an instance method which takes no inputs and returns a list of strings representing the room types available at the hotel

    def get_available_room_types(self):
        
# creating an empty list which will contain the strings representing the room types available at the hotel

        list_of_room_types = [] 
        
# The method now iterates through all the room objects present in the hotel which is stored in the instance attribute

        for elem in self.rooms:
            
            if (elem.room_type) not in list_of_room_types: # this makes sure no room type is repeated twice in the list 
                
# The room type is stored in the instance attribute room_type of each room object                    
                    
                list_of_room_types.append(elem.room_type)
                
# The method finally returns the list containing the strings representing the room types available at the hotel

        return list_of_room_types
    
    
# Creating a static method which takes as input a path to a hotel_info.txt file for a given hotel
# The method should read through the file and return a 2-tuple of the hotel's name and a list of Room objects

    @staticmethod
    
    def load_hotel_info_file(file_path):
        
# The method first opens the file using the built in function open
# The mode given in the open function is "r" as we want to read data from the file
# Assigning this to a variable called fobj 

        fobj = open(file_path, "r")
        
# Now, we used the read method which takes an optional argument which tells the number of characters to read from the file
# As no argument was given, it reads through all the characters of the file
# It returns a string which contains the entire string of the file
# The strip method is added when string cointaining all the characters of the file is read, as this removes all unwanted extra spaces/
# extra lines at the start or end of the file
        
        file_content = (fobj.read()).strip()
        
# Finally, we close the file using the close method 

        fobj.close()
        
# Now, the method creates a list where each element is a string in each different line of the file
# This is created using the split method on file_content and using "\n" as the delimiter as each string is in a different line

        list_of_file_strings = file_content.split("\n")
        
# The name of the hotel is the first element of the list_of_file_strings as it is on the first line of the input txt file

        name_of_hotel = list_of_file_strings[0]
        
# creating an empty list which will contain the Room objects created

        room_objects_list = [] 
        
# The method now iterates through the list_of_file_strings (starting from the 2 element to the last element)

        index = 1
        
# This ensures the loop is iterated as many times as we can have index from 1 to the last element of the list list_of_file_strings
        
        while index < len(list_of_file_strings): 
            
# The method then gets the element in that particular index in the list list_of_file_strings
# This element contains the room number, room type and the price of the room all seperated by commas

            room_string = list_of_file_strings[index]
            
# However, the room_string starts with "Room " and then it represents our valuable information room_num, room_type, price
# And thus we use the strip method on the string room_string to remove the additional characters infront
# Using "Room " wont be a problem as the last character of the room_string is a number and is not affected by this strip 

            room_string_reformed = room_string.strip("Room ")
            
# The room_string_reformed is a string where each piece of information is
# seperated by commas and thus we will call the split method on the room_string_reformed
# using "," as a delimiter

            list_of_room_attributes = room_string_reformed.split(",")
            
# Now, the string room_string_reformed has room_num, room_type, price seperated by a comma, in that particular order 
# all of these 3 is instance attributes of the object
# Room and thus using this instance we can create Room objects for each element of the list list_of_file_strings from the 2nd element
# to the last element
# All the Room objects are created and added to the list room_objects_list
# We have to ensure that room_num and price is converted to integer and float respectively
# However, we have to make sure the Room class takes the input in the following order room_type, room_num, price

            room_objects_list.append(Room(list_of_room_attributes[1], int(list_of_room_attributes[0]), float(list_of_room_attributes[2])))
            
            index += 1
            
# creating a 2-tuple of the hotel's name and a list of Room objects

        return (name_of_hotel, room_objects_list)
    
    
# Creating an instance method which saves the hotel's name and room  information into a file hotel_info.txt
# which should be located inside a folder named after the hotel (in all lowercase, with spaces replaced by underscores)
# and said folder should be in a folder called hotels
# The first line of the file will contain the hotel’s name, and each subsequent line will contain
# information for one of the hotel’s rooms, in the format given by the Room __str__ method

    def save_hotel_info_file(self):
        
# First we create the name of the folder which has the same name as of the hotel, but in all lowercases and spaces are replaced by
# underscores

        hotel_name_lower = (self.name).lower()
        
# we will now use, the replace method on the string hotel_name_lower which will return a copy of the string with all occurence of
# " " replaced by "_" 
        
        hotel_name = hotel_name_lower.replace(" ", "_")
        
# First, we open a file using the open function and using the mode "w" as we would want to write onto the file
# Since, the "w" mode was used it will open the file for writing only
# It overwrites if any file exists as the given filename/filepath or creates a new file if one does not exist
# We also provide the open function, the filename/filepath

        fobj = open(("hotels/" + hotel_name + "/" + "hotel_info.txt"), "w")
        
# The first line of the txt file will contain the hotel's name
# We use the write method to write on the file
# However, the write method does not automatically create a new line at the end of each write method and thus we have to add "\n"
# whenever we want to introduce a new line

        fobj.write((self.name) + "\n")
        
# The method now iterates through all the room objects stored in the instance attribute rooms
# each room object is written in each subsequent line and
# the information for each of the hotel’s rooms is given in the format given by the Room __str__ method

        for elem in self.rooms:
            
            fobj.write((str(elem)) + "\n")
            
# Finally, we close the file using the close method

        fobj.close()
        
        
# Creating a static method which takes as input a hotel folder name(string), a month ( a string from the MONTHS list) and a year (integer)
# The method should load the CSV filed named after the given month and year and located in the given folder name
# (which itself will be inside a folder called hotels)
# It should then return a dictionary, where each key is a room number (integer), and each corresponding value is a list of
# tuples corresponding to the reservation data for that room,
# one tuple for each day of the month
# Each tuple should contain four elements: the year, month, day and the short reservation string for that day

    @staticmethod
    
    def load_reservation_strings_for_month(folder_name, month, year):
        
# First, we open the CSV file stored in the folder name given as input which is stored in the folder hotels
# The name of the CSV file is given in the format YEAR_MONTH.csv
# We use the open function to open the csv file, and we use the "r" mode as we will road data from the CSV file

        year_string = str(year) # converting the year to string for string concatenation 

        fobj = open(("hotels/" + folder_name + "/" + (year_string + "_" + month) + ".csv"), "r")
        
# creating an empty dictionary where each key will a room number (integer), and
# each corresponding value will be a list of tuples

        reservation_dict = {}
        
# The method now iterates through each line of the CSV file

        for line in fobj:
            
# creating an empty list which will contain tuples corresponding to the reservation data of that room, one tuple for each day of month

            list_of_tuples = [] 
            
# we remove, any additional spaces or new line characters at the end or beginning of each line using the strip method

            reformed_line = line.strip()
        
# now for each row in CSV file, i.e for each room number, each information is seperated by commas
# with the first element in each row being the room number, while each Reservation short_string has the index corresponding to its
# day number
# If no reservations were made, that column contains an empty string
# from the string reformed_line, we use the split method on it to obtain a list with each element on the list being each element
# in the string reformed_line seperated by a comma

            list_of_room_num_and_short_string = reformed_line.split(",")
        
# Now we create tuples for each day of the month and add each tuple to the list_of_tuples
# This is done for every day of the month
# First we check, whether the month is a leap year February or not, as we account for the additional day

            month_integer = (MONTHS.index(month) + 1)
            
            if helper_is_leap_year_Feb(year, month_integer):
                
# The method then iterates the while in such a way, that there is a tuple created for each day,
# Each of the tuple contains year, month, day, reservation short string
# Each tuple is added to a list called list_of_tuples 
                
                day = 1
                
                while day < ((DAYS_PER_MONTH[MONTHS.index(month)]) + 2):
                    
                    reservation_tuple = (year, month, day, list_of_room_num_and_short_string[day])
                    
                    list_of_tuples.append(reservation_tuple)
                    
                    day += 1
                    
            else:
                
                day = 1
                
                month_index = MONTHS.index(month)
                
                while day < (DAYS_PER_MONTH[month_index] + 1):
                    
                    reservation_tuple = (year, month, day, list_of_room_num_and_short_string[day])
                    
                    list_of_tuples.append(reservation_tuple)
                    
                    day += 1
                    
# At the end of each line iteration, we add the keys and values to the dictioanary called reservation_dict
# where each key is a room number (integer), and
# each corresponding value will be a list of tuples

# The first element of the list list_of_room_num_and_short_string is the room number 
            
            room_number = list_of_room_num_and_short_string[0]
            
            reservation_dict[int(room_number)] = list_of_tuples
            
# Finally, we close the file using the close method

        fobj.close()
            
# Finally, we return the dictionary 
            
        return reservation_dict
    
    
# Creating an instance method which takes as input a string corresponding to a month from the list MONTHS and a year
# The method creates a new CSV file named after the given month and inside a folder named after the hotel (all in lowercase with
# spaces replaced by underscores) with that folder being in a folder called hotels 
                
# The CSV file should contain one row per room , the first column of each row will be the room number
# there will be as many subsequent columns for days in the given month
# In every row, after the room number, will be the reservation string as given by the Reservation to_short_string method
# if a reservation occurs in that room on the given day
# Or, if no reservation occurs in that room on that day, then the column should contain an empty string

    def save_reservations_for_month(self, month, year):
        
# First, we convert the name of the hotel to lowercase and then convert all the spaces in the string to underscores

        hotel_name_lower = (self.name).lower()
        
        hotel_name = hotel_name_lower.replace(" ","_")
        
# Now, we open a CSV file using the open function, with mode "w" as we want write data on the file
# The filename will be in the format YEAR_MONTH.csv, with that file being in a folder named after the hotel (all in lowercase with
# spaces replaced by underscores), which is placed in the hotels folder
# Since, the "w" mode is used, it overwrites, any file with the same filename/filepath, if no such file exist, it creates one  

        fobj = open(("hotels/" + hotel_name + "/" + str(year) + "_" + month + ".csv"), "w")
        
# The method now iterates through all the booking numbers stored in the instance attribute reservations

        for booking_numbers in self.reservations:
            
# For each booking number in the dictionary self.reservations, we obtain its corresponding reservation object 
            
            reservation_object = self.reservations[booking_numbers]
            
# Then, we use the instance method to_short_string on the reservation object to get the short string representing the booking name
# and booking number of the person, who did the booking

            reservation_short_string = reservation_object.to_short_string()
            
# Now, the method obtains the room object in the instance attribute room_reserved of the reservation_object

            room_object = reservation_object.room_reserved
            
# The method first writes the room number stored in the room_num attribute of the room_object into the file

            fobj.write(str(room_object.room_num))
            
# Each value seperated by a comma 
            
            fobj.write(",")
            
# The method now obtains the list stored in the availability dictionary of the room_object which corresponds the (year, month)
# gives as input
# First we get the month_integer of the month given as input
# We do not take the the first element of each list as the first element does not show availability of the room for a particular day
# of the month

            month_integer = (MONTHS.index(month) + 1)
            
            list_of_availability = room_object.availability[((year),(month_integer))][1:]
            
# The method now iterates through all the element of this list list_of_availability
# If the reservation is made for that day, the method writes the reservation_short_string to the file, other wise it adds an empty string
# We account for the last date of the month seperately 

            for elem in (list_of_availability[:(len(list_of_availability) - 1)]):
                
                if elem == False:
                    
                    fobj.write(reservation_short_string)
                    
                else:
                    
                    fobj.write("")
                    
# Each day is seperated by a comma 
                    
                fobj.write(",")
                
# This was done to make sure there is a comma not placed after the last date 
                
            if list_of_availability[-1] == False: 
                    
                fobj.write(reservation_short_string)
                    
            else:
                    
                fobj.write("")
                    
# At the end of each row, the method adds a newline character as for each room number, there should be an independent row

            fobj.write("\n")
            
# The method finally closes the file using the close method

        fobj.close()
        
        
# Creating an instance method which saves a file hotel_info.txt with the hotel’s name and
# room information, and CSV files (one for each month in which there are rooms available) containing the reservation data
# If the folders in which the files should be saved do not exist, then the function should create them

    def save_hotel(self):
        
# The method first gets the hotel name which will be used in the filename
# To obtain this, we convert the hotel name to lower case and replace all spaces with underscores

        hotel_name_lower = (self.name).lower()
        
        hotel_name = hotel_name_lower.replace(" ","_")
        
# The function now checks whether the folder, where I would want to save the file exists or not
# This is done using the os.path.exists function which returns True if the folder exists and False otherwise
# If the file folder does not exist,the method creates them using the function os.makedirs

        if not (os.path.exists(("hotels/" + hotel_name))):
            
            os.makedirs(("hotels/" + hotel_name))
            
# Now we are sure that the folder where I would like to save my files already exists
# as if it previously existed we can work with it, and if it previously did not exist, we have already created the file folder
# Now, the method uses the instance method save_hotel_info_file which saves the hotel's name and room information into a file
# hotel_info.txt which should be located inside a folder named after the hotel (in all lowercase, with spaces replaced by underscores)
# and said folder should be in a folder called hotels which exactly matches our need

        self.save_hotel_info_file()
        
# If the hotel has no rooms, then no CSV files should be created and thus we use to terminate the method 

        if (len(self.rooms)) == 0:
            
            return 
        
# The method now iterates through the booking numbers stored in the dictionary in the instance attribute reservations
# and for each booking number it obtains a reservation object which corresponds to the booking number

        for booking_number in self.reservations:
            
            reservation_object = self.reservations[booking_number]
            
# Each reservation_object has a room object stored in its instance attribute room_reserved, we obtain that room_object

            room_object = reservation_object.room_reserved
            
# Now, in the availability instance of the room_object which is a dictionary
# The keys of the dictionary are tuples in the form (year, month) which indicates rooms have been made available for all this
# (year, month)
# we will add all the available tuples as keys into an empty list called list_of_tuples by iterating through all the keys 

            list_of_tuples = []
            
            for keys in room_object.availability:
                
                list_of_tuples.append(keys)
                
# Now, we iterate through all the tuples stored in the list_of_tuples

            for tuples in list_of_tuples:
                
# The year is the first element of each tuple, and the month integer is the second element in each tuple
# from the month integer, we obtain the month string 
                
                year = tuples[0]
                
                month_string = MONTHS[(tuples[1]) - 1]
                    
# Now we are sure that the folder exists as we have created the folder already
# and thus we use the instance method save_reservations_for_month
# which takes as input a string corresponding to a month (from the MONTHS list) and a year (integer)
# The function should create a new CSV file named after the given month and inside a folder named after the hotel
# (all in lowercase, with spaces replaced by underscores) with that folder being in a folder called hotels which exactly matches our need

                self.save_reservations_for_month(month_string, year)
                
                
# creating a class method which takes a folder name as input and loads the hotel info file and reservation CSV files from inside that
# folder (itself being in a folder called hotels)
# then creates and returns an object of type Hotel with the loaded name, rooms and reservation information

    @classmethod
    
    def load_hotel(cls, folder_name):
        
# First, the method creates a list of strings each of which consists of filename including extension of a file stored
# in the folder given as input which itself is stored in a folder called hotels
# This is done using the os.listdir function which takes as input the path of the folder whose file we would like to see

        list_of_files = os.listdir("hotels/" + folder_name)
        
# The method now iterates through the list_of_files and checks for filenames ending with "txt" and "csv"
# All of this files are then added to the empty list called list_of_txt_files or list_of_csv files respectively 

        list_of_txt_files = []
        
        list_of_csv_files = [] 
        
        for elem in list_of_files:
            
# This gives us the last 3 characters of each filename (i.e the extension we need to check for csv and txt files)
# If there are other files which do not have 3 character extension, it does not affect our code, as we dont take those files under
# consideration

            last3characters = elem[(len(elem) - 3):]
            
            if last3characters == "txt":
                
                list_of_txt_files.append(elem)
                
            if last3characters == "csv":
                
                list_of_csv_files.append(elem)
                
# Since, there is only one txt file storing the hotel information for any given hotel
# we can directly use it in the input path given to the static method load_hotel_info_file
# which takes as input a path to a hotel_info.txt file for a given hotel
# The method will read in the file at that path and return a 2-tuple of the hotel’s name and a list of Room objects

        hotel_name, list_of_room_objects = Hotel.load_hotel_info_file("hotels/" + folder_name + "/" + list_of_txt_files[0])
        
# creating an empty dictionary which will later consist of booking numbers corresponding to reservation objects and stored in the
# instance attribute reservations of the hotel object created 
        
        reservation_dictionary = {}
        
# creating an empty dictionary called room_info_dictionary which will contain room numbers as keys and a list of tuple
# containing all reservation information of the room throughout the year 
        
        room_info_dictionary = {}

# The method now iterates through the elements of list_of_csv_files

        for elem in list_of_csv_files:
            
# First, we use the string slicing in a way that the extension has been removed
# Since, we are only considering ".csv" here we can not take the last 4 characters of the string to get the filename without extension 

            filename_without_ext = elem[:(len(elem) - 4)]
            
# The method then uses split method on filename_without_ext and using "_" as a delimiter which will form a list
# with first element of the list being the year and the second element being the month of that particular CSV file

            list_of_year_month = filename_without_ext.split("_")
            
            year = int(list_of_year_month[0])
            
            month = list_of_year_month[1]
            
# The method now iterates through the list list_of_room_objects and sets up availability using the room object instance method
# set_up_room_availability for all the rooms at this hotel for the month and year of the CSV file currently being iterated

            for rooms in list_of_room_objects:
                
                rooms.set_up_room_availability([month], year)
                
# The method now loads the CSV file using the static method load_reservation_strings_for_month which takes as input a hotel
# folder name, a month and the year which corresponds to the month and year being iterated
# The method returns a dictionary where each key is a room number and value of the dictionary is a tuple in the form
# (year, month, day, reservation short string)

            reservation_month_dict = Hotel.load_reservation_strings_for_month(folder_name, month, year)
            
# The method now obtains the room number and their corresponding tuples to the dictionary room_info_dictionary
# If the key is not in the dictionary, we add it to the dictionary, once the key has been added to the dictionary, we just
# append the tuple in the already existing list of tuples in the value of the dictionary 
            
            for keys in reservation_month_dict:
                
                if keys not in room_info_dictionary:
                    
                    room_info_dictionary[keys] = reservation_month_dict[keys]
                    
                else:
                    
                    for tuples in reservation_month_dict[keys]:
                    
                        room_info_dictionary[keys].append(tuples)
                        
# The method now creates the reservation object using the static method get_reservations_from_row which takes as input a room object
# and a list of tuples
# This list of tuples is in the same format as of the tuple in value of the dictionary returned from load_reservation_strings_for_month
# The method returns a dictionary where each key is a booking number and each value is a Reservation object for that booking number

# Now the method iterates through the list of room objects list_of_room_objects
# For each room object being iterated we obtain the room number and then from the room_info_dictionary the corresponding
# tuple storing reservation information is obtained

        for rooms in list_of_room_objects:
            
            tuple_list = room_info_dictionary[rooms.room_num]

            reservation_object_dictionary = Reservation.get_reservations_from_row(rooms, tuple_list)
                
            if len(reservation_object_dictionary) != 0:
                
# There will be a reservation_object_dictionary created at the end of each iteration, we will add the keys and the values
# of this dictionary to the dictionary reservation_dictionary at the end of each iteration will be stored in our Hotel object
# instance attribute

                for keys in reservation_object_dictionary:
                
                    reservation_dictionary[keys] = reservation_object_dictionary[keys]
                    
# The method finally returns an object of type Hotel with loaded name, rooms and reservation information

        return cls(hotel_name, list_of_room_objects, reservation_dictionary)
                
                 
                 
                 



                    
                    

                

                 
            
            
                
                

                
                
                

        


            
            
            
    
                    
                    
                    
            
            
            
           





















