
import serial
import csv
import os

ser = serial.Serial("COM8",115200)
line = ser.readline().decode("utf-8",errors="ignore").strip()
print("line",line)
#filename = "c:\Users\\pbarry\Desktop\Python Programs\Sample_Final_2024\Br1-3-2026.csv"
#filename = "Br1-3-Naomi-Data.csv"
filename = "Br1-3-2026.csv"



for x in range(4):
    print(line)
    parts = line.split(",")
    print(parts)
    Moisture = int(parts[0])
    Temp = int(parts[1])
    #light = int(parts[2])
    #sound = int(parts[3])
    
    print("My Moisture is ", Moisture, "MyTemp is ", Temp, )
    line = ser.readline().decode("utf-8",errors="ignore").strip()

    with open(filename, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([Moisture,Temp])
print(os.getcwd())
