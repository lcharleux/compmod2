import numpy as np
import pandas as pd
import argiope
import os, subprocess, inspect
from string import Template

# PATH TO MODULE
import compmod2
MODPATH = os.path.dirname(inspect.getfile(compmod2))


################################################################################
# MODEL DEFINITION
################################################################################

class Cuboid(argiope.models.Model, argiope.utils.Container):
  """
  A cuboid that can be loaded in any direction with various boundary conditions.
  """
  def __init__(self, dim, shape, 
                     boundary_conditions = "pseudo homogeneous",
                     **kwargs):
    self.dim = dim
    self.shape = shape
    self.boundary_conditions = boundary_conditions
    argiope.models.Model.__init__(self, **kwargs)
                
  
    
  def write_input(self):
    """
    Writes the input file in the chosen format.
    """
    hardness.models.indentation_2D_input(sample_mesh = self.parts["sample"],
                                   indenter_mesh = self.parts["indenter"],
                                   steps = self.steps,
                                   materials = self.materials,
                                   solver = self.solver,
                                   path = "{0}/{1}.inp".format(self.workdir,
                                                               self.label))
                                   
                                   
    
  def write_postproc(self):
    """
    Writes the prosproc scripts for the chosen solver.
    """
    if self.solver == "abaqus":
      hardness.postproc.indentation_abqpostproc(
          path = "{0}/{1}_abqpp.py".format(
              self.workdir,
              self.label),
          label = self.label,    
          solver= self.solver)
  
  def postproc(self):
     """
     Runs the whole post proc.
     """
     self.write_postproc()
     self.run_postproc()
     #HISTORY OUTPUTS
     hist_path = self.workdir + "/reports/{0}_hist.hrpt".format(self.label)
     if os.path.isfile(hist_path):
       hist = argiope.abq.pypostproc.read_history_report(
            hist_path, steps = self.steps, x_name = "t") 
       hist["F"] = hist.CF + hist.RF
       self.data["history"] = hist
     # FIELD OUTPUTS
     files = os.listdir(self.workdir + "reports/")
     files = [f for f in files if f.endswith(".frpt")]
     files.sort()
     for path in files:
       field = argiope.abq.pypostproc.read_field_report(
                           self.workdir + "reports/" + path)
       if field.part == "I_SAMPLE":
         self.parts["sample"].mesh.fields.append(field)
       if field.part == "I_INDENTER":
         self.parts["indenter"].mesh.fields.append(field)
         
################################################################################
# PARTS
################################################################################  

class CuboidSample(argiope.models.Part):
  """
  A cuboid test sample.
  """
  def __init__(self, dim = (10, 10, 10), shape = (1., 1., 1.)):
    self.dim = dim
    self.shape = shape
    
  def make_mesh(self):
    """
    Makes the mesh
    """    
    mesh = argiope.mesh.structured_mesh(dim = self.dim, shape = self.shape)
    
    
    
    
    
    
    
    
    
    

