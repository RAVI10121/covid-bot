from bot import telegram_chatbot
from nested_lookup import nested_lookup
import json
from urllib.request import urlopen

import ast
# loads subscriber data

bot = telegram_chatbot("s")


# this is main function which uses json data from covid 19 api and searches it "
def informer(dist):
    jurl = urlopen("https://api.covid19india.org/state_district_wise.json")
    obj = json.loads(jurl.read())
    val = nested_lookup(dist, obj)
    try:
            return "Active cases in "+dist+" are: " + str(
                val[0]['active']) + "\n\n" + "The total cases till date are: " + str(
                val[0]["confirmed"]) + "\nTotal deaths till now: " + str(
                val[0]['deceased']) + "\nPatients Recovered: " + str(val[0]["recovered"])
   
    except:
        return "enter correct district name"



print("Bot server is ON")


update_id = None
# this lop fetch updates and passes it
while True:
  
    # check if message has been sent by any user
    updates = bot.get_updates(offset=update_id)
    updates = updates["result"]  # this stors all user id text etc

    # below lines checks if updates have came or timeout is done(came is +1 update id)
    # if came it fetch message text and user id . it sends meesage INPUT to the make reply function ,the OUTPUT
    # from this make reply is returned to send message function with user id that this fetched from updates
    # takes input and SUBSCRIBER ID and sends ,this message reciever
    if updates:
        for item in updates:
            update_id = item["update_id"]
            try:
                message = str(item["message"]["text"])
            except:
                message = None
            from_ = item["message"]["from"]["id"]  # id

            if(message.lower()=="hi"):
                bot.send_message("HELLO THERE \n I am made by ravi",from_)
            else:
                msg=informer(message)
                bot.send_message(msg,from_)
          
          
