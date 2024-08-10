#!/usr/bin/env python

###
### This file is based on the automatically generated one by SALOME v9.12.0 with dump python functionality
###

import sys
import salome

salome.salome_init()
import salome_notebook
notebook = salome_notebook.NoteBook()

###
### SHAPER component
###

from SketchAPI import *

from salome.shaper import model

model.begin()
partSet = model.moduleDocument()

### Create Part
Part_1 = model.addPart(partSet)
Part_1_doc = Part_1.document()

### Create Box
Box_1 = model.addBox(Part_1_doc, 10, 10, 10)

### Create Sketch
Sketch_1 = model.addSketch(Part_1_doc, model.selection("FACE", "Box_1_1/Left"))

### Create SketchLine
SketchLine_1 = Sketch_1.addLine(0, 10, 10, 10)
Sketch_1.setHorizontal(SketchLine_1.result())

### Create SketchLine
SketchLine_2 = Sketch_1.addLine(10, 10, 10, 0)
Sketch_1.setCoincident(SketchLine_1.endPoint(), SketchLine_2.startPoint())
Sketch_1.setVertical(SketchLine_2.result())

### Create SketchLine
SketchLine_3 = Sketch_1.addLine(10, 0, 8, 0)
Sketch_1.setCoincident(SketchLine_2.endPoint(), SketchLine_3.startPoint())
Sketch_1.setHorizontal(SketchLine_3.result())

### Create SketchLine
SketchLine_4 = Sketch_1.addLine(8, 0, 8, 8)
Sketch_1.setCoincident(SketchLine_3.endPoint(), SketchLine_4.startPoint())
Sketch_1.setVertical(SketchLine_4.result())

### Create SketchLine
SketchLine_5 = Sketch_1.addLine(8, 8, 0, 8)
Sketch_1.setCoincident(SketchLine_4.endPoint(), SketchLine_5.startPoint())
Sketch_1.setHorizontal(SketchLine_5.result())

### Create SketchLine
SketchLine_6 = Sketch_1.addLine(0, 8, 0, 10)
Sketch_1.setCoincident(SketchLine_5.endPoint(), SketchLine_6.startPoint())
Sketch_1.setCoincident(SketchLine_1.startPoint(), SketchLine_6.endPoint())

### Create SketchProjection
SketchProjection_1 = Sketch_1.addProjection(model.selection("VERTEX", "[Box_1_1/Back][Box_1_1/Left][Box_1_1/Top]"), False)
SketchPoint_1 = SketchProjection_1.createdFeature()
Sketch_1.setCoincident(SketchLine_6.endPoint(), SketchAPI_Point(SketchPoint_1).coordinates())

### Create SketchProjection
SketchProjection_2 = Sketch_1.addProjection(model.selection("VERTEX", "[Box_1_1/Front][Box_1_1/Left][Box_1_1/Bottom]"), False)
SketchPoint_2 = SketchProjection_2.createdFeature()
Sketch_1.setCoincident(SketchLine_3.startPoint(), SketchAPI_Point(SketchPoint_2).coordinates())

### Create SketchProjection
SketchProjection_3 = Sketch_1.addProjection(model.selection("EDGE", "[Box_1_1/Back][Box_1_1/Left]"), False)
SketchLine_7 = SketchProjection_3.createdFeature()
Sketch_1.setCoincident(SketchLine_6.startPoint(), SketchLine_7.result())
Sketch_1.setDistance(SketchLine_7.result(), SketchLine_4.endPoint(), 8, True)

### Create SketchProjection
SketchProjection_4 = Sketch_1.addProjection(model.selection("EDGE", "[Box_1_1/Left][Box_1_1/Bottom]"), False)
SketchLine_8 = SketchProjection_4.createdFeature()
Sketch_1.setDistance(SketchLine_8.result(), SketchLine_4.endPoint(), 8, True)

### Create SketchPoint
SketchPoint_3 = Sketch_1.addPoint(8, 8)
Sketch_1.setCoincident(SketchPoint_3.coordinates(), SketchLine_4.result())
Sketch_1.setCoincident(SketchPoint_3.coordinates(), SketchLine_4.endPoint())
model.do()

