# ------------------------------------------------- #
# Title: Assignment 07
# Description: Demonstrate Pickling and Error Handling
# ChangeLog: (Who, When, What)
# Key Murray, 05/31/2022, Created Script
# ------------------------------------------------- #
import pickle


# Data -------------------------------------------- #

strFileName = "PlayerData.dat"
lstFavorite = []

# Processing -------------------------------------- #


def save_data_to_file(file_name, list_of_data):
    file = open(file_name, "wb")
    pickle.dump(list_of_data, file)
    file.close


def read_data_from_file(file_name):
    file = open(file_name, "rb")
    list_of_data = pickle.load(file)
    file.close
    return list_of_data


# Presentation ------------------------------------#


print("Enter your favorite Basketball Player, their Team, and Jersey Number:")
strPlayer = str(input("\nEnter your favorite Player's name:"))
strTeam = str(input("\nEnter the Team of your favorite Player:"))

while True:

    try:
        intJersey = int(input("\nEnter your favorite Player's Jersey Number:"))
        lstFavorite = [strPlayer, strTeam, intJersey]
    except ValueError:
        print("\nInvalid input. Please only provide a Jersey Number!\n")
        continue
    else:
        break

save_data_to_file(strFileName, lstFavorite)

print("\nHere are the details of your favorite Player:", "\n", read_data_from_file(strFileName))

print("\nExiting script!")
