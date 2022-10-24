from flask import Flask, request, jsonify

app = Flask(__name__)

# Most basic hardcoded version
@app.route("/data/2.5/weather")
def serve_weather():
    result = {
        "coord": {"lon": -123.3, "lat": 44.56}, 
        "weather": [{"id": 800, "main": "Clear", "description": "clear sky", "icon": "01d"}], 
        "base": "stations", 
        "main": {"temp": 287.23, "feels_like": 286.16, "temp_min": 285.39, "temp_max": 288.65, "pressure": 1022, "humidity": 56},
        "visibility": 10000, 
        "wind": {"speed": 2.06, "deg": 270}, 
        "clouds": {"all": 0}, 
        "dt": 1666570688, 
        "sys": {"type": 2, "id": 2040223, "country": "US", "sunrise": 1666535925, "sunset": 1666574158}, 
        "timezone": -25200, "id": 5720727, "name": "Corvallis", "cod": 200
    }
    return jsonify(result)

# import requests
# First iteration
# @app.route("/data/2.5/weather")
# def serve_weather():
    # "https://api.openweathermap.org/data/2.5/weather?lat=44.56&lon=-123.30&appid=d9721734a23ddd5b8f9affc44c6c557e"
    # if len(request.args) != 3:
    #     return jsonify("Error servicing request")

    # lat = request.args.get("lat")
    # lon = request.args.get("lon")
    # key = request.args.get("appid")
    # if not lat or not lon or not key:
    #     return jsonify("Error servicing request")

    # query = "https://api.openweathermap.org/data/2.5/weather?lat=" + lat + "&lon=" + lon + "&appid=" + key
    # result = requests.get(query)
    # return result.json()
