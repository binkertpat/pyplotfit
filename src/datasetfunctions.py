import math

import numpy as np


def readfile(filename):
    """read file and return a directory with time, channels and counts"""
    channel = []
    counts = []
    counter = 0
    with open("../datas/" + filename, "r") as file:
        for i, line in enumerate(file):
            if 12 <= i <= 8202:
                channel.append(counter)
                counter = counter + 1
                counts.append(int(line.strip()))
            elif i == 9:
                measuretime = (int(line.split()[0]) + int(line.split()[1])) / 2

    dataset = {
        'name': filename.split('.')[0],
        'time': int(measuretime),
        'channel': channel,
        'counts': counts
    }

    print("Successfully read the given dataset. The measuretime was: ", measuretime, ".\n")

    return dataset


def calculatestatisticalerrors(dataset):
    """calculate sqrt(N) as error for x- or y-datas (exclusive)"""
    error = []
    for el in dataset:
        error.append(math.sqrt(el))
    return error


def sumdatas(dataset, lowerlimit, upperlimit):
    """sum counts from lower to upper limit"""
    return np.sum(dataset[lowerlimit:upperlimit])


def countingrate(dataset, time):
    """create coutingrate from absolute counts and measuretime"""
    coutingrate = []
    for el in dataset:
        coutingrate.append(el / time)
    return coutingrate


def calibrate_dataSets(dataset, params):
    """calculate new y with an linear expression"""
    newScale = []
    for el in dataset["channel"]:
        newScale.append(params[0] * el + params[1])
    return newScale


def substracttwodatasets_scaledtomeasuretimeofdataset1(dataset1, dataset2):
    """
    input two datasets, get scaled and substracted dataset with measuretime from dataset1

    Parameters
    ----------
    dataset1: dict
        complete read dictionary for dataset with time, name, counts and channel
    dataset2: dict
        complete read dictionary for dataset with time, name, counts and channel
    """
    scalingFactor = dataset1["time"] / dataset2["time"]
    scaledSubstractedDatas = []
    for i in range(0, len(dataset1["channel"])):
        scaledSubstractedDatas.append(max(dataset1['counts'][i] - dataset2['counts'][i] * scalingFactor, 0))
    return {'name': dataset1["name"], 'time': dataset1["time"], 'channel': dataset1["channel"],
            'counts': scaledSubstractedDatas}


def fromchannelstonewscale(value, params):
    """change scale from channel to energy, with linear expression and them parameters"""
    return params[0] * value + params[1]


def fromnewscaletochannels(value, params):
    """change scale from energy to channel, with linear expression and them parameters"""
    return (value - params[1]) / params[0]


def getArrayIndexForNearestValue(array, value):
    arr = np.array(array)
    return np.abs(arr - value).argmin()

