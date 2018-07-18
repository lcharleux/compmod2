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
    o7 = session.odbs['/home/lcharleux/Documents/Programmation/Python/Modules/compmod2/doc/tests/_workdir/RVE.odb']
    session.viewports['Viewport: 1'].setValues(displayedObject=o7)
    session.mdbData.summary()
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
    session.XYDataFromHistory(name='XYData-65', odb=odb, 
        outputVariableName='External work: ALLWK for Whole Model', steps=(
        'loading', 'loading2', ), )
    session.XYDataFromHistory(name='XYData-66', odb=odb, 
        outputVariableName='Plastic dissipation: ALLPD for Whole Model', 
        steps=('loading', 'loading2', ), )
    session.XYDataFromHistory(name='XYData-67', odb=odb, 
        outputVariableName='Point loads: CF1 at Node 126 in NSET CONTROL', 
        steps=('loading', 'loading2', ), )
    session.XYDataFromHistory(name='XYData-68', odb=odb, 
        outputVariableName='Point loads: CF2 at Node 126 in NSET CONTROL', 
        steps=('loading', 'loading2', ), )
    session.XYDataFromHistory(name='XYData-69', odb=odb, 
        outputVariableName='Point loads: CF3 at Node 126 in NSET CONTROL', 
        steps=('loading', 'loading2', ), )
    session.XYDataFromHistory(name='XYData-70', odb=odb, 
        outputVariableName='Reaction force: RF1 at Node 126 in NSET CONTROL', 
        steps=('loading', 'loading2', ), )
    session.XYDataFromHistory(name='XYData-71', odb=odb, 
        outputVariableName='Reaction force: RF2 at Node 126 in NSET CONTROL', 
        steps=('loading', 'loading2', ), )
    session.XYDataFromHistory(name='XYData-72', odb=odb, 
        outputVariableName='Reaction force: RF3 at Node 126 in NSET CONTROL', 
        steps=('loading', 'loading2', ), )
    session.XYDataFromHistory(name='XYData-73', odb=odb, 
        outputVariableName='Spatial displacement: U1 at Node 126 in NSET CONTROL', 
        steps=('loading', 'loading2', ), )
    session.XYDataFromHistory(name='XYData-74', odb=odb, 
        outputVariableName='Spatial displacement: U2 at Node 126 in NSET CONTROL', 
        steps=('loading', 'loading2', ), )
    session.XYDataFromHistory(name='XYData-75', odb=odb, 
        outputVariableName='Spatial displacement: U3 at Node 126 in NSET CONTROL', 
        steps=('loading', 'loading2', ), )
    session.XYDataFromHistory(name='XYData-76', odb=odb, 
        outputVariableName='Strain energy: ALLSE for Whole Model', steps=(
        'loading', 'loading2', ), )


