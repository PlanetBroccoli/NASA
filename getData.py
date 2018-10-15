

# Requirements: bs4 (Suggest to use pip)
from bs4 import BeautifulSoup
import urllib.request


def buildURL(station_name, month, year):
    month = month.lower()[:3]
    station_name = station_name.lower()

    ''' Districts and corresponding meteorological site(s)
    Beitou: Shipai
    Shilin: {Shezi, Tianmu, Shilin, Pingdeng}
    Datong: Zhongzheng
    Zhongshan: Dazhi
    Songshan: Songshan
    Neihu: Neihu
    Wanhua: Yonghe (New Taipei)
    Zhongzheng: Zhongzheng
    Da'an: Zhongzheng
    Xinyi: Xinyi
    Nangang: Neihu
    Wenshan: Wenshan
    '''

    station = {"taipei": "466920",
               "shezi": "C0A980",
               "dazhi": "C0A9A0",
               "shipai": "C0A9B0",
               "tianmu": "C0A9C0",
               "shilin": "C0A9E0",
               "neihu": "C0A9F0",
               "xinyi": "C0AC70",
               "wenshan": "C0AC80",
               "pingdeng": "C0AH40",
               "songshan": "C0AH70",
               "yonghe": "C0AH10",
               }

    stname = {"taipei": "%25E8%2587%25BA%25E5%258C%2597",
              "shezi": "%25E7%25A4%25BE%25E5%25AD%2590",
              "dazhi": "%25E5%25A4%25A7%25E7%259B%25B4",
              "shipai": "%25E7%259F%25B3%25E7%2589%258C",
              "tianmu": "%25E5%25A4%25A9%25E6%25AF%258D",
              "shilin": "%25E5%25A3%25AB%25E6%259E%2597",
              "neihu": "%25E5%2585%25A7%25E6%25B9%2596",
              "xinyi": "%25E4%25BF%25A1%25E7%25BE%25A9",
              "wenshan": "%25E6%2596%2587%25E5%25B1%25B1",
              "pingdeng": "%25E5%25B9%25B3%25E7%25AD%2589",
              "songshan": "%25E6%259D%25BE%25E5%25B1%25B1",
              "yonghe": "%25E6%25B0%25B8%25E5%2592%258C"
              }

    months = {"jan":   "01",
              "feb":   "02",
              "mar":   "03",
              "apr":   "04",
              "may":   "05",
              "jun":   "06",
              "jul":   "07",
              "aug":   "08",
              "sep":   "09",
              "oct":   "10",
              "nov":   "11",
              "dec":   "12",
              }

    url = "https://e-service.cwb.gov.tw/HistoryDataQuery/MonthDataController.do?command=viewMain&station=%s&stname=%s&datepicker=%s-%s" % (
        station[station_name], stname[station_name], year, months[month])

    return url


def getText(url):
    try:
        site = urllib.request.urlopen(url).read()
        soup = BeautifulSoup(site, "lxml")
        content = soup.findAll("table", {"id": "MyTable"})
        content_list = list(content)
        print(type(content_list))
        output = "".join([str(i) for i in content_list])
        print(type(output))
        return output

    except Exception as e:
        print(e)


def saveData(filename, url):
    try:
        print("Trying to obtain data from: %s" % (url))
        content = getText(url)
        if content == "":
            return

        with open(filename, "w", encoding="utf-8") as outp:
            outp.write(content)

    except Exception as e:
        print(e)


# End year is inclusive
def getData(start_year, end_year, stations):
    months = {"jan", "feb", "mar", "apr", "may", "jun",
              "jul", "aug", "sep", "oct", "nov", "dec"}
    try:
        for year in range(int(start_year), int(end_year+1)):
            for station in stations:
                for month in months:
                    url = buildURL(station_name=station,
                                   month=month, year=str(year))
                    filename = "%s_%s_%s" % (station, month, year)
                    saveData(filename, url)

    except Exception as e:
        print(e)


if __name__ == "__main__":
    # Change to test
    # Data grabber info
    stations = {"taipei", "shezi", "dazhi", "shipai", "tianmu", "shilin",
                "neihu", "xinyi", "wenshan", "pingdeng", "songshan", "yonghe"}
    start_year, end_year = 2010, 2018
    getData(start_year=start_year, end_year=end_year, stations=stations)
