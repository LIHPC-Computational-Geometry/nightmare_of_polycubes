#!/usr/bin/env python

###
### This file is based on the automatically generated one by SALOME v9.9.0 with dump python functionality
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
Box_1 = model.addBox(Part_1_doc, 3, 3, 1.2)

### Create Sketch
Sketch_1 = model.addSketch(Part_1_doc, model.selection("FACE", "Box_1_1/Bottom"))

### Create SketchLine
SketchLine_1 = Sketch_1.addLine(2, -2, 1, -2)

### Create SketchLine
SketchLine_2 = Sketch_1.addLine(1, -2, 1, -1)

### Create SketchLine
SketchLine_3 = Sketch_1.addLine(1, -1, 2, -1)

### Create SketchLine
SketchLine_4 = Sketch_1.addLine(2, -1, 2, -2)
Sketch_1.setCoincident(SketchLine_4.endPoint(), SketchLine_1.startPoint())
Sketch_1.setCoincident(SketchLine_1.endPoint(), SketchLine_2.startPoint())
Sketch_1.setCoincident(SketchLine_2.endPoint(), SketchLine_3.startPoint())
Sketch_1.setCoincident(SketchLine_3.endPoint(), SketchLine_4.startPoint())
Sketch_1.setHorizontal(SketchLine_1.result())
Sketch_1.setVertical(SketchLine_2.result())
Sketch_1.setHorizontal(SketchLine_3.result())
Sketch_1.setVertical(SketchLine_4.result())

### Create SketchProjection
SketchProjection_1 = Sketch_1.addProjection(model.selection("EDGE", "[Box_1_1/Front][Box_1_1/Bottom]"), False)
SketchLine_5 = SketchProjection_1.createdFeature()
Sketch_1.setDistance(SketchLine_1.startPoint(), SketchLine_5.result(), 1, True)

### Create SketchProjection
SketchProjection_2 = Sketch_1.addProjection(model.selection("EDGE", "[Box_1_1/Left][Box_1_1/Bottom]"), False)
SketchLine_6 = SketchProjection_2.createdFeature()
Sketch_1.setDistance(SketchLine_3.endPoint(), SketchLine_6.result(), 1, True)

### Create SketchProjection
SketchProjection_3 = Sketch_1.addProjection(model.selection("EDGE", "[Box_1_1/Back][Box_1_1/Bottom]"), False)
SketchLine_7 = SketchProjection_3.createdFeature()
Sketch_1.setDistance(SketchLine_3.startPoint(), SketchLine_7.result(), 1, True)

### Create SketchProjection
SketchProjection_4 = Sketch_1.addProjection(model.selection("EDGE", "[Box_1_1/Right][Box_1_1/Bottom]"), False)
SketchLine_8 = SketchProjection_4.createdFeature()
Sketch_1.setDistance(SketchLine_2.startPoint(), SketchLine_8.result(), 1, True)
model.do()

### Create ExtrusionCut
ExtrusionCut_1 = model.addExtrusionCut(Part_1_doc, [model.selection("FACE", "Sketch_1/Face-SketchLine_4r-SketchLine_3r-SketchLine_2r-SketchLine_1r")], model.selection(), 0, 1.2, [model.selection("SOLID", "Box_1_1")])

### Create Sketch
Sketch_2 = model.addSketch(Part_1_doc, model.selection("FACE", "Box_1_1/Back"))

### Create SketchLine
SketchLine_9 = Sketch_2.addLine(3, -1.1, 2, -1.1)

### Create SketchProjection
SketchProjection_5 = Sketch_2.addProjection(model.selection("EDGE", "[Box_1_1/Back][Box_1_1/Right]"), False)
SketchLine_10 = SketchProjection_5.createdFeature()
Sketch_2.setCoincident(SketchLine_9.startPoint(), SketchLine_10.result())
Sketch_2.setHorizontal(SketchLine_9.result())

### Create SketchLine
SketchLine_11 = Sketch_2.addLine(2, -1.1, 0.9999999999999999, -1.2)
Sketch_2.setCoincident(SketchLine_9.endPoint(), SketchLine_11.startPoint())

