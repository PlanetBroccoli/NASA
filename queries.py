import mysql.connector

# Change this!
mydb = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    passwd="",
    database="nasa",
)

mycursor = mydb.cursor()


def test():
    mycursor.execute("SELECT * FROM lol")

    data_labels = ["humidity", "temperature",
                   "pressure", "wind_speed", "rain"]
    data = mycursor.fetchall()
    return mycursor.fetchall()


def getLatestWeather(city, district, language="en"):
    try:
        station = getStation(city, district, language)["station"]
        condition = "`station_name` = '%s'" % (station)
        database = "weather"
        query = "SELECT `pressure`, `max_pressure`, `min_pressure`, `temperature`, `max_temperature`, `min_temperature`, `humidity`, `min_humidity`, `wind_speed`, `max_gust`, `precipitation` FROM %s WHERE %s ORDER BY `id` DESC LIMIT 1" % (
            database, condition)

        mycursor.execute(query)

        # Humidity, Temperature, Pressure, Wind Speed, Rainfall
        data_labels = ["pressure", "max_pressure", "min_pressure", "temperature", "max_temperature",
                       "min_temperature", "humidity", "min_humidity", "wind_speed", "max_gust", "precipitation"]
        data = [mycursor.fetchone()]

        return generateDictionary(data, data_labels)

    except Exception as e:
        print(e)


def getPopulationData(city, district, language="en"):
    try:
        district_languages = {"en": "district_en", "zh": "district"}
        city_languages = {"en": "city_en", "zh": "city"}

        district_lang, city_lang = district_languages[language], city_languages[language]
        database = "districts"
        condition = "`%s` LIKE '%s' AND `%s` LIKE '%s'" % (
            city_lang, city, district_lang, district)

        query = "SELECT `population`, `males`, `females`, `area`, `density`, `type` FROM %s WHERE %s" % (
            database, condition)

        mycursor.execute(query)

        # Population, Males, Females, Area, Population Density, Type
        data_labels = ["population", "males",
                       "females", "area", "density", "type"]
        data = mycursor.fetchall()

        return generateDictionary(data, data_labels)

    except Exception as e:
        print(e)


def getStation(city, district, language="en"):
    try:
        district_languages = {"en": "district_en", "zh": "district"}
        city_languages = {"en": "city_en", "zh": "city"}

        district_lang, city_lang = district_languages[language], city_languages[language]

        database = "districts"

        condition = "`%s` LIKE '%s' AND `%s` LIKE '%s'" % (
            city_lang, city, district_lang, district)

        mycursor.execute(
            "SELECT `station` FROM %s WHERE %s" % (database, condition))

        # Station
        data_labels = ["station"]
        data = mycursor.fetchall()

        return generateDictionary(data, data_labels)

    except Exception as e:
        print(e)


def getDataForTheWeek(year, week, station):
    try:
        year_column = "year"
        week_column = "week"
        station_column = "station_name"
        database = "weather"

        condition = "`%s` LIKE '%s' AND `%s` LIKE '%s' AND `%s` LIKE '%s'" % (
            year_column, year, week_column, week, station_column, station)

        mycursor.execute("SELECT * FROM %s WHERE %s" % (database, condition))

        data_labels = ["id", "year", "month", "week", "day_of_year",
                       "station_name", "pressure", "max_pressure", "min_pressure", "temperature", "max_temperature", "min_temperature", "humidity", "min_humidity", "wind_speed", "max_gust", "precipitation", "sunshine", "max_uv", "cloud"]
        data = mycursor.fetchall()
        return generateDictionary(data, data_labels)
    except Exception as e:
        print(e)


def getWeeklyData(year, week, station):
    try:
        year_column = "year"
        week_column = "week"
        station_column = "station_name"
        database = "week_weather"

        condition = "`%s` = '%s' AND `%s` = '%s' AND `%s` LIKE '%s'" % (
            year_column, year, week_column, week, station_column, station)

        mycursor.execute("SELECT * FROM %s WHERE %s" % (database, condition))
        data_labels = ["id", "year", "week", "station_name", "pressure", "max_pressure", "min_pressure", "temperature", "max_temperature",
                       "min_temperature", "humidity", "min_humidity", "wind_speed", "max_gust", "precipitation", "sunshine", "max_uv", "cloud"]
        data = mycursor.fetchall()

        return generateDictionary(data, data_labels)

    except Exception as e:
        print(e)


def generateDictionary(data, labels):
    if len(data) == 1:
        output = {}

        for i in range(len(labels)):
            output[labels[i]] = data[0][i]
        return output

    else:
        output_list = []
        for elem in data:
            output = {}
            for i in range(len(labels)):
                output[labels[i]] = elem[i]

            output_list.append(output)
        return output_list
