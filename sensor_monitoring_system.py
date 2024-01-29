'''
    This is a Environment monioring and Alerting System.
    More details will follow.
'''
import random
import asyncio
from global_variables import alert_zones
import time,sys
from global_variables import api_token,group_chat_id
from telegram_bot_class import Telegram_Module
from telegram.error import TelegramError
from telegram.error import BadRequest

#I am initializing my Environment parameters
try:

    co2 = 0.00
    temp = 0.00
    humdty = 0.00
    sensor_values_dict = {}
    telgram = Telegram_Module(api_token,group_chat_id)
    # created the function for the Co2
    def is_co2_voilated(co2):
        if co2 >= alert_zones['co2']['LL'] and  co2 <= alert_zones['co2']['UL'] :
            return True
        else:
            return False
    # created the function for the temp
    def is_temp_voilated(temp):
        if temp >= alert_zones['temp']['LL'] and  temp <= alert_zones['temp']['UL'] :

            return True
        else:
            return False
    # created the function for the humidity
    def is_hum_voilated(hum):
        if hum >= alert_zones['humdty']['LL'] and  hum <= alert_zones['humdty']['UL'] :
            return True
        else:
            return False
    def main():

        while True:
            co2=round(random.uniform(400,1500),2)
            temp=round(random.uniform(14,45),2)
            hum=round(random.uniform(30,60),2)

            #storing the sensor values in a dictionary
            sensor_values_dict['co2']=co2
            sensor_values_dict['temp']=temp
            sensor_values_dict['hum']=hum
            print(f'Generated values are : Co2:{co2} PPM ,Temp: {temp} Deg Cel,Humidity {hum} %')
            
            # Analysing the voilation of the co2
            violated_flg = is_co2_voilated(co2)
            print(is_co2_voilated(co2))

            if violated_flg == True:
                messg = f'Alert: CO2 levels Violated. CO2 value is {co2}'
                print(f'Violation detected: ${messg}')
                asyncio.run(telgram.send_test_message(messg))

           
            # Analysing the voilation of the Temp
            is_temp_voilated(temp)
            print(is_temp_voilated(temp))

            # Analysing the voilation of the Humidity
            is_hum_voilated(hum)
            print(is_hum_voilated(hum))

            for (k,v) in sensor_values_dict.items():
                print(f'{k}:{v}')
                
            #print(type(co2))
            #print("co2 = ",co2,"Temp = ",temp,"Humidity = ",hum)

            num = int(input('If you wanna break the code enter -1'))
            if (num == -1):
                break
            else :
                time.sleep(5) 

    if __name__ == '__main__':
        main()

except ModuleNotFoundError as e:
    print(f'Sorry the module was not found. Exception is {e}')
    sys.exit(0)
except TelegramError as e:
    print(f' Exception is {e}')
    if isinstance(e, BadRequest):
        print("Handle BadRequest")
    

    