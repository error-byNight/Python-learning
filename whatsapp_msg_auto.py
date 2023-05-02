import pywhatkit
import time

phone_no = "+916206030600"
message = "Sonu Kumar singh"
hour = 17
minute = 13

for i in range(3):
    if i == 0:
        # Send the first message with a delay of 21 seconds
        pywhatkit.sendwhatmsg(phone_no, message, hour, minute, wait_time=10)
    else:
        # Send subsequent messages with a delay of 24 hours (approximately 86375 seconds)
        pywhatkit.sendwhatmsg(phone_no, message, hour, minute, wait_time=86375)
    time.sleep(10) # wait for 10 seconds before sending the next message
