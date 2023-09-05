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
Box_1 = model.addBox(Part_1_doc, 10, 10, 8)

### Create Sketch
Sketch_1 = model.addSketch(Part_1_doc, model.selection("FACE", "Box_1_1/Front"))

### Create SketchProjection
SketchProjection_1 = Sketch_1.addProjection(model.selection("VERTEX", "[Box_1_1/Front][Box_1_1/Right][Box_1_1/Top]"), False)
SketchPoint_1 = SketchProjection_1.createdFeature()

### Create SketchProjection
SketchProjection_2 = Sketch_1.addProjection(model.selection("EDGE", "[Box_1_1/Front][Box_1_1/Top]"), False)
SketchLine_1 = SketchProjection_2.createdFeature()
SketchLine_1.setName("SketchLine_2")
SketchLine_1.result().setName("SketchLine_2")

### Create SketchLine
SketchLine_2 = Sketch_1.addLine(8, 7, 1, 6)
SketchLine_2.setName("SketchLine_3")
SketchLine_2.result().setName("SketchLine_3")

### Create SketchLine
SketchLine_3 = Sketch_1.addLine(1, 6, 0, 6)
SketchLine_3.setName("SketchLine_4")
SketchLine_3.result().setName("SketchLine_4")
Sketch_1.setCoincident(SketchLine_2.endPoint(), SketchLine_3.startPoint())

### Create SketchProjection
SketchProjection_3 = Sketch_1.addProjection(model.selection("EDGE", "[Box_1_1/Front][Box_1_1/Left]"), False)
SketchLine_4 = SketchProjection_3.createdFeature()
SketchLine_4.setName("SketchLine_5")
SketchLine_4.result().setName("SketchLine_5")
Sketch_1.setCoincident(SketchLine_3.endPoint(), SketchLine_4.result())
Sketch_1.setHorizontal(SketchLine_3.result())

### Create SketchLine
SketchLine_5 = Sketch_1.addLine(8, 7, 8, 8)
SketchLine_5.setName("SketchLine_6")
SketchLine_5.result().setName("SketchLine_6")
Sketch_1.setCoincident(SketchLine_2.startPoint(), SketchLine_5.startPoint())
Sketch_1.setCoincident(SketchLine_5.endPoint(), SketchLine_1.result())
Sketch_1.setVertical(SketchLine_5.result())

### Create SketchLine
SketchLine_6 = Sketch_1.addLine(8, 8, 0, 8)
SketchLine_6.setName("SketchLine_7")
SketchLine_6.result().setName("SketchLine_7")
Sketch_1.setCoincident(SketchLine_5.endPoint(), SketchLine_6.startPoint())
Sketch_1.setCoincident(SketchAPI_Line(SketchLine_1).startPoint(), SketchLine_6.endPoint())

### Create SketchLine
SketchLine_7 = Sketch_1.addLine(0, 8, 0, 6)
SketchLine_7.setName("SketchLine_8")
SketchLine_7.result().setName("SketchLine_8")
Sketch_1.setCoincident(SketchAPI_Line(SketchLine_1).startPoint(), SketchLine_7.startPoint())
Sketch_1.setCoincident(SketchLine_3.endPoint(), SketchLine_7.endPoint())
Sketch_1.setVerticalDistance(SketchLine_6.startPoint(), SketchLine_2.startPoint(), 1)
Sketch_1.setHorizontalDistance(SketchLine_6.startPoint(), SketchAPI_Line(SketchLine_1).endPoint(), 2)
Sketch_1.setHorizontalDistance(SketchLine_3.startPoint(), SketchLine_3.endPoint(), 1)
Sketch_1.setVerticalDistance(SketchLine_3.startPoint(), SketchLine_2.startPoint(), 1)
model.do()

### Create ExtrusionCut
ExtrusionCut_1 = model.addExtrusionCut(Part_1_doc, [model.selection("FACE", "Sketch_1/Face-SketchLine_6f-SketchLine_7f-SketchLine_8f-SketchLine_4r-SketchLine_3r")], model.selection(), 0, 1, [model.selection("SOLID", "Box_1_1")])

### Create Sketch
Sketch_2 = model.addSketch(Part_1_doc, model.selection("FACE", "ExtrusionCut_1_1/Modified_Face&Box_1_1/Left"))

### Create SketchLine
SketchLine_8 = Sketch_2.addLine(9, 6, 1, 5)
SketchLine_8.setName("SketchLine_9")
SketchLine_8.result().setName("SketchLine_9")

### Create SketchProjection
SketchProjection_4 = Sketch_2.addProjection(model.selection("VERTEX", "[ExtrusionCut_1_1/Modified_Face&Box_1_1/Left][ExtrusionCut_1_1/Generated_Face&Sketch_1/SketchLine_4][ExtrusionCut_1_1/From_Face]"), False)
SketchPoint_2 = SketchProjection_4.createdFeature()
Sketch_2.setCoincident(SketchLine_8.startPoint(), SketchPoint_2.result())

