import pandas as pd
import serial # imports the commands used for serial import
import csv # csv commands
import time
import matplotlib.pyplot as plt
def menu():
    print("\n************************************") 
    print("************** MENU ****************") 
    print("*1: Run inputs from device         *") 
    print("*2: Run inputs using national data *") 
    print("*3: What Ifs                       *") 
    print("*4: Exit                           *") 
    print("************************************")
    print()

            # Fire risk function
def fire_risk(temperature, soil_moisture, wind_speed):
    score = 0
    if temperature >= 30:
        score += 2
    elif temperature >= 20:
        score += 1
    elif temperature >= 10:
        score += 0
    if soil_moisture <= 10:
        score += 2
    elif soil_moisture <= 20:
        score += 1
    elif soil_moisture <= 30:
        score += 0
    if wind_speed >= 10:
        score += 2
    elif wind_speed >= 5:
        score += 1
    elif wind_speed >= 0:
        score += 0
    return "Fire Risk" if score >= 4 else "No Fire Risk"



def fire_risk_whatifs(temperature, soil_moisture, wind_speed):
    # Start with 0 points
    score = 0

    # Rule 1: Temperature
    if temperature >= 30:
        score += 2
    elif temperature >= 20:
        score += 1
    elif temperature >= 10:
        score += 0
            

    # Rule 2: Soil moisture
    if soil_moisture <= 10:
        score += 2
    elif soil_moisture <= 20:
        score += 1
    elif soil_moisture <= 30:
        score += 0

    # Rule 3: Wind speed
    if wind_speed >= 10:
        score += 2
    elif wind_speed >= 5:
        score += 1
    elif wind_speed >= 0:
        score += 0

    # Final decision
    if score >= 4:
        return "Fire Risk"
    else:
        return "No Fire Risk"
  
