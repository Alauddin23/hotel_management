# Name: Md Alauddin Siddiqui
# McGill ID : 260951950

# importing the datetime module

import datetime

# importing the random module

import random

# importing matplotlib.pyplot module

import matplotlib.pyplot as plt

# importing the os module

import os

# importing the hotel module

import hotel 

# creating a class called Booking

class Booking:
    
# creating a constructor that takes as input a list of hotels and initializes an instance attribute of the same name accordingly

    def __init__(self, hotels):
        
        self.hotels = hotels
        
    
# Creating a class method that loads in all the hotels in the hotels folder and creates and returns an object of Type Booking
# with said list of hotels

    @classmethod
    
    def load_system(cls):
        
# First, we obtain a list of strings, each of which is a name of a folder stored inside the folder hotels

        list_of_folder_name = os.listdir("hotels/")
        
# For each folder name, which represents a hotel, we will give it as an input to the load_hotel which takes as input a folder name
# and loads the hotel info file and the CSV file inside the folder name given as input
# The class method returns object of Type Hotel with the loaded names, rooms and the reservation information
# Each of the hotel object is then added to a list and then given as input when creating the class object Booking 

# creating an empty list which will contain the list of hotel objects

        list_of_hotels = [] 

        for folder_name in list_of_folder_name:
            
            list_of_hotels.append((hotel.Hotel).load_hotel(folder_name))
        
# The class method finally returns the Booking object

        return cls(list_of_hotels)
    
    
# We now create an instance method which takes no explicit input and does not return anything
# The method welcomes the user to the booking system, and asks which operation they would like to perform,
# create a new reservation, cancel a reservation, or look up a reservation
# After getting the input from the user, the method should call the appropriate method
# The user can also call the secret deletion mode, using the magic word xyzzy

    def menu(self):
        
# The method welcomes the user to the booking system and asks the user which operation they would like to perform
# create a new reservation, cancel a reservation, or look up a reservation

        print("Welcome to Booking system")
        
        print("\nWhat would you like to do?")
        
        print(str(1) + "        Make a reservation")
        
        print(str(2) + "        Cancel a reservation")
        
        print(str(3) + "        Look up a reservation")
        
# The method then retrieves an input from the user indicating their choice
# The input is an integer from 1 to 3 both inclusive

        user_input = input("\nPlease enter an integer between 1 and 3 indicating your choice: ")
        
# The method now calls the appropriate method as per the want of the user
# If the magic word is entered, then the secret deletion method should be called

        if user_input == "1":
            
            self.create_reservation()
            
        elif user_input == "2":
            
            self.cancel_reservation()
            
        elif user_input == "3":
            
            self.lookup_reservation()
            
        elif user_input == "xyzzy":
            
            self.delete_reservations_at_random()
            
# The method then saves all the hotels back to the disk using the instance method save_hotel on all the hotel objects stored in the
# instance attribute hotels of booking object

        for hotel_object in self.hotels:
            
            hotel_object.save_hotel()
            
            
# Creating an instance method that takes no input and does not return any value
# It should prompt the user for their name, and then display a list of hotels for them to choose from and then a list of
# room types at that hotel
# It should also prompt for a check-in and check-out date
# It should make a reservation with the given information and then print out their booking number and total amount owing
# rounded to two decimal places

    def create_reservation(self):
        
# The method first prompts the user for their name

        user_name = input("\nPlease enter your name: ")
        
# The method then displays a list of hotels for the user to choose from

        print("\nHi " + user_name + "! Which hotel would you like to book?")
        
# The method now iterates through the list of hotel stored inside the instance attribute of the booking object
# and then displays the name of the hotels for the user to choose from

        counter = 1 # keeps track of the number of the hotel object being iterated in the list 

        for hotel_obj in self.hotels:
            
            print(str(counter) + "        " + hotel_obj.name)
            
            counter += 1
            
        user_input_hotel_choice = input("Please enter an integer indicating the choice of the hotel you would like to book: ")
        
# Our hotel object selected, is the one at an index 1 less than the input provided, as index starts from 1

        hotel_object_selected = self.hotels[(int(user_input_hotel_choice)) - 1]
        
# The method now iterates through the list of rooms stored inside the rooms attribute of the hotel object
# and then displays the name of the type of rooms available at that hotel