### Create SketchLine
SketchLine_9 = Sketch_2.addLine(1, 5, 0, 5)
SketchLine_9.setName("SketchLine_10")
SketchLine_9.result().setName("SketchLine_10")
Sketch_2.setCoincident(SketchLine_8.endPoint(), SketchLine_9.startPoint())
Sketch_2.setHorizontal(SketchLine_9.result())

### Create SketchLine
SketchLine_10 = Sketch_2.addLine(0, 5, 0, 8)
SketchLine_10.setName("SketchLine_11")
SketchLine_10.result().setName("SketchLine_11")
Sketch_2.setCoincident(SketchLine_9.endPoint(), SketchLine_10.startPoint())

### Create SketchProjection
SketchProjection_5 = Sketch_2.addProjection(model.selection("VERTEX", "[Box_1_1/Back][ExtrusionCut_1_1/Modified_Face&Box_1_1/Left][ExtrusionCut_1_1/Modified_Face&Box_1_1/Top]"), False)
SketchPoint_3 = SketchProjection_5.createdFeature()
Sketch_2.setCoincident(SketchLine_10.endPoint(), SketchPoint_3.result())
Sketch_2.setVertical(SketchLine_10.result())

### Create SketchLine
SketchLine_11 = Sketch_2.addLine(0, 8, 9, 8)
SketchLine_11.setName("SketchLine_12")
SketchLine_11.result().setName("SketchLine_12")
Sketch_2.setCoincident(SketchLine_10.endPoint(), SketchLine_11.startPoint())

### Create SketchProjection
SketchProjection_6 = Sketch_2.addProjection(model.selection("VERTEX", "[ExtrusionCut_1_1/Modified_Face&Box_1_1/Left][ExtrusionCut_1_1/Modified_Face&Box_1_1/Top][ExtrusionCut_1_1/From_Face]"), False)
SketchPoint_4 = SketchProjection_6.createdFeature()
Sketch_2.setCoincident(SketchLine_11.endPoint(), SketchPoint_4.result())

### Create SketchLine
SketchLine_12 = Sketch_2.addLine(9, 8, 9, 6)
SketchLine_12.setName("SketchLine_13")
SketchLine_12.result().setName("SketchLine_13")
Sketch_2.setCoincident(SketchLine_11.endPoint(), SketchLine_12.startPoint())
Sketch_2.setCoincident(SketchLine_8.startPoint(), SketchLine_12.endPoint())
Sketch_2.setHorizontalDistance(SketchLine_9.endPoint(), SketchLine_9.startPoint(), 1)
Sketch_2.setVerticalDistance(SketchLine_9.startPoint(), SketchLine_8.startPoint(), 1)
model.do()

### Create ExtrusionCut
ExtrusionCut_2 = model.addExtrusionCut(Part_1_doc, [model.selection("FACE", "Sketch_2/Face-SketchLine_13r-SketchLine_12r-SketchLine_11r-SketchLine_10r-SketchLine_9r")], model.selection(), 0, 1, [model.selection("SOLID", "ExtrusionCut_1_1")])

### Create Sketch
Sketch_3 = model.addSketch(Part_1_doc, model.selection("FACE", "ExtrusionCut_2_1/Modified_Face&Box_1_1/Back"))

### Create SketchLine
SketchLine_13 = Sketch_3.addLine(1, -5, 9, -4)
SketchLine_13.setName("SketchLine_14")
SketchLine_13.result().setName("SketchLine_14")

### Create SketchProjection
SketchProjection_7 = Sketch_3.addProjection(model.selection("VERTEX", "[ExtrusionCut_2_1/Modified_Face&Box_1_1/Back][ExtrusionCut_2_1/Generated_Face&Sketch_2/SketchLine_10][ExtrusionCut_2_1/Modified_Face&ExtrusionCut_2_1/From_Face]"), False)
SketchPoint_5 = SketchProjection_7.createdFeature()
Sketch_3.setCoincident(SketchLine_13.startPoint(), SketchPoint_5.result())

### Create SketchLine
SketchLine_14 = Sketch_3.addLine(9, -4, 10, -4)
SketchLine_14.setName("SketchLine_15")
SketchLine_14.result().setName("SketchLine_15")
Sketch_3.setCoincident(SketchLine_13.endPoint(), SketchLine_14.startPoint())

### Create SketchProjection
SketchProjection_8 = Sketch_3.addProjection(model.selection("EDGE", "[ExtrusionCut_2_1/Modified_Face&Box_1_1/Back][Box_1_1/Right]"), False)
SketchLine_15 = SketchProjection_8.createdFeature()
SketchLine_15.setName("SketchLine_16")
SketchLine_15.result().setName("SketchLine_16")
Sketch_3.setCoincident(SketchLine_14.endPoint(), SketchLine_15.result())
Sketch_3.setHorizontal(SketchLine_14.result())

### Create SketchLine
SketchLine_16 = Sketch_3.addLine(10, -4, 10, -8)
SketchLine_16.setName("SketchLine_17")
SketchLine_16.result().setName("SketchLine_17")
Sketch_3.setCoincident(SketchLine_14.endPoint(), SketchLine_16.startPoint())
Sketch_3.setCoincident(SketchAPI_Line(SketchLine_15).endPoint(), SketchLine_16.endPoint())

