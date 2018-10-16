from flask import Flask, render_template, request, jsonify
import queries
import calculate

app = Flask(__name__)


@app.route("/", methods=["GET"])
def main():
    return render_template("index.html")


@app.route("/calculate", methods=["GET"])
def calc():
    humidity = request.args.get("h")
    temperature = request.args.get("t")
    pressure = request.args.get("p")
    wind_speed = request.args.get("w")
    rain = request.args.get("r")
    population = request.args.get("pop")
    area = request.args.get("a")

    attributes = [pressure, temperature, humidity,
                  wind_speed, rain, population, area]
    prediction_matrix = [0, 0, 0, 0, 0]

    prob = calculate.calculateProbability(*attributes)

    return jsonify(probability=prob)


@app.route("/predict", methods=["GET"])
def predict():
    try:
        city = request.args.get("city").lower()
        district = request.args.get("district").lower()

        h, t, p, w, r = queries.getLatestWeather(city, district)

        prob = 0.2

        return jsonify(probability=prob)

    except Exception as e:
        print(e)


if __name__ == "__main__":
    app.run()
