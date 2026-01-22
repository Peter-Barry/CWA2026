import pandas as pd
import serial
df = pd.read_csv('Br1-3-2026-data.csv')
#print(df)


def get_alert(score):
    if score > 15:
        return "High Flood Risk"
    return "No Flood Risk- Safe"


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
    print(data)
    """
    x = int(data[1])
    y = int(data[2])
    temp = int(data[4])
    print(f"moisture - (x,y) temp - {temp}")
    risk, defined = check_flood_risk(x,y,moisture)
    print(f'risk-{risk}')
    print(f'{defined}')
       """ 