### Create SketchLine
SketchLine_17 = Sketch_3.addLine(10, -8, 1, -8)
SketchLine_17.setName("SketchLine_18")
SketchLine_17.result().setName("SketchLine_18")
Sketch_3.setCoincident(SketchAPI_Line(SketchLine_15).endPoint(), SketchLine_17.startPoint())

### Create SketchProjection
SketchProjection_9 = Sketch_3.addProjection(model.selection("VERTEX", "[ExtrusionCut_2_1/Modified_Face&Box_1_1/Back][ExtrusionCut_2_1/Modified_Face&ExtrusionCut_2_1/From_Face][ExtrusionCut_2_1/Modified_Face&Box_1_1/Top]"), False)
SketchPoint_6 = SketchProjection_9.createdFeature()
Sketch_3.setCoincident(SketchLine_17.endPoint(), SketchPoint_6.result())

### Create SketchLine
SketchLine_18 = Sketch_3.addLine(1, -8, 1, -5)
SketchLine_18.setName("SketchLine_19")
SketchLine_18.result().setName("SketchLine_19")
Sketch_3.setCoincident(SketchLine_17.endPoint(), SketchLine_18.startPoint())
Sketch_3.setCoincident(SketchLine_13.startPoint(), SketchLine_18.endPoint())
Sketch_3.setHorizontalDistance(SketchLine_14.endPoint(), SketchLine_13.endPoint(), 1)
Sketch_3.setVerticalDistance(SketchLine_13.endPoint(), SketchAPI_Point(SketchPoint_5).coordinates(), 1)
model.do()

### Create ExtrusionCut
ExtrusionCut_3 = model.addExtrusionCut(Part_1_doc, [model.selection("FACE", "Sketch_3/Face-SketchLine_19r-SketchLine_18r-SketchLine_17r-SketchLine_15r-SketchLine_14r")], model.selection(), 0, 1, [model.selection("SOLID", "ExtrusionCut_2_1")])

### Create Sketch
Sketch_4 = model.addSketch(Part_1_doc, model.selection("FACE", "ExtrusionCut_3_1/Modified_Face&Box_1_1/Right"))

### Create SketchLine
SketchLine_19 = Sketch_4.addLine(1, -4, 9, -3)
SketchLine_19.setName("SketchLine_20")
SketchLine_19.result().setName("SketchLine_20")

### Create SketchProjection
SketchProjection_10 = Sketch_4.addProjection(model.selection("VERTEX", "[ExtrusionCut_3_1/Generated_Face&Sketch_3/SketchLine_15][ExtrusionCut_3_1/Modified_Face&Box_1_1/Right][ExtrusionCut_3_1/Modified_Face&ExtrusionCut_3_1/From_Face]"), False)
SketchPoint_7 = SketchProjection_10.createdFeature()
Sketch_4.setCoincident(SketchLine_19.startPoint(), SketchPoint_7.result())

### Create SketchLine
SketchLine_20 = Sketch_4.addLine(9, -3, 10, -3)
SketchLine_20.setName("SketchLine_21")
SketchLine_20.result().setName("SketchLine_21")
Sketch_4.setCoincident(SketchLine_19.endPoint(), SketchLine_20.startPoint())
Sketch_4.setHorizontal(SketchLine_20.result())

### Create SketchLine
SketchLine_21 = Sketch_4.addLine(10, -3, 10, -8)
SketchLine_21.setName("SketchLine_22")
SketchLine_21.result().setName("SketchLine_22")
Sketch_4.setCoincident(SketchLine_20.endPoint(), SketchLine_21.startPoint())

### Create SketchProjection
SketchProjection_11 = Sketch_4.addProjection(model.selection("VERTEX", "[ExtrusionCut_3_1/Modified_Face&Box_1_1/Right][ExtrusionCut_1_1/Modified_Face&Box_1_1/Front][ExtrusionCut_3_1/Modified_Face&Box_1_1/Top]"), False)
SketchPoint_8 = SketchProjection_11.createdFeature()
Sketch_4.setCoincident(SketchLine_21.endPoint(), SketchPoint_8.result())
Sketch_4.setVertical(SketchLine_21.result())

### Create SketchLine
SketchLine_22 = Sketch_4.addLine(10, -8, 1, -8)
SketchLine_22.setName("SketchLine_23")
SketchLine_22.result().setName("SketchLine_23")
Sketch_4.setCoincident(SketchLine_21.endPoint(), SketchLine_22.startPoint())

### Create SketchProjection
SketchProjection_12 = Sketch_4.addProjection(model.selection("VERTEX", "[ExtrusionCut_3_1/Modified_Face&Box_1_1/Right][ExtrusionCut_3_1/Modified_Face&ExtrusionCut_3_1/From_Face][ExtrusionCut_3_1/Modified_Face&Box_1_1/Top]"), False)
SketchPoint_9 = SketchProjection_12.createdFeature()
Sketch_4.setCoincident(SketchLine_22.endPoint(), SketchPoint_9.result())

