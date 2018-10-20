

# Requirements: bs4 (Suggest to use pip)
from bs4 import BeautifulSoup
import urllib.request


def buildURL(station, stname, month, year):
    month = month.lower()[:3]

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
        station, stname, year, months[month])

    return url


def getText(url):
    try:
        site = urllib.request.urlopen(url).read()
        soup = BeautifulSoup(site, "lxml")
        content = soup.findAll("table", {"id": "MyTable"})
        content_list = list(content)
        output = "".join([str(i) for i in content_list])
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

    else:
        print("Success!")


# End year is inclusive
def getData(start_year, end_year, stations):
    months = ["jan", "feb", "mar", "apr", "may", "jun",
              "jul", "aug", "sep", "oct", "nov", "dec"]

    data_directory = "data_south/"

    try:
        for year in range(int(start_year), int(end_year+1)):
            for station in stations:
                month_count = 1
                for month in months:
                    url = buildURL(station=station, stname=stations[station],
                                   month=month, year=str(year))
                    filename = data_directory + \
                        "%s_%s_%s" % (station, year, month_count)
                    saveData(filename, url)
                    month_count += 1

    except Exception as e:
        print(e)


def mergeFiles(filenames, output):
    _ = []
    print("Reading files...")
    for file in filenames:
        with open(file, "r", encoding="utf-8") as inp:
            _.append(inp.read())

    print("Writing file...")
    with open(output, "a", encoding="utf-8") as outp:
        for text in _:
            outp.write(text)

    print("Completed.")


