lx = 1.;
ly = 1.;
lz = 1.;
lc = 1.;
Nx = 16 + 1;
Ny = 64 + 1;
Nz = 32 + 1;


Point(1) = {0.,  0., 0., lc};
Point(2) = {lx,  0., 0., lc};
Point(3) = {lx,  ly, 0., lc};
Point(4) = {0.,  ly, 0., lc};

Line(1)  = {1,2};
Line(2)  = {2,3};
Line(3)  = {3,4};
Line(4)  = {4,1};

Transfinite Line {1,3} = Nx;
Transfinite Line {2,4} = Ny;

Line Loop(1) = {1,2,3,4};
Plane Surface(1) = {1};
Transfinite Surface {1};
Recombine Surface {1};

extruded[] = Extrude {0,0,lz} { Surface{1}; Layers{Nz}; Recombine;};
Physical Surface("BACK") = {extruded[1]};
Physical Surface("FRONT") = {extruded[0]};
Physical Volume("BULK") = {1};