### Create SketchLine
SketchLine_23 = Sketch_4.addLine(1, -8, 1, -4)
SketchLine_23.setName("SketchLine_24")
SketchLine_23.result().setName("SketchLine_24")
Sketch_4.setCoincident(SketchLine_22.endPoint(), SketchLine_23.startPoint())
Sketch_4.setCoincident(SketchLine_19.startPoint(), SketchLine_23.endPoint())
Sketch_4.setHorizontalDistance(SketchLine_19.endPoint(), SketchLine_20.endPoint(), 1)
Sketch_4.setVerticalDistance(SketchLine_19.endPoint(), SketchAPI_Point(SketchPoint_7).coordinates(), 1)
model.do()

### Create ExtrusionCut
ExtrusionCut_4 = model.addExtrusionCut(Part_1_doc, [model.selection("FACE", "Sketch_4/Face-SketchLine_24r-SketchLine_23r-SketchLine_22r-SketchLine_21r-SketchLine_20r")], model.selection(), 0, 1, [model.selection("SOLID", "ExtrusionCut_3_1")])

### Create Sketch
Sketch_5 = model.addSketch(Part_1_doc, model.selection("FACE", "ExtrusionCut_4_1/Modified_Face&Box_1_1/Front"))

### Create SketchLine
SketchLine_24 = Sketch_5.addLine(9, 3, 2, 2)
SketchLine_24.setName("SketchLine_25")
SketchLine_24.result().setName("SketchLine_25")

### Create SketchProjection
SketchProjection_13 = Sketch_5.addProjection(model.selection("VERTEX", "[ExtrusionCut_4_1/Modified_Face&Box_1_1/Front][ExtrusionCut_4_1/Generated_Face&Sketch_4/SketchLine_21][ExtrusionCut_4_1/Modified_Face&ExtrusionCut_4_1/From_Face]"), False)
SketchPoint_10 = SketchProjection_13.createdFeature()
Sketch_5.setCoincident(SketchLine_24.startPoint(), SketchPoint_10.result())

### Create SketchLine
SketchLine_25 = Sketch_5.addLine(2, 2, 0, 2)
SketchLine_25.setName("SketchLine_26")
SketchLine_25.result().setName("SketchLine_26")
Sketch_5.setCoincident(SketchLine_24.endPoint(), SketchLine_25.startPoint())

### Create SketchProjection
SketchProjection_14 = Sketch_5.addProjection(model.selection("EDGE", "[ExtrusionCut_2_1/Modified_Face&Box_1_1/Left][ExtrusionCut_4_1/Modified_Face&Box_1_1/Front]"), False)
SketchLine_26 = SketchProjection_14.createdFeature()
SketchLine_26.setName("SketchLine_27")
SketchLine_26.result().setName("SketchLine_27")
Sketch_5.setCoincident(SketchLine_25.endPoint(), SketchLine_26.result())
Sketch_5.setHorizontal(SketchLine_25.result())

### Create SketchLine
SketchLine_27 = Sketch_5.addLine(0, 2, 0, 5)
SketchLine_27.setName("SketchLine_28")
SketchLine_27.result().setName("SketchLine_28")
Sketch_5.setCoincident(SketchLine_25.endPoint(), SketchLine_27.startPoint())
Sketch_5.setCoincident(SketchLine_27.endPoint(), SketchLine_26.result())

### Create SketchLine
SketchLine_28 = Sketch_5.addLine(0, 5, 1, 5)
SketchLine_28.setName("SketchLine_29")
SketchLine_28.result().setName("SketchLine_29")
Sketch_5.setCoincident(SketchLine_27.endPoint(), SketchLine_28.startPoint())
Sketch_5.setHorizontal(SketchLine_28.result())

### Create SketchLine
SketchLine_29 = Sketch_5.addLine(1, 5, 8, 6)
SketchLine_29.setName("SketchLine_30")
SketchLine_29.result().setName("SketchLine_30")
Sketch_5.setCoincident(SketchLine_28.endPoint(), SketchLine_29.startPoint())

### Create SketchLine
SketchLine_30 = Sketch_5.addLine(8, 6, 9, 6)
SketchLine_30.setName("SketchLine_31")
SketchLine_30.result().setName("SketchLine_31")
Sketch_5.setCoincident(SketchLine_29.endPoint(), SketchLine_30.startPoint())

### Create SketchProjection
SketchProjection_15 = Sketch_5.addProjection(model.selection("EDGE", "[ExtrusionCut_4_1/Modified_Face&Box_1_1/Front][ExtrusionCut_4_1/Modified_Face&ExtrusionCut_4_1/From_Face]"), False)
SketchLine_31 = SketchProjection_15.createdFeature()
SketchLine_31.setName("SketchLine_32")
SketchLine_31.result().setName("SketchLine_32")
Sketch_5.setCoincident(SketchLine_30.endPoint(), SketchLine_31.result())
Sketch_5.setHorizontal(SketchLine_30.result())