def Macro2():
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
    session.XYDataFromHistory(name='XYData-77', odb=odb, 
        outputVariableName='External work: ALLWK for Whole Model', steps=(
        'loading', 'loading2', ), )
    session.XYDataFromHistory(name='XYData-78', odb=odb, 
        outputVariableName='Plastic dissipation: ALLPD for Whole Model', 
        steps=('loading', 'loading2', ), )
    session.XYDataFromHistory(name='XYData-79', odb=odb, 
        outputVariableName='Point loads: CF1 at Node 126 in NSET CONTROL', 
        steps=('loading', 'loading2', ), )
    session.XYDataFromHistory(name='XYData-80', odb=odb, 
        outputVariableName='Point loads: CF2 at Node 126 in NSET CONTROL', 
        steps=('loading', 'loading2', ), )
    session.XYDataFromHistory(name='XYData-81', odb=odb, 
        outputVariableName='Point loads: CF3 at Node 126 in NSET CONTROL', 
        steps=('loading', 'loading2', ), )
    session.XYDataFromHistory(name='XYData-82', odb=odb, 
        outputVariableName='Reaction force: RF1 at Node 126 in NSET CONTROL', 
        steps=('loading', 'loading2', ), )
    session.XYDataFromHistory(name='XYData-83', odb=odb, 
        outputVariableName='Reaction force: RF2 at Node 126 in NSET CONTROL', 
        steps=('loading', 'loading2', ), )
    session.XYDataFromHistory(name='XYData-84', odb=odb, 
        outputVariableName='Reaction force: RF3 at Node 126 in NSET CONTROL', 
        steps=('loading', 'loading2', ), )
    session.XYDataFromHistory(name='XYData-85', odb=odb, 
        outputVariableName='Spatial displacement: U1 at Node 126 in NSET CONTROL', 
        steps=('loading', 'loading2', ), )
    session.XYDataFromHistory(name='XYData-86', odb=odb, 
        outputVariableName='Spatial displacement: U2 at Node 126 in NSET CONTROL', 
        steps=('loading', 'loading2', ), )
    session.XYDataFromHistory(name='XYData-87', odb=odb, 
        outputVariableName='Spatial displacement: U3 at Node 126 in NSET CONTROL', 
        steps=('loading', 'loading2', ), )
    session.XYDataFromHistory(name='XYData-88', odb=odb, 
        outputVariableName='Strain energy: ALLSE for Whole Model', steps=(
        'loading', 'loading2', ), )
    pass
    import atxPdb;atxPdb.setFirstTrace(0)
    import atxPdb;atxPdb.debugFile(
        fileName='/home/lcharleux/Documents/Programmation/Python/Modules/compmod2/doc/tests/_workdir/RVE_abqposproc.py', 
        serverPort=48279)
    pass
    import atxPdb;atxPdb.setFirstTrace(1)
    pass
    import atxPdb;atxPdb.setFirstTrace(0)
    import atxPdb;atxPdb.debugFile(
        fileName='/home/lcharleux/Documents/Programmation/Python/Modules/compmod2/doc/tests/_workdir/RVE_abqposproc.py', 
        serverPort=48279)
    pass
    import atxPdb;atxPdb.setFirstTrace(1)


