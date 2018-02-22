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

class RVETest(argiope.models.Model, argiope.utils.Container):
  """
  A general purpose class for RVE testing.
  """
  def __init__(self, boundary_conditions = "periodic",**kwargs):
    self.boundary_conditions = boundary_conditions
    argiope.models.Model.__init__(self, **kwargs)
   
  def write_input(self):
    """
    Writes the input file in the chosen format.
    """
    main_template = open(MODPATH + "/templates/models/RVETest/main_input.inp").read()
    step_template = open(MODPATH + "/templates/models/RVETest/step.inp").read()
    """
    E = 1.
    nu = .3
    dist = compmod2.distributions.Weibull(k = 1., l = 1.e-2)
    xt, x = dist.discretize(Ne, xmax = 1.)
    np.random.shuffle(x)
    materials = [argiope.materials.ElasticPerfectlyPlastic(
                                     label = "mat{0}".format(i+1), 
                                     young_modulus = E, 
                                     poisson_ratio = nu, 
                                     yield_stress = x[i] * E) 
                                     for i in range(Ne)]
    
    sample = compmod2.models.RVE(shape = shape)
    """
    # MESH
    sample = self.parts["sample"]
    if sample.mesh == None: sample.make_mesh()
    m = sample.mesh
    n = m.nodes
    c = n.coords
    xm, ym, zm = c.max(axis = 0)
    shape = np.array(sample.shape)
    Ne = shape.prod()
    # MATERIALS & ELEMENTS
    materials = self.materials
    #m.elements.materials = ["mat{0}".format(i) for i in m.elements.index]
    #m.elements.loc[:, ("type", "solver", "") ] = "C3D8"
    
    
    # GENERAL PURPOSE ORDERED SETS
    n[("sets", "left")]      = (c.x == 0.) 
    n[("sets", "right")]     = (c.x == xm) 
    n[("sets", "bottom")]    = (c.y == 0.) 
    n[("sets", "top")]       = (c.y == ym) 
    n[("sets", "back")]      = (c.z == 0.) 
    n[("sets", "front")]     = (c.z == zm) 
    n[("sets", "pinned")]    = n.sets.left & n.sets.bottom & n.sets.back  
    
    control_node = n.index.max() + 1
    m.nodes.loc[control_node, [("coords")]] = xm, ym, zm
    m.nodes.loc[control_node,"sets"] = False
    m.nodes[("sets", "control")] = False
    m.nodes.loc[control_node, ("sets", "control")] = True
    
    
    
    # BOUNDARY CONDITIONS
    bc_type = "periodic" # TEST
    if bc_type == "periodic":
        # FACE TO FACE PAIR EQUATIONS
        faces = {"uleft"   : n.coords[n.sets.left  ].sort_values(["y", "z"]),
                 "uright"  : n.coords[n.sets.right ].sort_values(["y", "z"]),    
                 "ubottom" : n.coords[n.sets.bottom 
                         & (n.sets.right == False)  ].sort_values(["x", "z"]),
                 "utop"    : n.coords[n.sets.top   
                         & (n.sets.right == False)  ].sort_values(["x", "z"]),
                 "uback"   : n.coords[n.sets.back  
                         & (n.sets.right == False)
                         & (n.sets.top == False)].sort_values(["x", "y"]),                   
                 "ufront"  : n.coords[n.sets.front 
                         & (n.sets.right == False)
                         & (n.sets.top == False)].sort_values(["x", "y"])}
        bc = "\n".join([argiope.utils._unsorted_set(v, k) 
                        for k, v in faces.items()]) + "\n"
    
        bc += argiope.utils._equation(nodes = ["uright", "uleft"], 
                                      dofs = [2,2], 
                                      coefficients = [1., -1.]) + "\n"
        bc += argiope.utils._equation(nodes = ["uright", "uleft"], 
                                      dofs = [3,3], 
                                      coefficients = [1., -1.]) + "\n"
        bc += argiope.utils._equation(nodes = ["utop", "ubottom"], 
                                      dofs = [1,1], 
                                      coefficients = [1., -1.]) + "\n"
        bc += argiope.utils._equation(nodes = ["utop", "ubottom"], 
                                      dofs = [3,3], 
                                      coefficients = [1., -1.]) + "\n"
        bc += argiope.utils._equation(nodes = ["ufront", "uback"], 
                                      dofs = [1,1], 
                                      coefficients = [1., -1.]) + "\n"
        bc += argiope.utils._equation(nodes = ["ufront", "uback"], 
                                      dofs = [2,2], 
                                      coefficients = [1., -1.]) + "\n"
        # NORMAL DISPLACEMENT
        bc += argiope.utils._equation(nodes = ["uright", "uleft", "control"], 
                                      dofs = [1,1,1], 
                                      coefficients = [1., -1., -1.],
                                      comment = "LEFT-RIGHT NORMAL PAIRS") + "\n"
        bc += argiope.utils._equation(nodes = ["utop", "ubottom", "control"], 
                                      dofs = [2,2,2], 
                                      coefficients = [1., -1., -1.],
                                      comment = "BOTTOM-TOP NORMAL PAIRS") + "\n"
        bc += argiope.utils._equation(nodes = ["ufront", "uback", "control"], 
                                      dofs = [3,3,3], 
                                      coefficients = [1., -1., -1.],
                                      comment = "BACK-FRONT NORMAL PAIRS") + "\n"

    
    
    out = Template(main_template).substitute(
                MESH = sample.mesh.write_inp(),
                MATERIALS = "\n".join([mat.write_inp() for mat in materials]),
                BOUNDARY_CONDITIONS = bc.strip("\n"),)
    # STEPS
    steps = self.steps
    out += "\n".join([s.write_input() for s in steps])
    
    # OUTPUT
    path = "{0}/{1}.inp".format(self.workdir, self.label)
    open(path, "w").write(out)
                                   
                                   
    
  def write_postproc(self):
    """
    Writes the prosproc scripts for the chosen solver.
    """
    if self.solver == "abaqus":
      pattern = Template(
          open(MODPATH + "/templates/models/RVETest/abqpostproc.py").read())
      pattern = pattern.substitute(label = self.label)
      path = "{0}/{1}_abqpp.py".format(self.workdir, self.label)
      open(path, "w").write(pattern)
  
  def postproc(self):
    """
    Runs the whole post proc.
    """
    self.write_postproc()
    self.run_postproc()
    #HISTORY OUTPUTS
    hist_path = self.workdir + "/reports/{0}_hist.hrpt".format(self.label)
    if os.path.isfile(hist_path):
      data = argiope.abq.pypostproc.read_history_report(
            hist_path, steps = self.steps, x_name = "t") 
      data2 = pd.DataFrame()
      data2[("time", "t")] = data.t
      data2[("step", "s")] = data.step
      # CF
      data2[("forces", "CF1")] = data.Cf1
      data2[("forces", "CF2")] = data.Cf2
      data2[("forces", "CF3")] = data.Cf3
      # RF
      data2[("forces", "RF1")] = data.Rf1
      data2[("forces", "RF2")] = data.Rf2
      data2[("forces", "RF3")] = data.Rf3
      # U
      data2[("disp", "U1")] = data.U1
      data2[("disp", "U2")] = data.U2
      data2[("disp", "U3")] = data.U3
      # Volume
      data2[("volume", "V")] = data.volume
      # Dimensions
      data2[("dimensions", "L1")] = data.CONTROL_COOR1 - data.PINNED_COOR1
      data2[("dimensions", "L2")] = data.CONTROL_COOR2 - data.PINNED_COOR2
      data2[("dimensions", "L3")] = data.CONTROL_COOR3 - data.PINNED_COOR3
      # Multi indexing
      data2.columns = pd.MultiIndex.from_tuples(data2.columns)
      # Cross sections
      data2[("areas", "A1")] = data2.volume.V / data2.dimensions.L1
      data2[("areas", "A2")] = data2.volume.V / data2.dimensions.L2
      data2[("areas", "A3")] = data2.volume.V / data2.dimensions.L3
      # Forces
      data2[("forces", "F1")] = data2.forces.CF1 + data2.forces.RF1
      data2[("forces", "F2")] = data2.forces.CF2 + data2.forces.RF2
      data2[("forces", "F3")] = data2.forces.CF3 + data2.forces.RF3
      # Stresses
      data2[("stress", "S11")] = data2.forces.F1 / data2.areas.A1
      data2[("stress", "S22")] = data2.forces.F2 / data2.areas.A2
      data2[("stress", "S33")] = data2.forces.F3 / data2.areas.A3
      # Strains
      L1 = data2.dimensions.L1.values[0]
      L2 = data2.dimensions.L2.values[0]
      L3 = data2.dimensions.L3.values[0]
      data2[("strains", "E11")] = data2.disp.U1 / L1
      data2[("strains", "E22")] = data2.disp.U2 / L2
      data2[("strains", "E33")] = data2.disp.U3 / L3
      data2[("strains", "LE11")]  = np.log(1. + data2.strains.E11)
      data2[("strains", "LE22")]  = np.log(1. + data2.strains.E22)
      data2[("strains", "LE33")]  = np.log(1. + data2.strains.E33)
      # Last modifications
      data2.index.name = "frame"
      self.data["history"] = data2.sort_index(axis = 1)
     
         
