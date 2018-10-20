from flask import Flask, render_template, request, jsonify
import queries
import calculate
import datetime

app = Flask(__name__)


@app.route("/", methods=["GET"])
def main():
    return render_template("index.html")
    # return "Hello World"


@app.route("/predictcoords", methods=["GET"])
def predict_coords():
    try:
        lat, lon = request.args.get("lat"), request.args.get("lon")

    except Exception as e:
        print(e)


@app.route("/predict", methods=["GET"])
def predict():
    try:
        city = request.args.get("city").lower()
        district = request.args.get("district").lower()
        weather_data = queries.getLatestWeather(city, district)
        print(weather_data)
        population_data = queries.getPopulationData(city, district)
        print(population_data)

        prob = calculate.calculateProbability(weather_data)

        return jsonify(time=datetime.datetime.now(), city=city, district=district, probability=prob)

    except Exception as e:
        print(e)


@app.route("/test", methods=["GET"])
def test():
    return jsonify(queries.test())


if __name__ == "__main__":
    app.run()
