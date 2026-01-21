# This is a copy of ar1_2026 however when looking at the atu video for ar2
# you will see how to progress by modifying this code.
# I originally thought it would be an interface to a user and then ask a question on
#an item like "enter a fllod risk threshold" however I think it can all be done interanally
#using scenarios 1 & 2 and defining the variables internally and then using the model to
#predict the outcome.


import pandas as pd
import serial
#Import the data
df = pd.read_csv('Br1-3-2026-data.csv')
#Calculate the risk
df['Flood Risk'] = df['Moisture']*3
df['Storm Risk'] = df['Sound'] * df['Temp']/2
print(df)


def get_alert(score):
    if score > 55:
        return "High Flood Risk"
    return "No Flood Risk- Safe"
#apply the warning to every row
df['Alert'] = df['Flood Risk'].apply(get_alert)
#1. Create a copy of DATA
df_flood = df.copy()
#2 Create a disaster conditions
df_flood['Moisture'] = 100
df_flood['Temp'] = 60

#Re-Run Storm Logic
df_flood['Flood Risk'] = df_flood['Moisture'] *2
df_flood['Alert'] = df_flood['Flood Risk'].apply(get_alert)

print("-----Scenario results -----")
print(f"Average Non-Flood Risk: {df['Flood Risk'].mean():.2f}")
print(f"Average Flood Risk: {df_flood['Flood Risk'].mean():.2f}")
print("Number of Warnings :", df_flood[df_flood['Alert'] == "High Flood Risk"].shape[0])

"""
#used for processing Embedded CSV file
def get_alert(score):
    if score > 15:
        return "High Flood Risk"
    return "No Flood Risk- Safe"

def check_flood_risk(x,z):
    #print("indside func")
    risk = x*z
    if x > 2000:
        return "High Flood Risk"
    return "No flood risk"

df['Flood_risk'] = df['Moisture'] * 5
df['Alert'] = df['Flood_risk'].apply(get_alert)
print(df['Alert'].value_counts())
print(df)

ser = serial.Serial("COM3",115200)
#ser.open()
port = "COM3"
print(port)
if port:
    print(f"Connected to {port}")
    #ser = serial.Serial(port, 115200)
else:
    print("No MicroBit Found")
print('Live Data')
while True:
    line = ser.readline().decode('utf-8').strip()
    print(line)
    data = line.split(':')
    print("data",data)
    #print("data[2]",data[2])
    x = int(data[1])   #microbit moisture
    y = int(data[2])   #microbit temp
    z = 2 #Moisture multiplier
    temp = int(data[1])
    #print(f"moisture - (x,y) temp - {temp}")
    
    risk = check_flood_risk(x,z)
    print(f'risk-{risk}')
  """      

