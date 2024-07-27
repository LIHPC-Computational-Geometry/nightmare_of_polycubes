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
Box_1 = model.addBox(Part_1_doc, 3, 1.2, 3)

### Create Sketch
Sketch_1 = model.addSketch(Part_1_doc, model.selection("FACE", "Box_1_1/Right"))

### Create SketchLine
SketchLine_1 = Sketch_1.addLine(1, -2, 2, -2)

### Create SketchLine
SketchLine_2 = Sketch_1.addLine(2, -2, 2, -1.000000000000008)

### Create SketchLine
SketchLine_3 = Sketch_1.addLine(2, -1.000000000000008, 1, -1)

### Create SketchLine
SketchLine_4 = Sketch_1.addLine(1, -1, 1, -2)
Sketch_1.setCoincident(SketchLine_4.endPoint(), SketchLine_1.startPoint())
Sketch_1.setCoincident(SketchLine_1.endPoint(), SketchLine_2.startPoint())
Sketch_1.setCoincident(SketchLine_2.endPoint(), SketchLine_3.startPoint())
Sketch_1.setCoincident(SketchLine_3.endPoint(), SketchLine_4.startPoint())
Sketch_1.setPerpendicular(SketchLine_1.result(), SketchLine_2.result())
Sketch_1.setPerpendicular(SketchLine_2.result(), SketchLine_3.result())
Sketch_1.setPerpendicular(SketchLine_3.result(), SketchLine_4.result())

### Create SketchProjection
SketchProjection_1 = Sketch_1.addProjection(model.selection("VERTEX", "[Box_1_1/Front][Box_1_1/Right][Box_1_1/Top]"), False)
SketchPoint_1 = SketchProjection_1.createdFeature()
Sketch_1.setHorizontalDistance(SketchLine_1.endPoint(), SketchAPI_Point(SketchPoint_1).coordinates(), 1)

### Create SketchProjection
SketchProjection_2 = Sketch_1.addProjection(model.selection("VERTEX", "[Box_1_1/Back][Box_1_1/Right][Box_1_1/Bottom]"), False)
SketchPoint_2 = SketchProjection_2.createdFeature()
Sketch_1.setHorizontalDistance(SketchLine_3.endPoint(), SketchAPI_Point(SketchPoint_2).coordinates(), 1)
Sketch_1.setHorizontal(SketchLine_1.result())
Sketch_1.setVerticalDistance(SketchLine_2.startPoint(), SketchAPI_Point(SketchPoint_1).coordinates(), 1)
Sketch_1.setVerticalDistance(SketchLine_4.startPoint(), SketchAPI_Point(SketchPoint_2).coordinates(), 1)
model.do()

### Create ExtrusionCut
ExtrusionCut_1 = model.addExtrusionCut(Part_1_doc, [model.selection("FACE", "Sketch_1/Face-SketchLine_1r-SketchLine_2f-SketchLine_3f-SketchLine_4f")], model.selection(), 0, 1.2, [model.selection("SOLID", "Box_1_1")])

### Create Sketch
Sketch_2 = model.addSketch(Part_1_doc, model.selection("FACE", "Box_1_1/Back"))

### Create SketchLine
SketchLine_5 = Sketch_2.addLine(1.2, -2, 1.1, -1)

### Create SketchProjection
SketchProjection_3 = Sketch_2.addProjection(model.selection("EDGE", "[Box_1_1/Back][ExtrusionCut_1_1/Modified_Face&Box_1_1/Right]"), False)
SketchLine_6 = SketchProjection_3.createdFeature()
Sketch_2.setCoincident(SketchLine_5.startPoint(), SketchLine_6.result())

### Create SketchLine
SketchLine_7 = Sketch_2.addLine(1.1, -1, 1.1, 0)
Sketch_2.setCoincident(SketchLine_5.endPoint(), SketchLine_7.startPoint())

### Create SketchProjection
SketchProjection_4 = Sketch_2.addProjection(model.selection("EDGE", "[Box_1_1/Back][Box_1_1/Bottom]"), False)
SketchLine_8 = SketchProjection_4.createdFeature()
Sketch_2.setCoincident(SketchLine_7.endPoint(), SketchLine_8.result())
Sketch_2.setVertical(SketchLine_7.result())