menu()
userInput = int(input("Please enter your selection"))
while userInput!=4:
    if userInput ==1:
        
        ser = serial.Serial("COM7", 115200) #links the port for communication 

        line = ser.readline().decode ("utf-8", errors = "ignore").strip()
        #sets the read as variable line. .strip removes empty spaces. Sets the data to UTF-8
        filename = "BR2.CSV"

        for x in range(100):
            line = ser.readline().decode ("utf-8", errors = "ignore").strip()
        # print (line)

            parts = line.split(",") # splits the line data using the comma

            micro_temp = parts[0] # sets the temp as the first column

            micro_moisture = parts[1] # sets the light as the second column

            micro_wind = parts[2]
            
            print ("The temp is", micro_temp, "The moisture level is", micro_moisture,"The speed is",micro_wind) 

            with open(filename, "a", newline="") as file: # using with open measn we won't have to use file.close()
                writer = csv.writer(file)

                writer.writerow([micro_temp, micro_moisture,micro_wind])
            time.sleep(0.5)
        print ("BR2: I saved my csv file as", filename)
        
        """
        Code from the model can go in here. Change the CSV to BR2.csv.
        """
        userInput = 0
        
    elif userInput ==2:
            #import the national csv data from CSO etc.
        
        file = pd.read_csv("environment_data.csv") #sample csv with rows and columsn


            
        results = []

        for row in file.itertuples():#(index=False):#can use a tuple as the data won't change
            #index = false removes the row index from the beginning of the output
            risk = fire_risk(row.temperature, row.soil_moisture, row.wind_speed)
            results.append(risk)
        
        file["risk"] = results
        #playing around with interface here - not required but looks cool
        file["icon"] = file["risk"].apply(lambda r: "🔥" if r == "Fire Risk" else "😊")

        print("\033[1mMy AR1 national data model output is\n\n\033[0m",file)#makes the output bold
        
        
        

        risk_counts = file["risk"].value_counts()
        plt.bar(risk_counts.index, risk_counts.values)
        plt.xlabel("Risk")
        plt.ylabel("Frequency")
        plt.title("Fire Risk in Forestry")
        plt.show()
        

        userInput = 0
            
    elif userInput == 3:
        print()
        print()
        print("What If Menu")
        print("Please choose one of the following:")
        print("1. Manual input of readings\n2. Pre defined scenarios\n3. Exit")
        option = int(input("Please enter the option you would like"))
        while option !=3:
            if option ==1:
                    
                #assign user inputs to the variables to use in the model
                temp = float(input("Please enter your what if temperature (°C): "))
                moisture = float(input("Please enter your what if soil moisture (%): "))
                wind = float(input("Please enter your what if wind speed (m/s): "))

                result = fire_risk_whatifs(temp, moisture, wind)
                print("Your resulting scenario is:", result)
                option = 0
            elif option ==2:
                print("Choose from one of the following")
                print("1. Temp and wind speed increase by 20%")
                print("2. Wind and soil moisture increase by 25%")
                print("3. All 3 inputs increase by 50%")
 
                scenario_input = int(input("Enter 1,2 or 3"))
                print()
                print()
                if scenario_input == 1:
                    file = pd.read_csv("environment_data.csv") #sample csv with rows and columsn


            
                    results = []

                    for row in file.itertuples():#(index=False):#can use a tuple as the data won't change
                        #index = false removes the row index from the beginning of the output
                        risk = fire_risk(row.temperature*1.2, row.soil_moisture*1.2, row.wind_speed)
                        results.append(risk)
                    
                    file["risk"] = results
                    #playing around with interface here - not required but looks cool
                    file["icon"] = file["risk"].apply(lambda r: "🔥" if r == "Fire Risk" else "😊")

                    print("\033[1mMy AR2 Scenario 1 model output is\n\n\033[0m",file)
                    print()
                    print()
                    risk_counts = file["risk"].value_counts()
                    plt.bar(risk_counts.index, risk_counts.values)
                    plt.xlabel("Risk")
                    plt.ylabel("Frequency")
                    plt.title("Fire Risk in Forestry")
                    plt.show()
                elif scenario_input ==2:
                   
                    file = pd.read_csv("environment_data.csv") #sample csv with rows and columns
                    results = []

                    for row in file.itertuples():#(index=False):#can use a tuple as the data won't change
                        #index = false removes the row index from the beginning of the output
                        risk = fire_risk(row.temperature, row.soil_moisture*1.25, row.wind_speed*1.25)
                        results.append(risk)
                    
                    file["risk"] = results
                    #playing around with interface here - not required but looks cool
                    file["icon"] = file["risk"].apply(lambda r: "🔥" if r == "Fire Risk" else "😊")

                    print("\033[1mMy AR2 Scenario 2 model output is\n\n\033[0m",file)
                    print()
                    print()
                    risk_counts = file["risk"].value_counts()
                    plt.bar(risk_counts.index, risk_counts.values)
                    plt.xlabel("Risk")
                    plt.ylabel("Frequency")
                    plt.title("Fire Risk in Forestry")
                    plt.show()

                elif scenario_input ==3:
                    file = pd.read_csv("environment_data.csv") #sample csv with rows and columsn
                    results = []

                    for row in file.itertuples():#(index=False):#can use a tuple as the data won't change
                        #index = false removes the row index from the beginning of the output
                        risk = fire_risk(row.temperature*1.5, row.soil_moisture*1.5, row.wind_speed*1.5)
                        results.append(risk)
                    
                    file["risk"] = results
                    #playing around with interface here - not required but looks cool
                    file["icon"] = file["risk"].apply(lambda r: "🔥" if r == "Fire Risk" else "😊")

                    
                    print("\033[1mMy AR2 Scenario 3 model output is\n\n\033[0m",file)
                    risk_counts = file["risk"].value_counts()
                    plt.bar(risk_counts.index, risk_counts.values)
                    plt.xlabel("Risk")
                    plt.ylabel("Frequency")
                    plt.title("Fire Risk in Forestry")
                    plt.show()
                option = 0
            else:
                print("\033[1mInvalid choice\033[0m")
                print()
                print()
            print()
            print()
            print("Please choose one of the following:")
            print("1. Manual input of readings\n2. Pre defined scenarios\n3. Exit")
            print()
            option = int(input("Please enter the option you would like"))
            print()
            print()
                
    else:
        print("\033[1mInvalid choice\033[0m")
        print()
    menu()
    print()
    userInput = int(input("\033[1mPlease enter your selection\033[0m"))
    print()
    
print("Thank you for using the forestry fire risk monitor")
            

         