# obtaining a list of available room types in a hotel using the instance method get_available_room_types on the hotel object

        list_of_available_rooms = hotel_object_selected.get_available_room_types()

        print("\nWhich type of room would you like?")

        counter_2 = 1 #  keeps track of the number of the hotel object being iterated in the list 
        
        for room_type in list_of_available_rooms:
            
            print(str(counter_2) + "        " + room_type)
            
            counter_2 += 1
            
        user_input_room_type_choice = input("Please enter an integer indicating the choice of the room type you would like to book: ")
        
# We get the room type selected from the list list_of_available_rooms but subtracting 1 from the input value as index starts from 0 

        room_type_selected = list_of_available_rooms[(int(user_input_room_type_choice)) - 1]
        
# The method now obtains the check-in and check-out date from the user

        check_in = input("\nEnter check-in date (YYYY-MM-DD): ")
        
# The date is converted to a list using the split method and "-" as a delimiter
# The first element of the list is the year, the second element is the month and the last element is the day
# we create the appropriate datetime objects for this

        list_of_year_month_day = check_in.split("-")
        
        check_in_datetime = datetime.date(int(list_of_year_month_day[0]), int(list_of_year_month_day[1]), int(list_of_year_month_day[2]))
        
# The method repeats the same process for the check out date to obtain the datetime object of check out 

        check_out = input("Enter check-out date (YYYY-MM-DD): ")
        
        list_of_year_month_day2 = check_out.split("-")
        
        check_out_datetime = datetime.date(int(list_of_year_month_day2[0]), int(list_of_year_month_day2[1]), int(list_of_year_month_day2[2]))
        
# The method now creates the reservation with the given information using the instance method make_reservation on the selected
# hotel object which takes as input name of the person, the type of room desired and check-in, check-out dates and returns the booking
# number of the reservation

        booking_number = hotel_object_selected.make_reservation(user_name, room_type_selected, check_in_datetime, check_out_datetime)
        
# creating an empty list which will contain all the booking numbers

        booking_number_list = []
        
# Adding the booking number to the list

        booking_number_list.append(booking_number)
        
# The method finally calculates the total amount owing using the get_receipt instance method on the hotel object

        total_amount_owing = hotel_object_selected.get_receipt(booking_number_list)
        
# The method finally prints the booking number and the total amount owing

        print("\nOk. Making your reservation for a " + room_type_selected + " room")
        
        print("Your reservation number is: " + str(booking_number))
        
        print("Your total amount due is: $" + str(round(total_amount_owing,2)))
        
        print("\nThank you!")
        
        
# Creating an instance method that takes no input and returns nothing
# The method promots the user to enter a booking number and tries to cancel the reservation with that booking number at any hotel
# If the reservation could not be found, then the user must be informed

    def cancel_reservation(self):
        
# The method first prompts the user to enter a booking number

        user_booking_number = int(input("Please enter your booking number: "))
    
# First, we check whether the booking number entered corresponds to a particular reservation in any of the hotel
# This is done by iterating through all the hotel objects stored in the instance variable hotels of the booking object
# For each hotel object, if the booking number was not found in the reservation dictionary, we append the boolean False
# into a list of booleans, otherwise True
# When we are done iterating through all the hotel objects in the instance variable hotels of the booking objects
# and the list does not contain any True, it refers to that in none of the hotels there is a reservation made with this booking number

        list_of_booleans = [] 

        for hotel_object in self.hotels:
        
            if user_booking_number not in hotel_object.reservations:
            
                list_of_booleans.append(False)
            
            else:
            
                list_of_booleans.append(True)
            
# If there is atleast one True in the list_of_booleans it means there is a reservation for this booking number atleast in one of the hotel
# If not, the method makes the user know that there is no booking in any of the hotels with this reservation number   
        
        if not (True in list_of_booleans):
        
            print("\nCould not find a reservation with that booking number.")
            
# If the booking number corresponds to atleast one of the hotel objects in the hotels attribute of the booking object
# The method cancels the reservation using the instance method on all the hotel objects using instance method cancel_reservation
        
        else:
            
            for hotel_object in self.hotels:  
            
                hotel_object.cancel_reservation(user_booking_number)
                
            print("\nCancelled successfully.")
            
            
# Creating an instance method, which takes no input and returns no value
# It asks the user if they have a booking number(s)
# If they do, it asks them to enter them one at a time and then find the asscociate reservations at any hotel
# and then prints the reservation to the screen
# If any of the numbers are invalid, it informs the user about it

