# Nightmare of polycubes

(Very) challenging 3D shapes for polycube-based hex-meshing

## Files

All models were designed with the [Shaper](https://www.salome-platform.org/?page_id=327) module of the open-source [SALOME platform](https://www.salome-platform.org/). For each of them, you can download the study (.hdf) and the exported Python script, STEP, B-Rep and STL files.

<details> <summary>How to load a .hdf study file in SALOME?</summary>

In the menu bar, click on "File" > "Open", select the .hdf file, then open the Shaper module.

</details>

<details> <summary>How to load a .py Shaper script in SALOME?</summary>

First, open the Shaper module, then in the menu bar click on "File" > "Load Script" and select the .py file.

</details>

For STL files I used the default relative deflection of 0.0001.

Name | Thumbnail | Files | Comments
-----|-----------|-------|---------
`cuboid_screw_thread` | <img src="cuboid_screw_thread/thumbnail.png" width="300"/> | [.hdf](cuboid_screw_thread/SALOME_Study.hdf) <br/> [.py](cuboid_screw_thread/SALOME_Shaper.py) <br/> [.step](cuboid_screw_thread/CAD.step) <br/> [.brep](cuboid_screw_thread/CAD.brep) <br/> [.stl](cuboid_screw_thread/CAD.stl) | Introduced in [^2] and mentioned in appendices of [^3]. <br/> Labeling-based approaches [^1][^3] will collapse the two parts of the slope, constrained to the same top and bottom planes.
`cuboid_torus_with_step` | <img src="cuboid_torus_with_step/thumbnail.png" width="300"/> | [.hdf](cuboid_torus_with_step/SALOME_Study.hdf) <br/> [.py](cuboid_torus_with_step/SALOME_Shaper.py) <br/> [.step](cuboid_torus_with_step/CAD.step) <br/> [.brep](cuboid_torus_with_step/CAD.brep) <br/> [.stl](cuboid_torus_with_step/CAD.stl) | Introduced in [^2] I believe. <br/> Here too labeling-based approaches [^1][^3] will not detect any invalidity and crush the step into the z-axis plane.
`in-volume_twist` | <div align="center"><img src="in-volume_twist/thumbnail.png" width="300"/><br/><a href="https://3dviewer.net/#model=https://github.com/LIHPC-Computational-Geometry/nightmare_of_polycubes/blob/main/in-volume_twist/labeled_mesh.glb">3D viewer ↗</a></div> | [.hdf](in-volume_twist/SALOME_Study.hdf) <br/> [.py](in-volume_twist/SALOME_Shaper.py) <br/> [.step](in-volume_twist/CAD.step) <br/> [.brep](in-volume_twist/CAD.brep) <br/> [.stl](in-volume_twist/CAD.stl) <br/> [.obj](in-volume_twist/triangle_mesh.obj) | Introduced in [^4] <br/> Labeling-based approaches [^1][^3] will not detect the twist. The slits prevent hex-mesh extraction algorithms from un-twisting the through-hole and pushing all distorsion towards the left and right faces.
`in-volume_knot` | <div align="center"><img src="in-volume_knot/thumbnail.png" width="300"/><br/><a href="https://3dviewer.net/#model=https://github.com/LIHPC-Computational-Geometry/nightmare_of_polycubes/blob/main/in-volume_knot/labeled_mesh.glb">3D viewer ↗</a></div> | [.hdf](in-volume_knot/SALOME_Study.hdf) <br/> [.py](in-volume_knot/SALOME_Shaper.py) <br/> [.step](in-volume_knot/CAD.step) <br/> [.brep](in-volume_knot/CAD.brep) <br/> [.stl](in-volume_knot/CAD.stl) <br/> [.obj](in-volume_knot/triangle_mesh.obj) | Similar to the previous model, but the through-hole is twisting around itself.
`pipe_helix` | <img src="pipe_helix/thumbnail.png" width="300"/> | [.hdf](pipe_helix/SALOME_Study.hdf) <br/> [.py](pipe_helix/SALOME_Shaper.py) <br/> [.step](pipe_helix/CAD.step) <br/> [.brep](pipe_helix/CAD.brep) <br/> [.stl](pipe_helix/CAD.stl) | 
`pipe_helix_7` | <img src="pipe_helix_7/thumbnail.png" width="300"/> | [.hdf](pipe_helix_7/SALOME_Study.hdf) <br/> [.py](pipe_helix_7/SALOME_Shaper.py) <br/> [.step](pipe_helix_7/CAD.step) <br/> [.brep](pipe_helix_7/CAD.brep) <br/> [.stl](pipe_helix_7/CAD.stl) | 

> [!NOTE]
> To generate a mesh, you can use the [SMESH](https://www.salome-platform.org/?page_id=374) module of SALOME, which bundles open-source ([NETGEN](https://sourceforge.net/projects/netgen-mesher/), [GMSH](http://gmsh.info/)) and commercial ([3D Precise Mesh](https://www.spatial.com/products/3d-precise-mesh)) meshing tools.

Thanks to François Protais for the ideas and to Christophe Bourcier for the help.

## License

[CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/)

How to give attribution:
> "[Nightmare of polycubes](https://github.com/LIHPC-Computational-Geometry/nightmare_of_polycubes)" by Sébastien Mestrallet and Christophe Bourcier, licensed under [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/)

[^1]: Marco Livesu, Nicholas Vining, Alla Sheffer, James Gregson, Riccardo Scateni, "PolyCut: Monotone Graph-Cuts for PolyCube Base-Complex Construction", _Transactions on Graphics_ (Proc. SIGGRAPH ASIA 2013), 2013, [DOI](https://dl.acm.org/doi/10.1145/2508363.2508388), [project page](http://www.cs.ubc.ca/labs/imager/tr/2013/polycut/)

[^2]: Dmitry Sokolov, Nicolas Ray, "Fixing normal constraints for generation of polycubes", research report, LORIA, 2015, [HAL](https://inria.hal.science/hal-01211408)

[^3]: Corentin Dumery, François Protais, Sébastien Mestrallet, Christophe Bourcier, Franck Ledoux, "Evocube: a Genetic Labeling Framework for Polycube-Maps", _Computer Graphics Forum_, 2022, [DOI](http://doi.org/10.1111/cgf.14649), [HAL](https://hal-cea.archives-ouvertes.fr/hal-03657779v2), [project page](https://corentindumery.github.io/projects/evocube.html)

[^4]: Sébastien Mestrallet, François Protais, Christophe Bourcier, Franck Ledoux, "Limits and prospects of polycube labelings", _SIAM International Meshing Roundtable_ Workshop, March 2023, [HAL](https://cea.hal.science/cea-04169841)
