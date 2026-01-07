import serial
import csv
import os

ser = serial.Serial("COM3",115200)
line = ser.readline().decode("utf-8",errors="ignore").strip()
#filename = "c:\Users\\pbarry\Desktop\Python Programs\Sample_Final_2024\Br1-3-2026.csv"
filename = "Br1-3-2026.csv"

for x in range(4):
    print(line)
    parts = line.split(",")
    microtemp = parts[0]
    extlight = parts[1]
    print("My Temp is ", microtemp, "MyLight is ", extlight)
    
    with open(filename, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([microtemp,extlight])
print(os.getcwd())