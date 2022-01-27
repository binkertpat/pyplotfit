import matplotlib.pyplot as mpl
import matplotlib.patches as mpatches
import numpy as np
import math


class Plot:
    """
    realize a line-plot

    Parameters
    ----------
    xAxis : list
        lower and upper limit for x-Axis
    xDatas: list
        datset (x-dimension)
    yDatas: list
        datset (y-dimension)
    dataLabel: str
        description of what you plot
    lineType: str
        '-', '--', '-.', ':', '.', ',', '+', 'x', '|', '_'
    lineColor: str
        ‘b’	blue, ‘g’ green, ‘r’ red, ‘c’ cyan, ‘m’ magenta, ‘y’ yellow, ‘k’ black, ‘w’ white
    grid: bool
        show grid true/false
    extraLegendComponent: str
        set an extra entry to the legend
    """

    def __init__(self, xDatas, yDatas, dataLabel=None, axisLabel=None, xAxis=None, lineType="--", lineColor="blue",
                 grid=True, extraLegendComponent=None):

        self.fity = None
        self.fitx = None
        self.xDatas = xDatas
        self.yDatas = yDatas

        if dataLabel is None:
            self.dataLabel = "Dataset"
        else:
            self.dataLabel = dataLabel

        if axisLabel is None:
            self.axisLabel = {"x": "x", "y": "y"}
        else:
            self.axisLabel = {"x": axisLabel[0], "y": axisLabel[1]}

        if xAxis is None:
            self.xaxis = {"min": np.min(xDatas), "max": np.max(xDatas)}
        else:
            self.xaxis = {"min": xAxis[0], "max": xAxis[1]}

        self.yAxis = {"min": 0, "max": 0}
        self.lineType = lineType
        self.lineColor = lineColor
        self.grid = grid
        self.extraLegendComponent = extraLegendComponent

    def setxDatas(self, xDatas):
        """set x-axis-array"""
        self.xDatas = xDatas

    def getxDatas(self):
        """get x-axis-array"""
        return self.xDatas

    def setyDatas(self, yDatas):
        """set y-axis-array"""
        self.yDatas = yDatas

    def getyDatas(self):
        """get y-axis-array"""
        return self.yDatas

    def setDataLabel(self, dataLabel):
        """set label for legend"""
        self.dataLabel = dataLabel

    def getDataLabel(self):
        """get label for legend"""
        return self.dataLabel

    def setAxisLabel(self, axisLabel):
        """set x-y-axis label"""
        self.axisLabel = axisLabel

    def getAxisLabel(self):
        """get x-y-axis label"""
        return self.axisLabel

    def setxAxis(self, xAxis):
        """set x-axis dimension"""
        self.xaxis = {"min": xAxis[0], "max": xAxis[1]}

    def getxAxis(self):
        """get x-axis dimension"""
        return self.xaxis

    def setyAxis(self, yAxis):
        """set y-axis dimension"""
        self.yAxis = yAxis

    def getyAxis(self):
        """get y-axis dimension"""
        return self.yAxis

    def setLineType(self, lineType):
        """set line type"""
        self.lineType = lineType

    def getLineType(self):
        """get line type"""
        return self.lineType

    def setLineColor(self, lineColor):
        """set color line"""
        self.lineColor = lineColor

    def getLineColor(self):
        """get color line"""
        return self.lineColor

    def setGrid(self, grid):
        """set grid setting to true/false"""
        self.grid = grid

    def getGrid(self):
        """get grid setting"""
        return self.grid

    def setExtraLegendComponent(self, extraLegendComponent):
        """set an extra legend component"""
        self.extraLegendComponent = extraLegendComponent

    def getExtraLegendComponent(self):
        """get extra legend component"""
        return self.extraLegendComponent

    def calculateYAxis(self):
        """scale y-axis according to max y-datas"""
        self.yAxis["min"] = np.min(self.getyDatas()[self.getxAxis()["min"]:self.getxAxis()["max"]])
        self.yAxis["max"] = np.max(self.getyDatas()[self.getxAxis()["min"]:self.getxAxis()["max"]]) + (
                    1.2 * math.sqrt(np.max(self.getyDatas()[self.getxAxis()["min"]:self.getxAxis()["max"]])))

    def generateAxisDefinition(self):
        """generate new axis-definition"""
        self.calculateYAxis()
        return [self.getxAxis()["min"], self.getxAxis()["max"], self.getyAxis()["min"], self.getyAxis()["max"]]

    def plotFit(self, fitx, fity, color="red", label="Fit"):
        """function called by fit-object, show fit in plot"""
        self.fitx = fitx
        self.fity = fity
        mpl.plot(fitx, fity, '--', color=color, label=label)

    def definePlot(self):
        """define style of plot"""
        mpl.plot(self.getxDatas(), self.getyDatas(), self.getLineType(), color=self.getLineColor(),
                 label=self.getDataLabel())

    def showPlot(self):
        """define all plot settings and show the plot"""
        self.definePlot()

        mpl.axis(self.generateAxisDefinition())

        mpl.legend(loc='best', fancybox=True, shadow=True)
        if self.getExtraLegendComponent() is not None:
            handles, labels = mpl.gca().get_legend_handles_labels()
            empty_patch = mpatches.Patch(color="none", label="extraLegendComponent")
            handles.append(empty_patch)
            labels.append(self.getExtraLegendComponent())
            mpl.legend(handles, labels)

        mpl.xlabel(self.getAxisLabel()["x"])
        mpl.ylabel(self.getAxisLabel()["y"])
        mpl.grid(self.getGrid())
        mpl.subplots_adjust(left=0.06, right=0.98, top=0.98, bottom=0.055)
        mpl.show()


