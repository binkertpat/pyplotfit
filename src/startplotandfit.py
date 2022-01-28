from src import datasetfunctions, fit, plot

if __name__ == '__main__':
    dataset = datasetfunctions.readfile("cs.Spe")
    X, Y = dataset["channel"], dataset["counts"]

    #Y = [1173.23,1332.492,80.9979,276.3989,302.8508,356.0129,383.8485,121.7817,244.6974,344.2785,411.1165,443.9606,778.9045,867.38,964.057,1112.076,1408.013,661.657]
    #X = [2926.2,3323.979,201.341,688.847,754.816,887.384,956.607,303.092,409.7,858.21,1024.55,1106.01,1940.257,2403.248,2707.59,2773.39,3512.64,1567.696]

    ### VAEV-Koff
    X = [80.9979,121.7817,244.6974,276.3989,302.8508,344.2785,356.0129,383.8485,411.1165,443.9606,661.657,778.9045,
         964.057,1112.076,1173.23,1332.492,1408.013]
    Y = [2.75726676474188,2.3375577388139,1.49946629854519,1.41940416200523,1.28273154159796,1.18492431002056,
         1.15604780017171,1.0364414897928,0.981117207247956,0.998035457651571,0.681009397042416,0.598057076329598,0.22931568296954,0.442622400126309,0.448547102149797,0.400079023798581,0.364293297821452]

    #X = datasetfunctions.calibrate_dataSets(X, [0.386, 28.62])

    print(len(X), len(Y))

    #print(datasetfunctions.getArrayIndexForNearestValue(X, 300))
    #Y = datasetfunctions.countingrate(Y, dataset["time"])

    yerr = datasetfunctions.calculatestatisticalerrors(Y)

    plot = plot.Errorbar(X, Y, xAxis=[0, 1200], axisLabel=["Kanal", "Ereignisse N"], ecolor="grey", yerr=yerr)

    plot.setDataLabel("Gamma-Spektrum für 133-Ba")
    #GaussFit = fit.Fit(plot, X, Y, 2, initialGuesses=[1000, 955, 7, 1, 1], lowerLimit=945, upperLimit=965)
    #doubleGaussFit = fit.Fit(plot, X, Y, 1, initialGuesses=[25000, 98, 7, 7000, 110, 7, 1, 1], lowerLimit=85, upperLimit=120)
    #linFit = fit.Fit(plot, X, Y, 3, initialGuesses=[1, 1], lowerLimit=0, upperLimit=3000)
    expfit = fit.Fit(plot, X, Y, 2, initialGuesses=[1, 1], lowerLimit=datasetfunctions.getArrayIndexForNearestValue(X, 0), upperLimit=datasetfunctions.getArrayIndexForNearestValue(X, 1000))
    plot.showPlot()