### Create SketchLine
SketchLine_9 = Sketch_2.addLine(1.1, 0, 1.2, 0)
Sketch_2.setCoincident(SketchLine_7.endPoint(), SketchLine_9.startPoint())
Sketch_2.setCoincident(SketchAPI_Line(SketchLine_6).startPoint(), SketchLine_9.endPoint())

### Create SketchLine
SketchLine_10 = Sketch_2.addLine(1.2, 0, 1.2, -2)
Sketch_2.setCoincident(SketchAPI_Line(SketchLine_6).startPoint(), SketchLine_10.startPoint())
Sketch_2.setCoincident(SketchLine_5.startPoint(), SketchLine_10.endPoint())

### Create SketchProjection
SketchProjection_5 = Sketch_2.addProjection(model.selection("EDGE", "[Box_1_1/Back][Box_1_1/Top]"), False)
SketchLine_11 = SketchProjection_5.createdFeature()
Sketch_2.setDistance(SketchLine_10.endPoint(), SketchLine_11.result(), 1, True)
Sketch_2.setDistance(SketchLine_7.startPoint(), SketchLine_8.result(), 1, True)
Sketch_2.setHorizontalDistance(SketchLine_9.startPoint(), SketchLine_10.endPoint(), 0.1)
model.do()

### Create ExtrusionCut
ExtrusionCut_2 = model.addExtrusionCut(Part_1_doc, [model.selection("FACE", "Sketch_2/Face-SketchLine_10r-SketchLine_9r-SketchLine_7r-SketchLine_5r")], model.selection(), 0, 1, [model.selection("SOLID", "ExtrusionCut_1_1")])

### Create Sketch
Sketch_3 = model.addSketch(Part_1_doc, model.selection("FACE", "ExtrusionCut_2_1/Modified_Face&Box_1_1/Bottom"))

### Create SketchLine
SketchLine_12 = Sketch_3.addLine(1, -1.1, 2, -0.9999999999999998)

### Create SketchProjection
SketchProjection_6 = Sketch_3.addProjection(model.selection("VERTEX", "[ExtrusionCut_2_1/Generated_Face&Sketch_2/SketchLine_7][ExtrusionCut_2_1/Modified_Face&Box_1_1/Bottom][ExtrusionCut_2_1/Modified_Face&ExtrusionCut_2_1/From_Face]"), False)
SketchPoint_3 = SketchProjection_6.createdFeature()
Sketch_3.setCoincident(SketchLine_12.startPoint(), SketchPoint_3.result())

### Create SketchLine
SketchLine_13 = Sketch_3.addLine(2, -0.9999999999999998, 3, -0.9999999999999998)
Sketch_3.setCoincident(SketchLine_12.endPoint(), SketchLine_13.startPoint())

### Create SketchProjection
SketchProjection_7 = Sketch_3.addProjection(model.selection("EDGE", "[ExtrusionCut_2_1/Modified_Face&Box_1_1/Bottom][Box_1_1/Front]"), False)
SketchLine_14 = SketchProjection_7.createdFeature()
Sketch_3.setCoincident(SketchLine_13.endPoint(), SketchLine_14.result())
Sketch_3.setHorizontal(SketchLine_13.result())

### Create SketchLine
SketchLine_15 = Sketch_3.addLine(3, -0.9999999999999998, 3, -1.2)
Sketch_3.setCoincident(SketchLine_13.endPoint(), SketchLine_15.startPoint())
Sketch_3.setCoincident(SketchAPI_Line(SketchLine_14).endPoint(), SketchLine_15.endPoint())

### Create SketchLine
SketchLine_16 = Sketch_3.addLine(3, -1.2, 1, -1.2)
Sketch_3.setCoincident(SketchAPI_Line(SketchLine_14).endPoint(), SketchLine_16.startPoint())

