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

from salome.shaper import model

model.begin()
partSet = model.moduleDocument()

### Create Part
Part_1 = model.addPart(partSet)
Part_1_doc = Part_1.document()

### Create Box
Box_1 = model.addBox(Part_1_doc, 10, 10, 10)

### Create Sketch
Sketch_1 = model.addSketch(Part_1_doc, model.selection("FACE", "Box_1_1/Top"))

### Create SketchPoint
SketchPoint_1 = Sketch_1.addPoint(0, 5)
SketchPoint_1.setAuxiliary(True)

### Create SketchProjection
SketchProjection_1 = Sketch_1.addProjection(model.selection("EDGE", "[Box_1_1/Back][Box_1_1/Top]"), False)
SketchLine_1 = SketchProjection_1.createdFeature()
Sketch_1.setCoincident(SketchPoint_1.coordinates(), SketchLine_1.result())

### Create SketchPoint
SketchPoint_2 = Sketch_1.addPoint(10, 5)

### Create SketchProjection
SketchProjection_2 = Sketch_1.addProjection(model.selection("EDGE", "[Box_1_1/Front][Box_1_1/Top]"), False)
SketchLine_2 = SketchProjection_2.createdFeature()
Sketch_1.setCoincident(SketchPoint_2.coordinates(), SketchLine_2.result())
Sketch_1.setMiddlePoint(SketchPoint_1.coordinates(), SketchLine_1.result())
Sketch_1.setMiddlePoint(SketchPoint_2.coordinates(), SketchLine_2.result())

### Create SketchLine
SketchLine_3 = Sketch_1.addLine(0, 5, 10, 5)
SketchLine_3.setAuxiliary(True)
Sketch_1.setCoincident(SketchPoint_1.coordinates(), SketchLine_3.startPoint())
Sketch_1.setCoincident(SketchPoint_2.coordinates(), SketchLine_3.endPoint())

### Create SketchLine
SketchLine_4 = Sketch_1.addLine(4, 10, 5, 5)

### Create SketchProjection
SketchProjection_3 = Sketch_1.addProjection(model.selection("EDGE", "[Box_1_1/Right][Box_1_1/Top]"), False)
SketchLine_5 = SketchProjection_3.createdFeature()
Sketch_1.setCoincident(SketchLine_4.startPoint(), SketchLine_5.result())
Sketch_1.setCoincident(SketchLine_4.endPoint(), SketchLine_3.result())

### Create SketchLine
SketchLine_6 = Sketch_1.addLine(5, 5, 6, 10)
Sketch_1.setCoincident(SketchLine_4.endPoint(), SketchLine_6.startPoint())
Sketch_1.setCoincident(SketchLine_6.endPoint(), SketchLine_5.result())

### Create SketchLine
SketchLine_7 = Sketch_1.addLine(4, 10, 6, 10)
Sketch_1.setCoincident(SketchLine_4.startPoint(), SketchLine_7.startPoint())
Sketch_1.setCoincident(SketchLine_6.endPoint(), SketchLine_7.endPoint())
Sketch_1.setDistance(SketchLine_7.endPoint(), SketchLine_2.result(), 4, True)
Sketch_1.setDistance(SketchLine_1.result(), SketchLine_4.startPoint(), 4, True)
Sketch_1.setMiddlePoint(SketchLine_4.endPoint(), SketchLine_3.result())
model.do()

### Create ExtrusionCut
ExtrusionCut_1 = model.addExtrusionCut(Part_1_doc, [model.selection("FACE", "Sketch_1/Face-SketchLine_4f-SketchLine_6f-SketchLine_7r")], model.selection(), 0, 10, [model.selection("SOLID", "Box_1_1")])

### Create Sketch
Sketch_2 = model.addSketch(Part_1_doc, model.selection("FACE", "Box_1_1/Front"))

### Create SketchPoint
SketchPoint_3 = Sketch_2.addPoint(5, 10)
SketchPoint_3.setAuxiliary(True)