################################################################################
# PARTS
################################################################################  

class RVESample(argiope.models.Part):
    """
    A RVE class.
    """
    def __init__(self, shape = (1, 1, 1), dim = (1., 1., 1.), **kwargs):
        self.dim = dim
        self.shape = shape
        super().__init__(**kwargs)

    def make_mesh(self):
        """
        Makes the mesh.
        """    
        mesh = argiope.mesh.structured_mesh(dim = self.dim, 
                                            shape = self.shape)
        if self.element_map != None:
            mesh = self.element_map(mesh)
        if self.material_map != None:
            mesh = self.material_map(mesh)
        self.mesh = mesh
            

################################################################################
# STEPS
################################################################################  
class RVEStep:
    """
    RVE step.
    """
    def __init__(self, 
                 cx = ("free", 0.),
                 cy = ("free", 0.),
                 cz = ("free", 0.),
                 name = "STEP", 
                 duration = 1., 
                 nframes = 100,
                 min_frame_duration = 1.e-8,
                 field_output_frequency = 99999,
                 solver = "abaqus"):
    
        self.cx = cx
        self.cy = cy
        self.cz = cz
        self.name = name  
        self.duration = duration
        self.nframes = nframes
        self.min_frame_duration = min_frame_duration
        self.field_output_frequency = field_output_frequency
        self.solver = solver

    def write_input(self):
        """
        Return the inputs.
        """
        if self.solver == "abaqus":
            disp_control, force_control = "", ""
            template = Template(open(MODPATH + 
                       "/templates/models/RVETest/step.inp").read())
            controls = self.cx, self.cy, self.cz
            for i in range(3):
                control = controls[i]
                if control[0] == None: 
                    pass
                elif control[0] == "disp":
                    if disp_control == None: disp_control = "\n"
                    disp_control += "\nISAMPLE.CONTROL, {0}, {0}, {1}".format(
                                    i+1, control[1])
                elif control[0] == "force":
                    if force_control == "": force_control = "\n"
                    force_control += "*CLOAD\nISAMPLE.CONTROL, {0}, {1}".format(
                                     i+1, control[1])
            out = {"DISP_CONTROL": disp_control,
                   "FORCE_CONTROL": force_control,
                   "NAME": self.name,
                   "DURATION": self.duration,
                   "FRAME_DURATION": float(self.duration) / self.nframes,
                   "MIN_FRAME_DURATION": self.min_frame_duration,
                   "FIELD_OUTPUT_FREQUENCY": self.field_output_frequency,} 
            return template.substitute(out)
    
    
    
    
    
    
    