# If they do not have the booking numbers, then its asks to enter their name, hotel name, room number, check in, check out date
# and tries to find the reservation matching the given information
# If it finds such a reservation then prints the reservation to the screen
# If no search reservation was found, it informs the user

    def lookup_reservation(self):
        
# The method first asks the user if they have a booking number or not

        user_answer = input("Do you have your booking number(s)? ")
        
# If the user has the booking number(s), the method asks them to enter them one at a time until they enter the word "end"
# The user enters "end" if they have given all the booking numbers they have and the methods stop asking them for any more
# booking numbers

# creating a list which will contain all the booking numbers entered by the user

        list_of_booking_numbers = [] 

        if user_answer == "yes":
            
            user_booking_number_input = input("Please enter a booking number (or 'end'): ")
            
            if user_booking_number_input != "end":
                
                list_of_booking_numbers.append(int(user_booking_number_input))
                
            while user_booking_number_input != "end":
                
                user_booking_number_input = input("Please enter a booking number (or 'end'): ")
                
                if user_booking_number_input != "end":
                    
                    list_of_booking_numbers.append(int(user_booking_number_input))
                    
# The method now iterates through all the hotel object stored inside the instance attribute hotels of the booking object
# Then for each booking number, the method tries to find the reservation in any of the hotels, this is done by the instance method
# get_reservation_for_booking_number on the hotel object being iterated and then the method prints the reservation object 
# The instance method returns None if there was no reservation made with this booking number in the hotel object being iterated

# creating a counter which gives us a count of the number of reservation objects found in any of the hotels
# for the booking number being iterated 

            for booking_numbers in list_of_booking_numbers:
            
                counter = 0
                
                for hotel_objects in self.hotels:
                
                    if hotel_objects.get_reservation_for_booking_number(booking_numbers) != None:
                        
                        counter += 1 # A reservation object is found
                        
# If a reservation object is found, then the method prints the reservation on the screen 
                        
                        print("\nReservation found at hotel " + hotel_objects.name + ":\n")
                        
                        print(hotel_objects.get_reservation_for_booking_number(booking_numbers))
                        
# The method also prints the total amount the user owes for each reservation corrected to 2 decimal place

                        amount_owing = hotel_objects.get_receipt([booking_numbers])
                        
                        print("Total amount due: $" + str(round(amount_owing,2)))
                        
# The method also informs the user, if there is no reservation object found at any of the hotels for the booking numbers
# being iterated, the method makes the user know about it

                if counter == 0:
                    
                    print("\nAtleast one of the booking number given as input has no reservation associated with it!")
                    
# Now, the method considers the situation, when the user does not have a booking number

        elif user_answer == "no":
            
# The method asks the user to enter their name, hotel name, room number, and check-in and check-out dates and tries to find out
# a reservation matching the given information

            user_name = input("\nPlease enter your name: ")
            
            hotel_name = input("Please enter the hotel you are booked at: ")
            
            room_number = input("Enter the reserved room number: ")
            
            check_in = input("Enter the check-in date (YYYY-MM-DD): ")
            
# We will now convert the check in and check out dates to datetime object
# This is done by first using a split method on the check_in string using "-" as a delimiter
# The list now as 3 elements in the order of year, month and day
# we create datetime objects using this

            list_of_year_month_date = check_in.split("-")
            
            check_in_datetime = datetime.date(int(list_of_year_month_date[0]), int(list_of_year_month_date[1]), int(list_of_year_month_date[2]))
            
            check_out = input("Enter the check-out date (YYYY-MM-DD): ")
            
            list_of_year_month_date2 = check_out.split("-")
            
            check_out_datetime = datetime.date(int(list_of_year_month_date2[0]), int(list_of_year_month_date2[1]), int(list_of_year_month_date2[2]))
            
# The method now iterates through the list of hotels stored in the instance attribute hotel in the booking objects
# and checks whether any hotel object which has the same name as the hotel name given as input
# If yes, the method also adds True to the list_of_bool
# If there is no True in this list it means, there is no hotel with this name in the booking object and thus we inform the user about it

            list_of_bool = [] 
            
            for hotel_object in self.hotels:
                
                if hotel_object.name == hotel_name:
                    
                    list_of_bool.append(True)
                    
                    matched_hotel_object = hotel_object
                    
# If there is no True in the list_of_bool, the method informs the user about this

            if True not in (list_of_bool):
                
                print("\nYour input informations does not match any of the reservations")
                
            else:
                
# Now, we will get the reservation dictionary for the matched hotel object which is stored in the instance attribute reservations
# of the hotel object 

                reservation_dictionary = matched_hotel_object.reservations
                