class Scatter(Plot):
    def __init__(self, xDatas, yDatas, dataLabel=None, axisLabel=None, xAxis=None, lineType="--", lineColor="blue",
                 grid=True, extraLegendComponent=None, marker=None, edgecolors=None, linewidths=None):
        super().__init__(xDatas, yDatas, dataLabel, axisLabel, xAxis, lineType, lineColor, grid, extraLegendComponent)
        self.marker = marker
        self.edgecolors = edgecolors
        self.linewidths = linewidths

    def setMarker(self, marker):
        self.marker = marker

    def getMarker(self):
        return self.marker

    def setEdgecolor(self, edgecolors):
        self.edgecolors = edgecolors

    def getEdgecolor(self):
        return self.edgecolors

    def setLinewidths(self, linewidths):
        self.linewidths = linewidths

    def getLinewidths(self):
        return self.linewidths

    def definePlot(self):
        mpl.scatter(self.getxDatas(), self.getyDatas(), marker=self.getMarker(), edgecolors=self.getEdgecolor(),
                    linewidths=self.getLinewidths(), label=self.getDataLabel())


class Errorbar(Plot):
    """
    realize an plot with errorbars

    Parameters
    ----------
    xAxis : list
        lower and upper limit for x-Axis
    xDatas: list
        datset (x-dimension)
    yDatas: list
        datset (y-dimension)
    dataLabel: str
        description of what you plot
    lineType: str
        '-', '--', '-.', ':', '.', ',', '+', 'x', '|', '_'
    lineColor: str
        ‘b’	blue, ‘g’ green, ‘r’ red, ‘c’ cyan, ‘m’ magenta, ‘y’ yellow, ‘k’ black, ‘w’ white
    grid: bool
        show grid true/false
    extraLegendComponent: str
        set an extra entry to the legend
    yerr: list
        error for y-axis
    xerr: list
        error for x-axis
    elinewidth: float
        width of the errorbars
    markersize: float
        thickness of the measurepoint
    ecolor: str
        color of the errorbars
    fmt: str
        key for design of measurpoints
    """

    def __init__(self, xDatas, yDatas, dataLabel=None, axisLabel=None, xAxis=None, lineType="--", lineColor="blue",
                 grid=True, extraLegendComponent=None, yerr=None, xerr=None, elinewidth=1.5, markersize=5,
                 ecolor="lightgray", fmt="x"):
        super().__init__(xDatas, yDatas, dataLabel, axisLabel, xAxis, lineType, lineColor, grid, extraLegendComponent)
        self.yerr = yerr
        self.xerr = xerr
        self.elinewidth = elinewidth
        self.markersize = markersize
        self.ecolor = ecolor
        self.fmt = fmt

    def setXerr(self, xerr):
        self.xerr = xerr

    def getXerr(self):
        return self.xerr

    def setYerr(self, yerr):
        self.yerr = yerr

    def getYerr(self):
        return self.yerr

    def setElinewidth(self, elinewidth):
        self.elinewidth = elinewidth

    def getElinewidth(self):
        return self.elinewidth

    def setMarkersize(self, markersize):
        self.markersize = markersize

    def getMarkersize(self):
        return self.markersize

    def setEcolor(self, ecolor):
        self.ecolor = ecolor

    def getEcolor(self):
        return self.ecolor

    def setFmt(self, fmt):
        self.fmt = fmt

    def getFmt(self):
        return self.fmt

    def definePlot(self):
        mpl.errorbar(self.getxDatas(), self.getyDatas(), label=self.getDataLabel(), yerr=self.getYerr(),
                     xerr=self.getXerr(),
                     fmt=self.getFmt(), elinewidth=self.getElinewidth(), markersize=self.getMarkersize(),
                     ecolor=self.getEcolor())
