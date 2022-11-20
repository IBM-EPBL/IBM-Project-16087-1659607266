import wiotp.sdk.device
import time
import random
import requests
myConfig = { 
    "identity": {
        "orgId": "1s2adz",
        "typeId": "ardiuno",
        "deviceId":"0910"
    },
    "auth": {
        "token": "12345678"
    }
}

def myCommandCallback(cmd):
    print("Message received from IBM IoT Platform: %s" % cmd.data['command'])
    m=cmd.data['command']

client = wiotp.sdk.device.DeviceClient(config=myConfig, logHandlers=None)
client.connect()
count=0
while True:

    s1=['Good','Need maintannce','bad condition','Needs checking']
    s2=['Good','Need maintanence','bad condition','Low water level','No water']
    s3=['Good','No electricity','bad condition','Needs checking']
    s4=['Good','Not working','bad condition','Needs checking']
    random.shuffle(s1)
    random.shuffle(s2)
    random.shuffle(s3)
    random.shuffle(s4)
    
    temp=random.randint(-40,84)
    humid=random.randint(0,100)
    gas=random.randint(0,100)

    if(temp>68 and gas>80):
        print("\n")
        myData={'temp':str(temp)+chr(176)+"C", 'humid':str(humid)+" %", 'gas':str(gas)+" %", 'sensors':str(s1[0]), 'sprinklers':str(s2[0]), 'exhaust':str(s3[0]), 'alarm':str(s4[0]), 'condition':"Turn On Harzard-Protection System" }
        message="ALERT MESSAGE FROM FIRE MANAGEMENT SYSTEM:\n\n"+'Temperature:'+str(temp)+" C"+'\nHumidity:'+str(humid)+" %"+'\nGas-level:'+str(gas)+" %"+"\nCondition:Turn On Harzard-Protection System\n\n"+"Sensors:"+str(s1[0])+"\n"+"Sprinklers:"+str(s2[0])+"\n"+"Exhaust:"+str(s3[0])+"\n"+"Alarm:"+str(s4[0])+"\n"
        url = " https://www.fast2sms.com/dev/bulkV2?authorization=oxXvdFwBIzPDuOfpJnALG0VhUkj2YSQN6cTRie8qtZrglbK491tgWTBzkZclr4mPLwOp2nfEKDqoFAGH&route=q&message="+message+"%0A%0AHIGH%20TEMPERATURE%20AND%20GAS%20DETECTED!%0ATURN%20ON%20SAFTEY%20PROTECTION%20SYSTEM&language=english&flash=0&numbers=9500490577 "
        #response = requests.request("GET", url)
        #print(response.text)
        print(message)
        print("Turn On Harzard-Protection System")

    elif(temp>68 and gas<80):
        print("\n")
        myData={'temp':str(temp)+chr(176)+"C", 'humid':str(humid)+" %", 'gas':str(gas)+" %", 'sensors':str(s1[0]), 'sprinklers':str(s2[0]), 'exhaust':str(s3[0]), 'alarm':str(s4[0]), 'condition':"Turn On Fire-Protection System" }
        message="ALERT MESSAGE FROM FIRE MANAGEMENT SYSTEM:\n\n"+'Temperature:'+str(temp)+" C"+'\nHumidity:'+str(humid)+" %"+'\nGas-level:'+str(gas)+" %"+"\nCondition:Turn On Fire-Protection System\n\n"+"Sensors:"+str(s1[0])+"\n"+"Sprinklers:"+str(s2[0])+"\n"+"Exhaust:"+str(s3[0])+"\n"+"Alarm:"+str(s4[0])+"\n"
        url = " https://www.fast2sms.com/dev/bulkV2?authorization=oxXvdFwBIzPDuOfpJnALG0VhUkj2YSQN6cTRie8qtZrglbK491tgWTBzkZclr4mPLwOp2nfEKDqoFAGH&route=q&message="+message+"%0A%0AHIGH%20TEMPERATURE%20DETECTED!%0ATURN%20ON%20FIRE-PROTECTION%20SYSTEM&language=english&flash=0&numbers=9500490577"
        #response = requests.request("GET", url)
        #print(response.text)
        print(message)
        print("Turn On Fire-Protection System")
        
    elif(temp<68 and gas>80):
        print("\n")
        myData={'temp':str(temp)+chr(176)+"C", 'humid':str(humid)+" %", 'gas':str(gas)+" %", 'sensors':str(s1[0]), 'sprinklers':str(s2[0]), 'exhaust':str(s3[0]), 'alarm':str(s4[0]), 'condition':"Turn On Ventilation System" }
        message="ALERT MESSAGE FROM FIRE MANAGEMENT SYSTEM:\n\n"+'Temperature:'+str(temp)+" C"+'\nHumidity:'+str(humid)+" %"+'\nGas-level:'+str(gas)+" %"+"\nCondition:Turn On Ventilation System\n\n"+"Sensors:"+str(s1[0])+"\n"+"Sprinklers:"+str(s2[0])+"\n"+"Exhaust:"+str(s3[0])+"\n"+"Alarm:"+str(s4[0])+"\n"
        url = " https://www.fast2sms.com/dev/bulkV2?authorization=oxXvdFwBIzPDuOfpJnALG0VhUkj2YSQN6cTRie8qtZrglbK491tgWTBzkZclr4mPLwOp2nfEKDqoFAGH&route=q&message="+message+"%0A%0AHIGH%20GAS%20DETECTED!%0ATURN%20ON%20VENTILATION%20SYSTEM&language=english&flash=0&numbers=9500490577"
        #response = requests.request("GET", url)
        #print(response.text)
        print(message)
        print("Turn On Ventilation-Protection System")

    else:
        print("\n")
        myData={'temp':str(temp)+chr(176)+"C", 'humid':str(humid)+" %", 'gas':str(gas)+" %", 'sensors':str(s1[0]), 'sprinklers':str(s2[0]), 'exhaust':str(s3[0]), 'alarm':str(s4[0]), 'condition':"SAFE" }
        message="ALERT MESSAGE FROM FIRE MANAGEMENT SYSTEM:\n\n"+'Temperature:'+str(temp)+" C"+'\nHumidity:'+str(humid)+" %"+'\nGas-level:'+str(gas)+" %"+"\nCondition:SAFE\n\n"+"Sensors:"+str(s1[0])+"\n"+"Sprinklers:"+str(s2[0])+"\n"+"Exhaust:"+str(s3[0])+"\n"+"Alarm:"+str(s4[0])+"\n"
        url = "https://www.fast2sms.com/dev/bulkV2?authorization=oxXvdFwBIzPDuOfpJnALG0VhUkj2YSQN6cTRie8qtZrglbK491tgWTBzkZclr4mPLwOp2nfEKDqoFAGH&route=q&message="+message+"%0A%0ANO%20HAZARD%20DETECTED%0A%22EVERYTHING%20IS%20IN%20SAFE%20CONDITION%22&language=english&flash=0&numbers=9500490577"
        #response = requests.request("GET", url)
        #print(response.text)
        print(message)
        print("SAFE")

    def myOnPublishCallback():
        print("Publish Temperature = %s c" % temp,"Humidity = %s %%" % humid,"Gas Level =%s %%"% gas,"to IBM Watson\n")
        print("sensors: %s" %s1[0])
        print("sprinklers %s" %s2[0])
        print("exhaust: %s" %s3[0])
        print("alarm %s" %s4[0])

    client.publishEvent(eventId="status", msgFormat="json", data=myData, qos=0, onPublish=None)
    print("Published data Successfully: %s", myData)
    client.commandCallback = myCommandCallback
    time.sleep(10)

client.disconnect()