### Create SketchProjection
SketchProjection_8 = Sketch_3.addProjection(model.selection("VERTEX", "[ExtrusionCut_2_1/Modified_Face&Box_1_1/Right][ExtrusionCut_2_1/Modified_Face&Box_1_1/Bottom][ExtrusionCut_2_1/Modified_Face&ExtrusionCut_2_1/From_Face]"), False)
SketchPoint_4 = SketchProjection_8.createdFeature()
Sketch_3.setCoincident(SketchLine_16.endPoint(), SketchPoint_4.result())

### Create SketchLine
SketchLine_17 = Sketch_3.addLine(1, -1.2, 1, -1.1)
Sketch_3.setCoincident(SketchLine_16.endPoint(), SketchLine_17.startPoint())
Sketch_3.setCoincident(SketchLine_12.startPoint(), SketchLine_17.endPoint())
Sketch_3.setDistance(SketchLine_12.endPoint(), SketchLine_14.result(), 1, True)
Sketch_3.setDistance(SketchLine_16.result(), SketchLine_12.endPoint(), 0.2, True)
model.do()

### Create ExtrusionCut
ExtrusionCut_3 = model.addExtrusionCut(Part_1_doc, [model.selection("FACE", "Sketch_3/Face-SketchLine_17r-SketchLine_16r-SketchLine_15r-SketchLine_13r-SketchLine_12r")], model.selection(), 0, 1, [model.selection("SOLID", "ExtrusionCut_2_1")])

### Create Sketch
Sketch_4 = model.addSketch(Part_1_doc, model.selection("FACE", "ExtrusionCut_3_1/Modified_Face&Box_1_1/Front"))

### Create SketchLine
SketchLine_18 = Sketch_4.addLine(0.9999999999999998, 1, 0.9000000000000001, 2)

### Create SketchProjection
SketchProjection_9 = Sketch_4.addProjection(model.selection("VERTEX", "[ExtrusionCut_3_1/Modified_Face&Box_1_1/Front][ExtrusionCut_3_1/Modified_Face&ExtrusionCut_3_1/From_Face][ExtrusionCut_3_1/Generated_Face&Sketch_3/SketchLine_13]"), False)
SketchPoint_5 = SketchProjection_9.createdFeature()
Sketch_4.setCoincident(SketchLine_18.startPoint(), SketchPoint_5.result())

### Create SketchLine
SketchLine_19 = Sketch_4.addLine(0.9000000000000001, 2, 0.9000000000000001, 3)
Sketch_4.setCoincident(SketchLine_18.endPoint(), SketchLine_19.startPoint())

### Create SketchProjection
SketchProjection_10 = Sketch_4.addProjection(model.selection("EDGE", "[Box_1_1/Top][ExtrusionCut_3_1/Modified_Face&Box_1_1/Front]"), False)
SketchLine_20 = SketchProjection_10.createdFeature()
Sketch_4.setCoincident(SketchLine_19.endPoint(), SketchLine_20.result())
Sketch_4.setVertical(SketchLine_19.result())

### Create SketchLine
SketchLine_21 = Sketch_4.addLine(0.9000000000000001, 3, 1.2, 3)
Sketch_4.setCoincident(SketchLine_19.endPoint(), SketchLine_21.startPoint())
Sketch_4.setCoincident(SketchAPI_Line(SketchLine_20).endPoint(), SketchLine_21.endPoint())

### Create SketchLine
SketchLine_22 = Sketch_4.addLine(1.2, 3, 1.2, 1)
Sketch_4.setCoincident(SketchAPI_Line(SketchLine_20).endPoint(), SketchLine_22.startPoint())

### Create SketchProjection
SketchProjection_11 = Sketch_4.addProjection(model.selection("VERTEX", "[ExtrusionCut_3_1/Modified_Face&Box_1_1/Right][ExtrusionCut_3_1/Modified_Face&Box_1_1/Front][ExtrusionCut_3_1/Modified_Face&ExtrusionCut_3_1/From_Face]"), False)
SketchPoint_6 = SketchProjection_11.createdFeature()
Sketch_4.setCoincident(SketchLine_22.endPoint(), SketchPoint_6.result())