### Create SketchLine
SketchLine_32 = Sketch_5.addLine(9, 6, 9, 3)
SketchLine_32.setName("SketchLine_33")
SketchLine_32.result().setName("SketchLine_33")
Sketch_5.setCoincident(SketchLine_30.endPoint(), SketchLine_32.startPoint())
Sketch_5.setCoincident(SketchLine_24.startPoint(), SketchLine_32.endPoint())
Sketch_5.setHorizontalDistance(SketchLine_29.endPoint(), SketchLine_32.startPoint(), 1)
Sketch_5.setHorizontalDistance(SketchLine_28.endPoint(), SketchLine_27.endPoint(), 1)
Sketch_5.setHorizontalDistance(SketchLine_25.startPoint(), SketchLine_25.endPoint(), 2)
Sketch_5.setVerticalDistance(SketchLine_28.endPoint(), SketchLine_29.endPoint(), 1)
Sketch_5.setVerticalDistance(SketchLine_24.startPoint(), SketchLine_25.startPoint(), 1)
Sketch_5.setVerticalDistance(SketchLine_27.endPoint(), SketchLine_25.endPoint(), 3)
model.do()

### Create ExtrusionCut
ExtrusionCut_5 = model.addExtrusionCut(Part_1_doc, [model.selection("FACE", "Sketch_5/Face-SketchLine_33r-SketchLine_31r-SketchLine_30r-SketchLine_29r-SketchLine_28r-SketchLine_26r-SketchLine_25r")], model.selection(), 0, 1, [model.selection("SOLID", "ExtrusionCut_4_1")])

### Create Sketch
Sketch_6 = model.addSketch(Part_1_doc, model.selection("FACE", "(ExtrusionCut_5_1/Modified_Face&Box_1_1/Left)(ExtrusionCut_4_1/Modified_Face&Box_1_1/Right)(Box_1_1/Bottom)(ExtrusionCut_5_1/Generated_Face&Sketch_5/SketchLine_26)(ExtrusionCut_5_1/Modified_Face&Sketch_4/SketchLine_21)(ExtrusionCut_5_1/Generated_Face&Sketch_5/SketchLine_25)"))

### Create SketchLine
SketchLine_33 = Sketch_6.addLine(2, 0, 2, 1)
SketchLine_33.setName("SketchLine_34")
SketchLine_33.result().setName("SketchLine_34")

### Create SketchProjection
SketchProjection_16 = Sketch_6.addProjection(model.selection("EDGE", "[Box_1_1/Bottom][(ExtrusionCut_5_1/Modified_Face&Box_1_1/Left)(ExtrusionCut_4_1/Modified_Face&Box_1_1/Right)(Box_1_1/Bottom)(ExtrusionCut_5_1/Generated_Face&Sketch_5/SketchLine_26)(ExtrusionCut_5_1/Modified_Face&Sketch_4/SketchLine_21)(ExtrusionCut_5_1/Generated_Face&Sketch_5/SketchLine_25)]"), False)
SketchLine_34 = SketchProjection_16.createdFeature()
SketchLine_34.setName("SketchLine_35")
SketchLine_34.result().setName("SketchLine_35")
Sketch_6.setCoincident(SketchLine_33.startPoint(), SketchLine_34.result())
Sketch_6.setVertical(SketchLine_33.result())

### Create SketchLine
SketchLine_35 = Sketch_6.addLine(2, 1, 9, 2)
SketchLine_35.setName("SketchLine_36")
SketchLine_35.result().setName("SketchLine_36")
Sketch_6.setCoincident(SketchLine_33.endPoint(), SketchLine_35.startPoint())

### Create SketchLine
SketchLine_36 = Sketch_6.addLine(9, 2, 10, 2)
SketchLine_36.setName("SketchLine_37")
SketchLine_36.result().setName("SketchLine_37")
Sketch_6.setCoincident(SketchLine_35.endPoint(), SketchLine_36.startPoint())

### Create SketchProjection
SketchProjection_17 = Sketch_6.addProjection(model.selection("EDGE", "[ExtrusionCut_4_1/Modified_Face&Box_1_1/Right][(ExtrusionCut_5_1/Modified_Face&Box_1_1/Left)(ExtrusionCut_4_1/Modified_Face&Box_1_1/Right)(Box_1_1/Bottom)(ExtrusionCut_5_1/Generated_Face&Sketch_5/SketchLine_26)(ExtrusionCut_5_1/Modified_Face&Sketch_4/SketchLine_21)(ExtrusionCut_5_1/Generated_Face&Sketch_5/SketchLine_25)]"), False)
SketchLine_37 = SketchProjection_17.createdFeature()
SketchLine_37.setName("SketchLine_38")
SketchLine_37.result().setName("SketchLine_38")
Sketch_6.setCoincident(SketchLine_36.endPoint(), SketchLine_37.result())
Sketch_6.setHorizontal(SketchLine_36.result())

### Create SketchLine
SketchLine_38 = Sketch_6.addLine(10, 2, 10, 0)
SketchLine_38.setName("SketchLine_39")
SketchLine_38.result().setName("SketchLine_39")
Sketch_6.setCoincident(SketchLine_36.endPoint(), SketchLine_38.startPoint())
Sketch_6.setCoincident(SketchAPI_Line(SketchLine_34).endPoint(), SketchLine_38.endPoint())

