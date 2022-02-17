import src.datasetfunctions as dsf
import src.fit as fit
import src.plot as plot

if __name__ == '__main__':

    #dataset = dsf.readcvsv("energiekalibrierung.CSV")
    #Y, X = dataset["x"], dataset["y"]

    # read your file and set x and y
    dataset = dsf.readSpeFile("Sichel-Tanne.Spe")
    X, Y = dataset["channel"], dataset["counts"]

    # change scale and calculate statistical error
    X = dsf.calibrate_dataSets(X, [0.39, 18.62])
    yerr = dsf.calculatestatisticalerrors(Y)

    # create plot object
    plot = plot.Errorbar(X, Y, xAxis=[625, 700], axisLabel=["Ereignisse N", "Energie E [keV]"], ecolor="grey")
    plot.setDataLabel("Energiekalibrierung")

    # create fit object
    GaussFit = fit.Fit(plot, X, Y, 3, upperLimit=670, lowerLimit=650, initialGuesses=[1000, 660, 1, 1, 1])

    # show everything you done
    plot.showPlot()
