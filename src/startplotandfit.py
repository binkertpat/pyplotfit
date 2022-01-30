from src import datasetfunctions, fit, plot
import numpy as np

if __name__ == '__main__':
    #dataset = datasetfunctions.readcvsv("energiekalibrierung.csv")
    #Y, X = dataset["x"], dataset["y"]

    #dataset = datasetfunctions.readcvsvwitherrors("vaev.csv")
    #X, Xerr, Y, Yerr = dataset["x"], dataset["xerr"], dataset["y"], dataset["yerr"]

    dataset = datasetfunctions.readSpeFile("Sichel-Tanne.Spe")
    X, Y = dataset["channel"], dataset["counts"]

    X = datasetfunctions.calibrate_dataSets(X, [0.39, 18.62])

    yerr = datasetfunctions.calculatestatisticalerrors(Y)

    plot = plot.Errorbar(X, Y, xAxis=[2555, 2570], axisLabel=["Energie E [keV]", "Ereignisse N"], ecolor="grey", yerr=yerr, extraLegendComponent="Messzeit: "+str(dataset["time"])+"s")
    plot.setDataLabel("Sichel-Tanne")
    GaussFit = fit.Fit(plot, X, Y, 3, initialGuesses=[12, 2562, 4, 1, 1], lowerLimit=2556, upperLimit=2568)
    plot.showPlot()
