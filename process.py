import queries
import sys

# Add station and data to each disease entry


def getData(line):
    line = line.split(",")

    # City, District
    return line[1], line[2], line[3], line[4]


if __name__ == "__main__":
    csv = sys.argv[1]
    out_file = sys.argv[2]
    out_list = []

    with open(csv, "r", encoding="utf-8") as inp:
        with open(out_file, "w", encoding="utf-8") as outp:
            for line in inp:
                try:
                    print(getData(line))
                    year, week, city, district = getData(line)

                    station = queries.getStation(
                        city, district, language="zh")["station"]

                    content = line.replace("\n", "") + "," + station + "\n"
                    print(content)
                    #data = queries.getWeeklyData(year, week, station)
                    #content = [data[i] for i in data]
                    #outp.write(line + "," + ",".join(content))
                    outp.write(content)

                except Exception as e:
                    print(e)
