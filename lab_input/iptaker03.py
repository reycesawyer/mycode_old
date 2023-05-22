#!/usr/bin/env python3
"""Alta3 Research | RZFeeser
   print() - concatenate vs print a series of items"""

def main():

    # collect string input from the user
    user_input = input("Please enter an IPv4 IP address:")
    
    ## the line below creates a single string that is passed to print()
    # print("You told me the IPv4 address is: " + user_input)
    
    ## print() can be given a series of objects separated by a comma
    print("You told me the IPv4 address is:", user_input)

    vendorname = input("Enter the vendor name of the device where the IP is assigned:")

    print("You told me the vendor name is:", vendorname)

main()


#CHALLENGE 01 - Add two more lines of code at the bottom of your script. They should be written as follows:

#The first line should collect and store input from the user. Ask the user for the 'vendor name' associated with the device. Use any variable name you would like.
#Use a second line of code to print the input you just collected from the user.
