

def buildURL(station_name, month, year):
    month = month.lower()[:3]
    station_name = station_name.lower()

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


if __name__ == "__main__":

    # Change to test
    station_name = "shipai"
    month = "january"
    year = "2017"
    print(buildURL(station_name, month, year))
