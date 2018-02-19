# -*- coding: mbcs -*-
#
# Abaqus/CAE Release 6.13-1 replay file
# Internal Version: 2013_05_16-01.56.28 126354
# Run by lcharleux on Mon Feb 19 18:57:52 2018
#

# from driverUtils import executeOnCaeGraphicsStartup
# executeOnCaeGraphicsStartup()
#: Executing "onCaeGraphicsStartup()" in the site directory ...
from abaqus import *
from abaqusConstants import *
session.Viewport(name='Viewport: 1', origin=(0.0, 0.0), width=161.736450195312, 
    height=116.566398620605)
session.viewports['Viewport: 1'].makeCurrent()
session.viewports['Viewport: 1'].maximize()
from caeModules import *
from driverUtils import executeOnCaeStartup
executeOnCaeStartup()
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
    referenceRepresentation=ON)
o1 = session.openOdb(
    name='/home/lcharleux/Documents/Programmation/Python/Modules/compmod2/doc/tests/workdir/cuboid.odb')
session.viewports['Viewport: 1'].setValues(displayedObject=o1)
#: Model: /home/lcharleux/Documents/Programmation/Python/Modules/compmod2/doc/tests/workdir/cuboid.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     1
#: Number of Meshes:             1
#: Number of Element Sets:       10
#: Number of Node Sets:          19
#: Number of Steps:              1
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    CONTOURS_ON_DEF, ))
session.animationController.setValues(animationType=TIME_HISTORY, viewports=(
    'Viewport: 1', ))
session.animationController.play(duration=UNLIMITED)
session.animationController.setValues(animationType=NONE)
o1 = session.openOdb(
    name='/home/lcharleux/Documents/Programmation/Python/Modules/compmod2/doc/tests/workdir/cuboid.odb')
session.viewports['Viewport: 1'].setValues(displayedObject=o1)
#: Model: /home/lcharleux/Documents/Programmation/Python/Modules/compmod2/doc/tests/workdir/cuboid.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     1
#: Number of Meshes:             1
#: Number of Element Sets:       10
#: Number of Node Sets:          19
#: Number of Steps:              1
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    CONTOURS_ON_DEF, ))
session.animationController.setValues(animationType=TIME_HISTORY, viewports=(
    'Viewport: 1', ))
session.animationController.play(duration=UNLIMITED)
session.animationController.setValues(animationType=NONE)
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='U', outputPosition=NODAL, refinement=(COMPONENT, 'U2'))
o1 = session.openOdb(
    name='/home/lcharleux/Documents/Programmation/Python/Modules/compmod2/doc/tests/workdir/cuboid.odb')
session.viewports['Viewport: 1'].setValues(displayedObject=o1)
#: Model: /home/lcharleux/Documents/Programmation/Python/Modules/compmod2/doc/tests/workdir/cuboid.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     1
#: Number of Meshes:             1
#: Number of Element Sets:       10
#: Number of Node Sets:          19
#: Number of Steps:              1
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    CONTOURS_ON_DEF, ))
session.animationController.setValues(animationType=TIME_HISTORY, viewports=(
    'Viewport: 1', ))
session.animationController.play(duration=UNLIMITED)
session.animationController.setValues(animationType=NONE)
o1 = session.openOdb(
    name='/home/lcharleux/Documents/Programmation/Python/Modules/compmod2/doc/tests/workdir/cuboid.odb')
session.viewports['Viewport: 1'].setValues(displayedObject=o1)
#: Model: /home/lcharleux/Documents/Programmation/Python/Modules/compmod2/doc/tests/workdir/cuboid.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     1
#: Number of Meshes:             1
#: Number of Element Sets:       127
#: Number of Node Sets:          19
#: Number of Steps:              1
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    CONTOURS_ON_DEF, ))
session.viewports['Viewport: 1'].view.setValues(nearPlane=2.28416, 
    farPlane=7.24462, width=4.81086, height=2.00847, viewOffsetX=-0.437666, 
    viewOffsetY=0.255185)
session.animationController.setValues(animationType=TIME_HISTORY, viewports=(
    'Viewport: 1', ))
session.animationController.play(duration=UNLIMITED)
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='LE', outputPosition=INTEGRATION_POINT, refinement=(
    COMPONENT, 'LE22'))
session.animationController.setValues(animationType=NONE)
#: Warning: The output database '/home/lcharleux/Documents/Programmation/Python/Modules/compmod2/doc/tests/workdir/cuboid.odb' disk file has changed.
#: 
#: The current plot operation has been canceled, re-open the file to view the results
o1 = session.openOdb(
    name='/home/lcharleux/Documents/Programmation/Python/Modules/compmod2/doc/tests/workdir/cuboid.odb')
session.viewports['Viewport: 1'].setValues(displayedObject=o1)
#: Model: /home/lcharleux/Documents/Programmation/Python/Modules/compmod2/doc/tests/workdir/cuboid.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     1
#: Number of Meshes:             1
#: Number of Element Sets:       127
#: Number of Node Sets:          19
#: Number of Steps:              1
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    CONTOURS_ON_DEF, ))
session.viewports['Viewport: 1'].view.setValues(nearPlane=23.2244, 
    farPlane=36.6412, width=3.71355, height=1.55036, viewOffsetX=0.2349, 
    viewOffsetY=4.51081)
session.animationController.setValues(animationType=TIME_HISTORY, viewports=(
    'Viewport: 1', ))
