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
Sketch_1 = model.addSketch(Part_1_doc, model.selection("FACE", "Box_1_1/Back"))

### Create SketchLine
SketchLine_1 = Sketch_1.addLine(10, -5, 5, -5)

### Create SketchLine
SketchLine_2 = Sketch_1.addLine(5, -5, 5, -10)

### Create SketchLine
SketchLine_3 = Sketch_1.addLine(5, -10, 10, -10)

### Create SketchLine
SketchLine_4 = Sketch_1.addLine(10, -10, 10, -5)
Sketch_1.setCoincident(SketchLine_4.endPoint(), SketchLine_1.startPoint())
Sketch_1.setCoincident(SketchLine_1.endPoint(), SketchLine_2.startPoint())
Sketch_1.setCoincident(SketchLine_2.endPoint(), SketchLine_3.startPoint())
Sketch_1.setCoincident(SketchLine_3.endPoint(), SketchLine_4.startPoint())
Sketch_1.setPerpendicular(SketchLine_1.result(), SketchLine_2.result())
Sketch_1.setPerpendicular(SketchLine_2.result(), SketchLine_3.result())
Sketch_1.setPerpendicular(SketchLine_3.result(), SketchLine_4.result())

### Create SketchProjection
SketchProjection_1 = Sketch_1.addProjection(model.selection("VERTEX", "[Box_1_1/Back][Box_1_1/Right][Box_1_1/Top]"), False)
SketchPoint_1 = SketchProjection_1.createdFeature()
Sketch_1.setCoincident(SketchLine_3.endPoint(), SketchPoint_1.result())
Sketch_1.setHorizontal(SketchLine_1.result())

### Create SketchProjection
SketchProjection_2 = Sketch_1.addProjection(model.selection("EDGE", "[Box_1_1/Back][Box_1_1/Bottom]"), False)
SketchLine_5 = SketchProjection_2.createdFeature()
Sketch_1.setDistance(SketchLine_5.result(), SketchLine_1.endPoint(), 5, True)

### Create SketchProjection
SketchProjection_3 = Sketch_1.addProjection(model.selection("EDGE", "[Box_1_1/Back][Box_1_1/Left]"), False)
SketchLine_6 = SketchProjection_3.createdFeature()
Sketch_1.setDistance(SketchLine_6.result(), SketchLine_1.endPoint(), 5, True)
model.do()

### Create ExtrusionCut
ExtrusionCut_1 = model.addExtrusionCut(Part_1_doc, [model.selection("FACE", "Sketch_1/Face-SketchLine_1r-SketchLine_2f-SketchLine_3f-SketchLine_4f")], model.selection(), 0, 10, [model.selection("SOLID", "Box_1_1")])

### Create Sketch
Sketch_2 = model.addSketch(Part_1_doc, model.selection("FACE", "ExtrusionCut_1_1/Generated_Face&Sketch_1/SketchLine_2"))

### Create SketchLine
SketchLine_7 = Sketch_2.addLine(5, -5, 6.000000000000002, -10)

### Create SketchProjection
SketchProjection_4 = Sketch_2.addProjection(model.selection("EDGE", "[ExtrusionCut_1_1/Generated_Face&Sketch_1/SketchLine_2][ExtrusionCut_1_1/Generated_Face&Sketch_1/SketchLine_1]"), False)
SketchLine_8 = SketchProjection_4.createdFeature()
Sketch_2.setCoincident(SketchLine_7.startPoint(), SketchLine_8.result())

### Create SketchProjection
SketchProjection_5 = Sketch_2.addProjection(model.selection("EDGE", "[ExtrusionCut_1_1/Modified_Face&Box_1_1/Top][ExtrusionCut_1_1/Generated_Face&Sketch_1/SketchLine_2]"), False)
SketchLine_9 = SketchProjection_5.createdFeature()
Sketch_2.setCoincident(SketchLine_7.endPoint(), SketchLine_9.result())

### Create SketchLine
SketchLine_10 = Sketch_2.addLine(6.000000000000002, -10, 4, -10)
Sketch_2.setCoincident(SketchLine_7.endPoint(), SketchLine_10.startPoint())
Sketch_2.setCoincident(SketchLine_10.endPoint(), SketchLine_9.result())

### Create SketchLine
SketchLine_11 = Sketch_2.addLine(4, -10, 5, -5)
Sketch_2.setCoincident(SketchLine_10.endPoint(), SketchLine_11.startPoint())
Sketch_2.setCoincident(SketchLine_7.startPoint(), SketchLine_11.endPoint())

### Create SketchProjection
SketchProjection_6 = Sketch_2.addProjection(model.selection("EDGE", "Sketch_1/SketchLine_2"), False)
SketchLine_12 = SketchProjection_6.createdFeature()
Sketch_2.setDistance(SketchLine_11.startPoint(), SketchLine_12.result(), 4, True)

### Create SketchProjection
SketchProjection_7 = Sketch_2.addProjection(model.selection("EDGE", "[ExtrusionCut_1_1/Generated_Face&Sketch_1/SketchLine_2][ExtrusionCut_1_1/Modified_Face&Box_1_1/Front]"), False)
SketchLine_13 = SketchProjection_7.createdFeature()
Sketch_2.setDistance(SketchLine_13.result(), SketchLine_7.endPoint(), 4, True)
Sketch_2.setMiddlePoint(SketchLine_11.endPoint(), SketchLine_8.result())
model.do()

