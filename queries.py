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


def getStationWithCoords(lat, lon):
    condition = "`latitude` = %s AND `longitude` = %s" % (lat, lon)
    database = "districts"
    query = "SELECT `station` FROM %s WHERE %s LIMIT 1" % (database, condition)
    print(query)
    mycursor.execute(query)

    data_labels = ["station"]
    data = mycursor.fetchall()
    print(data)
    return generateDictionary(data, data_labels)

def getAllStations():
    return ['C0R170','C0R220','C0R580','C0R360','C0R480','C0R280','C0R380','C0R400','C0R470','C0R540','C0R490','C0R520','C0R590','C0R530','C0R570','C0R270','C0R280','C0R580','C0R650','C0R510','C0R190','C0R550','C0R640','C0R160','C0R650','C0R260','C0R240','C0R150','C0R420','C0R100','C0R400','C0R600','C0R130','C0V490','C0V690','C0V810','C0V670','C0V440','C0V490','C0V490','C0V710','C0V710','C0V690','C0V450','C0V710','C0V720','C0V730','C0V350','C0V770','C0V680','C0V440','C0V660','C0V760','C0V400','C0V370','C0V530','C0V750','C0V640','C0V640','C0V620','C0V650','C0V610','C0V740','C0V310','C0V800','C0V250','C0V260','C0V360','C0V790','C0V210','C0M800','C0X160','C0X110','C0X100','C0O950','C0X190','C0X100','C0X250','C0X230','C0X240','C0X270','C0X260','C0X050','C0X120','C0X060','C0X270','C0X130','C0O930','C0X080','C0X220','C0X150','C0X310','C0X280','C0X290','C0O970','C0O900','C0O980','C0X150','C0X180','C0O930','C0O810','C0V250','C0X200','C0X160','C0X170','C0X170','C0O960','C0O990','C0H950','C0I390','C0I080','C0I460','C0I410','C0I420','C0H890','C0I360','C0I110','C0H960','C0I380','C0I370','C0I090','C0M730','C0M730','C0M640','C0M740','C0M410','C0M670','C0M760','C0M750','C0M790','C0M650','C0M710','C0M530','C0M760','C0M690','C0M660','C0M720','C0M700','C0M520','C0M820','C0M780','C0B010','C0B010','C0A660','C0B010','C0A660','C0B010','C0AH30','C0U890','C0U780','C0U910','C0Z220','C0U900','C0U970','C0UA30','C0U990','C0U600','C0U780','C0UA50','C0U860','C0G730','C0G880','C0G890','C0G840','C0G890','C0G650','C0G650','C0G800','C0G830','C0G740','C0G790','C0G790','C0G860','C0G720','C0G660','C0G850','C0G820','C0G860','C0G770','C0G780','C0G830','C0G890','C0G620','C0G790','C0G730','C0G770','C0AC60','C0AD00','C0A9E0','C0AG90','C0AI00','C0AD10','C0AD40','C0A530','C0A650','C0AC80','C0ACA0','C0AG90','C0AH50','C0AD40','C0AH10','C0AH00','C0ACA0','C0AD10','C0AH80','C0A570','C0A660','C0A640','C0A920','C0A860','C0AD30','C0A880','C0A940','C0A550','C0AD50','C0D660','C0D660','C0D570','C0D540','C0D430','C0D580','C0UA10','C0D430','C0D480','C0D650','C0D540','C0D650','C0D660','C0D560','C0D540','C0D390','C0C700','C0C490','C0C540','C0C630','C0C650','C0C460','C0D650','C0C480','C0C660','C0C690','C0C590','C0C670','C0C680','C0W130','C0W130','C0W120','C0W120','C0W120','C0W120','C0F970','C0F970','C0F970','C0F9U0','C0F9U0','C0F9L0','C0UA20','CM0030','C0F9K0','C0F930','C0F000','C0F9N0','C0F9X0','C0F9A0','C0F9V0','C0F850','C0F970','C0F9R0','C0F9X0','C0F9P0','C0F9O0','C0F9S0','C0F0B0','CM0010','C0F9U0','C0F9T0','C0F9M0','C0F9A0','C0F9R0','C0A9A0','C0AH70','C0AC70','C0A9F0','C0A9B0','C0AH80','C0A9A0','C0A9A0','C0AC70','C0AC80','C0AC70','C0AH10','C0S700','C0S770','C0S690','C0S710','C0Z020','C0S740','C0S740','C0S740','C0S730','C0S700','C0S730','C0S840','C0S790','C0Z290','C0S890','C0S710','C0T960','C0Z050','C0Z150','C0T9E0','C0Z020','C0Z180','C0Z290','C0Z210','C0T820','C0Z180','C0T9G0','C0T9I0','C0Z160','C0E850','C0E530','C0E780','C0E790','C0E430','C0E610','C0E540','C0E610','C0E820','C0E420','C0E830','C0E750','C0E780','C0E590','C0E550','C0E780','C0E730','C0E550','C0W110','C0W110','C0W170','C0W110','C0W150','C0W160','C0W150','C0W150','C0W140','C0W140','C0K440','C0K500','C0K410','C0K280','C0K490','C0K280','C0K390','C0K450','C0K250','C0K400','C0K520','C0K470','C0K510','C0K530','C0K480','C0K330','C0K430','C0K420','C0K460','C0K250']