### Create SketchProjection
SketchProjection_4 = Sketch_2.addProjection(model.selection("EDGE", "[ExtrusionCut_1_1/Modified_Face&Box_1_1/Top][Box_1_1/Front]"), False)
SketchLine_8 = SketchProjection_4.createdFeature()
Sketch_2.setCoincident(SketchPoint_3.coordinates(), SketchLine_8.result())

### Create SketchPoint
SketchPoint_4 = Sketch_2.addPoint(5, 0)

### Create SketchProjection
SketchProjection_5 = Sketch_2.addProjection(model.selection("EDGE", "[ExtrusionCut_1_1/Modified_Face&Box_1_1/Bottom][Box_1_1/Front]"), False)
SketchLine_9 = SketchProjection_5.createdFeature()
Sketch_2.setCoincident(SketchPoint_4.coordinates(), SketchLine_9.result())
Sketch_2.setMiddlePoint(SketchPoint_3.coordinates(), SketchLine_8.result())
Sketch_2.setMiddlePoint(SketchPoint_4.coordinates(), SketchLine_9.result())

### Create SketchLine
SketchLine_10 = Sketch_2.addLine(5, 10, 5, 0)
SketchLine_10.setAuxiliary(True)
Sketch_2.setCoincident(SketchPoint_3.coordinates(), SketchLine_10.startPoint())
Sketch_2.setCoincident(SketchPoint_4.coordinates(), SketchLine_10.endPoint())

### Create SketchLine
SketchLine_11 = Sketch_2.addLine(10, 6, 10, 4)

### Create SketchProjection
SketchProjection_6 = Sketch_2.addProjection(model.selection("EDGE", "[Box_1_1/Front][(ExtrusionCut_1_1/Modified_Face&Box_1_1/Top)(ExtrusionCut_1_1/Modified_Face&Box_1_1/Bottom)(Box_1_1/Front)(ExtrusionCut_1_1/Generated_Face&Sketch_1/SketchLine_6)]"), False)
SketchLine_12 = SketchProjection_6.createdFeature()
Sketch_2.setCoincident(SketchLine_11.startPoint(), SketchLine_12.result())
Sketch_2.setCoincident(SketchLine_11.endPoint(), SketchLine_12.result())

### Create SketchLine
SketchLine_13 = Sketch_2.addLine(10, 4, 5, 5)
Sketch_2.setCoincident(SketchLine_11.endPoint(), SketchLine_13.startPoint())
Sketch_2.setCoincident(SketchLine_13.endPoint(), SketchLine_10.result())

### Create SketchLine
SketchLine_14 = Sketch_2.addLine(5, 5, 10, 6)
Sketch_2.setCoincident(SketchLine_13.endPoint(), SketchLine_14.startPoint())
Sketch_2.setCoincident(SketchLine_11.startPoint(), SketchLine_14.endPoint())
Sketch_2.setDistance(SketchLine_8.result(), SketchLine_11.startPoint(), 4, True)
Sketch_2.setDistance(SketchLine_9.result(), SketchLine_13.startPoint(), 4, True)
Sketch_2.setMiddlePoint(SketchLine_13.endPoint(), SketchLine_10.result())
model.do()

### Create ExtrusionCut
ExtrusionCut_2 = model.addExtrusionCut(Part_1_doc, [model.selection("FACE", "Sketch_2/Face-SketchLine_14r-SketchLine_13r-SketchLine_11r")], model.selection(), 0, 10, [model.selection("SOLID", "ExtrusionCut_1_1")])

model.end()

###
### SHAPERSTUDY component
###

model.publishToShaperStudy()
import SHAPERSTUDY
ExtrusionCut_2_1, = SHAPERSTUDY.shape(model.featureStringId(ExtrusionCut_2))

if salome.sg.hasDesktop():
  salome.sg.updateObjBrowser()