### Create SketchLine
SketchLine_39 = Sketch_6.addLine(10, 0, 2, 0)
SketchLine_39.setName("SketchLine_40")
SketchLine_39.result().setName("SketchLine_40")
Sketch_6.setCoincident(SketchAPI_Line(SketchLine_34).endPoint(), SketchLine_39.startPoint())
Sketch_6.setCoincident(SketchLine_33.startPoint(), SketchLine_39.endPoint())
Sketch_6.setHorizontalDistance(SketchLine_35.endPoint(), SketchLine_38.startPoint(), 1)
Sketch_6.setVerticalDistance(SketchLine_33.endPoint(), SketchLine_33.startPoint(), 1)
Sketch_6.setVerticalDistance(SketchLine_33.endPoint(), SketchLine_35.endPoint(), 1)
Sketch_6.setHorizontalDistance(SketchLine_33.startPoint(), SketchAPI_Line(SketchLine_34).startPoint(), 2)
model.do()

### Create ExtrusionCut
ExtrusionCut_6 = model.addExtrusionCut(Part_1_doc, [model.selection("WIRE", "Sketch_6/Face-SketchLine_40r-SketchLine_39r-SketchLine_37r-SketchLine_36r-SketchLine_34r_wire")], model.selection(), 0, 1, [model.selection("SOLID", "ExtrusionCut_5_1")])

### Create Sketch
Sketch_7 = model.addSketch(Part_1_doc, model.selection("FACE", "ExtrusionCut_5_1/Modified_Face&Box_1_1/Left"))

### Create SketchLine
SketchLine_40 = Sketch_7.addLine(9, 5, 1, 4)
SketchLine_40.setName("SketchLine_41")
SketchLine_40.result().setName("SketchLine_41")

### Create SketchProjection
SketchProjection_18 = Sketch_7.addProjection(model.selection("VERTEX", "[ExtrusionCut_5_1/Modified_Face&Box_1_1/Left][ExtrusionCut_5_1/Modified_Face&ExtrusionCut_5_1/From_Face][ExtrusionCut_5_1/Generated_Face&Sketch_5/SketchLine_29]"), False)
SketchPoint_11 = SketchProjection_18.createdFeature()
Sketch_7.setCoincident(SketchLine_40.startPoint(), SketchPoint_11.result())

### Create SketchLine
SketchLine_41 = Sketch_7.addLine(1, 4, 0, 4)
SketchLine_41.setName("SketchLine_42")
SketchLine_41.result().setName("SketchLine_42")
Sketch_7.setCoincident(SketchLine_40.endPoint(), SketchLine_41.startPoint())

### Create SketchProjection
SketchProjection_19 = Sketch_7.addProjection(model.selection("EDGE", "[ExtrusionCut_3_1/Modified_Face&Box_1_1/Back][ExtrusionCut_5_1/Modified_Face&Box_1_1/Left]"), False)
SketchLine_42 = SketchProjection_19.createdFeature()
SketchLine_42.setName("SketchLine_43")
SketchLine_42.result().setName("SketchLine_43")
Sketch_7.setCoincident(SketchLine_41.endPoint(), SketchLine_42.result())
Sketch_7.setHorizontal(SketchLine_41.result())

### Create SketchLine
SketchLine_43 = Sketch_7.addLine(0, 4, 0, 0)
SketchLine_43.setName("SketchLine_44")
SketchLine_43.result().setName("SketchLine_44")
Sketch_7.setCoincident(SketchLine_41.endPoint(), SketchLine_43.startPoint())
Sketch_7.setCoincident(SketchAPI_Line(SketchLine_42).startPoint(), SketchLine_43.endPoint())

### Create SketchLine
SketchLine_44 = Sketch_7.addLine(0, 0, 10, 0)
SketchLine_44.setName("SketchLine_45")
SketchLine_44.result().setName("SketchLine_45")
Sketch_7.setCoincident(SketchAPI_Line(SketchLine_42).startPoint(), SketchLine_44.startPoint())

### Create SketchProjection
SketchProjection_20 = Sketch_7.addProjection(model.selection("VERTEX", "[ExtrusionCut_5_1/Modified_Face&Box_1_1/Left][ExtrusionCut_6_1/Modified_Face&Box_1_1/Bottom][ExtrusionCut_6_1/Modified_Face&Box_1_1/Front]"), False)
SketchPoint_12 = SketchProjection_20.createdFeature()
Sketch_7.setCoincident(SketchLine_44.endPoint(), SketchPoint_12.result())

### Create SketchLine
SketchLine_45 = Sketch_7.addLine(10, 0, 10, 2)
SketchLine_45.setName("SketchLine_46")
SketchLine_45.result().setName("SketchLine_46")
Sketch_7.setCoincident(SketchLine_44.endPoint(), SketchLine_45.startPoint())

### Create SketchProjection
SketchProjection_21 = Sketch_7.addProjection(model.selection("VERTEX", "[ExtrusionCut_5_1/Modified_Face&Box_1_1/Left][ExtrusionCut_6_1/Modified_Face&Box_1_1/Front][ExtrusionCut_5_1/Generated_Face&Sketch_5/SketchLine_26]"), False)
SketchPoint_13 = SketchProjection_21.createdFeature()
Sketch_7.setCoincident(SketchLine_45.endPoint(), SketchPoint_13.result())