def Macro3():
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
    del session.xyDataObjects['_temp_3']
    del session.xyDataObjects['evol_1']
    del session.xyDataObjects['evol_2']
    del session.xyDataObjects['evol_3']
    del session.xyDataObjects['evol_4']
    del session.xyDataObjects['evol_5']
    del session.xyDataObjects['evol_6']
    del session.xyDataObjects['evol_7']
    del session.xyDataObjects['evol_8']
    del session.xyDataObjects['evol_9']
    del session.xyDataObjects['evol_10']
    del session.xyDataObjects['evol_11']
    del session.xyDataObjects['evol_12']
    del session.xyDataObjects['evol_13']
    del session.xyDataObjects['evol_14']
    del session.xyDataObjects['evol_15']
    del session.xyDataObjects['evol_16']
    del session.xyDataObjects['evol_17']
    del session.xyDataObjects['evol_18']
    del session.xyDataObjects['evol_19']
    del session.xyDataObjects['evol_20']
    del session.xyDataObjects['evol_21']
    del session.xyDataObjects['evol_22']
    del session.xyDataObjects['evol_23']
    del session.xyDataObjects['evol_24']
    del session.xyDataObjects['evol_25']
    del session.xyDataObjects['evol_26']
    del session.xyDataObjects['evol_27']
    del session.xyDataObjects['evol_28']
    del session.xyDataObjects['evol_29']
    del session.xyDataObjects['evol_30']
    del session.xyDataObjects['evol_31']
    del session.xyDataObjects['evol_32']
    del session.xyDataObjects['evol_33']
    del session.xyDataObjects['evol_34']
    del session.xyDataObjects['evol_35']
    del session.xyDataObjects['evol_36']
    del session.xyDataObjects['evol_37']
    del session.xyDataObjects['evol_38']
    del session.xyDataObjects['evol_39']
    del session.xyDataObjects['evol_40']
    del session.xyDataObjects['evol_41']
    del session.xyDataObjects['evol_42']
    del session.xyDataObjects['evol_43']
    del session.xyDataObjects['evol_44']
    del session.xyDataObjects['evol_45']
    del session.xyDataObjects['evol_46']
    del session.xyDataObjects['evol_47']
    del session.xyDataObjects['evol_48']
    del session.xyDataObjects['evol_49']
    del session.xyDataObjects['evol_50']
    del session.xyDataObjects['evol_51']
    del session.xyDataObjects['evol_52']
    del session.xyDataObjects['evol_53']
    del session.xyDataObjects['evol_54']
    del session.xyDataObjects['evol_55']
    del session.xyDataObjects['evol_56']
    del session.xyDataObjects['evol_57']
    del session.xyDataObjects['evol_58']
    del session.xyDataObjects['evol_59']
    del session.xyDataObjects['evol_60']
    del session.xyDataObjects['evol_61']
    del session.xyDataObjects['evol_62']
    del session.xyDataObjects['evol_63']
    del session.xyDataObjects['evol_64']
    del session.xyDataObjects['volume']
    pass
    import atxPdb;atxPdb.setFirstTrace(0)
    import atxPdb;atxPdb.debugFile(
        fileName='/home/lcharleux/Documents/Programmation/Python/Modules/compmod2/doc/tests/_workdir/RVE_abqposproc.py', 
        serverPort=48279)
    pass
    import atxPdb;atxPdb.setFirstTrace(1)
    pass
    import atxPdb;atxPdb.setFirstTrace(0)
    import atxPdb;atxPdb.debugFile(
        fileName='/home/lcharleux/Documents/Programmation/Python/Modules/compmod2/doc/tests/_workdir/RVE_abqposproc.py', 
        serverPort=48279)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=2.63398, 
        farPlane=5.41481, width=2.67619, height=1.11727, 
        viewOffsetX=-0.0769621, viewOffsetY=-0.0379817)
    pass
    import atxPdb;atxPdb.setFirstTrace(0)
    pass
    import atxPdb;atxPdb.setFirstTrace(0)
    pass
    import atxPdb;atxPdb.setFirstTrace(0)
    pass
    import atxPdb;atxPdb.setFirstTrace(1)
    import atxPdb
    atxPdb.setAtxGuiPort(-1)
    atxPdb.setFirstTrace(False)
    pass
    import atxPdb;atxPdb.setFirstTrace(1)
    import atxPdb
    atxPdb.setAtxGuiPort(56633)
    pass
    import atxPdb;atxPdb.setFirstTrace(0)
    import atxPdb;atxPdb.debugFile(
        fileName='/home/lcharleux/Documents/Programmation/Python/Modules/compmod2/doc/tests/_workdir/RVE_abqposproc.py', 
        serverPort=56633)
    pass
    import atxPdb;atxPdb.setFirstTrace(1)
    pass
    import atxPdb;atxPdb.setFirstTrace(0)
    import atxPdb;atxPdb.debugFile(
        fileName='/home/lcharleux/Documents/Programmation/Python/Modules/compmod2/doc/tests/_workdir/RVE_abqposproc.py', 
        serverPort=56633)
    pass
    import atxPdb;atxPdb.setFirstTrace(1)
    pass
    import atxPdb;atxPdb.setFirstTrace(1)
    pass
    import atxPdb;atxPdb.setFirstTrace(0)
    import atxPdb;atxPdb.debugFile(
        fileName='/home/lcharleux/Documents/Programmation/Python/Modules/compmod2/doc/tests/_workdir/RVE_abqposproc.py', 
        serverPort=56633)
    pass
    import atxPdb;atxPdb.setFirstTrace(1)
    del session.xyDataObjects['Cf1']
    del session.xyDataObjects['Cf2']
    del session.xyDataObjects['Cf3']
    del session.xyDataObjects['Rf1']
    del session.xyDataObjects['Rf2']
    del session.xyDataObjects['Rf3']
    del session.xyDataObjects['We']
    del session.xyDataObjects['Wp']
    del session.xyDataObjects['Wtot']
    del session.xyDataObjects['evol_1']
    del session.xyDataObjects['evol_2']
    del session.xyDataObjects['evol_3']
    del session.xyDataObjects['evol_4']
    del session.xyDataObjects['evol_5']
    del session.xyDataObjects['evol_6']
    del session.xyDataObjects['evol_7']
    del session.xyDataObjects['evol_8']
    del session.xyDataObjects['evol_9']
    del session.xyDataObjects['evol_10']
    del session.xyDataObjects['evol_11']
    del session.xyDataObjects['evol_12']
    del session.xyDataObjects['evol_13']
    del session.xyDataObjects['evol_14']
    del session.xyDataObjects['evol_15']
    del session.xyDataObjects['evol_16']
    del session.xyDataObjects['evol_17']
    del session.xyDataObjects['evol_18']
    del session.xyDataObjects['evol_19']
    del session.xyDataObjects['evol_20']
    del session.xyDataObjects['evol_21']
    del session.xyDataObjects['evol_22']
    del session.xyDataObjects['evol_23']
    del session.xyDataObjects['evol_24']
    del session.xyDataObjects['evol_25']
    del session.xyDataObjects['evol_26']
    del session.xyDataObjects['evol_27']
    del session.xyDataObjects['evol_28']
    del session.xyDataObjects['evol_29']
    del session.xyDataObjects['evol_30']
    del session.xyDataObjects['evol_31']
    del session.xyDataObjects['evol_32']
    del session.xyDataObjects['evol_33']
    del session.xyDataObjects['evol_34']
    del session.xyDataObjects['evol_35']
    del session.xyDataObjects['evol_36']
    del session.xyDataObjects['evol_37']
    del session.xyDataObjects['evol_38']
    del session.xyDataObjects['evol_39']
    del session.xyDataObjects['evol_40']
    del session.xyDataObjects['evol_41']
    del session.xyDataObjects['evol_42']
    del session.xyDataObjects['evol_43']
    del session.xyDataObjects['evol_44']
    del session.xyDataObjects['evol_45']
    del session.xyDataObjects['evol_46']
    del session.xyDataObjects['evol_47']
    del session.xyDataObjects['evol_48']
    del session.xyDataObjects['evol_49']
    del session.xyDataObjects['evol_50']
    del session.xyDataObjects['evol_51']
    del session.xyDataObjects['evol_52']
    del session.xyDataObjects['evol_53']
    del session.xyDataObjects['evol_54']
    del session.xyDataObjects['evol_55']
    del session.xyDataObjects['evol_56']
    del session.xyDataObjects['evol_57']
    del session.xyDataObjects['evol_58']
    del session.xyDataObjects['evol_59']
    del session.xyDataObjects['evol_60']
    del session.xyDataObjects['evol_61']
    del session.xyDataObjects['evol_62']
    del session.xyDataObjects['evol_63']
    del session.xyDataObjects['evol_64']
    del session.xyDataObjects['volume']
    odb = session.odbs['/home/lcharleux/Documents/Programmation/Python/Modules/compmod2/doc/tests/_workdir/RVE.odb']
    xy0 = session.XYDataFromHistory(name='XYData-1', odb=odb, 
        outputVariableName='Spatial displacement: U1 at Node 126 in NSET CONTROL', 
        steps=('loading', 'loading2', ), )
    c0 = session.Curve(xyData=xy0)
    xy1 = session.XYDataFromHistory(name='XYData-2', odb=odb, 
        outputVariableName='Spatial displacement: U2 at Node 126 in NSET CONTROL', 
        steps=('loading', 'loading2', ), )
    c1 = session.Curve(xyData=xy1)
    xy2 = session.XYDataFromHistory(name='XYData-3', odb=odb, 
        outputVariableName='Spatial displacement: U3 at Node 126 in NSET CONTROL', 
        steps=('loading', 'loading2', ), )
    c2 = session.Curve(xyData=xy2)
    xyp = session.XYPlot('XYPlot-1')
    chartName = xyp.charts.keys()[0]
    chart = xyp.charts[chartName]
    chart.setValues(curvesToPlot=(c0, c1, c2, ), )
    session.viewports['Viewport: 1'].setValues(displayedObject=xyp)
    pass
    import atxPdb;atxPdb.setFirstTrace(0)
    import atxPdb;atxPdb.debugFile(
        fileName='/home/lcharleux/Documents/Programmation/Python/Modules/compmod2/doc/tests/_workdir/RVE_abqposproc.py', 
        serverPort=56633)
    pass
    import atxPdb;atxPdb.setFirstTrace(1)
    pass
    import atxPdb;atxPdb.setFirstTrace(0)
    import atxPdb;atxPdb.debugFile(
        fileName='/home/lcharleux/Documents/Programmation/Python/Modules/compmod2/doc/tests/_workdir/RVE_abqposproc.py', 
        serverPort=56633)
    pass
    import atxPdb;atxPdb.setFirstTrace(1)