### Create SketchProjection
SketchProjection_6 = Sketch_2.addProjection(model.selection("EDGE", "[Box_1_1/Back][ExtrusionCut_1_1/Modified_Face&Box_1_1/Top]"), False)
SketchLine_12 = SketchProjection_6.createdFeature()
Sketch_2.setCoincident(SketchLine_11.endPoint(), SketchLine_12.result())

### Create SketchProjection
SketchProjection_7 = Sketch_2.addProjection(model.selection("EDGE", "[Box_1_1/Back][Box_1_1/Left]"), False)
SketchLine_13 = SketchProjection_7.createdFeature()
Sketch_2.setDistance(SketchLine_11.endPoint(), SketchLine_13.result(), 1, True)
Sketch_2.setDistance(SketchLine_11.startPoint(), SketchLine_9.startPoint(), 1, True)
Sketch_2.setDistance(SketchLine_11.startPoint(), SketchLine_12.result(), 0.1, True)

### Create SketchLine
SketchLine_14 = Sketch_2.addLine(3, -1.1, 3, -1.2)
Sketch_2.setCoincident(SketchLine_9.startPoint(), SketchLine_14.startPoint())
Sketch_2.setCoincident(SketchAPI_Line(SketchLine_10).endPoint(), SketchLine_14.endPoint())

### Create SketchLine
SketchLine_15 = Sketch_2.addLine(3, -1.2, 0.9999999999999999, -1.2)
Sketch_2.setCoincident(SketchAPI_Line(SketchLine_10).endPoint(), SketchLine_15.startPoint())
Sketch_2.setCoincident(SketchLine_11.endPoint(), SketchLine_15.endPoint())
model.do()

### Create ExtrusionCut
ExtrusionCut_2 = model.addExtrusionCut(Part_1_doc, [model.selection("FACE", "Sketch_2/Face-SketchLine_9r-SketchLine_11f-SketchLine_15r-SketchLine_14r")], model.selection(), 0, 1, [model.selection("SOLID", "ExtrusionCut_1_1")])

### Create Sketch
Sketch_3 = model.addSketch(Part_1_doc, model.selection("FACE", "ExtrusionCut_2_1/Modified_Face&Box_1_1/Right"))

### Create SketchLine
SketchLine_16 = Sketch_3.addLine(1, -1.1, 2, -0.9999999999999999)

### Create SketchProjection
SketchProjection_8 = Sketch_3.addProjection(model.selection("VERTEX", "[ExtrusionCut_2_1/Generated_Face&Sketch_2/SketchLine_9][ExtrusionCut_2_1/Modified_Face&Box_1_1/Right][ExtrusionCut_2_1/Modified_Face&ExtrusionCut_2_1/From_Face]"), False)
SketchPoint_1 = SketchProjection_8.createdFeature()
Sketch_3.setCoincident(SketchLine_16.startPoint(), SketchPoint_1.result())

### Create SketchLine
SketchLine_17 = Sketch_3.addLine(2, -0.9999999999999999, 3, -0.9999999999999999)
Sketch_3.setCoincident(SketchLine_16.endPoint(), SketchLine_17.startPoint())

### Create SketchProjection
SketchProjection_9 = Sketch_3.addProjection(model.selection("EDGE", "[ExtrusionCut_2_1/Modified_Face&Box_1_1/Right][Box_1_1/Front]"), False)
SketchLine_18 = SketchProjection_9.createdFeature()
Sketch_3.setCoincident(SketchLine_17.endPoint(), SketchLine_18.result())
Sketch_3.setHorizontal(SketchLine_17.result())

### Create SketchLine
SketchLine_19 = Sketch_3.addLine(3, -0.9999999999999999, 3, -1.2)
Sketch_3.setCoincident(SketchLine_17.endPoint(), SketchLine_19.startPoint())
Sketch_3.setCoincident(SketchAPI_Line(SketchLine_18).endPoint(), SketchLine_19.endPoint())

### Create SketchLine
SketchLine_20 = Sketch_3.addLine(3, -1.2, 1, -1.2)
Sketch_3.setCoincident(SketchAPI_Line(SketchLine_18).endPoint(), SketchLine_20.startPoint())