def getAllLocations():
    return [(22.6558, 120.47), (22.5294, 120.562), (22.4629, 120.47), (22.0008, 120.745), (22.7008, 120.562), (22.0843, 120.746), (22.3961, 120.585), (22.2606, 120.657), (22.8255, 120.6), (22.4271, 120.539), (22.7336, 120.489), (22.5158, 120.499), (22.7962, 120.516), (22.4347, 120.515), (22.6515, 120.526), (22.3404, 120.372), (22.0438, 120.838), (22.4747, 120.516), (22.6151, 120.566), (22.5915, 120.47), (22.584, 120.608), (22.4818, 120.585), (22.4774, 120.442), (22.7437, 120.562), (22.5939, 120.533), (22.3852, 120.689), (22.4922, 120.625), (22.6904, 120.638), (22.152, 120.781), (22.7854, 120.682), (22.2472, 120.735), (22.578, 120.635), (22.751, 120.781), (22.6224, 120.283), (22.6496, 120.269), (22.6877, 120.292), (22.7175, 120.303), (22.6483, 120.326), (22.6284, 120.306), (22.6254, 120.295), (22.6269, 120.326), (22.5971, 120.315), (22.6142, 120.266), (22.5553, 120.361), (22.6114, 120.349), (22.4987, 120.401), (22.5845, 120.401), (22.7084, 120.424), (22.7377, 120.361), (22.6948, 120.361), (22.6602, 120.372), (22.8016, 120.286), (22.7539, 120.309), (22.7824, 120.378), (22.8633, 120.401), (22.8779, 120.332), (22.8494, 120.263), (22.8954, 120.222), (22.8763, 120.211), (22.8113, 120.24), (22.7832, 120.246), (22.7486, 120.257), (22.8702, 120.47), (22.8854, 120.551), (23.0026, 120.655), (23.1146, 120.631), (23.0008, 120.562), (22.956, 120.47), (22.9319, 120.735), (23.2281, 120.85), (23.2743, 120.735), (22.9813, 120.222), (22.9564, 120.188), (23.0085, 120.208), (23.0585, 120.136), (22.9934, 120.165), (22.9948, 120.196), (23.312, 120.309), (23.2622, 120.24), (23.3336, 120.459), (23.2807, 120.355), (23.3665, 120.355), (23.2825, 120.447), (23.1763, 120.24), (23.2293, 120.269), (23.2427, 120.332), (23.1949, 120.355), (23.1422, 120.401), (23.1694, 120.17), (23.2554, 120.17), (23.1258, 120.199), (23.1195, 120.101), (23.2055, 120.101), (23.2866, 120.124), (23.0281, 120.332), (23.1403, 120.309), (23.0807, 120.286), (23.0953, 120.217), (23.0893, 120.372), (23.1061, 120.47), (23.182, 120.516), (23.1079, 120.562), (23.0301, 120.424), (22.9401, 120.24), (22.9519, 120.286), (22.9637, 120.332), (22.954, 120.378), (23.0212, 120.263), (23.9059, 120.781), (24.0214, 121.125), (23.668, 120.988), (23.918, 120.678), (23.8538, 120.678), (24.0564, 120.873), (23.9933, 120.965), (23.792, 120.861), (23.7122, 120.689), (23.9934, 120.723), (23.828, 120.793), (23.8754, 120.919), (23.7348, 120.781), (23.4853, 120.476), (23.4804, 120.424), (23.3996, 120.551), (23.5298, 120.287), (23.304, 120.597), (23.6041, 120.454), (23.4964, 120.384), (23.3628, 120.17), (23.5381, 120.355), (23.4464, 120.257), (23.4702, 120.17), (23.541, 120.689), (23.5204, 120.44), (23.4287, 120.4), (23.5926, 120.401), (23.4407, 120.608), (23.505, 120.608), (23.353, 120.217), (23.4355, 120.781), (23.4193, 120.309), (25.1144, 121.685), (25.1526, 121.725), (25.149, 121.774), (25.1187, 121.745), (25.1284, 121.782), (25.1474, 121.702), (25.0836, 121.748), (24.6665, 121.652), (24.6888, 121.805), (24.6319, 121.754), (24.4066, 121.674), (24.7381, 121.663), (24.7696, 121.799), (24.5498, 121.514), (24.7591, 121.754), (24.8214, 121.77), (24.6756, 121.771), (24.5942, 121.853), (24.8576, 121.823), (23.9141, 120.401), (23.8115, 120.616), (24.1582, 120.498), (23.8692, 120.534), (24.1123, 120.498), (23.9596, 120.585), (23.943, 120.559), (23.9898, 120.447), (23.8777, 120.47), (23.8484, 120.309), (23.9891, 120.566), (24.0717, 120.562), (23.9202, 120.545), (23.8248, 120.516), (23.9583, 120.493), (23.8525, 120.585), (23.9038, 120.522), (23.8992, 120.583), (24.0377, 120.424), (24.0349, 120.511), (23.8448, 120.424), (24.1317, 120.462), (24.0136, 120.628), (24.0288, 120.562), (23.9456, 120.355), (24.0755, 120.447), (24.9359, 121.374), (25.2593, 121.502), (25.0615, 121.487), (24.9962, 121.485), (25.0848, 121.439), (25.1444, 121.398), (24.9684, 121.438), (24.9351, 121.711), (25.0248, 121.741), (24.9783, 121.539), (25.0266, 121.418), (25.0114, 121.462), (25.079, 121.388), (24.9816, 121.42), (25.0103, 121.515), (25.0616, 121.64), (25.0582, 121.433), (25.172, 121.443), (25.0034, 121.617), (24.8664, 121.55), (25.1031, 121.822), (25.0099, 121.645), (25.2908, 121.567), (25.1676, 121.64), (25.0869, 121.472), (25.0169, 121.946), (25.2224, 121.637), (24.9972, 121.822), (24.9615, 121.343), (24.8239, 120.947), (24.7921, 120.993), (24.7798, 120.93), (24.6298, 121.119), (24.6631, 121.068), (24.7428, 120.999), (24.5761, 121.308), (24.6788, 120.999), (24.8496, 121.091), (24.9133, 120.999), (24.7113, 121.137), (24.8814, 121.045), (24.8347, 120.993), (24.7749, 121.045), (24.7658, 121.108), (24.8045, 121.148), (24.9722, 121.205), (24.9469, 121.291), (25.0493, 121.194), (24.8658, 121.297), (24.9296, 121.205), (24.7091, 121.377), (24.9827, 121.068), (24.9934, 121.297), (24.9242, 121.137), (25.0784, 121.297), (25.0359, 121.114), (24.8445, 121.205), (25.0199, 121.366), (23.2081, 119.429), (23.3833, 119.5), (23.5774, 119.662), (23.664, 119.595), (23.6055, 119.514), (23.5706, 119.577), (24.1403, 120.682), (24.1573, 120.683), (24.1815, 120.686), (24.1208, 120.662), (24.1471, 120.608), (24.3089, 120.722), (24.3207, 121.308), (24.3318, 120.653), (24.3702, 120.591), (24.3788, 120.649), (24.1359, 120.562), (24.1047, 120.681), (24.2225, 120.655), (24.1241, 120.717), (24.1867, 120.815), (24.26, 120.827), (24.1428, 120.694), (24.248, 120.539), (24.2378, 120.585), (24.302, 120.585), (24.2164, 120.706), (24.1078, 120.638), (24.2742, 120.777), (24.2466, 120.683), (24.1431, 120.663), (24.177, 120.642), (24.2521, 120.722), (24.0443, 120.735), (24.2102, 120.516), (25.0792, 121.543), (25.0421, 121.52), (25.0287, 121.577), (25.0689, 121.591), (25.1152, 121.515), (25.0312, 121.611), (25.095, 121.525), (25.0627, 121.511), (25.0262, 121.543), (24.9929, 121.571), (25.0542, 121.564), (25.0263, 121.497), (22.7848, 121.083), (22.4142, 120.907), (22.6102, 121.004), (22.932, 121.034), (23.1262, 121.366), (23.0692, 121.286), (23.1207, 121.216), (23.1306, 121.176), (22.6621, 121.49), (22.7613, 121.144), (22.0269, 121.542), (22.3991, 120.827), (22.5604, 120.873), (23.3452, 121.434), (23.0496, 121.165), (22.9581, 121.16), (23.6351, 121.423), (23.404, 121.217), (23.9732, 121.584), (23.8593, 121.56), (23.1544, 121.286), (24.0327, 121.604), (23.3898, 121.377), (23.5206, 121.411), (24.2259, 121.537), (23.9911, 121.611), (23.7246, 121.308), (23.5852, 121.503), (23.7444, 121.457), (24.6305, 120.93), (24.3893, 120.769), (24.5019, 120.838), (24.3113, 120.825), (24.5803, 121.011), (24.3981, 120.873), (24.6144, 120.791), (24.3832, 121.034), (24.5239, 120.93), (24.7009, 120.879), (24.4098, 120.678), (24.5711, 120.815), (24.5274, 120.761), (24.4893, 120.68), (24.6248, 120.861), (24.4482, 120.792), (24.6884, 120.902), (24.5766, 120.855), (26.2246, 119.998), (26.1534, 119.931), (26.3657, 120.49), (25.9768, 119.931), (24.428, 118.235), (24.9887, 119.453), (24.4321, 118.316), (24.4566, 118.306), (24.4811, 118.428), (24.4377, 118.428), (23.8156, 120.406), (23.6289, 120.332), (23.5959, 120.286), (23.6178, 120.163), (23.645, 120.564), (23.6371, 120.194), (23.6883, 120.355), (23.6519, 120.424), (23.7602, 120.353), (23.7078, 120.541), (23.6933, 120.257), (23.7619, 120.608), (23.5628, 120.24), (23.723, 120.194), (23.7769, 120.539), (23.7162, 120.424), (23.6944, 120.31), (23.7755, 120.447), (23.6771, 120.476), (23.7485, 120.256)]