### Create SketchLine
SketchLine_46 = Sketch_7.addLine(10, 2, 9, 2)
SketchLine_46.setName("SketchLine_47")
SketchLine_46.result().setName("SketchLine_47")
Sketch_7.setCoincident(SketchLine_45.endPoint(), SketchLine_46.startPoint())

### Create SketchProjection
SketchProjection_22 = Sketch_7.addProjection(model.selection("VERTEX", "[ExtrusionCut_5_1/Modified_Face&Box_1_1/Left][ExtrusionCut_5_1/Generated_Face&Sketch_5/SketchLine_26][ExtrusionCut_5_1/Modified_Face&ExtrusionCut_5_1/From_Face]"), False)
SketchPoint_14 = SketchProjection_22.createdFeature()
Sketch_7.setCoincident(SketchLine_46.endPoint(), SketchPoint_14.result())

### Create SketchLine
SketchLine_47 = Sketch_7.addLine(9, 2, 9, 5)
SketchLine_47.setName("SketchLine_48")
SketchLine_47.result().setName("SketchLine_48")
Sketch_7.setCoincident(SketchLine_46.endPoint(), SketchLine_47.startPoint())
Sketch_7.setCoincident(SketchLine_40.startPoint(), SketchLine_47.endPoint())
Sketch_7.setHorizontalDistance(SketchLine_43.startPoint(), SketchLine_41.startPoint(), 1)
Sketch_7.setVerticalDistance(SketchLine_41.startPoint(), SketchLine_40.startPoint(), 1)
model.do()

### Create ExtrusionCut
ExtrusionCut_7 = model.addExtrusionCut(Part_1_doc, [model.selection("WIRE", "Sketch_7/Face-SketchLine_41r-SketchLine_42f-SketchLine_44f-SketchLine_45f-SketchLine_46f-SketchLine_47f-SketchLine_48f_wire")], model.selection(), 0, 1, [model.selection("SOLID", "ExtrusionCut_6_1")])

### Create Sketch
Sketch_8 = model.addSketch(Part_1_doc, model.selection("FACE", "ExtrusionCut_7_1/Modified_Face&Box_1_1/Back"))

### Create SketchLine
SketchLine_48 = Sketch_8.addLine(1, -4, 9, -3)
SketchLine_48.setName("SketchLine_49")
SketchLine_48.result().setName("SketchLine_49")

### Create SketchProjection
SketchProjection_23 = Sketch_8.addProjection(model.selection("VERTEX", "[ExtrusionCut_7_1/Modified_Face&Box_1_1/Back][ExtrusionCut_7_1/Modified_Face&ExtrusionCut_7_1/From_Face][ExtrusionCut_7_1/Generated_Face&Sketch_7/SketchLine_42]"), False)
SketchPoint_15 = SketchProjection_23.createdFeature()
Sketch_8.setCoincident(SketchLine_48.startPoint(), SketchPoint_15.result())

### Create SketchLine
SketchLine_49 = Sketch_8.addLine(9, -3, 10, -3)
SketchLine_49.setName("SketchLine_50")
SketchLine_49.result().setName("SketchLine_50")
Sketch_8.setCoincident(SketchLine_48.endPoint(), SketchLine_49.startPoint())

### Create SketchProjection
SketchProjection_24 = Sketch_8.addProjection(model.selection("EDGE", "[ExtrusionCut_7_1/Modified_Face&Box_1_1/Back][ExtrusionCut_6_1/Modified_Face&Box_1_1/Right]"), False)
SketchLine_50 = SketchProjection_24.createdFeature()
SketchLine_50.setName("SketchLine_51")
SketchLine_50.result().setName("SketchLine_51")
Sketch_8.setCoincident(SketchLine_49.endPoint(), SketchLine_50.result())
Sketch_8.setHorizontal(SketchLine_49.result())

### Create SketchLine
SketchLine_51 = Sketch_8.addLine(10, -3, 10, 0)
SketchLine_51.setName("SketchLine_52")
SketchLine_51.result().setName("SketchLine_52")
Sketch_8.setCoincident(SketchLine_49.endPoint(), SketchLine_51.startPoint())
Sketch_8.setCoincident(SketchAPI_Line(SketchLine_50).startPoint(), SketchLine_51.endPoint())

### Create SketchLine
SketchLine_52 = Sketch_8.addLine(10, 0, 1, 0)
SketchLine_52.setName("SketchLine_53")
SketchLine_52.result().setName("SketchLine_53")
Sketch_8.setCoincident(SketchAPI_Line(SketchLine_50).startPoint(), SketchLine_52.startPoint())

### Create SketchProjection
SketchProjection_25 = Sketch_8.addProjection(model.selection("VERTEX", "[ExtrusionCut_7_1/Modified_Face&Box_1_1/Back][ExtrusionCut_7_1/Modified_Face&Box_1_1/Bottom][ExtrusionCut_7_1/Modified_Face&ExtrusionCut_7_1/From_Face]"), False)
SketchPoint_16 = SketchProjection_25.createdFeature()
Sketch_8.setCoincident(SketchLine_52.endPoint(), SketchPoint_16.result())

