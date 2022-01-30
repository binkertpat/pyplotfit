import src.datasetfunctions as dsf
import src.fit as fit
import src.plot as plot

if __name__ == '__main__':

    # read your file and set x and y
    dataset = dsf.readSpeFile("Sichel-Tanne.Spe")
    X, Y = dataset["channel"], dataset["counts"]

    # change scale and calculate statistical error
    X = dsf.calibrate_dataSets(X, [0.39, 18.62])
    yerr = dsf.calculatestatisticalerrors(Y)

    # create plot object
    plot = plot.Errorbar(X, Y, xAxis=[2555, 2570], axisLabel=["Energie E [keV]", "Ereignisse N"], ecolor="grey",
                         yerr=yerr, extraLegendComponent="Messzeit: "+str(dataset["time"])+"s")
    plot.setDataLabel("Sichel-Tanne")

    # create fit object
    GaussFit = fit.Fit(plot, X, Y, 3, initialGuesses=[12, 2562, 4, 1, 1], lowerLimit=2556, upperLimit=2568)

    # show everything you done
    plot.showPlot()
