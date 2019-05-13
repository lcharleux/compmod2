# -*- coding: mbcs -*-
# Do not delete the following import lines
from abaqus import *
from abaqusConstants import *
import __main__

def Macro1():
    import section
    import regionToolset
    import displayGroupMdbToolset as dgm
    import part
    import material
    import assembly
    import step
    import interaction
    import load
    import mesh
    import optimization
    import job
    import sketch
    import visualization
    import xyPlot
    import displayGroupOdbToolset as dgo
    import connectorBehavior
    odb = session.odbs['/home/lcharleux/Documents/Programmation/Python/Modules/compmod2/doc/tests/_workdir/RVE.odb']
    session.XYDataFromHistory(name='XYData-1', odb=odb, 
        outputVariableName='Element volume: EVOL at Element 1 in ELSET ALL', 
        steps=('loading', 'loading2', ), )
    session.XYDataFromHistory(name='XYData-2', odb=odb, 
        outputVariableName='Element volume: EVOL at Element 2 in ELSET ALL', 
        steps=('loading', 'loading2', ), )
    session.XYDataFromHistory(name='XYData-3', odb=odb, 
        outputVariableName='Element volume: EVOL at Element 3 in ELSET ALL', 
        steps=('loading', 'loading2', ), )
    session.XYDataFromHistory(name='XYData-4', odb=odb, 
        outputVariableName='Element volume: EVOL at Element 4 in ELSET ALL', 
        steps=('loading', 'loading2', ), )
    session.XYDataFromHistory(name='XYData-5', odb=odb, 
        outputVariableName='Element volume: EVOL at Element 5 in ELSET ALL', 
        steps=('loading', 'loading2', ), )
    session.XYDataFromHistory(name='XYData-6', odb=odb, 
        outputVariableName='Element volume: EVOL at Element 6 in ELSET ALL', 
        steps=('loading', 'loading2', ), )
    session.XYDataFromHistory(name='XYData-7', odb=odb, 
        outputVariableName='Element volume: EVOL at Element 7 in ELSET ALL', 
        steps=('loading', 'loading2', ), )
    session.XYDataFromHistory(name='XYData-8', odb=odb, 
        outputVariableName='Element volume: EVOL at Element 8 in ELSET ALL', 
        steps=('loading', 'loading2', ), )
    session.XYDataFromHistory(name='XYData-9', odb=odb, 
        outputVariableName='Element volume: EVOL at Element 9 in ELSET ALL', 
        steps=('loading', 'loading2', ), )
    session.XYDataFromHistory(name='XYData-10', odb=odb, 
        outputVariableName='Element volume: EVOL at Element 10 in ELSET ALL', 
        steps=('loading', 'loading2', ), )
    session.XYDataFromHistory(name='XYData-11', odb=odb, 
        outputVariableName='Element volume: EVOL at Element 11 in ELSET ALL', 
        steps=('loading', 'loading2', ), )
    session.XYDataFromHistory(name='XYData-12', odb=odb, 
        outputVariableName='Element volume: EVOL at Element 12 in ELSET ALL', 
        steps=('loading', 'loading2', ), )
    session.XYDataFromHistory(name='XYData-13', odb=odb, 
        outputVariableName='Element volume: EVOL at Element 13 in ELSET ALL', 
        steps=('loading', 'loading2', ), )
    session.XYDataFromHistory(name='XYData-14', odb=odb, 
        outputVariableName='Element volume: EVOL at Element 14 in ELSET ALL', 
        steps=('loading', 'loading2', ), )
    session.XYDataFromHistory(name='XYData-15', odb=odb, 
        outputVariableName='Element volume: EVOL at Element 15 in ELSET ALL', 
        steps=('loading', 'loading2', ), )
    session.XYDataFromHistory(name='XYData-16', odb=odb, 
        outputVariableName='Element volume: EVOL at Element 16 in ELSET ALL', 
        steps=('loading', 'loading2', ), )
    session.XYDataFromHistory(name='XYData-17', odb=odb, 
        outputVariableName='Element volume: EVOL at Element 17 in ELSET ALL', 
        steps=('loading', 'loading2', ), )
    session.XYDataFromHistory(name='XYData-18', odb=odb, 
        outputVariableName='Element volume: EVOL at Element 18 in ELSET ALL', 
        steps=('loading', 'loading2', ), )
    session.XYDataFromHistory(name='XYData-19', odb=odb, 
        outputVariableName='Element volume: EVOL at Element 19 in ELSET ALL', 
        steps=('loading', 'loading2', ), )
    session.XYDataFromHistory(name='XYData-20', odb=odb, 
        outputVariableName='Element volume: EVOL at Element 20 in ELSET ALL', 
        steps=('loading', 'loading2', ), )
    session.XYDataFromHistory(name='XYData-21', odb=odb, 
        outputVariableName='Element volume: EVOL at Element 21 in ELSET ALL', 
        steps=('loading', 'loading2', ), )
    session.XYDataFromHistory(name='XYData-22', odb=odb, 
        outputVariableName='Element volume: EVOL at Element 22 in ELSET ALL', 
        steps=('loading', 'loading2', ), )
    session.XYDataFromHistory(name='XYData-23', odb=odb, 
        outputVariableName='Element volume: EVOL at Element 23 in ELSET ALL', 
        steps=('loading', 'loading2', ), )
    session.XYDataFromHistory(name='XYData-24', odb=odb, 
        outputVariableName='Element volume: EVOL at Element 24 in ELSET ALL', 
        steps=('loading', 'loading2', ), )
    session.XYDataFromHistory(name='XYData-25', odb=odb, 
        outputVariableName='Element volume: EVOL at Element 25 in ELSET ALL', 
        steps=('loading', 'loading2', ), )
    session.XYDataFromHistory(name='XYData-26', odb=odb, 
        outputVariableName='Element volume: EVOL at Element 26 in ELSET ALL', 
        steps=('loading', 'loading2', ), )
    session.XYDataFromHistory(name='XYData-27', odb=odb, 
        outputVariableName='Element volume: EVOL at Element 27 in ELSET ALL', 
        steps=('loading', 'loading2', ), )
    session.XYDataFromHistory(name='XYData-28', odb=odb, 
        outputVariableName='Element volume: EVOL at Element 28 in ELSET ALL', 
        steps=('loading', 'loading2', ), )
    session.XYDataFromHistory(name='XYData-29', odb=odb, 
        outputVariableName='Element volume: EVOL at Element 29 in ELSET ALL', 
        steps=('loading', 'loading2', ), )
    session.XYDataFromHistory(name='XYData-30', odb=odb, 
        outputVariableName='Element volume: EVOL at Element 30 in ELSET ALL', 
        steps=('loading', 'loading2', ), )
    session.XYDataFromHistory(name='XYData-31', odb=odb, 
        outputVariableName='Element volume: EVOL at Element 31 in ELSET ALL', 
        steps=('loading', 'loading2', ), )
    session.XYDataFromHistory(name='XYData-32', odb=odb, 
        outputVariableName='Element volume: EVOL at Element 32 in ELSET ALL', 
        steps=('loading', 'loading2', ), )
    session.XYDataFromHistory(name='XYData-33', odb=odb, 
        outputVariableName='Element volume: EVOL at Element 33 in ELSET ALL', 
        steps=('loading', 'loading2', ), )
    session.XYDataFromHistory(name='XYData-34', odb=odb, 
        outputVariableName='Element volume: EVOL at Element 34 in ELSET ALL', 
        steps=('loading', 'loading2', ), )
    session.XYDataFromHistory(name='XYData-35', odb=odb, 
        outputVariableName='Element volume: EVOL at Element 35 in ELSET ALL', 
        steps=('loading', 'loading2', ), )
    session.XYDataFromHistory(name='XYData-36', odb=odb, 
        outputVariableName='Element volume: EVOL at Element 36 in ELSET ALL', 
        steps=('loading', 'loading2', ), )
    session.XYDataFromHistory(name='XYData-37', odb=odb, 
        outputVariableName='Element volume: EVOL at Element 37 in ELSET ALL', 
        steps=('loading', 'loading2', ), )
    session.XYDataFromHistory(name='XYData-38', odb=odb, 
        outputVariableName='Element volume: EVOL at Element 38 in ELSET ALL', 
        steps=('loading', 'loading2', ), )
    session.XYDataFromHistory(name='XYData-39', odb=odb, 
        outputVariableName='Element volume: EVOL at Element 39 in ELSET ALL', 
        steps=('loading', 'loading2', ), )
    session.XYDataFromHistory(name='XYData-40', odb=odb, 
        outputVariableName='Element volume: EVOL at Element 40 in ELSET ALL', 
        steps=('loading', 'loading2', ), )
    session.XYDataFromHistory(name='XYData-41', odb=odb, 
        outputVariableName='Element volume: EVOL at Element 41 in ELSET ALL', 
        steps=('loading', 'loading2', ), )
    session.XYDataFromHistory(name='XYData-42', odb=odb, 
        outputVariableName='Element volume: EVOL at Element 42 in ELSET ALL', 
        steps=('loading', 'loading2', ), )
    session.XYDataFromHistory(name='XYData-43', odb=odb, 
        outputVariableName='Element volume: EVOL at Element 43 in ELSET ALL', 
        steps=('loading', 'loading2', ), )
    session.XYDataFromHistory(name='XYData-44', odb=odb, 
        outputVariableName='Element volume: EVOL at Element 44 in ELSET ALL', 
        steps=('loading', 'loading2', ), )
    session.XYDataFromHistory(name='XYData-45', odb=odb, 
        outputVariableName='Element volume: EVOL at Element 45 in ELSET ALL', 
        steps=('loading', 'loading2', ), )
    session.XYDataFromHistory(name='XYData-46', odb=odb, 
        outputVariableName='Element volume: EVOL at Element 46 in ELSET ALL', 
        steps=('loading', 'loading2', ), )
    session.XYDataFromHistory(name='XYData-47', odb=odb, 
        outputVariableName='Element volume: EVOL at Element 47 in ELSET ALL', 
        steps=('loading', 'loading2', ), )
    session.XYDataFromHistory(name='XYData-48', odb=odb, 
        outputVariableName='Element volume: EVOL at Element 48 in ELSET ALL', 
        steps=('loading', 'loading2', ), )
    session.XYDataFromHistory(name='XYData-49', odb=odb, 
        outputVariableName='Element volume: EVOL at Element 49 in ELSET ALL', 
        steps=('loading', 'loading2', ), )
    session.XYDataFromHistory(name='XYData-50', odb=odb, 
        outputVariableName='Element volume: EVOL at Element 50 in ELSET ALL', 
        steps=('loading', 'loading2', ), )
    session.XYDataFromHistory(name='XYData-51', odb=odb, 
        outputVariableName='Element volume: EVOL at Element 51 in ELSET ALL', 
        steps=('loading', 'loading2', ), )
    session.XYDataFromHistory(name='XYData-52', odb=odb, 
        outputVariableName='Element volume: EVOL at Element 52 in ELSET ALL', 
        steps=('loading', 'loading2', ), )
    session.XYDataFromHistory(name='XYData-53', odb=odb, 
        outputVariableName='Element volume: EVOL at Element 53 in ELSET ALL', 
        steps=('loading', 'loading2', ), )
    session.XYDataFromHistory(name='XYData-54', odb=odb, 
        outputVariableName='Element volume: EVOL at Element 54 in ELSET ALL', 
        steps=('loading', 'loading2', ), )
    session.XYDataFromHistory(name='XYData-55', odb=odb, 
        outputVariableName='Element volume: EVOL at Element 55 in ELSET ALL', 
        steps=('loading', 'loading2', ), )
    session.XYDataFromHistory(name='XYData-56', odb=odb, 
        outputVariableName='Element volume: EVOL at Element 56 in ELSET ALL', 
        steps=('loading', 'loading2', ), )
    session.XYDataFromHistory(name='XYData-57', odb=odb, 
        outputVariableName='Element volume: EVOL at Element 57 in ELSET ALL', 
        steps=('loading', 'loading2', ), )
    session.XYDataFromHistory(name='XYData-58', odb=odb, 
        outputVariableName='Element volume: EVOL at Element 58 in ELSET ALL', 
        steps=('loading', 'loading2', ), )
    session.XYDataFromHistory(name='XYData-59', odb=odb, 
        outputVariableName='Element volume: EVOL at Element 59 in ELSET ALL', 
        steps=('loading', 'loading2', ), )
    session.XYDataFromHistory(name='XYData-60', odb=odb, 
        outputVariableName='Element volume: EVOL at Element 60 in ELSET ALL', 
        steps=('loading', 'loading2', ), )
    session.XYDataFromHistory(name='XYData-61', odb=odb, 
        outputVariableName='Element volume: EVOL at Element 61 in ELSET ALL', 
        steps=('loading', 'loading2', ), )
    session.XYDataFromHistory(name='XYData-62', odb=odb, 
        outputVariableName='Element volume: EVOL at Element 62 in ELSET ALL', 
        steps=('loading', 'loading2', ), )
    session.XYDataFromHistory(name='XYData-63', odb=odb, 
        outputVariableName='Element volume: EVOL at Element 63 in ELSET ALL', 
        steps=('loading', 'loading2', ), )
    session.XYDataFromHistory(name='XYData-64', odb=odb, 
        outputVariableName='Element volume: EVOL at Element 64 in ELSET ALL', 
        steps=('loading', 'loading2', ), )
    xy1 = session.xyDataObjects['XYData-1']
    xy2 = session.xyDataObjects['XYData-2']
    xy3 = session.xyDataObjects['XYData-3']
    xy4 = session.xyDataObjects['XYData-4']
    xy5 = session.xyDataObjects['XYData-5']
    xy6 = session.xyDataObjects['XYData-6']
    xy7 = session.xyDataObjects['XYData-7']
    xy8 = session.xyDataObjects['XYData-8']
    xy9 = session.xyDataObjects['XYData-9']
    xy10 = session.xyDataObjects['XYData-10']
    xy11 = session.xyDataObjects['XYData-11']
    xy12 = session.xyDataObjects['XYData-12']
    xy13 = session.xyDataObjects['XYData-13']
    xy14 = session.xyDataObjects['XYData-14']
    xy15 = session.xyDataObjects['XYData-15']
    xy16 = session.xyDataObjects['XYData-16']
    xy17 = session.xyDataObjects['XYData-17']
    xy18 = session.xyDataObjects['XYData-18']
    xy19 = session.xyDataObjects['XYData-19']
    xy20 = session.xyDataObjects['XYData-20']
    xy21 = session.xyDataObjects['XYData-21']
    xy22 = session.xyDataObjects['XYData-22']
    xy23 = session.xyDataObjects['XYData-23']
    xy24 = session.xyDataObjects['XYData-24']
    xy25 = session.xyDataObjects['XYData-25']
    xy26 = session.xyDataObjects['XYData-26']
    xy27 = session.xyDataObjects['XYData-27']
    xy28 = session.xyDataObjects['XYData-28']
    xy29 = session.xyDataObjects['XYData-29']
    xy30 = session.xyDataObjects['XYData-30']
    xy31 = session.xyDataObjects['XYData-31']
    xy32 = session.xyDataObjects['XYData-32']
    xy33 = session.xyDataObjects['XYData-33']
    xy34 = session.xyDataObjects['XYData-34']
    xy35 = session.xyDataObjects['XYData-35']
    xy36 = session.xyDataObjects['XYData-36']
    xy37 = session.xyDataObjects['XYData-37']
    xy38 = session.xyDataObjects['XYData-38']
    xy39 = session.xyDataObjects['XYData-39']
    xy40 = session.xyDataObjects['XYData-40']
    xy41 = session.xyDataObjects['XYData-41']
    xy42 = session.xyDataObjects['XYData-42']
    xy43 = session.xyDataObjects['XYData-43']
    xy44 = session.xyDataObjects['XYData-44']
    xy45 = session.xyDataObjects['XYData-45']
    xy46 = session.xyDataObjects['XYData-46']
    xy47 = session.xyDataObjects['XYData-47']
    xy48 = session.xyDataObjects['XYData-48']
    xy49 = session.xyDataObjects['XYData-49']
    xy50 = session.xyDataObjects['XYData-50']
    xy51 = session.xyDataObjects['XYData-51']
    xy52 = session.xyDataObjects['XYData-52']
    xy53 = session.xyDataObjects['XYData-53']
    xy54 = session.xyDataObjects['XYData-54']
    xy55 = session.xyDataObjects['XYData-55']
    xy56 = session.xyDataObjects['XYData-56']
    xy57 = session.xyDataObjects['XYData-57']
    xy58 = session.xyDataObjects['XYData-58']
    xy59 = session.xyDataObjects['XYData-59']
    xy60 = session.xyDataObjects['XYData-60']
    xy61 = session.xyDataObjects['XYData-61']
    xy62 = session.xyDataObjects['XYData-62']
    xy63 = session.xyDataObjects['XYData-63']
    xy64 = session.xyDataObjects['XYData-64']
    xy65 = sum(xy1, xy2, xy3, xy4, xy5, xy6, xy7, xy8, xy9, xy10, xy11, xy12, xy13, 
        xy14, xy15, xy16, xy17, xy18, xy19, xy20, xy21, xy22, xy23, xy24, xy25, 
        xy26, xy27, xy28, xy29, xy30, xy31, xy32, xy33, xy34, xy35, xy36, xy37, 
        xy38, xy39, xy40, xy41, xy42, xy43, xy44, xy45, xy46, xy47, xy48, xy49, 
        xy50, xy51, xy52, xy53, xy54, xy55, xy56, xy57, xy58, xy59, xy60, xy61, 
        xy62, xy63, xy64)
    xyp = session.XYPlot('XYPlot-1')
    chartName = xyp.charts.keys()[0]
    chart = xyp.charts[chartName]
    c1 = session.Curve(xyData=xy65)
    chart.setValues(curvesToPlot=(c1, ), )
    session.viewports['Viewport: 1'].setValues(displayedObject=xyp)
    xy1 = session.xyDataObjects['XYData-1']
    xy2 = session.xyDataObjects['XYData-2']
    xy3 = session.xyDataObjects['XYData-3']
    xy4 = session.xyDataObjects['XYData-4']
    xy5 = session.xyDataObjects['XYData-5']
    xy6 = session.xyDataObjects['XYData-6']
    xy7 = session.xyDataObjects['XYData-7']
    xy8 = session.xyDataObjects['XYData-8']
    xy9 = session.xyDataObjects['XYData-9']
    xy10 = session.xyDataObjects['XYData-10']
    xy11 = session.xyDataObjects['XYData-11']
    xy12 = session.xyDataObjects['XYData-12']
    xy13 = session.xyDataObjects['XYData-13']
    xy14 = session.xyDataObjects['XYData-14']
    xy15 = session.xyDataObjects['XYData-15']
    xy16 = session.xyDataObjects['XYData-16']
    xy17 = session.xyDataObjects['XYData-17']
    xy18 = session.xyDataObjects['XYData-18']
    xy19 = session.xyDataObjects['XYData-19']
    xy20 = session.xyDataObjects['XYData-20']
    xy21 = session.xyDataObjects['XYData-21']
    xy22 = session.xyDataObjects['XYData-22']
    xy23 = session.xyDataObjects['XYData-23']
    xy24 = session.xyDataObjects['XYData-24']
    xy25 = session.xyDataObjects['XYData-25']
    xy26 = session.xyDataObjects['XYData-26']
    xy27 = session.xyDataObjects['XYData-27']
    xy28 = session.xyDataObjects['XYData-28']
    xy29 = session.xyDataObjects['XYData-29']
    xy30 = session.xyDataObjects['XYData-30']
    xy31 = session.xyDataObjects['XYData-31']
    xy32 = session.xyDataObjects['XYData-32']
    xy33 = session.xyDataObjects['XYData-33']
    xy34 = session.xyDataObjects['XYData-34']
    xy35 = session.xyDataObjects['XYData-35']
    xy36 = session.xyDataObjects['XYData-36']
    xy37 = session.xyDataObjects['XYData-37']
    xy38 = session.xyDataObjects['XYData-38']
    xy39 = session.xyDataObjects['XYData-39']
    xy40 = session.xyDataObjects['XYData-40']
    xy41 = session.xyDataObjects['XYData-41']
    xy42 = session.xyDataObjects['XYData-42']
    xy43 = session.xyDataObjects['XYData-43']
    xy44 = session.xyDataObjects['XYData-44']
    xy45 = session.xyDataObjects['XYData-45']
    xy46 = session.xyDataObjects['XYData-46']
    xy47 = session.xyDataObjects['XYData-47']
    xy48 = session.xyDataObjects['XYData-48']
    xy49 = session.xyDataObjects['XYData-49']
    xy50 = session.xyDataObjects['XYData-50']
    xy51 = session.xyDataObjects['XYData-51']
    xy52 = session.xyDataObjects['XYData-52']
    xy53 = session.xyDataObjects['XYData-53']
    xy54 = session.xyDataObjects['XYData-54']
    xy55 = session.xyDataObjects['XYData-55']
    xy56 = session.xyDataObjects['XYData-56']
    xy57 = session.xyDataObjects['XYData-57']
    xy58 = session.xyDataObjects['XYData-58']
    xy59 = session.xyDataObjects['XYData-59']
    xy60 = session.xyDataObjects['XYData-60']
    xy61 = session.xyDataObjects['XYData-61']
    xy62 = session.xyDataObjects['XYData-62']
    xy63 = session.xyDataObjects['XYData-63']
    xy64 = session.xyDataObjects['XYData-64']
    xy65 = sum((xy1, xy2, xy3, xy4, xy5, xy6, xy7, xy8, xy9, xy10, xy11, xy12, 
        xy13, xy14, xy15, xy16, xy17, xy18, xy19, xy20, xy21, xy22, xy23, xy24, 
        xy25, xy26, xy27, xy28, xy29, xy30, xy31, xy32, xy33, xy34, xy35, xy36, 
        xy37, xy38, xy39, xy40, xy41, xy42, xy43, xy44, xy45, xy46, xy47, xy48, 
        xy49, xy50, xy51, xy52, xy53, xy54, xy55, xy56, xy57, xy58, xy59, xy60, 
        xy61, xy62, xy63, xy64))
    xyp = session.xyPlots['XYPlot-1']
    chartName = xyp.charts.keys()[0]
    chart = xyp.charts[chartName]
    c1 = session.Curve(xyData=xy65)
    chart.setValues(curvesToPlot=(c1, ), )
    xy1 = session.xyDataObjects['XYData-1']
    xy2 = session.xyDataObjects['XYData-2']
    xy3 = session.xyDataObjects['XYData-3']
    xy4 = session.xyDataObjects['XYData-4']
    xy5 = session.xyDataObjects['XYData-5']
    xy6 = session.xyDataObjects['XYData-6']
    xy7 = session.xyDataObjects['XYData-7']
    xy8 = session.xyDataObjects['XYData-8']
    xy9 = session.xyDataObjects['XYData-9']
    xy10 = session.xyDataObjects['XYData-10']
    xy11 = session.xyDataObjects['XYData-11']
    xy12 = session.xyDataObjects['XYData-12']
    xy13 = session.xyDataObjects['XYData-13']
    xy14 = session.xyDataObjects['XYData-14']
    xy15 = session.xyDataObjects['XYData-15']
    xy16 = session.xyDataObjects['XYData-16']
    xy17 = session.xyDataObjects['XYData-17']
    xy18 = session.xyDataObjects['XYData-18']
    xy19 = session.xyDataObjects['XYData-19']
    xy20 = session.xyDataObjects['XYData-20']
    xy21 = session.xyDataObjects['XYData-21']
    xy22 = session.xyDataObjects['XYData-22']
    xy23 = session.xyDataObjects['XYData-23']
    xy24 = session.xyDataObjects['XYData-24']
    xy25 = session.xyDataObjects['XYData-25']
    xy26 = session.xyDataObjects['XYData-26']
    xy27 = session.xyDataObjects['XYData-27']
    xy28 = session.xyDataObjects['XYData-28']
    xy29 = session.xyDataObjects['XYData-29']
    xy30 = session.xyDataObjects['XYData-30']
    xy31 = session.xyDataObjects['XYData-31']
    xy32 = session.xyDataObjects['XYData-32']
    xy33 = session.xyDataObjects['XYData-33']
    xy34 = session.xyDataObjects['XYData-34']
    xy35 = session.xyDataObjects['XYData-35']
    xy36 = session.xyDataObjects['XYData-36']
    xy37 = session.xyDataObjects['XYData-37']
    xy38 = session.xyDataObjects['XYData-38']
    xy39 = session.xyDataObjects['XYData-39']
    xy40 = session.xyDataObjects['XYData-40']
    xy41 = session.xyDataObjects['XYData-41']
    xy42 = session.xyDataObjects['XYData-42']
    xy43 = session.xyDataObjects['XYData-43']
    xy44 = session.xyDataObjects['XYData-44']
    xy45 = session.xyDataObjects['XYData-45']
    xy46 = session.xyDataObjects['XYData-46']
    xy47 = session.xyDataObjects['XYData-47']
    xy48 = session.xyDataObjects['XYData-48']
    xy49 = session.xyDataObjects['XYData-49']
    xy50 = session.xyDataObjects['XYData-50']
    xy51 = session.xyDataObjects['XYData-51']
    xy52 = session.xyDataObjects['XYData-52']
    xy53 = session.xyDataObjects['XYData-53']
    xy54 = session.xyDataObjects['XYData-54']
    xy55 = session.xyDataObjects['XYData-55']
    xy56 = session.xyDataObjects['XYData-56']
    xy57 = session.xyDataObjects['XYData-57']
    xy58 = session.xyDataObjects['XYData-58']
    xy59 = session.xyDataObjects['XYData-59']
    xy60 = session.xyDataObjects['XYData-60']
    xy61 = session.xyDataObjects['XYData-61']
    xy62 = session.xyDataObjects['XYData-62']
    xy63 = session.xyDataObjects['XYData-63']
    xy64 = session.xyDataObjects['XYData-64']
    xy65 = sum((xy1, xy2, xy3, xy4, xy5, xy6, xy7, xy8, xy9, xy10, xy11, xy12, 
        xy13, xy14, xy15, xy16, xy17, xy18, xy19, xy20, xy21, xy22, xy23, xy24, 
        xy25, xy26, xy27, xy28, xy29, xy30, xy31, xy32, xy33, xy34, xy35, xy36, 
        xy37, xy38, xy39, xy40, xy41, xy42, xy43, xy44, xy45, xy46, xy47, xy48, 
        xy49, xy50, xy51, xy52, xy53, xy54, xy55, xy56, xy57, xy58, xy59, xy60, 
        xy61, xy62, xy63, xy64))
    xy65.setValues(
        sourceDescription='sum(("XYData-1", "XYData-2", "XYData-3", "XYData-4", "XYData-5", "XYData-6", "XYData-7", "XYData-8", "XYData-9", "XYData-10", "XYData-11", "XYData-12", "XYData-13", "XYData-14", "XYData-15", "XYData-16", "XYData-17", "XYData-18", "XYData-19", "XYData-20", "XYData-21", "XYData-22", "XYData-23", "XYData-24", "XYData-25", "XYData-26", "XYData-27", "XYData-28", "XYData-29", "XYData-30", "XYData-31", "XYData-32", "XYData-33", "XYData-34", "XYData-35", "XYData-36", "XYData-37", "XYData-38", "XYData-39", "XYData-40", "XYData-41", "XYData-42", "XYData-43", "XYData-44", "XYData-45", "XYData-46", "XYData-47", "XYData-48", "XYData-49", "XYData-50", "XYData-51", "XYData-52", "XYData-53", "XYData-54", "XYData-55", "XYData-56", "XYData-57", "XYData-58", "XYData-59", "XYData-60", "XYData-61", "XYData-62", "XYData-63", "XYData-64"))')
    tmpName = xy65.name
    session.xyDataObjects.changeKey(tmpName, 'volume')