### Create Axis
Axis_4 = model.addAxis(Part_1_doc, model.selection("VERTEX", "Sketch_1/SketchLine_5_StartVertex"), model.selection("VERTEX", "[Box_1_1/Front][Box_1_1/Right][Box_1_1/Top]"))

### Create ExtrusionCut
ExtrusionCut_1 = model.addExtrusionCut(Part_1_doc, [model.selection("FACE", "Sketch_1/Face-SketchLine_6r-SketchLine_5r-SketchLine_4r-SketchLine_3r-SketchLine_2r-SketchLine_1r")], model.selection("EDGE", "Axis_1"), 11, 0, [model.selection("SOLID", "Box_1_1")])

### Create Sketch
Sketch_2 = model.addSketch(Part_1_doc, model.selection("FACE", "ExtrusionCut_1_1/Modified_Face&Box_1_1/Back"))

### Create SketchLine
SketchLine_9 = Sketch_2.addLine(10, -10, 0, -10)
Sketch_2.setHorizontal(SketchLine_9.result())

### Create SketchLine
SketchLine_10 = Sketch_2.addLine(0, -10, 0, -8)
Sketch_2.setCoincident(SketchLine_9.endPoint(), SketchLine_10.startPoint())
Sketch_2.setVertical(SketchLine_10.result())

### Create SketchLine
SketchLine_11 = Sketch_2.addLine(0, -8, 8, -8)
Sketch_2.setCoincident(SketchLine_10.endPoint(), SketchLine_11.startPoint())
Sketch_2.setHorizontal(SketchLine_11.result())

### Create SketchLine
SketchLine_12 = Sketch_2.addLine(8, -8, 8, 0)
Sketch_2.setCoincident(SketchLine_11.endPoint(), SketchLine_12.startPoint())
Sketch_2.setVertical(SketchLine_12.result())

### Create SketchLine
SketchLine_13 = Sketch_2.addLine(8, 0, 10, 0)
Sketch_2.setCoincident(SketchLine_12.endPoint(), SketchLine_13.startPoint())
Sketch_2.setHorizontal(SketchLine_13.result())

### Create SketchLine
SketchLine_14 = Sketch_2.addLine(10, 0, 10, -10)
Sketch_2.setCoincident(SketchLine_13.endPoint(), SketchLine_14.startPoint())
Sketch_2.setCoincident(SketchLine_9.startPoint(), SketchLine_14.endPoint())
Sketch_2.setVertical(SketchLine_14.result())

### Create SketchProjection
SketchProjection_5 = Sketch_2.addProjection(model.selection("VERTEX", "[ExtrusionCut_1_1/Modified_Face&Box_1_1/Back][ExtrusionCut_1_1/Modified_Face&Box_1_1/Right][ExtrusionCut_1_1/Modified_Face&Box_1_1/Bottom]"), False)
SketchPoint_4 = SketchProjection_5.createdFeature()
Sketch_2.setCoincident(SketchLine_13.endPoint(), SketchAPI_Point(SketchPoint_4).coordinates())

### Create SketchProjection
SketchProjection_6 = Sketch_2.addProjection(model.selection("VERTEX", "Sketch_1/SketchLine_1_StartVertex"), False)
SketchPoint_5 = SketchProjection_6.createdFeature()
Sketch_2.setCoincident(SketchLine_10.startPoint(), SketchAPI_Point(SketchPoint_5).coordinates())

### Create SketchProjection
SketchProjection_7 = Sketch_2.addProjection(model.selection("EDGE", "[ExtrusionCut_1_1/Modified_Face&Box_1_1/Back][ExtrusionCut_1_1/Modified_Face&Box_1_1/Bottom]"), False)
SketchLine_15 = SketchProjection_7.createdFeature()
Sketch_2.setDistance(SketchLine_15.result(), SketchLine_10.endPoint(), 8, True)

