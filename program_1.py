#Matthew Tyler
#09/28/2025
#Kilometer Converter

def kilometer_conversion(kilometers):    
    miles = kilometers * 0.6214

    # Return the variable to the calling function
    return miles

#### This piece of the code has been done for you,
#### you only need to worry about the actual kilometer
#### conversion logic in the kilometer_conversion function
if __name__ == '__main__':
    # Get User Input
    print("This program will convert Kilometer to Miles")
    input_kilometers = float(input("How many kilometers do you want to convert?"))

    # Call kilometer_conversion, don't forget to pass in the kilometer parameter!
    new_measurement = kilometer_conversion(input_kilometers)

    # Display the miles
    print(format(input_kilometers, ".2f"), " Kilometers converts to: ", format(new_measurement,".2f"),"Miles")
