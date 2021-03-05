import requests
from datetime import datetime
import smtplib
import time

# throw away
MY_EMAIL = 'nick6999@yahoo.ca'
MY_PW = 'kbyqimwzidbxorqq'
MY_LAT = 46.220196  # Your latitude
MY_LONG = -64.534683  # Your longitude

WHIT_LAT = 46.093570
WHIT_LONG = -67.268540

JOE_LAT = 46.176530
JOE_LONG = -67.573020

global_msg = 'Subject: Look Up The ISS is above you in the sky right now.'


def is_iss_overhead():
    global global_msg
    global_msg = 'fuck you'
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    # Your position is within +5 or -5 degrees of the ISS position.
    if MY_LAT - 5 <= iss_latitude <= MY_LAT + 5 and MY_LONG - 5 <= iss_longitude <= MY_LONG + 5:
        return True


def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now().hour

    if time_now >= sunset or time_now <= sunrise:
        return True


# If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.

while True:
    time.sleep(60)
    if is_night() and is_iss_overhead():
        conn = smtplib.SMTP('smtp.mail.yahoo.com', 587)
        conn.starttls()
        conn.login(MY_EMAIL, MY_PW)
        conn.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg='Look above for the International Space Station!'
        )