# The function now iterates through the reservation_dictionary and then for each reservation object which is a value of the
# reservation dictionary, the method checks whether that reservation object has the same name, room number , check in and check out
# dates

# If a match was found, the method stores the booking number in a variable and appends True to a list called list_of_bool2
# If there was no True in this list, we can conclude, there was not match and thus the method lets the user know about it

                list_of_bool2 = []
            
                for keys in reservation_dictionary:
                
                    reservation_object = reservation_dictionary[keys]
                
                    if reservation_object.name == user_name:
                    
# Here, we first obtain the room object stored in the reservation object instance attribute room_reserved and then obtain the room number
# which is an instance attribute in the room object called room_num 
                    
                        if ((reservation_object.room_reserved).room_num) == int(room_number):
                        
                            if reservation_object.check_in == check_in_datetime:
                            
                                if reservation_object.check_out == check_out_datetime:
                                
# The method now have found the match and thus it now prints the reservation object on the screen and add True to the list_of_bool2
# and also add store the booking number in a variabe corresponding this matched reservation

                                    list_of_bool2.append(True)
                                
                                    booking_number = keys
                                
                                    print("\nReservation found under booking number " + str(booking_number) + "." + "\n")
                                
                                    print("\nHere are the details:")
                                
                                    print(reservation_object)
                                
# The method also prints the total amount due for each reservation which is calculate using the instance method
# on the matched hotel object

                                    amount_owed = matched_hotel_object.get_receipt([booking_number])
                                
                                    print("\nTotal amount due: $" + str(round(amount_owed,2)))
                                
# However, if there was no match, i.e no True in list_of_bool2, the method makes the user know this

                if not (True in list_of_bool2):
                
                    print("\nYour input informations does not match any of the reservations")
                    

# Creating an instance method, which takes no input and returns nothing
# The method should print You said the magic word!
# then choose a hotel at random and delete all of its reservations

    def delete_reservations_at_random(self):
        
# The method prints "You said the magic word!"

        print("\nYou said the magic word!")
        
# The method then calculate the number of the hotel objects stored in the instance attribute hotels of the booking object

        number_of_hotels = len(self.hotels)
        
# The list objects will have index from 0 to 1 less than the number_of_hotels, as index starts from 0
# we use the randint method to create a random index and then we delete all the reservations of the hotel at that particular index

        random_index = random.randint(0, (number_of_hotels - 1))
        
# Now we get the hotel object at that index

        hotel_object = self.hotels[random_index]
        
# The hotel objects has all its reservation stored in the instance attribute reservations which is a dictionary
# The method first creates a list containing all the keys of the reservation dictionary of our random hotel object 

        list_of_keys = []
        
        for keys in (hotel_object.reservations):
            
            list_of_keys.append(keys)
            
# The method now iterates through all the elements of the list_of_keys and delete the corresponding key value pairs from the
# reservation dictionary

        for elem in list_of_keys:
            
            del hotel_object.reservations[elem]
            
            
# Now, we create an instance method which takes one string as input corresponding to a month from the MONTHS list
# The function should create a line plot with one line per hotel showing the number of reservations for each day of the month
# over all the years
# The method returns a two-dimensional list of 2-tuples of the list of x-values and y-values for each hotel

    def plot_occupancies(self, months_string):
        
# First we create a list for the number of days for the given month

        month_index = (hotel.MONTHS).index(months_string)
        
        number_of_days = hotel.DAYS_PER_MONTH[month_index]
        
        list_of_days = [] 
        
        counter = 1
        
        while counter != (number_of_days + 1):
            
            list_of_days.append(counter)
            
            counter += 1
            
        list_of_x_and_y = []
        
        list_of_hotel_names = [] 
            
# The method first iterates through all the hotles of the booking object which is stored in the instance attribute hotels of the
# booking object

        for hotel_object in self.hotels:
            
# creating an empty dictionary which will have all the year for which room is available at hotel as key and values will be the
# reservation information for each for each day of the month given as input 
            
            year_reservation_info_dictionary = {}
            
# The method now gets a list of files inside the folder with the name of the hotel being iterated which is inside the folder
# called hotels

            list_of_hotel_names.append(hotel_object.name)

            hotel_object_name_lower = (hotel_object.name).lower()
            
            hotel_folder_name = hotel_object_name_lower.replace(" ","_")
            
            list_of_files = os.listdir("hotels/" + hotel_folder_name)
            
