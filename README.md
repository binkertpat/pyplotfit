# pyplotfit  
## dependencies / used modules 
- matplotlib.pyplot   
- matplotlib.patches  
- numpy  
- math  
- scipy  
- inspect  
  
## HOW-TO
### read datas
 First of all reading your Dataset. According to our experiment, we designed a method for reading the output file of an Gamma-Ray-Detektor. Feel free to add or change other reading functions in <code> datasetfunctions.py</code>.
```python
dataset = datasetfunctions.readfile("EU152.Spe")
```
The output of <code> readfile(filename)</code>  is an dictionary.
```python
dataset = {  
	  'name': filename.split('.')[0],  
	  'time': int(measuretime),  
	  'channel': channel,  
	  'counts': counts  
}
```
### realize plot
In the next step you are able to create an <code>Plot()</code>-, <code>Scatter()</code>- or <code>Errorbar()</code>-Object. 
The only required parameters are the datas for x and y. For example:
```python
plot = plot.Errorbar(X, Y)
```
All other parameters are not required or there are default settings. In depends on the chosen plot style you are able to set ... (with default values)
```python
Plot(
	x: list (required)
	y: list (required)
	dataLabel=None: str 
	axisLabel=None: list
	xAxis=None: list
	lineType="--": str
	lineColor="blue": str 
	grid=True: bool
	extraLegendComponent=None: str
)

Scatter(
	x: list (required)
	y: list (required)
	dataLabel=None: str 
	axisLabel=None: list
	xAxis=None: list
	lineType="--": str
	lineColor="blue": str 
	grid=True: bool
	extraLegendComponent=None: str
	marker=None: str
	edgecolors=None: str
	linewidths=None: str
)

Errorbar(
	x: list (required)
	y: list (required)
	dataLabel=None: str 
	axisLabel=None: list
	xAxis=None: list
	lineType="--": str
	lineColor="blue": str 
	grid=True: bool
	extraLegendComponent=None: str
	yerr=None: list (same dimension like y required)
	xerr=None: list (same dimension like x required) 
	elinewidth=1.5: float
	markersize=5: float  
	ecolor="lightgray": str 
	fmt="x": str
)
```
### add fits



## open TODOs  
- Update functioncollection for more fit functions  
- function for find index in sorted array for nearest given value  