### Create SketchLine
SketchLine_23 = Sketch_4.addLine(1.2, 1, 0.9999999999999998, 1)
Sketch_4.setCoincident(SketchLine_22.endPoint(), SketchLine_23.startPoint())
Sketch_4.setCoincident(SketchLine_18.startPoint(), SketchLine_23.endPoint())
Sketch_4.setDistance(SketchLine_19.endPoint(), SketchLine_18.endPoint(), 1, True)
Sketch_4.setDistance(SketchLine_22.result(), SketchLine_18.endPoint(), 0.3, True)
model.do()

### Create ExtrusionCut
ExtrusionCut_4 = model.addExtrusionCut(Part_1_doc, [model.selection("FACE", "Sketch_4/Face-SketchLine_23r-SketchLine_22r-SketchLine_21r-SketchLine_19r-SketchLine_18r")], model.selection(), 0, 1, [model.selection("SOLID", "ExtrusionCut_3_1")])

### Create Sketch
Sketch_5 = model.addSketch(Part_1_doc, model.selection("FACE", "ExtrusionCut_4_1/Modified_Face&Box_1_1/Top"))

### Create SketchLine
SketchLine_24 = Sketch_5.addLine(1, 1.2, 2, 1.2)

### Create SketchProjection
SketchProjection_12 = Sketch_5.addProjection(model.selection("VERTEX", "[ExtrusionCut_4_1/Modified_Face&Box_1_1/Top][ExtrusionCut_4_1/Modified_Face&Box_1_1/Right][ExtrusionCut_4_1/Modified_Face&ExtrusionCut_4_1/From_Face]"), False)
SketchPoint_7 = SketchProjection_12.createdFeature()
Sketch_5.setCoincident(SketchLine_24.endPoint(), SketchPoint_7.result())

### Create SketchLine
SketchLine_25 = Sketch_5.addLine(2, 1.2, 2, 0.9)

### Create SketchLine
SketchLine_26 = Sketch_5.addLine(2, 0.9, 1, 0.8999999999999997)

### Create SketchLine
SketchLine_27 = Sketch_5.addLine(1, 0.8999999999999997, 1, 1.2)
Sketch_5.setCoincident(SketchLine_27.endPoint(), SketchLine_24.startPoint())
Sketch_5.setCoincident(SketchLine_24.endPoint(), SketchLine_25.startPoint())
Sketch_5.setCoincident(SketchLine_25.endPoint(), SketchLine_26.startPoint())
Sketch_5.setCoincident(SketchLine_26.endPoint(), SketchLine_27.startPoint())
Sketch_5.setPerpendicular(SketchLine_24.result(), SketchLine_25.result())
Sketch_5.setPerpendicular(SketchLine_25.result(), SketchLine_26.result())
Sketch_5.setPerpendicular(SketchLine_26.result(), SketchLine_27.result())
Sketch_5.setHorizontal(SketchLine_26.result())
Sketch_5.setDistance(SketchLine_24.result(), SketchLine_26.startPoint(), 0.3, True)

### Create SketchProjection
SketchProjection_13 = Sketch_5.addProjection(model.selection("EDGE", "[ExtrusionCut_2_1/Modified_Face&Box_1_1/Back][ExtrusionCut_4_1/Modified_Face&Box_1_1/Top]"), False)
SketchLine_28 = SketchProjection_13.createdFeature()
Sketch_5.setDistance(SketchLine_28.result(), SketchLine_27.startPoint(), 1, True)
model.do()

### Create ExtrusionCut
ExtrusionCut_5 = model.addExtrusionCut(Part_1_doc, [model.selection("FACE", "Sketch_5/Face-SketchLine_27r-SketchLine_26r-SketchLine_25r-SketchLine_24r")], model.selection(), 0, 1, [model.selection("SOLID", "ExtrusionCut_4_1")])

model.end()

###
### SHAPERSTUDY component
###

model.publishToShaperStudy()
import SHAPERSTUDY
ExtrusionCut_5_1, = SHAPERSTUDY.shape(model.featureStringId(ExtrusionCut_5))

if salome.sg.hasDesktop():
  salome.sg.updateObjBrowser()
