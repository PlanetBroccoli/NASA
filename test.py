import queries
import calculate

if __name__ == "__main__":
    # print(calculate.calculateWeeklyData(queries.getWeeklyData(2013, 16, "C0O810")))
    # print(queries.getStation("kaohsiung", "zuoying"))

    stations = ['C0O810',
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
                'C0R270', ]

    with open("output.txt", "w", encoding="utf-8") as outp:
        for year in range(2014, 2018):
            for week in range(1, 54):
                for station in stations:
                    data = calculate.calculateWeeklyData(
                        queries.getDataForTheWeek(year, week, station))
                    print(data)
                    outp.write(str(year) + "," + str(week) +
                               "," + station + "," + "".join(str(data).replace(")", "").replace("(", "")) + "\n")
