import requests
#from pygame import mixer 
from datetime import datetime, timedelta
import time

Pincode=input("Enter your pincode \n ")
date=int(input("Enter the no. of days"))
age = 18
pincodes = [Pincode]
num_days = date 

print_flag = 'Y'  #optional Can be removed.

print("Starting search for Covid vaccine slots!")

actual = datetime.today()
list_format = [actual + timedelta(days=i) for i in range(num_days)]
actual_dates = [i.strftime("%d-%m-%Y") for i in list_format]

while True:
    counter = 0   

    for pincode in pincodes:   
        for given_date in actual_dates:

            URL = "https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByPin?pincode={}&date={}" .format(pincode, given_date)
            header = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36'} 
            
            result = requests.get(URL, headers=header)

            if result.ok:
                response_json = result.json()
                if response_json["centers"]:
                    if(print_flag.lower() =='y'):   #can be removed (optional).
                        for center in response_json["centers"]:
                            for session in center["sessions"]:
                                if (session["min_age_limit"] <= age and session["available_capacity"] > 0 ) :
                                    #print(session , center)
                                    print('Pincode: ' + pincode)
                                    print("Available on: {}".format(given_date))
                                    print("\t Center Name: ", center["name"])
                                    print("\t Address:", center["address"])
                                    #print("\t", center["block_name"])
                                    print("\t Price: ", center["fee_type"])
                                    print("\t Availablity : ", session["available_capacity"])
                                    print("\t Dose- 1 : ", session["available_capacity_dose1"])
                                    #print("\t Dose- 2 : ", session["available_capacity_dose2"])

                                    if(session["vaccine"] != ''):
                                        print("\t Vaccine type: ", session["vaccine"])
                                    print("\n")
                                    counter = counter + 1
                                
            else:
                print("No Response!")
                
    if counter:
        print("No Vaccination slot available!")
    else:
        #mixer.init()
        #mixer.music.load('D:\\The feels.mp3')
        #mixer.music.play()
        print("Search Completed!")

    dt = datetime.now() + timedelta(minutes=3)

    while datetime.now() < dt:
        time.sleep(1) # 1 means true.
