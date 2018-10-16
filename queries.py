import mysql.connector

# Change this!
mydb = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    passwd="",
    database="nasa",
)

mycursor = mydb.cursor()


def getLatestWeather(city, district):
    try:
        mycursor.execute(
            "SELECT `humidity`, `temperature`, `pressure`, `wind_speed`, `rain` FROM weather WHERE `city` = %s AND `district` = %s `humidity` != "" AND `temperature` != "" AND `pressure` != "" AND `wind_speed` != "" AND `rain` != "" ORDER BY `id` DESC LIMIT 1" % (city, district))

        # Humidity, Temperature, Pressure, Wind Speed, Rainfall
        return mycursor.fetchone()

    except Exception as e:
        print(e)


def getPopulationData(city, district):
    try:
        mycursor.execute(
            "SELECT `males`, `females`, `area`, `type` FROM districts WHERE `city` = %s AND `district` = %s" % (city, district))

        # Males, Females, Area, Type
        data = mycursor.fetchone()
        pop = int(data[0]) + int(data[1])

    except Exception as e:
        print(e)