# The method now iterates through the list_of_files and obtain all the YEAR for any CSV file which has the MONTH which matches
# the month given as input
# Our desired file ends with MONTH.csv where month is given as input

            desired_file_ending = months_string + ".csv"
            
            list_of_year = [] 

            for elem in list_of_files:
                
                length_of_file_name = len(elem)
                
# All our desired YEAR_MONTH.csv files end with the format MONTH.csv
# So, whenever we find a file with such an ending we add the first 4 elements of that file into the list
# if it has not been added to the list before hand ( i.e making sure no duplicate year is stored in list to reduce redundancy)

                if elem[(len(elem) - 7):] == desired_file_ending: # last 7 elements taken into consideration 
                    
                    year = int(elem[:4]) # First 4 elements of a CSV file represents the year 
                    
                    if year not in list_of_year:
                    
                        list_of_year.append(year)
                        
# creating an empty list which will contain all the tuples from the values of the room_info_dictionary
                        
            list_of_tuples = [] 
                    
            for year in list_of_year:
                
                room_info_dictionary = hotel_object.load_reservation_strings_for_month(hotel_folder_name, months_string, year)
                
# creating a dictionary which will have year in list_of_year as its keys and the values of the dictionary will be
# the values of room_info_dictionary for that particular year

                for keys in room_info_dictionary:
                    
                    for tuples in room_info_dictionary[keys]:
                        
                        list_of_tuples.append(tuples)
                
                year_reservation_info_dictionary[year] = list_of_tuples
              
# The method now iterates through year_reservation_info_dictionary as many as times as the number of days of the month
# The method checks from the tuples, for the day being iterated, for how many tuples the 4th element is not an empty string
# i.e booking is made for that for each of that day
# The method increases the value of reservation_counter then by 1 and appends it to a list
# which contains the number of reservations of a particular hotel for month given as input for all year

            list_of_reservation_number = [] 
            
            counter1 = 1
            
            while counter1 < (number_of_days + 1):
                
                number_of_reservations = 0 
                
                for keys in year_reservation_info_dictionary:
                    
                    for tuples in year_reservation_info_dictionary[keys]:
                        
                        if tuples[2] == counter1:
                            
                            if len(tuples[3]) != 0:
                                
                                number_of_reservations += 1
                                
                counter1 += 1                
                                
                list_of_reservation_number.append(number_of_reservations)
                
# creating a tuple with one list being the number of days of the month given as input, while the under list represents the number of
# reservations for each day for all the years for the hotel object being iterated 
                
            hotel_reservation_tuple = (list_of_days, list_of_reservation_number)
            
# This tuple for each hotel object is then added to the list_of_x_and_y which is
# a a two-dimensional list of 2-tuples of the list of x-values and y-values for each hotel

            list_of_x_and_y.append(hotel_reservation_tuple)
            
# The method now creates a line plot with one line per hotel, showing the number reservations each day of the month (all over the years)
# We should give titles for our axes and plot, and also display a legend containing a label with the hotel’s name for each line
# When finished plotting, the method saves the figure to a file called hotel_occupancies_MONTH.png
# where MONTH is given by the argument to the method

# The method now iterates through the list list_of_x_and_y
# Each element of this list is a tuple which has the x and y co-ordinate for a particular hotel

        counter2 = 0 # keeps track of the hotel object being plotted so that we can obtain their name

        for tuples in list_of_x_and_y:
            
            plt.plot(tuples[0], tuples[1], label = list_of_hotel_names[counter2])
            
            counter2 += 1
                     
# The method now adds appropriate title for the axes and the plot

        plt.title("Occupancies for month of " + months_string)
        
        plt.xlabel("Day of month")
        
        plt.ylabel("Number of reservations")
        
# The method now displays a legend containing a label with the hotel’s name for each line
        
        plt.legend()
        
# The method now saves the file in hotel_occupancies_MONTH.png where MONTH is given as input to this instance attribute

        plt.savefig("hotel_occupancies_" + months_string + ".png")
            
# The two-dimensional list of 2-tuples of the list of x-values and y-values for each hotel is then finally returned         
        
        return(list_of_x_and_y)
    


            

                


                
                
                
                
                    
            
                    
            
            

                                
                            
                


                    
                    

                        
        
                    
            
                
                    

                    
                    
                
                
                
                
        

            
            
        
        
        
        
            
            
            
            
        
        

    
























      
        

