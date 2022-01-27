import numpy as np
from src import functioncollection
import scipy.optimize as sp
import inspect


class Fit:
    def __init__(self, plotobject, xDatas, yDatas, fit=0, lowerLimit=None, upperLimit=None, initialGuesses=None):
        self.xDatas = xDatas
        self.yDatas = yDatas

        match fit:
            case 0:
                self.listAvaiableFits()
            case 1:
                self.fit = functioncollection.doublegaussianwithlinearunderground
                self.fitlabel = functioncollection.getdoublegaussianwithlinearundergroundlabel()
                print("Try to fit the given area with an double gaussian function.\n")
            case 2:
                self.fit = functioncollection.gaussianwithlinearunderground
                self.fitlabel = functioncollection.getdoublegaussianwithlinearundergroundlabel()
                print("Try to fit the given area with an gaussian function.\n")
            case 3:
                self.fit = functioncollection.linear
                self.fitlabel = functioncollection.getlinearlabel()
                print("Try to fit the given area with an linear function.\n")

        if lowerLimit is None:
            self.lowerLimit = np.min(self.xDatas)
            self.xDatas = xDatas
        else:
            self.lowerLimit = lowerLimit

        if upperLimit is None:
            self.upperLimit = np.max(self.xDatas)
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

    def listAvaiableFits(self):
        print("\nList of all key numbers of available fits:")
        allFunctions = inspect.getmembers(functioncollection, inspect.isfunction)
        for i in range(0, int(len(allFunctions)/2)):
            print(str(i+1)+":", allFunctions[i][0])

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