### Create SketchProjection
SketchProjection_8 = Sketch_2.addProjection(model.selection("EDGE", "[ExtrusionCut_1_1/Modified_Face&Box_1_1/Back][ExtrusionCut_1_1/Modified_Face&Box_1_1/Left]"), False)
SketchLine_16 = SketchProjection_8.createdFeature()
Sketch_2.setDistance(SketchLine_16.result(), SketchLine_13.startPoint(), 8, True)
model.do()

### Create Axis
Axis_5 = model.addAxis(Part_1_doc, model.selection("VERTEX", "Sketch_2/SketchLine_12_StartVertex"), model.selection("VERTEX", "[ExtrusionCut_1_1/Modified_Face&Box_1_1/Right][ExtrusionCut_1_1/Generated_Face&Sketch_1/SketchLine_4][ExtrusionCut_1_1/Generated_Face&Sketch_1/SketchLine_5]"))

### Create ExtrusionCut
ExtrusionCut_2 = model.addExtrusionCut(Part_1_doc, [model.selection("FACE", "Sketch_2/Face-SketchLine_14r-SketchLine_13r-SketchLine_12r-SketchLine_11r-SketchLine_10r-SketchLine_9r")], model.selection("EDGE", "all-in-Axis_2"), 11, 0, [model.selection("SOLID", "ExtrusionCut_1_1")])

### Create Sketch
Sketch_3 = model.addSketch(Part_1_doc, model.selection("FACE", "ExtrusionCut_2_1/Modified_Face&Box_1_1/Bottom"))

### Create SketchLine
SketchLine_17 = Sketch_3.addLine(0, -10, 0, -8)
Sketch_3.setVertical(SketchLine_17.result())

### Create SketchLine
SketchLine_18 = Sketch_3.addLine(0, -8, 8, -8)
Sketch_3.setCoincident(SketchLine_17.endPoint(), SketchLine_18.startPoint())
Sketch_3.setHorizontal(SketchLine_18.result())

### Create SketchLine
SketchLine_19 = Sketch_3.addLine(8, -8, 8, 0)
Sketch_3.setCoincident(SketchLine_18.endPoint(), SketchLine_19.startPoint())
Sketch_3.setVertical(SketchLine_19.result())

### Create SketchLine
SketchLine_20 = Sketch_3.addLine(8, 0, 10, 0)
Sketch_3.setCoincident(SketchLine_19.endPoint(), SketchLine_20.startPoint())
Sketch_3.setHorizontal(SketchLine_20.result())

### Create SketchLine
SketchLine_21 = Sketch_3.addLine(10, 0, 10, -10)
Sketch_3.setCoincident(SketchLine_20.endPoint(), SketchLine_21.startPoint())
Sketch_3.setVertical(SketchLine_21.result())

### Create SketchLine
SketchLine_22 = Sketch_3.addLine(10, -10, 0, -10)
Sketch_3.setCoincident(SketchLine_21.endPoint(), SketchLine_22.startPoint())
Sketch_3.setCoincident(SketchLine_17.startPoint(), SketchLine_22.endPoint())
Sketch_3.setHorizontal(SketchLine_22.result())

### Create SketchProjection
SketchProjection_9 = Sketch_3.addProjection(model.selection("VERTEX", "Sketch_1/SketchLine_3_StartVertex"), False)
SketchPoint_6 = SketchProjection_9.createdFeature()
Sketch_3.setCoincident(SketchLine_20.endPoint(), SketchAPI_Point(SketchPoint_6).coordinates())

### Create SketchProjection
SketchProjection_10 = Sketch_3.addProjection(model.selection("VERTEX", "Sketch_2/SketchLine_13_EndVertex"), False)
SketchPoint_7 = SketchProjection_10.createdFeature()
Sketch_3.setCoincident(SketchLine_17.startPoint(), SketchAPI_Point(SketchPoint_7).coordinates())

