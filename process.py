import queries
import sys

# Add station and data to each disease entry


def getData(line):
    line = line.split(",")

    # Year, Week, City, District
    return line[0:4]


if __name__ == "__main__":
    csv = sys.argv[1]
    out_file = sys.argv[2]
    out_list = []

    with open(csv, "r", encoding="utf-8") as inp:
        with open(out_file, "w", encoding="utf-8") as outp:
            for line in inp:
                try:
                    line = line.replace("\n", "")
                    year, week, city, district = getData(line)
                    station = queries.getStation(city, district, language="zh")[
                        "station"].replace("\n", "")
                    print(queries.getStation(city, district, language="zh"))
                    print(city, district, station)
                    data = queries.getWeeklyData(year, week, station)
                    content = line + "," + \
                        ",".join([str(data[i]) for i in data]) + "\n"
                    print(content)
                    outp.write(content)

                except Exception as e:
                    print(e)