def getLatestWeatherStation(station):
    try:
        condition = "`station_id` = '%s'" % (station)
        database = "save_weather"
        query = "SELECT `pressure`, `temperature`, `max_temperature`, `min_temperature`, `humidity`, `wind_speed`, `max_gust`, `precipitation` FROM %s WHERE %s ORDER BY `id` DESC LIMIT 1" % (
                database, condition)
        mycursor.execute(query)

        # Humidity, Temperature, Pressure, Wind Speed, Rainfall
        data_labels = ["pressure", "temperature", "max_temperature",
                       "min_temperature", "humidity", "wind_speed", "max_gust", "precipitation"]
        data = [mycursor.fetchone()]

        return generateDictionary(data, data_labels)

    except Exception as e:
        print(e)


def getLatestWeather(city, district, language="en"):
    try:
        station = getStation(city, district, language)["station"]
        condition = "`station_id` = '%s'" % (station)
        database = "save_weather"
        query = "SELECT `pressure`, `temperature`, `max_temperature`, `min_temperature`, `humidity`, `wind_speed`, `max_gust`, `precipitation` FROM %s WHERE %s ORDER BY `id` DESC LIMIT 1" % (
            database, condition)
        mycursor.execute(query)

        # Humidity, Temperature, Pressure, Wind Speed, Rainfall
        data_labels = ["pressure", "temperature", "max_temperature",
                       "min_temperature", "humidity", "wind_speed", "max_gust", "precipitation"]
        data = [mycursor.fetchone()]

        return generateDictionary(data, data_labels)

    except Exception as e:
        print(e)


