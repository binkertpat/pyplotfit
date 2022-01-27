# pyplotfit
## dependencies
- matplotlib.pyplot 
- matplotlib.patches
- numpy
- math
- scipy
- inspect
---
## Workflow
1. read dataset, use datasetfunctions
2. create new plot-object (line-, scatter or errorbarplot)
3. create new fit-object (use fitobject.listAvaiableFits())
---
## open TODOS
- Update functioncollection for more fit functions
- better fit function selection in fit.__init__ (use inspector.isFunction $$ inspector.isCalllable)
- function for find index in sorted array for nearest given value