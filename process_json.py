import json
import urllib.request
import queries

def processDate(datestring):
    line = datestring.split("-")
    year, month = line[0:2]
    day = line[2].split("T")[0]
    
    return year, month, day

if __name__ == "__main__":
    try:
        key = "CWB-5BD5DE1A-8D3C-4A37-ABA6-9055D130DC0E"
        url = "https://opendata.cwb.gov.tw/fileapi/v1/opendataapi/O-A0001-001?Authorization=%s&downloadType=WEB&format=JSON" % (key)
        
        resp = urllib.request.urlopen(url)
        content = resp.read()
        json_file = json.loads(content)
        locations = json_file["cwbopendata"]["location"]
        
        output = {}
        output_str = []
        entry_id = 0
        
        for _ in locations:            
            params = []
            values = []
            time = _["time"]["obsTime"]
            lat, lon = _["lat"], _["lon"]
            station_name, station_id = _["locationName"], _["stationId"]
            others = _["parameter"]
            
            city = others[0]["parameterValue"]
            town = others[2]["parameterValue"]
            
            elements = {"WDSD", "TEMP", "HUMD", "PRES", "H_24R", "H_FX", "D_TX", "D_TN"}
            
            for m in _["weatherElement"]:
                if m["elementName"] in elements:
                    params.append(m["elementName"])
                    values.append(m["elementValue"]["value"])
            
            
            year, month, day = processDate(time)
            
            output[entry_id] = {"year" : year, "month" : month, "day" : day, "station_id" : station_id, "station_name" : station_name, "lat" : lat, "lon" : lon, "city" : city, "town" : town, "values" : ",".join(values)}
            
            entry_id += 1
            
        for entry in output.values():
            temp_str = ""
            #print(entry)
            for item in entry.values():
                temp_str += item+","
            
            temp_str += "\n"
            output_str.append(temp_str)

        for line in output_str:
            queries.saveData(line)
            
        # title = ",".join([key.keys() for key in output.values()][0]) + ",".join(params) + "\n"
        # with open("temp.csv", "w", encoding="utf-8") as outp:
            # outp.write(title)
            # for line in output_str:
                # outp.write(line)
    except Exception as e:
        print(e)
    