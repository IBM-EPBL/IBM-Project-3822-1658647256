import random
import time
a=random.random()

while True:
    temperature=random.randint(0, 100 )
    if(temperature > 50):
        print(f"The Temperature is {temperature} higher then 50: ,⏰ alarm is on")
    else:
        print("The Temperature is less than 50")
    humidity =random.randint(10, 100)
    if(humidity > 50):
        print(f"The Humidity is {humidity} greater than 50:,⏰ alarm is on")
    else:
        print("The Humidity is lesser than 50")
    time.sleep(1.5)