### Create SketchProjection
SketchProjection_10 = Sketch_3.addProjection(model.selection("VERTEX", "[ExtrusionCut_2_1/Modified_Face&Box_1_1/Top][ExtrusionCut_2_1/Modified_Face&Box_1_1/Right][ExtrusionCut_2_1/Modified_Face&ExtrusionCut_2_1/From_Face]"), False)
SketchPoint_2 = SketchProjection_10.createdFeature()
Sketch_3.setCoincident(SketchLine_20.endPoint(), SketchPoint_2.result())

### Create SketchLine
SketchLine_21 = Sketch_3.addLine(1, -1.2, 1, -1.1)
Sketch_3.setCoincident(SketchLine_20.endPoint(), SketchLine_21.startPoint())
Sketch_3.setCoincident(SketchLine_16.startPoint(), SketchLine_21.endPoint())
Sketch_3.setVerticalDistance(SketchAPI_Point(SketchPoint_1).coordinates(), SketchLine_16.endPoint(), 0.1)
Sketch_3.setHorizontalDistance(SketchLine_16.endPoint(), SketchAPI_Point(SketchPoint_1).coordinates(), 1)
model.do()

### Create ExtrusionCut
ExtrusionCut_3 = model.addExtrusionCut(Part_1_doc, [model.selection("FACE", "Sketch_3/Face-SketchLine_21r-SketchLine_20r-SketchLine_19r-SketchLine_17r-SketchLine_16r")], model.selection(), 0, 1, [model.selection("SOLID", "ExtrusionCut_2_1")])

### Create Sketch
Sketch_4 = model.addSketch(Part_1_doc, model.selection("FACE", "ExtrusionCut_3_1/Modified_Face&Box_1_1/Front"))

### Create SketchLine
SketchLine_22 = Sketch_4.addLine(2, 0.9999999999999999, 1, 0.8999999999999999)

### Create SketchProjection
SketchProjection_11 = Sketch_4.addProjection(model.selection("VERTEX", "[ExtrusionCut_3_1/Modified_Face&ExtrusionCut_3_1/From_Face][ExtrusionCut_3_1/Modified_Face&Box_1_1/Front][ExtrusionCut_3_1/Generated_Face&Sketch_3/SketchLine_17]"), False)
SketchPoint_3 = SketchProjection_11.createdFeature()
Sketch_4.setCoincident(SketchLine_22.startPoint(), SketchPoint_3.result())

### Create SketchLine
SketchLine_23 = Sketch_4.addLine(1, 0.8999999999999999, 0, 0.8999999999999999)
Sketch_4.setCoincident(SketchLine_22.endPoint(), SketchLine_23.startPoint())

### Create SketchProjection
SketchProjection_12 = Sketch_4.addProjection(model.selection("EDGE", "[Box_1_1/Left][ExtrusionCut_3_1/Modified_Face&Box_1_1/Front]"), False)
SketchLine_24 = SketchProjection_12.createdFeature()
Sketch_4.setCoincident(SketchLine_23.endPoint(), SketchLine_24.result())
Sketch_4.setHorizontal(SketchLine_23.result())

### Create SketchLine
SketchLine_25 = Sketch_4.addLine(0, 0.8999999999999999, 0, 1.2)
Sketch_4.setCoincident(SketchLine_23.endPoint(), SketchLine_25.startPoint())
Sketch_4.setCoincident(SketchAPI_Line(SketchLine_24).endPoint(), SketchLine_25.endPoint())

### Create SketchLine
SketchLine_26 = Sketch_4.addLine(0, 1.2, 2, 1.2)
Sketch_4.setCoincident(SketchAPI_Line(SketchLine_24).endPoint(), SketchLine_26.startPoint())

### Create SketchProjection
SketchProjection_13 = Sketch_4.addProjection(model.selection("VERTEX", "[ExtrusionCut_3_1/Modified_Face&Box_1_1/Top][ExtrusionCut_3_1/Modified_Face&ExtrusionCut_3_1/From_Face][ExtrusionCut_3_1/Modified_Face&Box_1_1/Front]"), False)
SketchPoint_4 = SketchProjection_13.createdFeature()
Sketch_4.setCoincident(SketchLine_26.endPoint(), SketchPoint_4.result())

