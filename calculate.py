import numpy as np
import statistics
import math
import queries
from geopy.distance import geodesic

def calculateCoords(lat, lon):
        station = getStation(lat, lon)
        city, district = getDistrict(lat, lon)
        weather_data = queries.getLatestWeatherStation(station)
        print(lat, lon, station)
        prob = calculateProbability(weather_data)

        return city, district, prob

def calculateProbability(params, model="simple"):
    try:
        if model == "simple":
            values = [params["pressure"], params["temperature"], params["max_temperature"], params["min_temperature"], params["humidity"], params["wind_speed"], params["max_gust"], params["precipitation"]]
            values = [i if i > -99 else 0 for i in values]
            print (values)
            # This will be our calculation from logistic regression in R
            # Without intercept
            prediction_matrix = [-0.006946, 0.146294, -0.224428,
                                0.180175, 0.060302, 0.417116, 0.01195, -0.01588]

            # With intercept
            # prediction_matrix = [-116.945965, 0.146294, -0.224428, 0.180175, 0.060302, 0.417116, 0.01195, -0.01588, -0.007374]
            # values = [1] + values
        else:
            return 
        y = np.dot(prediction_matrix, values)

        # Probability of being High-Risk
        return math.exp(y) / (1 + math.exp(y))

    except Exception as e:
        print(e)

