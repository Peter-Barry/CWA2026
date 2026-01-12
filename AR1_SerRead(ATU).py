import serial
import mb_detect

def check_flood_risk(x,y,moisture):
    flood_risk = moisture * 5
    if flood_risk > 25:
        word = "Flood Warning"
    else:
        word = "Safe"
    return flood_risk, word
    
port = mb_detect.find()
print(port)
if port:
    print(f"Connected to {port}")
    ser = serial.Serial(port, 115200)
else:
    print("No MicroBit Found")
try:
    print('Live Data')
    while True:
        line = ser.readline().decode('utf-8').strip()
        print(line)
        data = line.split(':')
        print(data)
        x = int(data[1])
        y = int(data[2])
        temp = int(data[4])
        print(f"moisture - (x,y) temp - {temp}")
        risk, defined = check_flood_risk(x,y,moisture)
        print(f'risk-{risk}')
        print(f'{defined}')
        
        
except KeyboardInterrupt:
    print("\n\Exiting program.")
except Exception as e:
    print(f"An erro has occurred during data Comms:  {e}")
finally:
    if 'ser' in locals() and ser.is_open:
        ser.close()
        print("Serial Connnection Closed")
        
    



