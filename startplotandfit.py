import plot
import fit
import datasetfunctions


if __name__ == '__main__':
    dataset = datasetfunctions.readfile("EU152.Spe")

    X, Y = dataset["channel"], dataset["counts"]

    Y = datasetfunctions.countingrate(Y, dataset["time"])
    yerr = datasetfunctions.calculatestatisticalerrors(Y)

    plot = plot.Errorbar(X, Y, xAxis=[250, 350], ecolor="grey", extraLegendComponent="Messdauer: "+str(dataset["time"])+"s", yerr=yerr)
    doubleGaussFit = fit.Fit(plot, X, Y, 2, initialGuesses=[0.1, 302, 5, 0.1, 0.1], lowerLimit=260, upperLimit=340)
    doubleGaussFit.listAvaiableFits()
    plot.showPlot()