### Create SketchLine
SketchLine_53 = Sketch_8.addLine(1, 0, 1, -4)
SketchLine_53.setName("SketchLine_54")
SketchLine_53.result().setName("SketchLine_54")
Sketch_8.setCoincident(SketchLine_52.endPoint(), SketchLine_53.startPoint())
Sketch_8.setCoincident(SketchLine_48.startPoint(), SketchLine_53.endPoint())
Sketch_8.setHorizontalDistance(SketchLine_51.startPoint(), SketchLine_48.endPoint(), 1)
Sketch_8.setVerticalDistance(SketchLine_48.endPoint(), SketchLine_53.endPoint(), 1)
model.do()

### Create ExtrusionCut
ExtrusionCut_8 = model.addExtrusionCut(Part_1_doc, [model.selection("FACE", "Sketch_8/Face-SketchLine_49r-SketchLine_50f-SketchLine_52f-SketchLine_53f-SketchLine_54f")], model.selection(), 0, 1, [model.selection("SOLID", "ExtrusionCut_7_1")])

### Create Sketch
Sketch_9 = model.addSketch(Part_1_doc, model.selection("FACE", "ExtrusionCut_8_1/Modified_Face&Box_1_1/Right"))

### Create SketchLine
SketchLine_54 = Sketch_9.addLine(9, -2, 1, -3)
SketchLine_54.setName("SketchLine_55")
SketchLine_54.result().setName("SketchLine_55")

### Create SketchProjection
SketchProjection_26 = Sketch_9.addProjection(model.selection("VERTEX", "[ExtrusionCut_8_1/Modified_Face&Box_1_1/Right][ExtrusionCut_6_1/From_Face][ExtrusionCut_6_1/Generated_Face&Sketch_6/SketchLine_37]"), False)
SketchPoint_17 = SketchProjection_26.createdFeature()
Sketch_9.setCoincident(SketchLine_54.startPoint(), SketchPoint_17.result())

### Create SketchProjection
SketchProjection_27 = Sketch_9.addProjection(model.selection("VERTEX", "[ExtrusionCut_8_1/Modified_Face&Box_1_1/Right][ExtrusionCut_8_1/Generated_Face&Sketch_8/SketchLine_50][ExtrusionCut_8_1/Modified_Face&ExtrusionCut_8_1/From_Face]"), False)
SketchPoint_18 = SketchProjection_27.createdFeature()
Sketch_9.setCoincident(SketchLine_54.endPoint(), SketchPoint_18.result())

### Create SketchLine
SketchLine_55 = Sketch_9.addLine(1, -3, 1, 0)
SketchLine_55.setName("SketchLine_56")
SketchLine_55.result().setName("SketchLine_56")
Sketch_9.setCoincident(SketchLine_54.endPoint(), SketchLine_55.startPoint())

### Create SketchProjection
SketchProjection_28 = Sketch_9.addProjection(model.selection("VERTEX", "[ExtrusionCut_8_1/Modified_Face&Box_1_1/Right][ExtrusionCut_8_1/Modified_Face&ExtrusionCut_8_1/From_Face][ExtrusionCut_8_1/Modified_Face&Box_1_1/Bottom]"), False)
SketchPoint_19 = SketchProjection_28.createdFeature()
Sketch_9.setCoincident(SketchLine_55.endPoint(), SketchPoint_19.result())

### Create SketchLine
SketchLine_56 = Sketch_9.addLine(1, 0, 9, 0)
SketchLine_56.setName("SketchLine_57")
SketchLine_56.result().setName("SketchLine_57")
Sketch_9.setCoincident(SketchLine_55.endPoint(), SketchLine_56.startPoint())

### Create SketchProjection
SketchProjection_29 = Sketch_9.addProjection(model.selection("VERTEX", "[ExtrusionCut_8_1/Modified_Face&Box_1_1/Right][ExtrusionCut_8_1/Modified_Face&Box_1_1/Bottom][ExtrusionCut_6_1/From_Face]"), False)
SketchPoint_20 = SketchProjection_29.createdFeature()
Sketch_9.setCoincident(SketchLine_56.endPoint(), SketchPoint_20.result())

### Create SketchLine
SketchLine_57 = Sketch_9.addLine(9, 0, 9, -2)
SketchLine_57.setName("SketchLine_58")
SketchLine_57.result().setName("SketchLine_58")
Sketch_9.setCoincident(SketchLine_56.endPoint(), SketchLine_57.startPoint())
Sketch_9.setCoincident(SketchLine_54.startPoint(), SketchLine_57.endPoint())
model.do()

### Create ExtrusionCut
ExtrusionCut_9 = model.addExtrusionCut(Part_1_doc, [model.selection("WIRE", "Sketch_9/Face-SketchLine_58r-SketchLine_57r-SketchLine_56r-SketchLine_55r_wire")], model.selection(), 0, 1, [model.selection("SOLID", "ExtrusionCut_8_1")])

model.end()

###
### SHAPERSTUDY component
###

model.publishToShaperStudy()
import SHAPERSTUDY
ExtrusionCut_9_1, = SHAPERSTUDY.shape(model.featureStringId(ExtrusionCut_9))

if salome.sg.hasDesktop():
  salome.sg.updateObjBrowser()