if __name__ == "__main__":
    # Change to test

    # Save data to this directory
    data_directory = "data_south/"

    # Enter station variables here
    stations = {
        'C0R170':  '%25E5%25B1%258F%25E6%259D%25B1',
        'C0R220':  '%25E6%25BD%25AE%25E5%25B7%259E',
        'C0R640':  '%25E6%259D%25B1%25E6%25B8%25AF',
        '467590':  '%25E6%2581%2586%25E6%2598%25A5',
        'C0R480':  '%25E9%2595%25B7%25E6%25B2%25BB',
        'C0R420':  '%25E7%2589%25A1%25E4%25B8%25B9%25E6%25B1%25A0%25E5%25B1%25B1',
        'C0R380':  '%25E6%259E%258B%25E5%25AF%25AE',
        'C0R400':  '%25E6%25A5%2593%25E6%25B8%25AF',
        'C0R470':  '%25E9%25AB%2598%25E6%25A8%25B9',
        'C0R540':  '%25E4%25BD%25B3%25E5%2586%25AC',
        'C0R490':  '%25E4%25B9%259D%25E5%25A6%2582',
        'C0R520':  '%25E5%25B4%2581%25E9%25A0%2582',
        'C0R590':  '%25E9%2587%258C%25E6%25B8%25AF',
        'C0R530':  '%25E6%259E%2597%25E9%2582%258A',
        'C0R570':  '%25E9%25BA%259F%25E6%25B4%259B',
        'C0R270':  '%25E7%2590%2589%25E7%2590%2583%25E5%25B6%25BC',
        'C0R370':  '%25E4%25BD%25B3%25E6%25A8%2582%25E6%25B0%25B4',
        'C0R580':  '%25E5%258D%2597%25E5%25B7%259E',
        'C0R150':  '%25E4%25B8%2589%25E5%259C%25B0%25E9%2596%2580',
        'C0R510':  '%25E8%2590%25AC%25E4%25B8%25B9',
        'C0R240':  '%25E4%25BE%2586%25E7%25BE%25A9',
        'C0R550':  '%25E6%2596%25B0%25E5%259F%25A4',
        'C0R560':  '%25E6%2596%25B0%25E5%259C%2592',
        'C0R160':  '%25E9%25B9%25BD%25E5%259F%2594%25E6%2596%25B0%25E5%259C%258D',
        'C0R650':  '%25E7%25AB%25B9%25E7%2594%25B0',
        'C0R260':  '%25E6%2598%25A5%25E6%2597%25A5',
        'C0R600':  '%25E8%2588%258A%25E6%25B3%25B0%25E6%25AD%25A6',
        'C0R140':  '%25E7%2591%25AA%25E5%25AE%25B6',
        'C0R130':  '%25E9%2598%25BF%25E7%25A6%25AE',
        '467440':  '%25E9%25AB%2598%25E9%259B%2584',
        'C0V690':  '%25E9%25BC%2593%25E5%25B1%25B1',
        'C0V810':  '%25E5%25B7%25A6%25E7%2587%259F',
        'C0V670':  '%25E6%25A5%25A0%25E6%25A2%2593',
        'C0V700':  '%25E4%25B8%2589%25E6%25B0%2591',
        'C0V490':  '%25E6%2596%25B0%25E8%2588%2588',
        'C0V710':  '%25E8%258B%2593%25E9%259B%2585',
        'C0V500':  '%25E6%2597%2597%25E6%25B4%25A5',
        'C0V450':  '%25E9%25B3%25B3%25E6%25A3%25AE',
        'C0V440':  '%25E9%25B3%25B3%25E5%25B1%25B1',
        'C0V720':  '%25E6%259E%2597%25E5%259C%2592',
        'C0V730':  '%25E5%25A4%25A7%25E5%25AF%25AE',
        'C0V350':  '%25E6%25BA%25AA%25E5%259F%2594',
        'C0V770':  '%25E5%25A4%25A7%25E7%25A4%25BE',
        'C0V680':  '%25E4%25BB%2581%25E6%25AD%25A6',
        'C0V660':  '%25E5%25B2%25A1%25E5%25B1%25B1',
        'C0V760':  '%25E6%25A9%258B%25E9%25A0%25AD',
        'C0V400':  '%25E9%2598%25BF%25E5%2585%25AC%25E5%25BA%2597',
        'C0V370':  '%25E5%258F%25A4%25E4%25BA%25AD%25E5%259D%2591',
        'C0V530':  '%25E9%2598%25BF%25E8%2593%25AE',
        'C0V750':  '%25E8%25B7%25AF%25E7%25AB%25B9',
        'C0V640':  '%25E6%25B9%2596%25E5%2585%25A7',
        'C0V630':  '%25E8%258C%2584%25E8%2590%25A3',
        'C0V620':  '%25E6%25B0%25B8%25E5%25AE%2589',
        'C0V650':  '%25E5%25BD%258C%25E9%2599%2580',
        'C0V610':  '%25E6%25A2%2593%25E5%25AE%2598',
        'C0V740':  '%25E6%2597%2597%25E5%25B1%25B1',
        'C0V310':  '%25E7%25BE%258E%25E6%25BF%2583',
        'C0V800':  '%25E5%2585%25AD%25E9%25BE%259C',
        'C0V250':  '%25E7%2594%25B2%25E4%25BB%2599',
        'C0V260':  '%25E6%259C%2588%25E7%259C%2589',
        'C0V360':  '%25E5%2585%25A7%25E9%2596%2580',
        'C0V790':  '%25E8%2590%25AC%25E5%25B1%25B1',
        'C0V210':  '%25E5%25BE%25A9%25E8%2588%2588',
        'C0X050':  '%25E6%259D%25B1%25E6%25B2%25B3',
        'C0X110':  '%25E8%2587%25BA%25E5%258D%2597%25E5%25B8%2582%25E5%258D%2597%25E5%258D%2580',
        'C0X100':  '%25E8%2587%25BA%25E5%258D%2597%25E5%25B8%2582%25E5%258C%2597%25E5%258D%2580',
        'C0O950':  '%25E5%25AE%2589%25E5%258D%2597',
        'C0X190':  '%25E5%25AE%2589%25E5%25B9%25B3',
        '467410':  '%25E8%2587%25BA%25E5%258D%2597',
        'C0X250':  '%25E6%2596%25B0%25E7%2587%259F',
        'C0X230':  '%25E9%25B9%25BD%25E6%25B0%25B4',
        'C0X240':  '%25E9%2597%259C%25E5%25AD%2590%25E5%25B6%25BA',
        'C0X270':  '%25E6%259F%25B3%25E7%2587%259F',
        'C0X260':  '%25E5%25BE%258C%25E5%25A3%2581',
        'C0X120':  '%25E9%25BA%25BB%25E8%25B1%2586',
        'C0X060':  '%25E4%25B8%258B%25E7%2587%259F',
        'C0O840':  '%25E7%258E%258B%25E7%2588%25BA%25E5%25AE%25AE',
        'C0X130':  '%25E5%25AE%2598%25E7%2594%25B0',
        'C0O860':  '%25E5%25A4%25A7%25E5%2585%25A7',
        'C0X080':  '%25E4%25BD%25B3%25E9%2587%258C',
        'C0X220':  '%25E5%25AD%25B8%25E7%2594%25B2',
        'C0X140':  '%25E8%25A5%25BF%25E6%25B8%25AF',
        'C0X310':  '%25E4%25B8%2583%25E8%2582%25A1',
        'C0X280':  '%25E5%25B0%2587%25E8%25BB%258D',
        'C0X290':  '%25E5%258C%2597%25E9%2596%2580',
        'C0O970':  '%25E8%2599%258E%25E9%25A0%25AD%25E5%259F%25A4',
        'C0O900':  '%25E5%2596%2584%25E5%258C%2596',
        'C0O980':  '%25E6%2596%25B0%25E5%25B8%2582',
        'C0X150':  '%25E5%25AE%2589%25E5%25AE%259A',
        'C0X180':  '%25E5%25B1%25B1%25E4%25B8%258A',
        'C0O930':  '%25E7%258E%2589%25E4%25BA%2595',
        'C0O810':  '%25E6%259B%25BE%25E6%2596%2587',
        'C0O830':  '%25E5%258C%2597%25E5%25AF%25AE',
        'C0X200':  '%25E5%25B7%25A6%25E9%258E%25AE',
        'C0X160':  '%25E4%25BB%2581%25E5%25BE%25B7',
        'C0O990':  '%25E5%25AA%25BD%25E5%25BB%259F',
        'C0X170':  '%25E9%2597%259C%25E5%25BB%259F',
        'C0O960':  '%25E5%25B4%258E%25E9%25A0%2582',
        '467420':  '%25E6%25B0%25B8%25E5%25BA%25B7',
        'C0R100':  '%25E5%25B0%25BE%25E5%25AF%25AE%25E5%25B1%25B1',
    }
    start_year, end_year = 2010, 2018
    filename_suffix = ['_2010_1',
                       '_2010_2',
                       '_2010_3',
                       '_2010_4',
                       '_2010_5',
                       '_2010_6',
                       '_2010_7',
                       '_2010_8',
                       '_2010_9',
                       '_2010_10',
                       '_2010_11',
                       '_2010_12',
                       '_2011_1',
                       '_2011_2',
                       '_2011_3',
                       '_2011_4',
                       '_2011_5',
                       '_2011_6',
                       '_2011_7',
                       '_2011_8',
                       '_2011_9',
                       '_2011_10',
                       '_2011_11',
                       '_2011_12',
                       '_2012_1',
                       '_2012_2',
                       '_2012_3',
                       '_2012_4',
                       '_2012_5',
                       '_2012_6',
                       '_2012_7',
                       '_2012_8',
                       '_2012_9',
                       '_2012_10',
                       '_2012_11',
                       '_2012_12',
                       '_2013_1',
                       '_2013_2',
                       '_2013_3',
                       '_2013_4',
                       '_2013_5',
                       '_2013_6',
                       '_2013_7',
                       '_2013_8',
                       '_2013_9',
                       '_2013_10',
                       '_2013_11',
                       '_2013_12',
                       '_2014_1',
                       '_2014_2',
                       '_2014_3',
                       '_2014_4',
                       '_2014_5',
                       '_2014_6',
                       '_2014_7',
                       '_2014_8',
                       '_2014_9',
                       '_2014_10',
                       '_2014_11',
                       '_2014_12',
                       '_2015_1',
                       '_2015_2',
                       '_2015_3',
                       '_2015_4',
                       '_2015_5',
                       '_2015_6',
                       '_2015_7',
                       '_2015_8',
                       '_2015_9',
                       '_2015_10',
                       '_2015_11',
                       '_2015_12',
                       '_2016_1',
                       '_2016_2',
                       '_2016_3',
                       '_2016_4',
                       '_2016_5',
                       '_2016_6',
                       '_2016_7',
                       '_2016_8',
                       '_2016_9',
                       '_2016_10',
                       '_2016_11',
                       '_2016_12',
                       '_2017_1',
                       '_2017_2',
                       '_2017_3',
                       '_2017_4',
                       '_2017_5',
                       '_2017_6',
                       '_2017_7',
                       '_2017_8',
                       '_2017_9',
                       '_2017_10',
                       '_2017_11',
                       '_2017_12',
                       '_2018_1',
                       '_2018_2',
                       '_2018_3',
                       '_2018_4',
                       '_2018_5',
                       '_2018_6',
                       '_2018_7',
                       '_2018_8',
                       '_2018_9',
                       '_2018_10',
                       '_2018_11',
                       '_2018_12', ]

    data_directory = "data_south/"

    # Enter functions here (and comment out those that you do not need to use)
    getData(start_year=start_year, end_year=end_year, stations=stations)

    for station in stations:
        filenames = []
        for suffix in filename_suffix:
            filenames.append(data_directory+station+suffix)

        mergeFiles(filenames, station+"_merged.txt")
