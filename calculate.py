import numpy as np
import statistics


def calculateProbability(h, t, p, w, r, pop, a):
    '''
    h: Relative humidity
    t: Temperature
    p: Pressure
    w: Average wind speed
    r: Precipitation (rain)
    pop: Population
    a: Surface Area
    '''

    parameters = [h, t, p, w, r, pop, a]

    # This will be our calculation from logistic regression in R
    prediction_matrix = np.zeros(len(parameters))

    return np.dot(parameters, prediction_matrix)


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
        s = statistics.mean([d["sunshine"] for d in ld])
        max_uv = max([d["max_uv"] for d in ld])
        c = statistics.mean([d["cloud"] for d in ld])
        return p, max_p, min_p, t, max_t, min_t, h, min_h, w, g, r, s, max_uv, c

    except Exception as e:
        print(e)
