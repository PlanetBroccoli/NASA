import numpy as np


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
