import queries
import calculate


def processWeeklyData():
    available_stations = ['C0O810',
                          'C0O830',
                          'C0O840',
                          'C0O860',
                          'C0O900',
                          'C0O930',
                          'C0O950',
                          'C0O960',
                          'C0O970',
                          'C0O980',
                          'C0O990',
                          'C0R130',
                          'C0R140',
                          'C0R150',
                          'C0R160',
                          'C0R170',
                          'C0R180',
                          'C0R220',
                          'C0R240',
                          'C0R260',
                          'C0R270',
                          'C0R370',
                          'C0R380',
                          'C0R400',
                          'C0R420',
                          'C0R470',
                          'C0R480',
                          'C0R490',
                          'C0R510',
                          'C0R520',
                          'C0R530',
                          'C0R540',
                          'C0R550',
                          'C0R560',
                          'C0R570',
                          'C0R580',
                          'C0R590']

    with open("write_to_file.txt", "w", encoding="utf-8") as outp:
        for year in range(2013, 2019):
            for week in range(1, 53):
                for station in available_stations:
                    data = queries.getDataForTheWeek(year, week, station)

                    weekly_data = calculate.calculateWeeklyData(data)

                    if weekly_data != None:
                        merged = ",".join([str(i) for i in weekly_data])
                        output = "," + str(year) + "," + str(week) + \
                            "," + station + "," + merged + "\n"

                        outp.write(output)
                        print(output)


def groupCases():
    with open("input.csv", "r", encoding="utf-8") as inp:
        try:
            output = {}
            for line in inp:
                line = line.replace("\n", "")
                if line in output:
                    output[line] += 1
                else:
                    output[line] = 1

            with open("grouped.csv", "w", encoding="utf-8") as outp:
                for key, value in output.items():
                    outp.write(key + str(value) + "\n")

        except Exception as e:
            print(e)


def grabMiscData():
    with open("21100852_output.csv", "w", encoding="utf-8") as outp:
        with open("grouped.csv", "r", encoding="utf-8") as inp:
            try:
                for line in inp:
                    year, week, city, district = line.split(",")[0:4]

                    other_data = queries.getOtherData(city, district, "zh")
                    pop_data = queries.getPopulationData(city, district, "zh")
                    station = queries.getStation(city, district, "zh")
                    weekly_data = queries.getWeeklyData(
                        year, week, station["station"])

                    if len(weekly_data) > 0:
                        o_data = ",".join([str(i)
                                           for i in other_data.values()])
                        p_data = ",".join([str(i) for i in pop_data.values()])
                        w_data = ",".join([str(i)
                                           for i in weekly_data.values()])

                        outp.write(line.replace("\n", "") + "," + o_data + "," +
                                   p_data + "," + w_data + "\n")

            except Exception as e:
                print(e)


if __name__ == "__main__":
    # groupCases()
    # findStations()
    # print(queries.getWeeklyData(2015, 46, 'C0R170'))
    grabMiscData()
