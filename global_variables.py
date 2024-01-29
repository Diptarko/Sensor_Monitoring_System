'''
    This is a configurable settings module
'''
#Define the Alert zones for each paramater
alert_zones = {
    'co2':{'UL':1500,'LL':400},#CO2 levels
    'temp':{'UL':35,'LL':15},#Temp levels
    'humdty':{'UL':60,'LL':30}#Humidity Levels
}
api_token = '6550316879:AAHSV2gxUXjFCQ0PLOlsyEoevoo8YLP4xIk'
#https://api.telegram.org/bot6550316879:AAHSV2gxUXjFCQ0PLOlsyEoevoo8YLP4xIk/getUpdates
group_chat_id = '-4107383590'
