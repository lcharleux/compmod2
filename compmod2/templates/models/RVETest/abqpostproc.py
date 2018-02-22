# -*- coding: mbcs -*-
from abaqus import *
from abaqusConstants import *
import visualization, xyPlot
import displayGroupOdbToolset as dgo
import __main__
from argiope.abq import abqpostproc

# SETTINGS
simName= "${label}"


# REPORT FOLDER SETUP
try:
  os.mkdir("reports")
except:
  pass  
files2delete = os.listdir("reports/")
files2delete = [f for f in files2delete if f [-5:] in [".hrpt", ".frpt"]]
for f in files2delete:
  os.remove("reports/"+f)


# DATABASE SETUP
o1 = session.openOdb(name = simName + ".odb")
session.viewports['Viewport: 1'].setValues(displayedObject=o1)
session.xyReportOptions.setValues(numDigits=9, numberFormat=SCIENTIFIC)
odb = session.odbs[simName + ".odb"]

# SIMULATION STATUS 
job_completed = (odb.diagnosticData.jobStatus == JOB_STATUS_COMPLETED_SUCCESSFULLY)
open(simName + "_completed.txt", "wb").write(str(job_completed))

if job_completed:
  stepKeys = odb.steps.keys()
  
    
  # HISTORY OUTPUTS
  # 1: Volume
  try: 
      del session.xyDataObjects['volume']
  except:
      pass
  volume = sum([session.XYDataFromHistory(name = "evol_{0}".format(n.label),
                                          odb = odb,
                                          outputVariableName = "Element volume: EVOL at Element {0} in ELSET ALL".format(n.label), 
                                          steps = stepKeys)
                for n in  odb.rootAssembly.instances["ISAMPLE"].elementSets["ALL"].elements])
  volumeName = volume.name
  session.xyDataObjects.changeKey(volumeName, 'volume')
 
  # 2: Other history outputs
  control_node = [n.label for n in  odb.rootAssembly.instances["ISAMPLE"].nodeSets["CONTROL"].nodes][0]
  pinned_node = [n.label for n in  odb.rootAssembly.instances["ISAMPLE"].nodeSets["PINNED"].nodes][0]
  histDict = {
              "Wtot": "External work: ALLWK for Whole Model",
              "Wp"  : "Plastic dissipation: ALLPD for Whole Model",
              "We"  : "Strain energy: ALLSE for Whole Model",
              "Rf1" : "Reaction force: RF1 at Node {0} in NSET CONTROL".format(control_node),
              "Rf2" : "Reaction force: RF2 at Node {0} in NSET CONTROL".format(control_node),
              "Rf3" : "Reaction force: RF3 at Node {0} in NSET CONTROL".format(control_node),
              "Cf1" : "Point loads: CF1 at Node {0} in NSET CONTROL".format(control_node),
              "Cf2" : "Point loads: CF2 at Node {0} in NSET CONTROL".format(control_node),
              "Cf3" : "Point loads: CF3 at Node {0} in NSET CONTROL".format(control_node),
              "U1"  : "Spatial displacement: U1 at Node {0} in NSET CONTROL".format(control_node),
              "U2"  : "Spatial displacement: U2 at Node {0} in NSET CONTROL".format(control_node),
              "U3"  : "Spatial displacement: U3 at Node {0} in NSET CONTROL".format(control_node),
              "PINNED_COOR1"  : "Coordinates: COOR1 at Node {0} in NSET PINNED".format(pinned_node),
              "PINNED_COOR2"  : "Coordinates: COOR2 at Node {0} in NSET PINNED".format(pinned_node),
              "PINNED_COOR3"  : "Coordinates: COOR3 at Node {0} in NSET PINNED".format(pinned_node),
              "CONTROL_COOR1"  : "Coordinates: COOR1 at Node {0} in NSET CONTROL".format(control_node),
              "CONTROL_COOR2"  : "Coordinates: COOR2 at Node {0} in NSET CONTROL".format(control_node),
              "CONTROL_COOR3"  : "Coordinates: COOR3 at Node {0} in NSET CONTROL".format(control_node),
             }
  
  histData = [session.XYDataFromHistory(
                  name= key, 
                  odb=odb, 
                  outputVariableName= value, 
                  steps = stepKeys)
          for key, value in histDict.iteritems()] 
 
  session.writeXYReport(fileName="reports/" + simName + "_hist.hrpt", 
                        xyData = histData + [session.xyDataObjects['volume']] )

 

