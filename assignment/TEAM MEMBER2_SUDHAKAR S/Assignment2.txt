import random
import time
def temperature(temp):
        print(temp)
        if (temp > 70.0):
            print("Alarm detected for",temp,"... temperature is HIGH!")
            time.sleep(0.75)
        elif(temp >50.0):
            print(temp,"Normal temperature is detected")
            time.sleep(0.75)
        else:
            print(temp,"safe temperature is detected")
            time.sleep(0.75)
            
def humidity(hum):
    print(hum)
    if(hum >20.0):
        print(hum,"High humidity is detected! ")
        time.sleep(0.75)
    elif(hum >10.0):
        print(hum,"Normal humidity is detected")
        time.sleep(0.75)
    else:
        print(hum,"safe humidity is detected")
        time.sleep(0.75)
        
while(1):
    temperature(temp= (random.random())*100)
    humidity(hum=(random.random())*100)