### Create SketchLine
SketchLine_27 = Sketch_4.addLine(2, 1.2, 2, 0.9999999999999999)
Sketch_4.setCoincident(SketchLine_26.endPoint(), SketchLine_27.startPoint())
Sketch_4.setCoincident(SketchLine_22.startPoint(), SketchLine_27.endPoint())
Sketch_4.setVerticalDistance(SketchLine_23.startPoint(), SketchAPI_Point(SketchPoint_3).coordinates(), 0.1)
Sketch_4.setHorizontalDistance(SketchLine_23.startPoint(), SketchAPI_Point(SketchPoint_3).coordinates(), 1)
model.do()

### Create ExtrusionCut
ExtrusionCut_4 = model.addExtrusionCut(Part_1_doc, [model.selection("FACE", "Sketch_4/Face-SketchLine_27r-SketchLine_26r-SketchLine_25r-SketchLine_23r-SketchLine_22r")], model.selection(), 0, 1, [model.selection("SOLID", "ExtrusionCut_3_1")])

### Create Sketch
Sketch_5 = model.addSketch(Part_1_doc, model.selection("FACE", "ExtrusionCut_4_1/Modified_Face&Box_1_1/Left"))

### Create SketchLine
SketchLine_28 = Sketch_5.addLine(2, 0.8999999999999999, 1, 0.8999999999999999)

### Create SketchProjection
SketchProjection_14 = Sketch_5.addProjection(model.selection("VERTEX", "[ExtrusionCut_4_1/Modified_Face&Box_1_1/Left][ExtrusionCut_4_1/Modified_Face&ExtrusionCut_4_1/From_Face][ExtrusionCut_4_1/Generated_Face&Sketch_4/SketchLine_23]"), False)
SketchPoint_5 = SketchProjection_14.createdFeature()
Sketch_5.setCoincident(SketchLine_28.startPoint(), SketchPoint_5.result())

### Create SketchLine
SketchLine_29 = Sketch_5.addLine(1, 0.8999999999999999, 1, 1.2)
Sketch_5.setCoincident(SketchLine_28.endPoint(), SketchLine_29.startPoint())

### Create SketchProjection
SketchProjection_15 = Sketch_5.addProjection(model.selection("EDGE", "[ExtrusionCut_4_1/Modified_Face&Box_1_1/Top][ExtrusionCut_4_1/Modified_Face&Box_1_1/Left]"), False)
SketchLine_30 = SketchProjection_15.createdFeature()
Sketch_5.setCoincident(SketchLine_29.endPoint(), SketchLine_30.result())
Sketch_5.setVertical(SketchLine_29.result())

### Create SketchLine
SketchLine_31 = Sketch_5.addLine(1, 1.2, 2, 1.2)
Sketch_5.setCoincident(SketchLine_29.endPoint(), SketchLine_31.startPoint())
Sketch_5.setCoincident(SketchAPI_Line(SketchLine_30).endPoint(), SketchLine_31.endPoint())

### Create SketchLine
SketchLine_32 = Sketch_5.addLine(2, 1.2, 2, 0.8999999999999999)
Sketch_5.setCoincident(SketchAPI_Line(SketchLine_30).endPoint(), SketchLine_32.startPoint())
Sketch_5.setCoincident(SketchLine_28.startPoint(), SketchLine_32.endPoint())
Sketch_5.setVerticalDistance(SketchLine_29.startPoint(), SketchLine_28.startPoint(), 0)
Sketch_5.setHorizontalDistance(SketchLine_29.startPoint(), SketchLine_28.startPoint(), 1)
model.do()

### Create ExtrusionCut
ExtrusionCut_5 = model.addExtrusionCut(Part_1_doc, [model.selection("FACE", "Sketch_5/Face-SketchLine_32r-SketchLine_31r-SketchLine_29r-SketchLine_28r")], model.selection(), 0, 1, [model.selection("SOLID", "ExtrusionCut_4_1")])

model.end()

###
### SHAPERSTUDY component
###

model.publishToShaperStudy()
import SHAPERSTUDY
ExtrusionCut_5_1, = SHAPERSTUDY.shape(model.featureStringId(ExtrusionCut_5))

if salome.sg.hasDesktop():
  salome.sg.updateObjBrowser()