### Create ExtrusionCut
ExtrusionCut_2 = model.addExtrusionCut(Part_1_doc, [model.selection("FACE", "Sketch_2/Face-SketchLine_11r-SketchLine_10r-SketchLine_7r")], model.selection(), 0, 5, [model.selection("SOLID", "ExtrusionCut_1_1")])

### Create Sketch
Sketch_3 = model.addSketch(Part_1_doc, model.selection("FACE", "ExtrusionCut_1_1/Modified_Face&Box_1_1/Front"))

### Create SketchLine
SketchLine_14 = Sketch_3.addLine(5, 5, 10, 5)

### Create SketchProjection
SketchProjection_8 = Sketch_3.addProjection(model.selection("VERTEX", "[ExtrusionCut_2_1/Modified_Face&Sketch_1/SketchLine_1][(ExtrusionCut_2_1/Modified_Face&Sketch_1/SketchLine_1)(ExtrusionCut_1_1/Modified_Face&Box_1_1/Front)(ExtrusionCut_2_1/Generated_Face&Sketch_2/SketchLine_7)][ExtrusionCut_1_1/Modified_Face&Box_1_1/Front]"), False)
SketchPoint_2 = SketchProjection_8.createdFeature()
Sketch_3.setCoincident(SketchLine_14.startPoint(), SketchPoint_2.result())

### Create SketchProjection
SketchProjection_9 = Sketch_3.addProjection(model.selection("VERTEX", "[ExtrusionCut_2_1/Modified_Face&Sketch_1/SketchLine_1][ExtrusionCut_1_1/Modified_Face&Box_1_1/Right][ExtrusionCut_1_1/Modified_Face&Box_1_1/Front]"), False)
SketchPoint_3 = SketchProjection_9.createdFeature()
Sketch_3.setCoincident(SketchLine_14.endPoint(), SketchPoint_3.result())

### Create SketchLine
SketchLine_15 = Sketch_3.addLine(10, 5, 10, 0)
Sketch_3.setCoincident(SketchLine_14.endPoint(), SketchLine_15.startPoint())

### Create SketchProjection
SketchProjection_10 = Sketch_3.addProjection(model.selection("VERTEX", "[ExtrusionCut_1_1/Modified_Face&Box_1_1/Right][Box_1_1/Bottom][ExtrusionCut_1_1/Modified_Face&Box_1_1/Front]"), False)
SketchPoint_4 = SketchProjection_10.createdFeature()
Sketch_3.setCoincident(SketchLine_15.endPoint(), SketchPoint_4.result())

### Create SketchLine
SketchLine_16 = Sketch_3.addLine(10, 0, 0, 0)
Sketch_3.setCoincident(SketchLine_15.endPoint(), SketchLine_16.startPoint())

### Create SketchProjection
SketchProjection_11 = Sketch_3.addProjection(model.selection("VERTEX", "[Box_1_1/Bottom][ExtrusionCut_2_1/Modified_Face&Box_1_1/Left][ExtrusionCut_1_1/Modified_Face&Box_1_1/Front]"), False)
SketchPoint_5 = SketchProjection_11.createdFeature()
Sketch_3.setCoincident(SketchLine_16.endPoint(), SketchPoint_5.result())

### Create SketchLine
SketchLine_17 = Sketch_3.addLine(0, 0, 0, 4)
Sketch_3.setCoincident(SketchLine_16.endPoint(), SketchLine_17.startPoint())

### Create SketchProjection
SketchProjection_12 = Sketch_3.addProjection(model.selection("EDGE", "[ExtrusionCut_2_1/Modified_Face&Box_1_1/Left][ExtrusionCut_1_1/Modified_Face&Box_1_1/Front]"), False)
SketchLine_18 = SketchProjection_12.createdFeature()
Sketch_3.setCoincident(SketchLine_17.endPoint(), SketchLine_18.result())

### Create SketchLine
SketchLine_19 = Sketch_3.addLine(0, 4, 5, 5)
Sketch_3.setCoincident(SketchLine_17.endPoint(), SketchLine_19.startPoint())
Sketch_3.setCoincident(SketchLine_14.startPoint(), SketchLine_19.endPoint())
Sketch_3.setDistance(SketchLine_17.endPoint(), SketchAPI_Point(SketchPoint_5).coordinates(), 4, True)
model.do()

### Create ExtrusionCut
ExtrusionCut_3 = model.addExtrusionCut(Part_1_doc, [model.selection("FACE", "Sketch_3/Face-SketchLine_19r-SketchLine_17r-SketchLine_16r-SketchLine_15r-SketchLine_14r")], model.selection(), 0, 5, [model.selection("SOLID", "ExtrusionCut_2_1")])

model.end()

###
### SHAPERSTUDY component
###

model.publishToShaperStudy()
import SHAPERSTUDY
ExtrusionCut_3_1, = SHAPERSTUDY.shape(model.featureStringId(ExtrusionCut_3))

if salome.sg.hasDesktop():
  salome.sg.updateObjBrowser()
