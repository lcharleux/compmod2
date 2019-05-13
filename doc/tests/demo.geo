lx = 1.;
ly = 1.;
lz = 1.;
lc = 1.;

Nx = 32 + 1;
Ny = 32 + 1;
Nz = 32 + 1;

qx = 1.1;
qy = 1.1;

Point(1) = {0.,  0., 0., lc};
Point(2) = {lx,  0., 0., lc};
Point(3) = {lx,  ly, 0., lc};
Point(4) = {0.,  ly, 0., lc};

Line(1)  = {1,2};
Line(2)  = {2,3};
Line(3)  = {3,4};
Line(4)  = {4,1};

Transfinite Line {1,3} = Nx Using Progression qx;
Transfinite Line {-2,-4} = Ny Using Progression qy;;

Line Loop(1) = {1,2,3,4};
Plane Surface(1) = {1};
Transfinite Surface {1};
Recombine Surface {1};
Physical Surface("CORE") = {1};