def Macro4():
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
    del session.xyDataObjects['Cf1']
    del session.xyDataObjects['Cf2']
    del session.xyDataObjects['Cf3']
    del session.xyDataObjects['Rf1']
    del session.xyDataObjects['Rf2']
    del session.xyDataObjects['Rf3']
    del session.xyDataObjects['U1']
    del session.xyDataObjects['U2']
    del session.xyDataObjects['U3']
    del session.xyDataObjects['We']
    del session.xyDataObjects['Wp']
    del session.xyDataObjects['Wtot']
    del session.xyDataObjects['XYData-1']
    del session.xyDataObjects['XYData-2']
    del session.xyDataObjects['XYData-3']
    del session.xyDataObjects['evol_1']
    del session.xyDataObjects['evol_2']
    del session.xyDataObjects['evol_3']
    del session.xyDataObjects['evol_4']
    del session.xyDataObjects['evol_5']
    del session.xyDataObjects['evol_6']
    del session.xyDataObjects['evol_7']
    del session.xyDataObjects['evol_8']
    del session.xyDataObjects['evol_9']
    del session.xyDataObjects['evol_10']
    del session.xyDataObjects['evol_11']
    del session.xyDataObjects['evol_12']
    del session.xyDataObjects['evol_13']
    del session.xyDataObjects['evol_14']
    del session.xyDataObjects['evol_15']
    del session.xyDataObjects['evol_16']
    del session.xyDataObjects['evol_17']
    del session.xyDataObjects['evol_18']
    del session.xyDataObjects['evol_19']
    del session.xyDataObjects['evol_20']
    del session.xyDataObjects['evol_21']
    del session.xyDataObjects['evol_22']
    del session.xyDataObjects['evol_23']
    del session.xyDataObjects['evol_24']
    del session.xyDataObjects['evol_25']
    del session.xyDataObjects['evol_26']
    del session.xyDataObjects['evol_27']
    del session.xyDataObjects['evol_28']
    del session.xyDataObjects['evol_29']
    del session.xyDataObjects['evol_30']
    del session.xyDataObjects['evol_31']
    del session.xyDataObjects['evol_32']
    del session.xyDataObjects['evol_33']
    del session.xyDataObjects['evol_34']
    del session.xyDataObjects['evol_35']
    del session.xyDataObjects['evol_36']
    del session.xyDataObjects['evol_37']
    del session.xyDataObjects['evol_38']
    del session.xyDataObjects['evol_39']
    del session.xyDataObjects['evol_40']
    del session.xyDataObjects['evol_41']
    del session.xyDataObjects['evol_42']
    del session.xyDataObjects['evol_43']
    del session.xyDataObjects['evol_44']
    del session.xyDataObjects['evol_45']
    del session.xyDataObjects['evol_46']
    del session.xyDataObjects['evol_47']
    del session.xyDataObjects['evol_48']
    del session.xyDataObjects['evol_49']
    del session.xyDataObjects['evol_50']
    del session.xyDataObjects['evol_51']
    del session.xyDataObjects['evol_52']
    del session.xyDataObjects['evol_53']
    del session.xyDataObjects['evol_54']
    del session.xyDataObjects['evol_55']
    del session.xyDataObjects['evol_56']
    del session.xyDataObjects['evol_57']
    del session.xyDataObjects['evol_58']
    del session.xyDataObjects['evol_59']
    del session.xyDataObjects['evol_60']
    del session.xyDataObjects['evol_61']
    del session.xyDataObjects['evol_62']
    del session.xyDataObjects['evol_63']
    del session.xyDataObjects['evol_64']
    del session.xyDataObjects['volume']
    o1 = session.openOdb(
        name='/home/lcharleux/Documents/Programmation/Python/Modules/compmod2/doc/tests/_workdir/RVE.odb')
    session.viewports['Viewport: 1'].setValues(displayedObject=o1)
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
    xy65 = sum([xy1, xy2, xy3, xy4, xy5, xy6, xy7, xy8, xy9, xy10, xy11, xy12, 
        xy13, xy14, xy15, xy16, xy17, xy18, xy19, xy20, xy21, xy22, xy23, xy24, 
        xy25, xy26, xy27, xy28, xy29, xy30, xy31, xy32, xy33, xy34, xy35, xy36, 
        xy37, xy38, xy39, xy40, xy41, xy42, xy43, xy44, xy45, xy46, xy47, xy48, 
        xy49, xy50, xy51, xy52, xy53, xy54, xy55, xy56, xy57, xy58, xy59, xy60, 
        xy61, xy62, xy63, xy64])
    xy65.setValues(
        sourceDescription='sum(["XYData-1", "XYData-2", "XYData-3", "XYData-4", "XYData-5", "XYData-6", "XYData-7", "XYData-8", "XYData-9", "XYData-10", "XYData-11", "XYData-12", "XYData-13", "XYData-14", "XYData-15", "XYData-16", "XYData-17", "XYData-18", "XYData-19", "XYData-20", "XYData-21", "XYData-22", "XYData-23", "XYData-24", "XYData-25", "XYData-26", "XYData-27", "XYData-28", "XYData-29", "XYData-30", "XYData-31", "XYData-32", "XYData-33", "XYData-34", "XYData-35", "XYData-36", "XYData-37", "XYData-38", "XYData-39", "XYData-40", "XYData-41", "XYData-42", "XYData-43", "XYData-44", "XYData-45", "XYData-46", "XYData-47", "XYData-48", "XYData-49", "XYData-50", "XYData-51", "XYData-52", "XYData-53", "XYData-54", "XYData-55", "XYData-56", "XYData-57", "XYData-58", "XYData-59", "XYData-60", "XYData-61", "XYData-62", "XYData-63", "XYData-64"])')
    tmpName = xy65.name
    session.xyDataObjects.changeKey(tmpName, 'volume')
    odb = session.odbs['/home/lcharleux/Documents/Programmation/Python/Modules/compmod2/doc/tests/_workdir/RVE.odb']
    session.XYDataFromHistory(name='XYData-65', odb=odb, 
        outputVariableName='External work: ALLWK for Whole Model', steps=(
        'loading', 'loading2', ), )
    session.XYDataFromHistory(name='XYData-66', odb=odb, 
        outputVariableName='Plastic dissipation: ALLPD for Whole Model', 
        steps=('loading', 'loading2', ), )
    session.XYDataFromHistory(name='XYData-67', odb=odb, 
        outputVariableName='Point loads: CF1 at Node 126 in NSET CONTROL', 
        steps=('loading', 'loading2', ), )
    session.XYDataFromHistory(name='XYData-68', odb=odb, 
        outputVariableName='Point loads: CF2 at Node 126 in NSET CONTROL', 
        steps=('loading', 'loading2', ), )
    session.XYDataFromHistory(name='XYData-69', odb=odb, 
        outputVariableName='Point loads: CF3 at Node 126 in NSET CONTROL', 
        steps=('loading', 'loading2', ), )
    session.XYDataFromHistory(name='XYData-70', odb=odb, 
        outputVariableName='Reaction force: RF1 at Node 126 in NSET CONTROL', 
        steps=('loading', 'loading2', ), )
    session.XYDataFromHistory(name='XYData-71', odb=odb, 
        outputVariableName='Reaction force: RF2 at Node 126 in NSET CONTROL', 
        steps=('loading', 'loading2', ), )
    session.XYDataFromHistory(name='XYData-72', odb=odb, 
        outputVariableName='Reaction force: RF3 at Node 126 in NSET CONTROL', 
        steps=('loading', 'loading2', ), )
    session.XYDataFromHistory(name='XYData-73', odb=odb, 
        outputVariableName='Spatial displacement: U1 at Node 126 in NSET CONTROL', 
        steps=('loading', 'loading2', ), )
    session.XYDataFromHistory(name='XYData-74', odb=odb, 
        outputVariableName='Spatial displacement: U2 at Node 126 in NSET CONTROL', 
        steps=('loading', 'loading2', ), )
    session.XYDataFromHistory(name='XYData-75', odb=odb, 
        outputVariableName='Spatial displacement: U3 at Node 126 in NSET CONTROL', 
        steps=('loading', 'loading2', ), )
    session.XYDataFromHistory(name='XYData-76', odb=odb, 
        outputVariableName='Strain energy: ALLSE for Whole Model', steps=(
        'loading', 'loading2', ), )
    x0 = session.xyDataObjects['XYData-65']
    x1 = session.xyDataObjects['XYData-66']
    x2 = session.xyDataObjects['XYData-67']
    x3 = session.xyDataObjects['XYData-68']
    x4 = session.xyDataObjects['XYData-69']
    x5 = session.xyDataObjects['XYData-70']
    x6 = session.xyDataObjects['XYData-71']
    x7 = session.xyDataObjects['XYData-72']
    x8 = session.xyDataObjects['XYData-73']
    x9 = session.xyDataObjects['XYData-74']
    x10 = session.xyDataObjects['XYData-75']
    x11 = session.xyDataObjects['XYData-76']
    x12 = session.xyDataObjects['volume']
    session.writeXYReport(fileName='abaqus.rpt', xyData=(x0, x1, x2, x3, x4, x5, 
        x6, x7, x8, x9, x10, x11, x12))