session.animationController.play(duration=UNLIMITED)
session.viewports['Viewport: 1'].view.fitView()
session.animationController.setValues(animationType=NONE)
o1 = session.openOdb(
    name='/home/lcharleux/Documents/Programmation/Python/Modules/compmod2/doc/tests/workdir/cuboid.odb')
session.viewports['Viewport: 1'].setValues(displayedObject=o1)
#: Model: /home/lcharleux/Documents/Programmation/Python/Modules/compmod2/doc/tests/workdir/cuboid.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     1
#: Number of Meshes:             1
#: Number of Element Sets:       127
#: Number of Node Sets:          20
#: Number of Steps:              1
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    CONTOURS_ON_DEF, ))
session.animationController.setValues(animationType=TIME_HISTORY, viewports=(
    'Viewport: 1', ))
session.animationController.play(duration=UNLIMITED)
session.animationController.setValues(animationType=NONE)
o1 = session.openOdb(
    name='/home/lcharleux/Documents/Programmation/Python/Modules/compmod2/doc/tests/workdir/cuboid.odb')
session.viewports['Viewport: 1'].setValues(displayedObject=o1)
#: Model: /home/lcharleux/Documents/Programmation/Python/Modules/compmod2/doc/tests/workdir/cuboid.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     1
#: Number of Meshes:             1
#: Number of Element Sets:       127
#: Number of Node Sets:          20
#: Number of Steps:              1
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    CONTOURS_ON_DEF, ))
session.animationController.setValues(animationType=TIME_HISTORY, viewports=(
    'Viewport: 1', ))
session.animationController.play(duration=UNLIMITED)
session.animationController.setValues(animationType=NONE)
o1 = session.openOdb(
    name='/home/lcharleux/Documents/Programmation/Python/Modules/compmod2/doc/tests/workdir/cuboid.odb')
session.viewports['Viewport: 1'].setValues(displayedObject=o1)
#: Model: /home/lcharleux/Documents/Programmation/Python/Modules/compmod2/doc/tests/workdir/cuboid.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     1
#: Number of Meshes:             1
#: Number of Element Sets:       1002
#: Number of Node Sets:          20
#: Number of Steps:              1
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    CONTOURS_ON_DEF, ))
session.animationController.setValues(animationType=TIME_HISTORY, viewports=(
    'Viewport: 1', ))
session.animationController.play(duration=UNLIMITED)
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='LE', outputPosition=INTEGRATION_POINT, refinement=(
    INVARIANT, 'Max. Principal'))
session.animationController.setValues(animationType=NONE)
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=100)
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=100)
session.viewports['Viewport: 1'].view.setValues(nearPlane=2.64092, 
    farPlane=5.42954, width=2.96844, height=1.23928, cameraPosition=(4.04519, 
    1.94855, 2.00309), cameraUpVector=(-0.505893, 0.735304, -0.451), 
    cameraTarget=(0.569864, 0.506305, 0.575577))
session.viewports['Viewport: 1'].view.setValues(nearPlane=2.57828, 
    farPlane=5.45332, width=2.89803, height=1.20989, cameraPosition=(2.31641, 
    2.82886, 3.36236), cameraUpVector=(-0.569996, 0.566228, -0.595391), 
    cameraTarget=(0.565223, 0.508668, 0.579226))
session.viewports['Viewport: 1'].view.setValues(nearPlane=2.62628, 
    farPlane=5.3548, width=2.95199, height=1.23241, cameraPosition=(3.81098, 
    1.8438, -1.37612), cameraUpVector=(-0.615823, 0.76607, 0.184116), 
    cameraTarget=(0.562025, 0.510776, 0.589364))
session.viewports['Viewport: 1'].view.setValues(nearPlane=2.62886, 
    farPlane=5.41322, width=2.95489, height=1.23363, cameraPosition=(3.66772, 
    2.07661, 2.58063), cameraUpVector=(-0.500046, 0.732054, -0.462657), 
    cameraTarget=(0.563241, 0.5088, 0.555789))
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='U', outputPosition=NODAL, refinement=(COMPONENT, 'U2'))
session.viewports['Viewport: 1'].view.setValues(nearPlane=2.81642, 
    farPlane=5.28297, width=3.16573, height=1.32165, cameraPosition=(4.22623, 
    0.862747, 2.1841), cameraUpVector=(-0.284189, 0.882082, -0.375723), 
    cameraTarget=(0.562774, 0.509814, 0.55612))
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='U', outputPosition=NODAL, refinement=(COMPONENT, 'U3'))
session.viewports['Viewport: 1'].view.setValues(nearPlane=2.56386, 
    farPlane=5.46967, width=2.88186, height=1.20313, cameraPosition=(2.87971, 
    2.39349, 3.26029), cameraUpVector=(-0.414842, 0.675823, -0.609237), 
    cameraTarget=(0.554364, 0.519374, 0.562842))
o1 = session.openOdb(
    name='/home/lcharleux/Documents/Programmation/Python/Modules/compmod2/doc/tests/workdir/cuboid.odb')
session.viewports['Viewport: 1'].setValues(displayedObject=o1)
#: Model: /home/lcharleux/Documents/Programmation/Python/Modules/compmod2/doc/tests/workdir/cuboid.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     1
#: Number of Meshes:             1
#: Number of Element Sets:       1002
#: Number of Node Sets:          20
#: Number of Steps:              1
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    DEFORMED, ))
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    CONTOURS_ON_DEF, ))
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='U', outputPosition=NODAL, refinement=(COMPONENT, 'U2'))
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='U', outputPosition=NODAL, refinement=(COMPONENT, 'U3'))
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='PEEQ', outputPosition=INTEGRATION_POINT)