def getOtherData(city, district, language="en"):
    try:
        district_languages = {"en": "district_en", "zh": "district"}
        city_languages = {"en": "city_en", "zh": "city"}

        district_lang, city_lang = district_languages[language], city_languages[language]
        database = "districts"
        condition = "`%s` LIKE '%s' AND `%s` LIKE '%s'" % (
            city_lang, city, district_lang, district)

        query = "SELECT `total_housing`, `single_level`, `low_rise`, `mid_rise`, `high_rise`, `unoccupied`, `occupied`, `person_one`, `person_two`, `person_three`, `person_four`, `person_five`, `person_six`, `person_avg`, `age_forty`, `age_thirty`, `age_twenty`, `age_ten`, `age_zero`, `cultivated_land`, `forest`, `landfill` FROM %s WHERE %s" % (database, condition)

        mycursor.execute(query)

        # Population, Males, Females, Area, Population Density, Type
        data_labels = ["total_housing", "single_level", "low_rise", "mid_rise", "high_rise", "unoccupied", "occupied", "person_one", "person_two", "person_three", "person_four", "person_five", "person_six", "person_avg", "age_forty", "age_thirty", "age_twenty", "age_ten", "age_zero", "cultivated_land", "forest", "landfill"]
        data = mycursor.fetchall()

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

        query = "SELECT `station` FROM %s WHERE %s" % (database, condition)
        mycursor.execute(query)

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
                       "station_name", "pressure", "max_pressure", "min_pressure", "temperature", "max_temperature", "min_temperature", "humidity", "min_humidity", "wind_speed", "max_gust", "precipitation"]
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
        query = "SELECT `pressure`, `max_pressure`, `min_pressure`, `temperature`, `max_temperature`, `min_temperature`,`humidity`, `min_humidity`, `wind_speed`, `max_gust`, `precipitation` FROM %s WHERE %s" % (database, condition)
        mycursor.execute(query)
        
        data_labels = ["pressure", "max_pressure", "min_pressure", "temperature", "max_temperature",
                       "min_temperature", "humidity", "min_humidity", "wind_speed", "max_gust", "precipitation"]
        data = mycursor.fetchall()
        return generateDictionary(data, data_labels)

    except Exception as e:
        print(e)


def saveData(data):
    database = "save_weather"
    data_list = ["'" + i + "'" for i in data[0:-1].split(",") if i != ""]
    data = ",".join(data_list)

    data_labels = ["year", "month", "day", "station_id", "station_name", "lat", "lon", "city", "town", "wind_speed",
                   "temperature", "humidity", "pressure", "precipitation", "max_gust", "max_temperature", "min_temperature"]

    query = "INSERT INTO %s(%s) VALUES(%s)" % (
        database, ", ".join(data_labels), (data))
    print(data)
    print(len(data_list), len(data_labels))
    print(query)
    mycursor.execute(query)
    mydb.commit()

    print("Completed")
    return


def generateDictionary(data, labels):
    try:
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
            if output_list == []:
                return {}
            return output_list
    
    except Exception as e:
        print(e)