def Macro5():
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
    del session.xyDataObjects['XYData-1']
    del session.xyDataObjects['XYData-2']
    del session.xyDataObjects['XYData-3']
    del session.xyDataObjects['XYData-4']
    del session.xyDataObjects['XYData-5']
    del session.xyDataObjects['XYData-6']
    del session.xyDataObjects['XYData-7']
    del session.xyDataObjects['XYData-8']
    del session.xyDataObjects['XYData-9']
    del session.xyDataObjects['XYData-10']
    del session.xyDataObjects['XYData-11']
    del session.xyDataObjects['XYData-12']
    del session.xyDataObjects['XYData-13']
    del session.xyDataObjects['XYData-14']
    del session.xyDataObjects['XYData-15']
    del session.xyDataObjects['XYData-16']
    del session.xyDataObjects['XYData-17']
    del session.xyDataObjects['XYData-18']
    del session.xyDataObjects['XYData-19']
    del session.xyDataObjects['XYData-20']
    del session.xyDataObjects['XYData-21']
    del session.xyDataObjects['XYData-22']
    del session.xyDataObjects['XYData-23']
    del session.xyDataObjects['XYData-24']
    del session.xyDataObjects['XYData-25']
    del session.xyDataObjects['XYData-26']
    del session.xyDataObjects['XYData-27']
    del session.xyDataObjects['XYData-28']
    del session.xyDataObjects['XYData-29']
    del session.xyDataObjects['XYData-30']
    del session.xyDataObjects['XYData-31']
    del session.xyDataObjects['XYData-32']
    del session.xyDataObjects['XYData-33']
    del session.xyDataObjects['XYData-34']
    del session.xyDataObjects['XYData-35']
    del session.xyDataObjects['XYData-36']
    del session.xyDataObjects['XYData-37']
    del session.xyDataObjects['XYData-38']
    del session.xyDataObjects['XYData-39']
    del session.xyDataObjects['XYData-40']
    del session.xyDataObjects['XYData-41']
    del session.xyDataObjects['XYData-42']
    del session.xyDataObjects['XYData-43']
    del session.xyDataObjects['XYData-44']
    del session.xyDataObjects['XYData-45']
    del session.xyDataObjects['XYData-46']
    del session.xyDataObjects['XYData-47']
    del session.xyDataObjects['XYData-48']
    del session.xyDataObjects['XYData-49']
    del session.xyDataObjects['XYData-50']
    del session.xyDataObjects['XYData-51']
    del session.xyDataObjects['XYData-52']
    del session.xyDataObjects['XYData-53']
    del session.xyDataObjects['XYData-54']
    del session.xyDataObjects['XYData-55']
    del session.xyDataObjects['XYData-56']
    del session.xyDataObjects['XYData-57']
    del session.xyDataObjects['XYData-58']
    del session.xyDataObjects['XYData-59']
    del session.xyDataObjects['XYData-60']
    del session.xyDataObjects['XYData-61']
    del session.xyDataObjects['XYData-62']
    del session.xyDataObjects['XYData-63']
    del session.xyDataObjects['XYData-64']
    del session.xyDataObjects['XYData-65']
    del session.xyDataObjects['XYData-66']
    del session.xyDataObjects['XYData-67']
    del session.xyDataObjects['XYData-68']
    del session.xyDataObjects['XYData-69']
    del session.xyDataObjects['XYData-70']
    del session.xyDataObjects['XYData-71']
    del session.xyDataObjects['XYData-72']
    del session.xyDataObjects['XYData-73']
    del session.xyDataObjects['XYData-74']
    del session.xyDataObjects['XYData-75']
    del session.xyDataObjects['XYData-76']
    del session.xyDataObjects['volume']
    odb = session.odbs['/home/lcharleux/Documents/Programmation/Python/Modules/compmod2/doc/tests/_workdir/RVE.odb']
    session.XYDataFromHistory(name='XYData-1', odb=odb, 
        outputVariableName='Coordinates: COOR1 at Node 1 in NSET PINNED', 
        steps=('loading', 'loading2', ), )
    session.XYDataFromHistory(name='XYData-2', odb=odb, 
        outputVariableName='Coordinates: COOR1 at Node 126 in NSET CONTROL', 
        steps=('loading', 'loading2', ), )
    session.XYDataFromHistory(name='XYData-3', odb=odb, 
        outputVariableName='Coordinates: COOR2 at Node 1 in NSET PINNED', 
        steps=('loading', 'loading2', ), )
    session.XYDataFromHistory(name='XYData-4', odb=odb, 
        outputVariableName='Coordinates: COOR2 at Node 126 in NSET CONTROL', 
        steps=('loading', 'loading2', ), )
    session.XYDataFromHistory(name='XYData-5', odb=odb, 
        outputVariableName='Coordinates: COOR3 at Node 1 in NSET PINNED', 
        steps=('loading', 'loading2', ), )
    session.XYDataFromHistory(name='XYData-6', odb=odb, 
        outputVariableName='Coordinates: COOR3 at Node 126 in NSET CONTROL', 
        steps=('loading', 'loading2', ), )
    xyp = session.xyPlots['XYPlot-1']
    chartName = xyp.charts.keys()[0]
    chart = xyp.charts[chartName]
    xy1 = session.xyDataObjects['XYData-4']
    c1 = session.Curve(xyData=xy1)
    xy2 = session.xyDataObjects['XYData-5']
    c2 = session.Curve(xyData=xy2)
    xy3 = session.xyDataObjects['XYData-6']
    c3 = session.Curve(xyData=xy3)
    chart.setValues(curvesToPlot=(c1, c2, c3, ), )
    session.viewports['Viewport: 1'].setValues(displayedObject=xyp)
    odb = session.odbs['/home/lcharleux/Documents/Programmation/Python/Modules/compmod2/doc/tests/_workdir/RVE.odb']
    session.viewports['Viewport: 1'].setValues(displayedObject=odb)
    session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
        CONTOURS_ON_DEF, ))
    o1 = session.openOdb(
        name='/home/lcharleux/Documents/Programmation/Python/Modules/compmod2/doc/tests/_workdir/RVE.odb')
    session.viewports['Viewport: 1'].setValues(displayedObject=o1)
    session.odbs['/home/lcharleux/Documents/Programmation/Python/Modules/compmod2/doc/tests/_workdir/RVE.odb'].close(
        )
    o1 = session.openOdb(
        name='/home/lcharleux/Documents/Programmation/Python/Modules/compmod2/doc/tests/_workdir/RVE.odb')
    session.viewports['Viewport: 1'].setValues(displayedObject=o1)