def getDistrict(lat, lon):
    coords = lat, lon
    locations = [(22.6558,120.47),(22.5294,120.562),(22.4629,120.47),(22.0008,120.745),(22.7008,120.562),(22.0843,120.746),(22.3961,120.585),(22.2606,120.657),(22.8255,120.6),(22.4271,120.539),(22.7336,120.489),(22.5158,120.499),(22.7962,120.516),(22.4347,120.515),(22.6515,120.526),(22.3404,120.372),(22.0438,120.838),(22.4747,120.516),(22.6151,120.566),(22.5915,120.47),(22.584,120.608),(22.4818,120.585),(22.4774,120.442),(22.7437,120.562),(22.5939,120.533),(22.3852,120.689),(22.4922,120.625),(22.6904,120.638),(22.152,120.781),(22.7854,120.682),(22.2472,120.735),(22.578,120.635),(22.751,120.781),(22.6224,120.283),(22.6496,120.269),(22.6877,120.292),(22.7175,120.303),(22.6483,120.326),(22.6284,120.306),(22.6254,120.295),(22.6269,120.326),(22.5971,120.315),(22.6142,120.266),(22.5553,120.361),(22.6114,120.349),(22.4987,120.401),(22.5845,120.401),(22.7084,120.424),(22.7377,120.361),(22.6948,120.361),(22.6602,120.372),(22.8016,120.286),(22.7539,120.309),(22.7824,120.378),(22.8633,120.401),(22.8779,120.332),(22.8494,120.263),(22.8954,120.222),(22.8763,120.211),(22.8113,120.24),(22.7832,120.246),(22.7486,120.257),(22.8702,120.47),(22.8854,120.551),(23.0026,120.655),(23.1146,120.631),(23.0008,120.562),(22.956,120.47),(22.9319,120.735),(23.2281,120.85),(23.2743,120.735),(22.9813,120.222),(22.9564,120.188),(23.0085,120.208),(23.0585,120.136),(22.9934,120.165),(22.9948,120.196),(23.312,120.309),(23.2622,120.24),(23.3336,120.459),(23.2807,120.355),(23.3665,120.355),(23.2825,120.447),(23.1763,120.24),(23.2293,120.269),(23.2427,120.332),(23.1949,120.355),(23.1422,120.401),(23.1694,120.17),(23.2554,120.17),(23.1258,120.199),(23.1195,120.101),(23.2055,120.101),(23.2866,120.124),(23.0281,120.332),(23.1403,120.309),(23.0807,120.286),(23.0953,120.217),(23.0893,120.372),(23.1061,120.47),(23.182,120.516),(23.1079,120.562),(23.0301,120.424),(22.9401,120.24),(22.9519,120.286),(22.9637,120.332),(22.954,120.378),(23.0212,120.263),(23.9059,120.781),(24.0214,121.125),(23.668,120.988),(23.918,120.678),(23.8538,120.678),(24.0564,120.873),(23.9933,120.965),(23.792,120.861),(23.7122,120.689),(23.9934,120.723),(23.828,120.793),(23.8754,120.919),(23.7348,120.781),(23.4853,120.476),(23.4804,120.424),(23.3996,120.551),(23.5298,120.287),(23.304,120.597),(23.6041,120.454),(23.4964,120.384),(23.3628,120.17),(23.5381,120.355),(23.4464,120.257),(23.4702,120.17),(23.541,120.689),(23.5204,120.44),(23.4287,120.4),(23.5926,120.401),(23.4407,120.608),(23.505,120.608),(23.353,120.217),(23.4355,120.781),(23.4193,120.309),(25.1144,121.685),(25.1526,121.725),(25.149,121.774),(25.1187,121.745),(25.1284,121.782),(25.1474,121.702),(25.0836,121.748),(24.6665,121.652),(24.6888,121.805),(24.6319,121.754),(24.4066,121.674),(24.7381,121.663),(24.7696,121.799),(24.5498,121.514),(24.7591,121.754),(24.8214,121.77),(24.6756,121.771),(24.5942,121.853),(24.8576,121.823),(23.9141,120.401),(23.8115,120.616),(24.1582,120.498),(23.8692,120.534),(24.1123,120.498),(23.9596,120.585),(23.943,120.559),(23.9898,120.447),(23.8777,120.47),(23.8484,120.309),(23.9891,120.566),(24.0717,120.562),(23.9202,120.545),(23.8248,120.516),(23.9583,120.493),(23.8525,120.585),(23.9038,120.522),(23.8992,120.583),(24.0377,120.424),(24.0349,120.511),(23.8448,120.424),(24.1317,120.462),(24.0136,120.628),(24.0288,120.562),(23.9456,120.355),(24.0755,120.447),(24.9359,121.374),(25.2593,121.502),(25.0615,121.487),(24.9962,121.485),(25.0848,121.439),(25.1444,121.398),(24.9684,121.438),(24.9351,121.711),(25.0248,121.741),(24.9783,121.539),(25.0266,121.418),(25.0114,121.462),(25.079,121.388),(24.9816,121.42),(25.0103,121.515),(25.0616,121.64),(25.0582,121.433),(25.172,121.443),(25.0034,121.617),(24.8664,121.55),(25.1031,121.822),(25.0099,121.645),(25.2908,121.567),(25.1676,121.64),(25.0869,121.472),(25.0169,121.946),(25.2224,121.637),(24.9972,121.822),(24.9615,121.343),(24.8239,120.947),(24.7921,120.993),(24.7798,120.93),(24.6298,121.119),(24.6631,121.068),(24.7428,120.999),(24.5761,121.308),(24.6788,120.999),(24.8496,121.091),(24.9133,120.999),(24.7113,121.137),(24.8814,121.045),(24.8347,120.993),(24.7749,121.045),(24.7658,121.108),(24.8045,121.148),(24.9722,121.205),(24.9469,121.291),(25.0493,121.194),(24.8658,121.297),(24.9296,121.205),(24.7091,121.377),(24.9827,121.068),(24.9934,121.297),(24.9242,121.137),(25.0784,121.297),(25.0359,121.114),(24.8445,121.205),(25.0199,121.366),(23.2081,119.429),(23.3833,119.5),(23.5774,119.662),(23.664,119.595),(23.6055,119.514),(23.5706,119.577),(24.1403,120.682),(24.1573,120.683),(24.1815,120.686),(24.1208,120.662),(24.1471,120.608),(24.3089,120.722),(24.3207,121.308),(24.3318,120.653),(24.3702,120.591),(24.3788,120.649),(24.1359,120.562),(24.1047,120.681),(24.2225,120.655),(24.1241,120.717),(24.1867,120.815),(24.26,120.827),(24.1428,120.694),(24.248,120.539),(24.2378,120.585),(24.302,120.585),(24.2164,120.706),(24.1078,120.638),(24.2742,120.777),(24.2466,120.683),(24.1431,120.663),(24.177,120.642),(24.2521,120.722),(24.0443,120.735),(24.2102,120.516),(25.0792,121.543),(25.0421,121.52),(25.0287,121.577),(25.0689,121.591),(25.1152,121.515),(25.0312,121.611),(25.095,121.525),(25.0627,121.511),(25.0262,121.543),(24.9929,121.571),(25.0542,121.564),(25.0263,121.497),(22.7848,121.083),(22.4142,120.907),(22.6102,121.004),(22.932,121.034),(23.1262,121.366),(23.0692,121.286),(23.1207,121.216),(23.1306,121.176),(22.6621,121.49),(22.7613,121.144),(22.0269,121.542),(22.3991,120.827),(22.5604,120.873),(23.3452,121.434),(23.0496,121.165),(22.9581,121.16),(23.6351,121.423),(23.404,121.217),(23.9732,121.584),(23.8593,121.56),(23.1544,121.286),(24.0327,121.604),(23.3898,121.377),(23.5206,121.411),(24.2259,121.537),(23.9911,121.611),(23.7246,121.308),(23.5852,121.503),(23.7444,121.457),(24.6305,120.93),(24.3893,120.769),(24.5019,120.838),(24.3113,120.825),(24.5803,121.011),(24.3981,120.873),(24.6144,120.791),(24.3832,121.034),(24.5239,120.93),(24.7009,120.879),(24.4098,120.678),(24.5711,120.815),(24.5274,120.761),(24.4893,120.68),(24.6248,120.861),(24.4482,120.792),(24.6884,120.902),(24.5766,120.855),(26.2246,119.998),(26.1534,119.931),(26.3657,120.49),(25.9768,119.931),(24.428,118.235),(24.9887,119.453),(24.4321,118.316),(24.4566,118.306),(24.4811,118.428),(24.4377,118.428),(23.8156,120.406),(23.6289,120.332),(23.5959,120.286),(23.6178,120.163),(23.645,120.564),(23.6371,120.194),(23.6883,120.355),(23.6519,120.424),(23.7602,120.353),(23.7078,120.541),(23.6933,120.257),(23.7619,120.608),(23.5628,120.24),(23.723,120.194),(23.7769,120.539),(23.7162,120.424),(23.6944,120.31),(23.7755,120.447),(23.6771,120.476),(23.7485,120.256)]
    cities = ['屏東市','潮州鎮','東港鎮','恆春鎮','長治鄉','車城鄉','枋寮鄉','枋山鄉','高樹鄉','佳冬鄉','九如鄉','崁頂鄉','里港鄉','林邊鄉','麟洛鄉','琉球鄉','滿州鄉','南州鄉','內埔鄉','萬丹鄉','萬巒鄉','新埤鄉','新園鄉','鹽埔鄉','竹田鄉','春日鄉','來義鄉','瑪家鄉','牡丹鄉',' 三地門 ','獅子鄉','泰武鄉','霧臺鄉','鹽埕區','鼓山區','左營區','楠梓區','三民區','新興區','前金區','苓雅區','前鎮區','旗津區','小港區','鳳山區','林園區','大寮區','大樹區','大社區','仁武區','鳥松區','岡山區','橋頭區','燕巢區','田寮區','阿蓮區','路竹區','湖內區','茄萣區','永安區','彌陀區','梓官區','旗山區','美濃區','六龜區','甲仙區','杉林區','內門區','茂林區','桃源區','那瑪夏區','東區','南區','北區','安南區','安平區','中西區','新營區','鹽水區','白河區','柳營區','後壁區','東山區','麻豆區','下營區','六甲區','官田區','大內區','佳里區','學甲區','西港區','七股區','將軍區','北門區','新化區','善化區','新市區','安定區','山上區','玉井區','楠西區','南化區','左鎮區','仁德區','歸仁區','關廟區','龍崎區','永康區','中寮鄉','仁愛鄉','信義鄉','南投市','名間鄉','國姓鄉','埔里鎮','水里鄉','竹山鎮','草屯鎮','集集鎮','魚池鄉','鹿谷鄉','東區','西區','中埔鄉','六腳鄉','大埔鄉','大林鎮','太保市','布袋鎮','新港鄉','朴子市','東石鄉','梅山鄉','民雄鄉','水上鄉','溪口鄉','番路鄉','竹崎鄉','義竹鄉','阿里山鄉','鹿草鄉','七堵區','中山區','中正區','仁愛區','信義區','安樂區','暖暖區','三星鄉','五結鄉','冬山鄉','南澳鄉','員山鄉','壯圍鄉','大同鄉','宜蘭市','礁溪鄉','羅東鎮','蘇澳鎮','頭城鎮','二林鎮','二水鄉','伸港鄉','北斗鎮','和美鎮','員林市','埔心鄉','埔鹽鄉','埤頭鄉','大城鄉','大村鄉','彰化市','永靖鄉','溪州鄉','溪湖鎮','田中鎮','田尾鄉','社頭鄉','福興鄉','秀水鄉','竹塘鄉','線西鄉','芬園鄉','花壇鄉','芳苑鄉','鹿港鎮','三峽區','三芝區','三重區','中和區','五股區','八里區','土城區','坪林區','平溪區','新店區','新莊區','板橋區','林口區','樹林區','永和區','汐止區','泰山區','淡水區','深坑區','烏來區','瑞芳區','石碇區','石門區','萬里區','蘆洲區','貢寮區','金山區','雙溪區','鶯歌區','北區','東區','香山區','五峰鄉','北埔鄉','寶山鄉','尖石鄉','峨眉鄉','新埔鎮','新豐鄉','橫山鄉','湖口鄉','竹北市','竹東鎮','芎林鄉','關西鎮','中壢區','八德區','大園區','大溪區','平鎮區','復興區','新屋區','桃園區','楊梅區','蘆竹區','觀音區','龍潭區','龜山區','七美鄉','望安鄉','湖西鄉','白沙鄉','西嶼鄉','馬公市','中區','北區','北屯區','南區','南屯區','后里區','和平區','外埔區','大安區','大甲區','大肚區','大里區','大雅區','太平區','新社區','東勢區','東區','梧棲區','沙鹿區','清水區','潭子區','烏日區','石岡區','神岡區','西區','西屯區','豐原區','霧峰區','龍井區','中山區','中正區','信義區','內湖區','北投區','南港區','士林區','大同區','大安區','文山區','松山區','萬華區','卑南鄉','大武鄉','太麻里鄉','延平鄉','成功鎮','東河鄉','池上鄉','海端鄉','綠島鄉','臺東市','蘭嶼鄉','達仁鄉','金峰鄉','長濱鄉','關山鎮','鹿野鄉','光復鄉','卓溪鄉','吉安鄉','壽豐鄉','富里鄉','新城鄉','玉里鎮','瑞穗鄉','秀林鄉','花蓮市','萬榮鄉','豐濱鄉','鳳林鎮','三灣鄉','三義鄉','公館鄉','卓蘭鎮','南庄鄉','大湖鄉','後龍鎮','泰安鄉','獅潭鄉','竹南鎮','苑裡鎮','苗栗市','西湖鄉','通霄鎮','造橋鄉','銅鑼鄉','頭份市','頭屋鄉','北竿鄉','南竿鄉','東引鄉','莒光鄉','烈嶼鄉','烏坵鄉','金城鎮','金寧鄉','金沙鎮','金湖鎮','二崙鄉','元長鄉','北港鎮','口湖鄉','古坑鄉','四湖鄉','土庫鎮','大埤鄉','崙背鄉','斗六市','東勢鄉','林內鄉','水林鄉','臺西鄉','莿桐鄉','虎尾鎮','褒忠鄉','西螺鎮','鬥南鎮','麥寮鄉']
    districts = ['屏東縣','屏東縣','屏東縣','屏東縣','屏東縣','屏東縣','屏東縣','屏東縣','屏東縣','屏東縣','屏東縣','屏東縣','屏東縣','屏東縣','屏東縣','屏東縣','屏東縣','屏東縣','屏東縣','屏東縣','屏東縣','屏東縣','屏東縣','屏東縣','屏東縣','屏東縣','屏東縣','屏東縣','屏東縣',' 屏東 ','屏東縣','屏東縣','屏東縣','高雄市','高雄市','高雄市','高雄市','高雄市','高雄市','高雄市','高雄市','高雄市','高雄市','高雄市','高雄市','高雄市','高雄市','高雄市','高雄市','高雄市','高雄市','高雄市','高雄市','高雄市','高雄市','高雄市','高雄市','高雄市','高雄市','高雄市','高雄市','高雄市','高雄市','高雄市','高雄市','高雄市','高雄市','高雄市','高雄市','高雄市','高雄市','臺南市','臺南市','臺南市','臺南市','臺南市','臺南市','臺南市','臺南市','臺南市','臺南市','臺南市','臺南市','臺南市','臺南市','臺南市','臺南市','臺南市','臺南市','臺南市','臺南市','臺南市','臺南市','臺南市','臺南市','臺南市','臺南市','臺南市','臺南市','臺南市','臺南市','臺南市','臺南市','臺南市','臺南市','臺南市','臺南市','臺南市','南投縣','南投縣','南投縣','南投縣','南投縣','南投縣','南投縣','南投縣','南投縣','南投縣','南投縣','南投縣','南投縣','嘉義市','嘉義市','嘉義縣','嘉義縣','嘉義縣','嘉義縣','嘉義縣','嘉義縣','嘉義縣','嘉義縣','嘉義縣','嘉義縣','嘉義縣','嘉義縣','嘉義縣','嘉義縣','嘉義縣','嘉義縣','嘉義縣','嘉義縣','基隆市','基隆市','基隆市','基隆市','基隆市','基隆市','基隆市','宜蘭縣','宜蘭縣','宜蘭縣','宜蘭縣','宜蘭縣','宜蘭縣','宜蘭縣','宜蘭縣','宜蘭縣','宜蘭縣','宜蘭縣','宜蘭縣','彰化縣','彰化縣','彰化縣','彰化縣','彰化縣','彰化縣','彰化縣','彰化縣','彰化縣','彰化縣','彰化縣','彰化縣','彰化縣','彰化縣','彰化縣','彰化縣','彰化縣','彰化縣','彰化縣','彰化縣','彰化縣','彰化縣','彰化縣','彰化縣','彰化縣','彰化縣','新北市','新北市','新北市','新北市','新北市','新北市','新北市','新北市','新北市','新北市','新北市','新北市','新北市','新北市','新北市','新北市','新北市','新北市','新北市','新北市','新北市','新北市','新北市','新北市','新北市','新北市','新北市','新北市','新北市','新竹市','新竹市','新竹市','新竹縣','新竹縣','新竹縣','新竹縣','新竹縣','新竹縣','新竹縣','新竹縣','新竹縣','新竹縣','新竹縣','新竹縣','新竹縣','桃園市','桃園市','桃園市','桃園市','桃園市','桃園市','桃園市','桃園市','桃園市','桃園市','桃園市','桃園市','桃園市','澎湖縣','澎湖縣','澎湖縣','澎湖縣','澎湖縣','澎湖縣','臺中市','臺中市','臺中市','臺中市','臺中市','臺中市','臺中市','臺中市','臺中市','臺中市','臺中市','臺中市','臺中市','臺中市','臺中市','臺中市','臺中市','臺中市','臺中市','臺中市','臺中市','臺中市','臺中市','臺中市','臺中市','臺中市','臺中市','臺中市','臺中市','臺北市','臺北市','臺北市','臺北市','臺北市','臺北市','臺北市','臺北市','臺北市','臺北市','臺北市','臺北市','臺東縣','臺東縣','臺東縣','臺東縣','臺東縣','臺東縣','臺東縣','臺東縣','臺東縣','臺東縣','臺東縣','臺東縣','臺東縣','臺東縣','臺東縣','臺東縣','花蓮縣','花蓮縣','花蓮縣','花蓮縣','花蓮縣','花蓮縣','花蓮縣','花蓮縣','花蓮縣','花蓮縣','花蓮縣','花蓮縣','花蓮縣','苗栗縣','苗栗縣','苗栗縣','苗栗縣','苗栗縣','苗栗縣','苗栗縣','苗栗縣','苗栗縣','苗栗縣','苗栗縣','苗栗縣','苗栗縣','苗栗縣','苗栗縣','苗栗縣','苗栗縣','苗栗縣','連江縣','連江縣','連江縣','連江縣','金門縣','金門縣','金門縣','金門縣','金門縣','金門縣','雲林縣','雲林縣','雲林縣','雲林縣','雲林縣','雲林縣','雲林縣','雲林縣','雲林縣','雲林縣','雲林縣','雲林縣','雲林縣','雲林縣','雲林縣','雲林縣','雲林縣','雲林縣','雲林縣','雲林縣']

    min_distance = float('inf')
    index = 0

    for i in range(len(locations)):
        location_coords = locations[i]
        distance = geodesic(coords, location_coords).km
        if distance < min_distance:
            min_distance = distance
            index = i
        
    # print ("Minimum distance: ", distance, "City:", cities[index], "District:", districts[index])
    return cities[index], districts[index]

