score = int(input("Enter AQI: ").strip())

if 0 <= score <= 50:
    print("Good")
elif 51 <= score <= 100:
    print("Moderate")
elif 101 <= score <= 150:
    print("Unhealty for Sensitive Groups")
elif 151 <= score <= 200:
    print("Unhealthy")
elif 201 <= score <= 300:
    print("Very Unhealthy")
else:
    print("Hazadous")
