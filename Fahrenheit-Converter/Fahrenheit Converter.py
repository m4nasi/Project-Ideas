#Intro: this code is designed to calculate fahrenheit to celsius and vise versa
##Date: 12/09/17
###Author: Manasi Mehta
print ("Would you like the fahrenheit to celsius? If so please type yes. If not please type no.")
answer = (input("?"))
play = True
while play == True:
    if (answer.lower() == "no") :
        print ("What is the celsius of where you are? ")
        firstCelsius = int(input("?"))
        print ("The celsius is " + str(firstCelsius) + " degrees celsius right? Yes or No")
        answer = (input("?"))
        while (answer.lower() == "no") :
            print ("What is the celsius of where you are? ")
            firstCelsius = int(input("?"))
            print ("The celsius is " + str(firstCelsius) + " degrees celsius right? Yes or No")
            answer = (input("?"))
            
        realFahrenheit = firstCelsius + 32
        finalFahrenheit = realFahrenheit / 0.55555556
        print ("The fahrenheit is " + str(finalFahrenheit) + " fahrenheit")
        play = False
        
    elif (answer.lower() == "yes") :
        print ("What is the fahrenheit of where you are? ")
        fahrenheit = int(input("?"))
        print ("The fahrenheit is " + str(fahrenheit) + " fahrenheit right? Yes or No")
        answer = (input("?"))

        while (answer.lower() == "no")  :
            print ("What is the fahrenheit of where you are? ")
            fahrenheit = int(input("?"))
            print ("The fahrenheit is " + str(fahrenheit) + " fahrenheit right? Yes or No")
            answer = (input("?"))
            
        celsius = fahrenheit - 32
        realCelsius = celsius * 0.55555556
        print ("In celsius, the temperature is " + str (realCelsius) + (" degrees celsius"))
        play = False

print("Have a good day")
