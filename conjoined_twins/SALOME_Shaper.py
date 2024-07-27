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
model.addParameter(Part_1_doc, "cube_length", '10')
model.addParameter(Part_1_doc, "delta", '1')

### Create Box
Box_1 = model.addBox(Part_1_doc, "cube_length", "cube_length", "cube_length")

### Create Sketch
Sketch_1 = model.addSketch(Part_1_doc, model.selection("FACE", "Box_1_1/Top"))

### Create SketchLine
SketchLine_1 = Sketch_1.addLine(9, 10, 10, 10)

### Create SketchProjection
SketchProjection_1 = Sketch_1.addProjection(model.selection("EDGE", "[Box_1_1/Right][Box_1_1/Top]"), False)
SketchLine_2 = SketchProjection_1.createdFeature()
Sketch_1.setCoincident(SketchLine_1.startPoint(), SketchLine_2.result())
Sketch_1.setCoincident(SketchAPI_Line(SketchLine_2).endPoint(), SketchLine_1.endPoint())

### Create SketchLine
SketchLine_3 = Sketch_1.addLine(10, 10, 10, 0)
Sketch_1.setCoincident(SketchLine_1.endPoint(), SketchLine_3.startPoint())

### Create SketchProjection
SketchProjection_2 = Sketch_1.addProjection(model.selection("VERTEX", "[Box_1_1/Front][Box_1_1/Left][Box_1_1/Top]"), False)
SketchPoint_1 = SketchProjection_2.createdFeature()
Sketch_1.setCoincident(SketchLine_3.endPoint(), SketchPoint_1.result())

### Create SketchLine
SketchLine_4 = Sketch_1.addLine(10, 0, 9, 10)
Sketch_1.setCoincident(SketchLine_3.endPoint(), SketchLine_4.startPoint())
Sketch_1.setCoincident(SketchLine_1.startPoint(), SketchLine_4.endPoint())
Sketch_1.setDistance(SketchLine_4.endPoint(), SketchAPI_Line(SketchLine_2).endPoint(), "delta", True)
model.do()

### Create ExtrusionCut
ExtrusionCut_1 = model.addExtrusionCut(Part_1_doc, [model.selection("FACE", "Sketch_1/Face-SketchLine_4r-SketchLine_3r-SketchLine_1r")], model.selection(), 0, "cube_length", [model.selection("SOLID", "Box_1_1")])

### Create Sketch
Sketch_2 = model.addSketch(Part_1_doc, model.selection("FACE", "Box_1_1/Back"))

### Create SketchLine
SketchLine_5 = Sketch_2.addLine(10, -0.9999999999999999, 10, 0)

### Create SketchProjection
SketchProjection_3 = Sketch_2.addProjection(model.selection("EDGE", "[Box_1_1/Back][ExtrusionCut_1_1/Modified_Face&Box_1_1/Right]"), False)
SketchLine_6 = SketchProjection_3.createdFeature()
Sketch_2.setCoincident(SketchLine_5.startPoint(), SketchLine_6.result())
Sketch_2.setCoincident(SketchAPI_Line(SketchLine_6).startPoint(), SketchLine_5.endPoint())

### Create SketchLine
SketchLine_7 = Sketch_2.addLine(10, 0, 0, 0)
Sketch_2.setCoincident(SketchLine_5.endPoint(), SketchLine_7.startPoint())

### Create SketchProjection
SketchProjection_4 = Sketch_2.addProjection(model.selection("VERTEX", "[Box_1_1/Back][ExtrusionCut_1_1/Modified_Face&Box_1_1/Left][ExtrusionCut_1_1/Modified_Face&Box_1_1/Bottom]"), False)
SketchPoint_2 = SketchProjection_4.createdFeature()
Sketch_2.setCoincident(SketchLine_7.endPoint(), SketchPoint_2.result())

### Create SketchLine
SketchLine_8 = Sketch_2.addLine(0, 0, 10, -0.9999999999999999)
Sketch_2.setCoincident(SketchLine_7.endPoint(), SketchLine_8.startPoint())
Sketch_2.setCoincident(SketchLine_5.startPoint(), SketchLine_8.endPoint())
Sketch_2.setDistance(SketchLine_7.startPoint(), SketchLine_8.endPoint(), "delta", True)
model.do()

### Create ExtrusionCut
ExtrusionCut_2 = model.addExtrusionCut(Part_1_doc, [model.selection("FACE", "Sketch_2/Face-SketchLine_5r-SketchLine_7f-SketchLine_8f")], model.selection(), 0, "cube_length", [model.selection("SOLID", "ExtrusionCut_1_1")])

### Create AngularCopy
AngularCopy_1 = model.addMultiRotation(Part_1_doc, [model.selection("SOLID", "ExtrusionCut_2_1")], model.selection("EDGE", "[ExtrusionCut_2_1/Modified_Face&Box_1_1/Back][ExtrusionCut_1_1/Modified_Face&Box_1_1/Top]"), 2, keepSubResults = True)

### Create Translation
Translation_1 = model.addTranslation(Part_1_doc, [model.selection("SOLID", "AngularCopy_1_1_2")], vector = ["2*cube_length-delta", 0, "-2*cube_length+delta"], keepSubResults = True)

### Create Fuse
Fuse_1 = model.addFuse(Part_1_doc, [model.selection("SOLID", "Translation_1_1_1"), model.selection("SOLID", "Translation_1_1_2")], keepSubResults = True)

model.end()

###
### SHAPERSTUDY component
###

model.publishToShaperStudy()
import SHAPERSTUDY
Fuse_1_1, = SHAPERSTUDY.shape(model.featureStringId(Fuse_1))

if salome.sg.hasDesktop():
  salome.sg.updateObjBrowser()
