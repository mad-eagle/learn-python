import time

hour = int(time.strftime("%H"))

if 5 <= hour < 12 :
    print("Good Morning")
elif 12 <= hour < 18:
    print("Good Afternoon")
elif 18 <= hour < 20:
    print("Good Evening")
else:
    print("Good Night")