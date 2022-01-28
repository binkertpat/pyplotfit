import math

import numpy as np
from src import functioncollection
import scipy.optimize as sp
import inspect
import copy


class Fit:
    def __init__(self, plotobject, xDatas, yDatas, fit=0, lowerLimit=None, upperLimit=None, initialGuesses=None):
        self.xDatas = xDatas
        self.yDatas = yDatas

        self.avaiableFits = []
        self.listAvaiableFits()

        if fit != 0:
            self.fit = eval("functioncollection." + str(self.getAvaiableFits()[fit-1]))
            self.fitlabel = eval("functioncollection." + str(self.getAvaiableFits()[fit-1]) + "label")()

        if lowerLimit is None:
            self.lowerLimit = 0
            self.xDatas = xDatas
        else:
            self.lowerLimit = lowerLimit

        if upperLimit is None:
            self.upperLimit = len(self.xDatas)
        else:
            self.upperLimit = upperLimit

        self.xDatas = xDatas[self.lowerLimit: self.upperLimit]
        self.yDatas = yDatas[self.lowerLimit: self.upperLimit]
        self.initialGuesses = initialGuesses
        self.popt = None
        self.cov = None
        self.plotobject = plotobject

        if fit != 0:
            self.calculatefit()

    def getFitLabel(self):
        return self.fitlabel

    def getPlotObject(self):
        return self.plotobject

    def getXdatas(self):
        return self.xDatas

    def getYdatas(self):
        return self.yDatas

    def getLowerLimit(self):
        return self.lowerLimit

    def getUpperLimit(self):
        return self.upperLimit

    def setFit(self, fit):
        self.fit = fit

    def getFit(self):
        return self.fit

    def getPopt(self):
        return self.popt

    def getInitialGuesses(self):
        return self.initialGuesses

    def getAvaiableFits(self):
        return self.avaiableFits

    def listAvaiableFits(self):
        print("List of all key numbers of available fits:")
        allFunctions = inspect.getmembers(functioncollection, inspect.isfunction)
        outputIndex = 0
        for i in range(0, len(allFunctions)):
            if allFunctions[i][0].__contains__("label"):
                continue
            print(str(outputIndex+1)+":", allFunctions[i][0])
            self.avaiableFits.append(allFunctions[i][0])
            outputIndex = outputIndex + 1
        print(" ")

    def calculatefit(self):
        popt, cov = sp.curve_fit(self.getFit(), self.getXdatas(), self.getYdatas(), p0=self.getInitialGuesses())

        params = list(inspect.signature(self.getFit()).parameters)[1:]

        print("Calculated fit-params:")
        for i in range(len(params)):
            print("       ", params[i], " = ", popt[i], "with standard deviation +/-", np.sqrt(np.diag(cov))[i])

        self.popt = popt
        self.cov = cov
        self.calculateFitPlotDatas()

    def calculateFitPlotDatas(self):
        xLine = np.arange(self.getLowerLimit(), self.getUpperLimit(), 0.1)
        yLine = self.getFit()(xLine, *self.getPopt())
        self.getPlotObject().plotFit(xLine, yLine, label=self.getFitLabel())