### Create SketchProjection
SketchProjection_11 = Sketch_3.addProjection(model.selection("EDGE", "[ExtrusionCut_2_1/Modified_Face&Box_1_1/Left][ExtrusionCut_2_1/Modified_Face&Box_1_1/Bottom]"), False)
SketchLine_23 = SketchProjection_11.createdFeature()
Sketch_3.setDistance(SketchLine_23.result(), SketchLine_17.endPoint(), 8, True)

### Create SketchProjection
SketchProjection_12 = Sketch_3.addProjection(model.selection("EDGE", "[ExtrusionCut_2_1/Modified_Face&Box_1_1/Back][ExtrusionCut_2_1/Modified_Face&Box_1_1/Bottom]"), False)
SketchLine_24 = SketchProjection_12.createdFeature()
Sketch_3.setDistance(SketchLine_24.result(), SketchLine_20.startPoint(), 8, True)
model.do()

### Create Axis
Axis_6 = model.addAxis(Part_1_doc, model.selection("VERTEX", "Sketch_3/SketchLine_18_EndVertex"), model.selection("VERTEX", "[ExtrusionCut_2_1/Generated_Face&Sketch_2/SketchLine_11][ExtrusionCut_2_1/Generated_Face&Sketch_2/SketchLine_12][ExtrusionCut_1_1/Generated_Face&Sketch_1/SketchLine_4][ExtrusionCut_2_1/Modified_Face&Sketch_1/SketchLine_5]"))

### Create ExtrusionCut
ExtrusionCut_3 = model.addExtrusionCut(Part_1_doc, [model.selection("FACE", "Sketch_3/Face-SketchLine_22r-SketchLine_21r-SketchLine_20r-SketchLine_19r-SketchLine_18r-SketchLine_17r")], model.selection("EDGE", "Axis_3"), 11, 0, [model.selection("SOLID", "ExtrusionCut_2_1")])

### Create Axis
Axis_7 = model.addAxis(Part_1_doc, model.selection("VERTEX", "Sketch_3/SketchLine_22_StartVertex"), model.selection("VERTEX", "[ExtrusionCut_2_1/Generated_Face&Sketch_2/SketchLine_11][ExtrusionCut_3_1/Modified_Face&Sketch_2/SketchLine_12][ExtrusionCut_3_1/Modified_Face&Sketch_1/SketchLine_4][ExtrusionCut_2_1/Modified_Face&Sketch_1/SketchLine_5][ExtrusionCut_3_1/Generated_Face&Sketch_3/SketchLine_18][ExtrusionCut_3_1/Generated_Face&Sketch_3/SketchLine_19]"))

### Create AngularCopy
AngularCopy_1 = model.addMultiRotation(Part_1_doc, [model.selection("SOLID", "ExtrusionCut_3_1")], model.selection("EDGE", "Axis_4"), 4, keepSubResults = True)

### Create Symmetry
Symmetry_1 = model.addSymmetry(Part_1_doc, [model.selection("COMPOUND", "AngularCopy_1_1")], model.selection("VERTEX", "[AngularCopy_1_1_1/MF:Rotated&Sketch_2/SketchLine_11][AngularCopy_1_1_1/MF:Rotated&Sketch_2/SketchLine_12][AngularCopy_1_1_1/MF:Rotated&Sketch_1/SketchLine_4][AngularCopy_1_1_1/MF:Rotated&Sketch_1/SketchLine_5][AngularCopy_1_1_1/MF:Rotated&Sketch_3/SketchLine_18][AngularCopy_1_1_1/MF:Rotated&Sketch_3/SketchLine_19]"), keepOriginal = True, keepSubResults = True)

### Create Fuse
Fuse_1 = model.addFuse(Part_1_doc, [model.selection("COMPOUND", "Symmetry_1_1_1"), model.selection("COMPOUND", "Symmetry_1_1_2")], keepSubResults = True)

model.end()

###
### SHAPERSTUDY component
###

model.publishToShaperStudy()
import SHAPERSTUDY
Fuse_1_1, = SHAPERSTUDY.shape(model.featureStringId(Fuse_1))

if salome.sg.hasDesktop():
  salome.sg.updateObjBrowser()