def getStation(lat, lon):
    coords = lat, lon
    locations = [(22.6251,120.268),(24.2586,120.707),(24.3246,120.675),(24.3013,120.725),(25.9669,119.972),(23.5643,119.46),(23.4018,119.315),(24.4899,118.401),(24.4593,118.321),(24.9961,119.441),(26.3605,120.475),(25.0505,121.542),(24.609,120.818),(23.877,120.566),(23.7392,120.41),(25.0656,121.333),(24.6772,121.579),(24.6887,121.79),(24.5072,121.518),(24.4392,121.373),(24.7547,121.633),(24.855,121.823),(24.7928,121.667),(24.6699,121.645),(24.7199,121.679),(24.6355,121.785),(24.8193,121.757),(24.8434,121.945),(25.0094,121.994),(24.6836,121.741),(24.8993,121.784),(24.8024,121.806),(24.8666,121.766),(24.1814,121.488),(23.8971,121.542),(23.9374,121.501),(23.9936,121.529),(23.7371,121.412),(23.6625,121.417),(23.8137,121.433),(23.8117,121.532),(23.8824,121.574),(23.6847,121.519),(23.7989,121.534),(23.5857,121.507),(23.2106,121.254),(23.3233,121.332),(23.4697,121.366),(23.3475,121.205),(23.5898,121.37),(23.9327,121.587),(23.7479,121.445),(23.346,121.295),(24.0413,121.596),(24.1492,121.622),(23.711,121.412),(23.5257,121.382),(23.4946,121.299),(23.7402,121.532),(23.4761,121.403),(23.3707,121.375),(23.2703,121.297),(24.2201,121.681),(23.273,121.18),(23.2925,121.34),(23.4569,121.487),(23.2886,121.404),(22.9736,121.298),(22.669,121.467),(23.25,120.978),(23.0714,121.12),(23.1214,121.202),(22.9195,121.115),(23.0413,121.167),(22.48,120.935),(22.2919,120.882),(22.54,120.959),(22.6108,120.977),(22.6867,120.998),(24.9794,121.248),(22.3712,120.582),(22.1917,120.685),(22.1696,120.833),(22.0779,120.829),(21.9942,120.837),(21.9478,120.794),(21.9236,120.728),(21.9027,120.847),(24.5238,121.825),(24.4512,121.802),(24.2686,121.733),(24.5126,121.6),(24.3457,121.648),(24.309,121.762),(24.4157,121.775),(24.9644,121.881),(24.5572,121.794),(24.5624,121.744),(24.7625,121.573),(24.5921,121.404),(24.5296,121.511),(24.5784,121.487),(24.7461,121.714),(25.0861,121.257),(24.7129,121.109),(24.8724,120.969),(25.0289,121.145),(24.5287,121.108),(24.7693,121.05),(24.8994,121.206),(24.8847,121.257),(24.69,120.904),(24.7486,120.897),(24.7367,121.017),(24.541,120.912),(24.9141,121.135),(24.9066,121.035),(24.8718,121.213),(24.8004,120.979),(24.6198,120.941),(24.4345,121.296),(24.3906,121.263),(25.0302,121.378),(24.3655,121.436),(24.5667,120.816),(24.4915,120.783),(24.5644,120.74),(24.3474,120.58),(24.3121,120.721),(24.2563,120.712),(24.2148,120.696),(24.314,120.554),(24.3496,120.697),(24.1863,120.521),(24.1505,120.476),(24.4415,120.645),(24.2778,120.769),(24.2503,120.895),(23.8975,120.933),(24.0396,120.847),(24.0239,121.124),(23.8143,120.842),(23.83,120.793),(23.8388,120.693),(23.93,121.083),(24.0871,121.165),(23.4723,120.948),(24.1336,121.288),(24.111,121.318),(24.1056,120.743),(24.0944,120.692),(24.1088,120.616),(24.182,120.633),(24.1389,120.63),(24.043,120.43),(24.0359,120.496),(24.0178,120.544),(24.0022,120.424),(23.9487,120.518),(23.9034,120.501),(23.8678,120.445),(23.8792,120.507),(23.8587,120.58),(23.8994,120.578),(23.8128,120.609),(23.924,120.312),(24.6801,121.2),(24.94,121.702),(24.8944,121.738),(24.9731,121.815),(24.9945,121.482),(24.6924,121.009),(24.7108,120.881),(24.6032,120.992),(25.1339,121.6),(25.0687,121.651),(24.9408,121.362),(25.0396,121.556),(25.0041,121.568),(25.0532,121.439),(24.9767,121.394),(25.2656,121.557),(24.9242,121.538),(24.8501,121.59),(25.1149,121.793),(25.0192,121.934),(25.0379,121.856),(24.3704,121.365),(25.1308,121.915),(25.1677,121.625),(25.2349,121.587),(25.2253,121.636),(24.9958,121.655),(25.0044,121.735),(24.822,121.344),(25.0494,121.218),(24.9943,121.315),(24.9305,121.275),(24.8001,121.166),(25.0797,121.535),(25.0812,121.567),(25.1176,121.506),(25.1193,121.529),(25.092,121.495),(25.1114,121.461),(25.1773,121.514),(25.2596,121.493),(25.1523,121.395),(25.0885,121.464),(24.9749,121.437),(24.953,121.337),(25.013,121.5),(25.073,121.773),(25.1309,121.569),(25.074,121.373),(25.0045,121.62),(25.0966,121.709),(25.0762,121.419),(24.1448,121.264),(23.8863,120.759),(24.1749,120.714),(23.9517,120.471),(24.1547,120.564),(23.7297,120.779),(23.9483,120.578),(23.9754,120.672),(24.0172,120.613),(24.8517,121.143),(24.2482,120.825),(24.245,121.238),(23.7647,120.678),(23.5973,120.685),(24.4531,120.922),(24.6081,120.776),(24.5853,120.877),(24.3499,120.632),(24.4736,120.696),(24.4128,120.758),(24.2742,120.65),(24.3148,120.816),(24.2016,120.808),(23.9739,120.944),(23.6914,120.843),(24.1231,121.265),(24.035,121.173),(24.1879,121.308),(23.5345,120.836),(24.2171,120.616),(23.9115,120.687),(23.7575,120.311),(23.4958,120.691),(23.7209,120.434),(23.6311,120.217),(23.538,120.161),(23.2287,120.248),(23.3716,120.24),(23.2983,120.377),(23.175,120.137),(23.9051,120.368),(23.3492,120.406),(23.4664,120.546),(23.3124,120.309),(23.2167,120.128),(23.6927,120.296),(23.6059,120.395),(23.7745,120.401),(23.5279,120.547),(23.4271,120.515),(23.2743,120.24),(23.2321,120.174),(23.3681,120.354),(23.8022,120.459),(23.6808,120.387),(23.6024,120.45),(23.4607,120.146),(23.4215,120.381),(23.4594,120.452),(23.259,120.365),(23.3329,120.5),(23.0231,120.34),(22.9935,120.285),(22.9613,120.361),(23.0783,120.137),(23.0636,120.29),(23.0816,120.487),(23.3264,120.574),(23.1144,120.289),(23.2215,120.489),(23.1278,120.452),(22.9728,120.532),(23.2242,120.798),(23.0817,120.582),(23.2238,120.393),(23.1206,120.353),(22.8849,120.32),(23.0122,120.186),(22.963,120.18),(22.995,120.144),(23.1851,120.241),(23.1044,120.22),(23.0774,120.355),(22.9649,120.32),(23.195,120.308),(22.9701,120.25),(23.0585,120.4),(23.2436,120.634),(22.4327,120.502),(22.59,120.657),(22.9077,120.68),(22.9998,120.626),(22.781,120.487),(22.6767,120.277),(22.4642,120.433),(22.5866,120.535),(22.7444,120.736),(22.6847,120.679),(22.7403,120.439),(22.9006,120.511),(22.8349,120.676),(22.8059,120.347),(22.9769,120.458),(22.3722,120.62),(22.5291,120.617),(22.895,120.394),(22.334,120.354),(22.6486,120.348),(22.6619,120.484),(22.7413,120.523),(22.5469,120.384),(22.5941,120.606),(22.7117,120.632),(22.5361,120.532),(22.6291,120.291),(22.5904,120.278),(22.8889,120.236),(22.8249,120.229),(22.7319,120.339),(22.7624,120.259),(22.8566,120.251),(22.9084,120.175),(22.7988,120.287),(22.7856,120.238),(22.7596,120.298),(22.7215,120.278),(22.7029,120.34),(22.6469,120.303),(22.6251,120.268),(22.6245,120.323),(22.8904,120.476),(22.6948,120.535),(22.6526,120.519),(22.5896,120.482),(22.4698,120.575),(22.4877,120.495),(22.4212,120.544),(22.8282,120.593),(22.7423,120.482),(22.6074,120.388),(22.5452,120.453),(22.5166,120.499),(22.5096,120.387),(23.8533,120.491),(23.6805,120.47),(23.7223,120.533),(23.4364,120.231),(23.5758,120.284),(23.4568,120.323),(23.7504,120.602),(23.8542,120.313),(23.656,120.552),(23.6767,120.245),(23.5535,120.42),(23.6478,120.423),(23.7629,120.494),(23.8484,120.374),(23.7033,120.189),(23.5747,120.238),(23.6515,120.307),(23.3826,120.16),(23.4131,120.3),(23.4946,120.283),(23.555,120.338),(23.5871,120.547),(23.3856,120.66),(23.3909,120.709),(23.4558,120.741),(23.3878,120.469),(23.3008,120.657),(23.6882,120.595),(23.5161,120.222),(23.2695,120.117),(23.149,120.078)]
    stations = ['C0V690','CM0010','CM0030','CM0040','C0W110','C0W120','C0W130','C0W140','C0W150','C0W160','C0W170','C0AH70','C0E870','C0G760','C0K580','C0C690','C0U650','C0U780','C0U710','C0U720','C0U520','C0U860','C0U870','C0U890','C0U900','C0U910','C0U600','C0U750','C0A970','C0U940','C0U950','C0U970','C0U980','C0T820','C0Z100','C0T870','C0T9B0','C0T9G0','C0T960','C0T900','C0T9A0','C0T9E0','C0T9H0','C0T9F0','C0T9I0','C0Z020','C0Z061','C0Z070','C0Z050','C0Z080','C0Z150','C0Z160','C0Z170','C0Z180','C0Z190','C0Z200','C0Z210','C0Z250','C0Z270','C0Z280','C0Z290','C0Z300','C0Z310','C0Z320','C0Z330','C0T9M0','C0S830','C0S810','C0S730','C0S750','C0S760','C0S740','C0S710','C0S890','C0S770','C0S840','C0S790','C0S690','C0S700','C0C700','C0R380','C0R400','C0R420','C0R280','C0R370','C0R360','C0R350','C0R620','C0U760','C0U770','C0T9D0','C0U960','C0Z220','C0Z230','C0UA60','C0UA70','C0UA50','C0UA40','C0AH90','C0UA10','C0UA30','C0UA00','C0U990','C0C620','C0D540','C0D590','C0C590','C0D550','C0D560','C0C650','C0C630','C0E730','C0D570','C0D580','C0E820','C0C660','C0D650','C0C670','C0D660','C0E850','C0F9Y0','C0F9Z0','C0C680','C0F0E0','C0E750','C0E780','C0E810','C0F9K0','C0F9L0','C0F9M0','C0F9O0','C0F9P0','C0F9Q0','C0F9R0','C0G890','C0E830','C0F0B0','C0F0C0','C0I370','C0I420','C0I390','C0I360','C0I380','C0I410','C0I490','C0I480','C0I520','C0I530','C0I540','C0F9A0','C0F9N0','C0F9S0','C0F9T0','C0F9U0','C0G770','C0G780','C0G790','C0G800','C0G810','C0G820','C0G830','C0G840','C0G850','C0G860','C0G880','C0G870','C0D360','C0A530','C0A540','C0A550','C0AG90','C0D430','C0E420','C0E430','C0A870','C0AH00','C0AC60','C0AC70','C0AC80','C0ACA0','C0A520','C0A920','C0A580','C0A570','C0A660','C0A880','C0A890','C0UA20','C0A950','C0A860','C0A930','C0A940','C0A640','C0A650','C0C460','C0C540','C0C480','C0C490','C0D390','C0A9A0','C0A9F0','C0A9B0','C0A9C0','C0A9E0','C0A980','C0AC40','C0AD00','C0AD10','C0AD30','C0AD40','C0AD50','C0AH10','C0AH30','C0AH40','C0AH50','C0AH80','C0B010','C0AI00','C0H9C0','C0H950','C0F970','C0G660','C0F000','C0I090','C0G650','C0H960','C0G620','C0D480','C0F850','C0F860','C0I110','C0K240','C0E610','C0E540','C0E550','C0F930','C0E590','C0E530','C0F9I0','C0E790','C0F9V0','C0H890','C0I080','C0H990','C0I010','C0T790','C0H9A0','C0F9X0','C0I460','C0K250','C0M530','C0K330','C0K280','C0K291','C0X060','C0M520','C0X050','C0X080','C0G730','C0X210','C0M720','C0X250','C0X280','C0K430','C0M660','C0K440','C0M700','C0M640','C0X230','C0X220','C0X260','C0K420','C0K390','C0M670','C0M710','C0M690','C0M730','C0X270','C0X240','C0O970','C0O990','C0O960','C0O950','C0O980','C0O830','C0M410','C0O900','C0O810','C0O930','C0V260','C0V210','C0V250','C0O840','C0O860','C0V530','C0X100','C0X110','C0X190','C0X120','C0X150','C0X180','C0X170','C0X130','C0X160','C0X200','C0M850','C0R530','C0R600','C0V790','C0V800','C0R590','C0V810','C0R640','C0R650','C0R130','C0R140','C0V350','C0V310','C0R100','C0V400','C0V360','C0R260','C0R240','C0V370','C0R270','C0V440','C0R170','C0R160','C0V450','C0R190','C0R150','C0R220','C0V490','C0V500','C0V640','C0V620','C0V770','C0V610','C0V750','C0V630','C0V660','C0V650','C0V760','C0V670','C0V680','C0V700','C0V690','C0V710','C0V740','C0R480','C0R570','C0R510','C0R550','C0R580','C0R540','C0R470','C0R490','C0V730','C0R560','C0R520','C0V720','C0G720','C0K460','C0K400','C0M650','C0K410','C0M680','C0K470','C0G740','C0K490','C0K520','C0M760','C0K450','C0K480','C0G750','C0K530','C0K510','C0K500','C0M750','C0M780','C0M740','C0M790','C0M770','C0M830','C0M810','C0M820','C0X300','C0M800','C0K560','C0K550','C0X290','C0X310']

    min_distance = float('inf')
    index = 0

    for i in range(len(locations)):
        station_coords = locations[i]
        distance = geodesic(coords, station_coords).km
        if distance < min_distance:
            min_distance = distance
            index = i
        
    # print ("Minimum distance: ", distance, "Station:", stations[index])
    return stations[index]

def calculateWeeklyData(ld):
    try:
        p = statistics.mean([d["pressure"] for d in ld if d["pressure"] > 0])
        max_p = max([d["max_pressure"] for d in ld])
        min_p = min([d["min_pressure"] for d in ld if d["min_pressure"] > 0])
        t = statistics.mean([d["temperature"]
                             for d in ld if d["temperature"] > 0])
        max_t = max([d["max_temperature"] for d in ld])
        min_t = min([d["min_temperature"]
                     for d in ld if d["min_temperature"] > 0])
        h = statistics.mean([d["humidity"] for d in ld if d["humidity"] > 0])
        min_h = min([d["min_humidity"]
                     for d in ld if d["min_humidity"] > 0])
        w = statistics.mean([d["wind_speed"] for d in ld])
        g = max([d["max_gust"] for d in ld])
        r = statistics.mean([d["precipitation"] for d in ld])
        #s = statistics.mean([d["sunshine"] for d in ld])
        #max_uv = max([d["max_uv"] for d in ld])
        #c = statistics.mean([d["cloud"] for d in ld])
        return p, max_p, min_p, t, max_t, min_t, h, min_h, w, g, r

    except Exception as e:
        print(e)
