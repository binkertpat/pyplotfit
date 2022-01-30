from src import datasetfunctions, fit, plot
import numpy as np

if __name__ == '__main__':
    #dataset = datasetfunctions.readcvsv("energiekalibrierung.csv")
    #Y, X = dataset["x"], dataset["y"]

    #dataset = datasetfunctions.readcvsvwitherrors("vaev.csv")
    #X, Xerr, Y, Yerr = dataset["x"], dataset["xerr"], dataset["y"], dataset["yerr"]

    dataset = datasetfunctions.readSpeFile("Sichel-Tanne.Spe")
    X, Y = dataset["channel"], dataset["counts"]

    # VAEV-Koff
    #X = [80.9979, 121.7817, 244.6974, 276.3989, 302.8508, 344.2785, 356.0129, 383.8485, 411.1165, 443.9606, 661.657,
         #778.9045,
         #964.057, 1112.076, 1173.23, 1332.492, 1408.013]
    #Y = [2.75726676474188, 2.3375577388139, 1.49946629854519, 1.41940416200523, 1.28273154159796, 1.18492431002056,
         #1.15604780017171, 1.0364414897928, 0.981117207247956, 0.998035457651571, 0.681009397042416, 0.598057076329598,
         #0.22931568296954, 0.442622400126309, 0.448547102149797, 0.400079023798581, 0.364293297821452]

    X = datasetfunctions.calibrate_dataSets(X, [0.39, 18.62])

    yerr = datasetfunctions.calculatestatisticalerrors(Y)


    #[590, 620 ... 650, 680 ... 780, 800 ... 1430 1445 ... 2549.2569]
    plot = plot.Errorbar(X, Y, xAxis=[2555, 2570], axisLabel=["Energie E [keV]", "Ereignisse N"], ecolor="grey", yerr=yerr, extraLegendComponent="Messzeit: "+str(dataset["time"])+"s")
    #plot = plot.Errorbar(X, Y, xAxis=[0, 800], axisLabel=["Kanal", "Energie E"], ecolor="grey", yerr=yerr)
    plot.setDataLabel("Sichel-Tanne")
    GaussFit = fit.Fit(plot, X, Y, 3, initialGuesses=[12, 2562, 4, 1, 1], lowerLimit=2555, upperLimit=2570)
    #doubleGaussFit = fit.Fit(plot, X, Y, 1, initialGuesses=[55, 605, 7, 28, 608, 2, 1, 1], lowerLimit=85, upperLimit=120)
    #linFit = fit.Fit(plot, X, Y, 4, initialGuesses=[1, 1], lowerLimit=0, upperLimit=1408)
    #expfit = fit.Fit(plot, X, Y, 2, lowerLimit=0, upperLimit=20000, initialGuesses=[1, 1])
    plot.showPlot()
