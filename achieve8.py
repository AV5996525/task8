#Name:          achieve_8.py
#Author:        AJ Varatharajan
#Date Created:  February 22, 2023
#Date Last Modified: March 23, 2023
#Purpose: User is able to input a value as either a temperature or speed and convert to and from it's interchangeable state.
#
#This program will output the requested conversion.
def celToFah (cel) : #celsius to fahrenheit function
    
    conv = (cel * 1.8) + 32
    return conv
def fahToCel (fah) : #fahrenheit to celsius function
    
    conv = (5/9) * (fah-32)
    return conv
def mphToKm (mph) : #Miles to kilometers function
    if mph <= 0:
        raise Exception
    conv = (mph * 1.609344)
    return conv
def kmToMph (km) : #Kilometers to miles function
    if km <= 0:
        raise Exception
    conv = (km / 1.609344)
    return conv


while True: #intializing outter loop
    
    try:
        choice = int(input("Welcome to the conversion calculator! Would you like to convert: \n1. Temperature \n2. Speed\n")) #Prompting user input and stripping spaces and saving it to a variable
    except ValueError:
        print("Invalid value")
    else:
        if choice == 1: #Temperature conversion selection
            while True:
                try:
                    choiceT = input("Would you like to convert from Celcicus (C, c) or Fahernite (F, f):\n").strip().lower() #Prompting user input and stripping spaces, converting to lower case and saving it to a variable
                except ValueError: #Except block prevent crash if user enter integer or decimal
                    print("Invalid value")
                else:
                    if choiceT == "c" :
                        while True:
                            try:
                                celinput = celToFah(float(input("Enter your celcius temperature:"))) #Prompting user input casting float on the input and saving to variable
                                print("The temperature is {} fahernite".format(celinput))  
                                break
                            except ValueError: #Except block prevent crash if user enter non-int or non-float value      
                                print("Integers and decimals only")
                              
                    elif choiceT == "f" :
                        while True:
                            try:
                                fahinput = fahToCel(float(input("Enter your fahernite:"))) #Prompting user input casting float on the input and saving to variable
                                print("The temperature is {} degrees celcius".format(fahinput))
                            except ValueError: #Except block prevent crash if user enter non-int or non-float value   
                                print("Integers and decimals only")    
                
        elif choice == 2:
            while True:
                try:
                    choiceS = input("Would you like to convert from Kilometers Per Hour (KMH, kmh) or Miles Per Hour (MPH, mph):\n").strip().lower()  #Prompting user input and stripping spaces, converting to lower case and saving it to a variable
                    if choiceS.isdigit() :
                        raise Exception("Letters only")
                except:  #Except block prevent crash if user enter int or float value    
                    print("Letters only")
                else:
                    if choiceS == "kmh" :
                        while True:
                            try:
                                kmhInput = kmToMph(float(input("Enter your speed in kilometers per hour:\n"))) #Prompting user input casting float on the input and saving to variable                          
                                if kmhInput < 0:
                                    raise Exception
                            except:
                                print("Positive integers or decimals only") #Except block prevent crash if user enter non-int or non-float value 
                            else:
                                print("The speed is {} miles per hour".format(kmhInput))
                          
                    elif choiceS == "mph" :
                        while True:
                            try:
                                mphInput = mphToKm(float(input("Enter your speed in miles per hour:\n"))) #Prompting user input casting float on the input and saving to variable
                                
                            except: #Except block prevent crash if user enter non-int or non-float value 
                                print("Positive integers or decimals only")
                            else:
                                print("The speed is {} kilometers per hour".format(mphInput))             

