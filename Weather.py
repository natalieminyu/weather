
def main():

    print("Accessing weather data...")
    weather_dict = weather_report()
    print("The current weather has been access for", weather_dict.get("location"))
    print()
    
    prompt = input("What weather information would you like? ").lower()

    while prompt != "done":
        if prompt == "temperature":
            print ("The temperature in", weather_dict.get("location"), "is", weather_dict.get("temperature"), "degrees F")
            print()
        elif prompt == "wind speed":
            print ("The wind speed in", weather_dict.get("location"), "is", weather_dict.get("wind speed"), "mph")
            print()
        elif prompt == "weather":
            print ("The weather in", weather_dict.get("location"), "is", weather_dict.get("weather"))
            print()
        elif prompt == "humidity":
            print ("The humidity in " + weather_dict.get("location")+ " is "+ weather_dict.get("humidity") +"%")
            print()
        else:
            print("That data is not available.")
            print()

        prompt = input("What weather information would you like? Or, to end, enter 'done': ").lower()

    print()
    prompt2 = input("Would you like to export the full weather report? yes/no ").lower()

    if prompt2 == "yes":
        report(weather_dict)
        print("The weather report has been exported")

def weather_report():
    
    import urllib.request

    page = urllib.request.urlopen("http://w1.weather.gov/xml/current_obs/KTYS.xml")

    html = page.read() # reads all the info in one large chunk
    html = str(html)

    search_items = ["<location>", "<weather>", "<temp_f>", "<relative_humidity>", "<wind_mph>"]
    search_end = ["</location>", "</weather>", "</temp_f>", "</relative_humidity>", "</wind_mph>"]

    opening_tag = []
    
    for item in search_items: #searching for the index position of the opening tags, put in list
        a = html.find(item)
        length = len(item)
        opening_tag.append(a + length)

    closing_tag = []
    for item in search_end: #searching for the index position of the closing tags, put in list
        b = html.find(item)
        closing_tag.append(b)

    data = []   
    for i, j in zip(opening_tag, closing_tag):
        value = html[i:j]
        data.append(value)

    weather_dict = {}
    weather_dict["location"] = data[0]
    weather_dict["weather"] = data[1]
    weather_dict["temperature"] = data[2]
    weather_dict["humidity"] = data[3]
    weather_dict["wind speed"] = data[4]

    return weather_dict

def report(weather_dict):

    file = open("Full weather report", "w")

    for key, value in weather_dict.items():
        file.write(key)
        file.write(":")
        file.write(value)
        file.write("\n")

    file.close()

main()
