from src import datasetfunctions, fit, plot

if __name__ == '__main__':
    dataset = datasetfunctions.readfile("Eu.Spe")

    X, Y = dataset["channel"], dataset["counts"]

    #print(datasetfunctions.getArrayIndexForNearestValue(X, 300))

    #Y = datasetfunctions.countingrate(Y, dataset["time"])
    yerr = datasetfunctions.calculatestatisticalerrors(Y)

    plot = plot.Errorbar(X, Y, xAxis=[280, 330], axisLabel=["Kanal", "Ereignisse N"], ecolor="grey", extraLegendComponent="Messdauer: " + str(dataset["time"]) + "s", yerr=yerr)

    plot.setDataLabel("Gamma-Spektrum 133-Ba")
    GaussFit = fit.Fit(plot, X, Y, 2, initialGuesses=[400, 310, 7, 1, 1], lowerLimit=285, upperLimit=325)
    #doubleGaussFit = fit.Fit(plot, X, Y, 1, initialGuesses=[1000, 2700, 7, 300, 2730, 15, 1, 1], lowerLimit=2690, upperLimit=2728)
    plot.showPlot()
