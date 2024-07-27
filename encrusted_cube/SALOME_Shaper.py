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
model.addParameter(Part_1_doc, "cube_length", '4.25')

### Create Box
Box_1 = model.addBox(Part_1_doc, 10, 10, 10)

### Create Sketch
Sketch_1 = model.addSketch(Part_1_doc, model.selection("FACE", "Box_1_1/Left"))

### Create SketchPoint
SketchPoint_1 = Sketch_1.addPoint(5, 10)

### Create SketchProjection
SketchProjection_1 = Sketch_1.addProjection(model.selection("EDGE", "[Box_1_1/Left][Box_1_1/Top]"), False)
SketchLine_1 = SketchProjection_1.createdFeature()
Sketch_1.setCoincident(SketchPoint_1.coordinates(), SketchLine_1.result())

### Create SketchPoint
SketchPoint_2 = Sketch_1.addPoint(10, 5)

### Create SketchProjection
SketchProjection_2 = Sketch_1.addProjection(model.selection("EDGE", "[Box_1_1/Front][Box_1_1/Left]"), False)
SketchLine_2 = SketchProjection_2.createdFeature()
Sketch_1.setCoincident(SketchPoint_2.coordinates(), SketchLine_2.result())
Sketch_1.setMiddlePoint(SketchPoint_1.coordinates(), SketchLine_1.result())
Sketch_1.setMiddlePoint(SketchPoint_2.coordinates(), SketchLine_2.result())

### Create SketchArc
SketchArc_1 = Sketch_1.addArc(10, 10, 5, 10, 10, 5, False)
Sketch_1.setCoincident(SketchAPI_Line(SketchLine_1).endPoint(), SketchArc_1.center())
Sketch_1.setCoincident(SketchPoint_1.coordinates(), SketchArc_1.startPoint())
Sketch_1.setCoincident(SketchLine_2.result(), SketchArc_1.endPoint())

### Create SketchLine
SketchLine_3 = Sketch_1.addLine(5, 10, 10, 10)
Sketch_1.setCoincident(SketchPoint_1.coordinates(), SketchLine_3.startPoint())
Sketch_1.setCoincident(SketchAPI_Line(SketchLine_1).endPoint(), SketchLine_3.endPoint())

### Create SketchLine
SketchLine_4 = Sketch_1.addLine(10, 10, 10, 5)
Sketch_1.setCoincident(SketchAPI_Line(SketchLine_1).endPoint(), SketchLine_4.startPoint())
Sketch_1.setCoincident(SketchPoint_2.coordinates(), SketchLine_4.endPoint())

### Create SketchPoint
SketchPoint_3 = Sketch_1.addPoint(5.75, 10)
SketchPoint_3.setName("SketchPoint_7")
SketchPoint_3.result().setName("SketchPoint_7")
SketchPoint_3.setAuxiliary(True)
Sketch_1.setCoincident(SketchPoint_3.coordinates(), SketchLine_1.result())

### Create SketchPoint
SketchPoint_4 = Sketch_1.addPoint(5.75, 10)
SketchPoint_4.setName("SketchPoint_8")
SketchPoint_4.result().setName("SketchPoint_8")
SketchPoint_4.setAuxiliary(True)
Sketch_1.setCoincident(SketchPoint_3.coordinates(), SketchPoint_4.coordinates())

### Create SketchPoint
SketchPoint_5 = Sketch_1.addPoint(10, 5.75)
SketchPoint_5.setName("SketchPoint_9")
SketchPoint_5.result().setName("SketchPoint_9")
Sketch_1.setCoincident(SketchPoint_5.coordinates(), SketchLine_2.result())

### Create SketchPoint
SketchPoint_6 = Sketch_1.addPoint(5.75, 7.366086561658167)
SketchPoint_6.setName("SketchPoint_10")
SketchPoint_6.result().setName("SketchPoint_10")
Sketch_1.setCoincident(SketchPoint_6.coordinates(), SketchArc_1.results()[1])

### Create SketchPoint
SketchPoint_7 = Sketch_1.addPoint(6.464466094062259, 6.464466094062259)
SketchPoint_7.setName("SketchPoint_11")
SketchPoint_7.result().setName("SketchPoint_11")
Sketch_1.setCoincident(SketchPoint_7.coordinates(), SketchArc_1.results()[1])

### Create SketchPoint
SketchPoint_8 = Sketch_1.addPoint(7.366086561658168, 5.75)
SketchPoint_8.setName("SketchPoint_12")
SketchPoint_8.result().setName("SketchPoint_12")
Sketch_1.setCoincident(SketchPoint_8.coordinates(), SketchArc_1.results()[1])

### Create SketchPoint
SketchPoint_9 = Sketch_1.addPoint(10, 5.75)
SketchPoint_9.setName("SketchPoint_13")
SketchPoint_9.result().setName("SketchPoint_13")
SketchPoint_9.setAuxiliary(True)
Sketch_1.setCoincident(SketchPoint_5.coordinates(), SketchPoint_9.coordinates())

### Create SketchLine
SketchLine_5 = Sketch_1.addLine(5.75, 7.366086561658167, 5.75, 10)
SketchLine_5.setName("SketchLine_13")
SketchLine_5.result().setName("SketchLine_13")
SketchLine_5.setAuxiliary(True)
Sketch_1.setCoincident(SketchPoint_6.coordinates(), SketchLine_5.startPoint())
Sketch_1.setCoincident(SketchPoint_3.coordinates(), SketchLine_5.endPoint())

### Create SketchLine
SketchLine_6 = Sketch_1.addLine(7.366086561658168, 5.75, 10, 5.75)
SketchLine_6.setName("SketchLine_14")
SketchLine_6.result().setName("SketchLine_14")
SketchLine_6.setAuxiliary(True)
Sketch_1.setCoincident(SketchPoint_8.coordinates(), SketchLine_6.startPoint())
Sketch_1.setCoincident(SketchPoint_5.coordinates(), SketchLine_6.endPoint())
Sketch_1.setHorizontal(SketchLine_6.result())
Sketch_1.setVertical(SketchLine_5.result())
Sketch_1.setHorizontalDistance(SketchPoint_4.coordinates(), SketchAPI_Line(SketchLine_2).endPoint(), "cube_length")
Sketch_1.setVerticalDistance(SketchLine_6.endPoint(), SketchAPI_Line(SketchLine_2).endPoint(), "cube_length")

### Create SketchLine
SketchLine_7 = Sketch_1.addLine(0, 0, 10, 10)
SketchLine_7.setName("SketchLine_15")
SketchLine_7.result().setName("SketchLine_15")
SketchLine_7.setAuxiliary(True)

### Create SketchProjection
SketchProjection_3 = Sketch_1.addProjection(model.selection("VERTEX", "[Box_1_1/Back][Box_1_1/Left][Box_1_1/Bottom]"), False)
SketchProjection_3.setName("SketchProjection_7")
SketchProjection_3.result().setName("SketchProjection_7")
SketchPoint_10 = SketchProjection_3.createdFeature()
SketchPoint_10.setName("SketchPoint_14")
SketchPoint_10.result().setName("SketchPoint_14")
Sketch_1.setCoincident(SketchLine_7.startPoint(), SketchPoint_10.result())
Sketch_1.setCoincident(SketchAPI_Line(SketchLine_1).endPoint(), SketchLine_7.endPoint())
Sketch_1.setCoincident(SketchPoint_7.coordinates(), SketchLine_7.result())
model.do()

### Create ExtrusionCut
ExtrusionCut_1 = model.addExtrusionCut(Part_1_doc, [model.selection("FACE", "Sketch_1/Face-SketchArc_1_2f-SketchLine_4r-SketchLine_3r")], model.selection(), 0, 10, [model.selection("SOLID", "Box_1_1")])

### Create Sketch
Sketch_2 = model.addSketch(Part_1_doc, model.selection("FACE", "Box_1_1/Back"))

### Create SketchPoint
SketchPoint_11 = Sketch_2.addPoint(5, -10)
SketchPoint_11.setName("SketchPoint_3")
SketchPoint_11.result().setName("SketchPoint_3")

### Create SketchProjection
SketchProjection_4 = Sketch_2.addProjection(model.selection("EDGE", "[Box_1_1/Back][ExtrusionCut_1_1/Modified_Face&Box_1_1/Top]"), False)
SketchProjection_4.setName("SketchProjection_3")
SketchProjection_4.result().setName("SketchProjection_3")
SketchLine_8 = SketchProjection_4.createdFeature()
SketchLine_8.setName("SketchLine_5")
SketchLine_8.result().setName("SketchLine_5")
Sketch_2.setCoincident(SketchPoint_11.coordinates(), SketchLine_8.result())

### Create SketchPoint
SketchPoint_12 = Sketch_2.addPoint(10, -5)
SketchPoint_12.setName("SketchPoint_4")
SketchPoint_12.result().setName("SketchPoint_4")

### Create SketchProjection
SketchProjection_5 = Sketch_2.addProjection(model.selection("EDGE", "[Box_1_1/Back][ExtrusionCut_1_1/Modified_Face&Box_1_1/Right]"), False)
SketchProjection_5.setName("SketchProjection_4")
SketchProjection_5.result().setName("SketchProjection_4")
SketchLine_9 = SketchProjection_5.createdFeature()
SketchLine_9.setName("SketchLine_6")
SketchLine_9.result().setName("SketchLine_6")
Sketch_2.setCoincident(SketchPoint_12.coordinates(), SketchLine_9.result())
Sketch_2.setMiddlePoint(SketchPoint_11.coordinates(), SketchLine_8.result())
Sketch_2.setMiddlePoint(SketchPoint_12.coordinates(), SketchLine_9.result())

### Create SketchArc
SketchArc_2 = Sketch_2.addArc(10, -10, 10, -5, 5, -9.999999999999932, False)
Sketch_2.setCoincident(SketchAPI_Line(SketchLine_8).endPoint(), SketchArc_2.center())
Sketch_2.setCoincident(SketchPoint_12.coordinates(), SketchArc_2.startPoint())
Sketch_2.setCoincident(SketchLine_8.result(), SketchArc_2.endPoint())

### Create SketchLine
SketchLine_10 = Sketch_2.addLine(10, -10, 5, -10)
SketchLine_10.setName("SketchLine_7")
SketchLine_10.result().setName("SketchLine_7")
Sketch_2.setCoincident(SketchAPI_Line(SketchLine_8).endPoint(), SketchLine_10.startPoint())
Sketch_2.setCoincident(SketchPoint_11.coordinates(), SketchLine_10.endPoint())

### Create SketchLine
SketchLine_11 = Sketch_2.addLine(10, -10, 10, -5)
SketchLine_11.setName("SketchLine_8")
SketchLine_11.result().setName("SketchLine_8")
Sketch_2.setCoincident(SketchAPI_Line(SketchLine_8).endPoint(), SketchLine_11.startPoint())
Sketch_2.setCoincident(SketchPoint_12.coordinates(), SketchLine_11.endPoint())

### Create SketchPoint
SketchPoint_13 = Sketch_2.addPoint(5.75, -10)
SketchPoint_13.setName("SketchPoint_15")
SketchPoint_13.result().setName("SketchPoint_15")
SketchPoint_13.setAuxiliary(True)
Sketch_2.setCoincident(SketchPoint_13.coordinates(), SketchLine_10.result())

### Create SketchPoint
SketchPoint_14 = Sketch_2.addPoint(10, -5.75)
SketchPoint_14.setName("SketchPoint_16")
SketchPoint_14.result().setName("SketchPoint_16")
Sketch_2.setCoincident(SketchPoint_14.coordinates(), SketchLine_11.result())

### Create SketchPoint
SketchPoint_15 = Sketch_2.addPoint(7.366086561658168, -5.75)
SketchPoint_15.setName("SketchPoint_17")
SketchPoint_15.result().setName("SketchPoint_17")
Sketch_2.setCoincident(SketchPoint_15.coordinates(), SketchArc_2.results()[1])

### Create SketchPoint
SketchPoint_16 = Sketch_2.addPoint(5.75, -7.366086561658167)
SketchPoint_16.setName("SketchPoint_18")
SketchPoint_16.result().setName("SketchPoint_18")
Sketch_2.setCoincident(SketchPoint_16.coordinates(), SketchArc_2.results()[1])

### Create SketchPoint
SketchPoint_17 = Sketch_2.addPoint(6.464466094067262, -6.464466094067262)
SketchPoint_17.setName("SketchPoint_19")
SketchPoint_17.result().setName("SketchPoint_19")
Sketch_2.setCoincident(SketchPoint_17.coordinates(), SketchArc_2.results()[1])

### Create SketchLine
SketchLine_12 = Sketch_2.addLine(5.75, -10, 5.75, -7.366086561658167)
SketchLine_12.setName("SketchLine_16")
SketchLine_12.result().setName("SketchLine_16")
SketchLine_12.setAuxiliary(True)
Sketch_2.setCoincident(SketchPoint_13.coordinates(), SketchLine_12.startPoint())
Sketch_2.setCoincident(SketchPoint_16.coordinates(), SketchLine_12.endPoint())

### Create SketchLine
SketchLine_13 = Sketch_2.addLine(10, -5.75, 7.366086561658168, -5.75)
SketchLine_13.setName("SketchLine_17")
SketchLine_13.result().setName("SketchLine_17")
SketchLine_13.setAuxiliary(True)
Sketch_2.setCoincident(SketchPoint_14.coordinates(), SketchLine_13.startPoint())
Sketch_2.setCoincident(SketchPoint_15.coordinates(), SketchLine_13.endPoint())
Sketch_2.setHorizontalDistance(SketchLine_12.startPoint(), SketchAPI_Line(SketchLine_9).endPoint(), "cube_length")
Sketch_2.setVerticalDistance(SketchLine_13.startPoint(), SketchAPI_Line(SketchLine_8).endPoint(), "cube_length")
Sketch_2.setHorizontal(SketchLine_13.result())
Sketch_2.setVertical(SketchLine_12.result())

### Create SketchLine
SketchLine_14 = Sketch_2.addLine(10, -10, 0, 0)
SketchLine_14.setName("SketchLine_18")
SketchLine_14.result().setName("SketchLine_18")
SketchLine_14.setAuxiliary(True)
Sketch_2.setCoincident(SketchAPI_Line(SketchLine_8).endPoint(), SketchLine_14.startPoint())

### Create SketchProjection
SketchProjection_6 = Sketch_2.addProjection(model.selection("VERTEX", "Sketch_1/SketchLine_15_StartVertex"), False)
SketchProjection_6.setName("SketchProjection_8")
SketchProjection_6.result().setName("SketchProjection_8")
SketchPoint_18 = SketchProjection_6.createdFeature()
SketchPoint_18.setName("SketchPoint_20")
SketchPoint_18.result().setName("SketchPoint_20")
Sketch_2.setCoincident(SketchLine_14.endPoint(), SketchPoint_18.result())
Sketch_2.setCoincident(SketchPoint_17.coordinates(), SketchLine_14.result())
model.do()

### Create ExtrusionCut
ExtrusionCut_2 = model.addExtrusionCut(Part_1_doc, [model.selection("FACE", "Sketch_2/Face-SketchArc_2_2f-SketchLine_7r-SketchLine_8f")], model.selection(), 0, 10, [model.selection("SOLID", "ExtrusionCut_1_1")])

### Create Sketch
Sketch_3 = model.addSketch(Part_1_doc, model.selection("FACE", "Box_1_1/Bottom"))

### Create SketchPoint
SketchPoint_19 = Sketch_3.addPoint(5, -10)
SketchPoint_19.setName("SketchPoint_5")
SketchPoint_19.result().setName("SketchPoint_5")

### Create SketchProjection
SketchProjection_7 = Sketch_3.addProjection(model.selection("EDGE", "[ExtrusionCut_2_1/Modified_Face&Box_1_1/Right][Box_1_1/Bottom]"), False)
SketchProjection_7.setName("SketchProjection_5")
SketchProjection_7.result().setName("SketchProjection_5")
SketchLine_15 = SketchProjection_7.createdFeature()
SketchLine_15.setName("SketchLine_9")
SketchLine_15.result().setName("SketchLine_9")
Sketch_3.setCoincident(SketchPoint_19.coordinates(), SketchLine_15.result())

### Create SketchPoint
SketchPoint_20 = Sketch_3.addPoint(10, -5)
SketchPoint_20.setName("SketchPoint_6")
SketchPoint_20.result().setName("SketchPoint_6")

### Create SketchProjection
SketchProjection_8 = Sketch_3.addProjection(model.selection("EDGE", "[Box_1_1/Bottom][ExtrusionCut_2_1/Modified_Face&Box_1_1/Front]"), False)
SketchProjection_8.setName("SketchProjection_6")
SketchProjection_8.result().setName("SketchProjection_6")
SketchLine_16 = SketchProjection_8.createdFeature()
SketchLine_16.setName("SketchLine_10")
SketchLine_16.result().setName("SketchLine_10")
Sketch_3.setCoincident(SketchPoint_20.coordinates(), SketchLine_16.result())
Sketch_3.setMiddlePoint(SketchPoint_19.coordinates(), SketchLine_15.result())
Sketch_3.setMiddlePoint(SketchPoint_20.coordinates(), SketchLine_16.result())

### Create SketchArc
SketchArc_3 = Sketch_3.addArc(10, -10, 10, -5, 5, -10, False)
Sketch_3.setCoincident(SketchAPI_Line(SketchLine_15).endPoint(), SketchArc_3.center())
Sketch_3.setCoincident(SketchPoint_20.coordinates(), SketchArc_3.startPoint())
Sketch_3.setCoincident(SketchLine_15.result(), SketchArc_3.endPoint())

### Create SketchLine
SketchLine_17 = Sketch_3.addLine(10, -10, 5, -10)
SketchLine_17.setName("SketchLine_11")
SketchLine_17.result().setName("SketchLine_11")
Sketch_3.setCoincident(SketchAPI_Line(SketchLine_15).endPoint(), SketchLine_17.startPoint())
Sketch_3.setCoincident(SketchPoint_19.coordinates(), SketchLine_17.endPoint())

### Create SketchLine
SketchLine_18 = Sketch_3.addLine(10, -10, 10, -5)
SketchLine_18.setName("SketchLine_12")
SketchLine_18.result().setName("SketchLine_12")
Sketch_3.setCoincident(SketchAPI_Line(SketchLine_15).endPoint(), SketchLine_18.startPoint())
Sketch_3.setCoincident(SketchPoint_20.coordinates(), SketchLine_18.endPoint())

### Create SketchPoint
SketchPoint_21 = Sketch_3.addPoint(5.75, -10)
SketchPoint_21.setAuxiliary(True)
Sketch_3.setCoincident(SketchPoint_21.coordinates(), SketchLine_15.result())

### Create SketchPoint
SketchPoint_22 = Sketch_3.addPoint(10, -5.75)
Sketch_3.setCoincident(SketchPoint_22.coordinates(), SketchLine_16.result())

### Create SketchPoint
SketchPoint_23 = Sketch_3.addPoint(7.366086561617737, -5.75)
Sketch_3.setCoincident(SketchPoint_23.coordinates(), SketchArc_3.results()[1])

### Create SketchPoint
SketchPoint_24 = Sketch_3.addPoint(5.75, -7.366086561643447)
Sketch_3.setCoincident(SketchPoint_24.coordinates(), SketchArc_3.results()[1])

### Create SketchPoint
SketchPoint_25 = Sketch_3.addPoint(6.4644660940597, -6.4644660940597)
Sketch_3.setCoincident(SketchPoint_25.coordinates(), SketchArc_3.results()[1])

### Create SketchLine
SketchLine_19 = Sketch_3.addLine(5.75, -10, 5.75, -7.366086561643447)
SketchLine_19.setAuxiliary(True)
Sketch_3.setCoincident(SketchPoint_21.coordinates(), SketchLine_19.startPoint())
Sketch_3.setCoincident(SketchPoint_24.coordinates(), SketchLine_19.endPoint())

### Create SketchLine
SketchLine_20 = Sketch_3.addLine(10, -5.75, 7.366086561617737, -5.75)
SketchLine_20.setAuxiliary(True)
Sketch_3.setCoincident(SketchPoint_22.coordinates(), SketchLine_20.startPoint())
Sketch_3.setCoincident(SketchPoint_23.coordinates(), SketchLine_20.endPoint())

### Create SketchLine
SketchLine_21 = Sketch_3.addLine(10, -10, 0, 0)
SketchLine_21.setAuxiliary(True)
Sketch_3.setCoincident(SketchAPI_Line(SketchLine_15).endPoint(), SketchLine_21.startPoint())

### Create SketchProjection
SketchProjection_9 = Sketch_3.addProjection(model.selection("VERTEX", "Sketch_1/SketchLine_15_StartVertex"), False)
SketchPoint_26 = SketchProjection_9.createdFeature()
Sketch_3.setCoincident(SketchLine_21.endPoint(), SketchPoint_26.result())
Sketch_3.setHorizontalDistance(SketchAPI_Line(SketchLine_15).endPoint(), SketchLine_19.startPoint(), "cube_length")
Sketch_3.setVerticalDistance(SketchLine_21.startPoint(), SketchLine_20.startPoint(), "cube_length")
Sketch_3.setVertical(SketchLine_19.result())
Sketch_3.setHorizontal(SketchLine_20.result())
Sketch_3.setCoincident(SketchPoint_25.coordinates(), SketchLine_21.result())
model.do()

### Create ExtrusionCut
ExtrusionCut_3 = model.addExtrusionCut(Part_1_doc, [model.selection("FACE", "Sketch_3/Face-SketchArc_3_2f-SketchLine_11r-SketchLine_12f")], model.selection(), 0, 10, [model.selection("SOLID", "ExtrusionCut_2_1")])

### Create Box
Box_2 = model.addBox(Part_1_doc, "cube_length", "cube_length", "cube_length")

### Create Translation
Translation_1 = model.addTranslation(Part_1_doc, [model.selection("SOLID", "Box_2_1")], vector = ["10-cube_length", "10-cube_length", "10-cube_length"], keepSubResults = True)

### Create Fuse
Fuse_1 = model.addFuse(Part_1_doc, [model.selection("SOLID", "ExtrusionCut_3_1"), model.selection("SOLID", "Translation_1_1")], removeEdges = True, keepSubResults = True)

### Create Sketch
Sketch_4 = model.addSketch(Part_1_doc, model.selection("FACE", "Fuse_1_1/Modified_Face&Box_2_1/Left"))

### Create SketchLine
SketchLine_22 = Sketch_4.addLine(5.75, 10, 10, 5.75)
SketchLine_22.setAuxiliary(True)

### Create SketchProjection
SketchProjection_10 = Sketch_4.addProjection(model.selection("VERTEX", "[Fuse_1_1/Modified_Face&Box_2_1/Back][Fuse_1_1/Modified_Face&Box_2_1/Left][Translation_1_1/MF:Translated&Box_2_1/Top]"), False)
SketchPoint_27 = SketchProjection_10.createdFeature()
Sketch_4.setCoincident(SketchLine_22.startPoint(), SketchPoint_27.result())

### Create SketchProjection
SketchProjection_11 = Sketch_4.addProjection(model.selection("VERTEX", "[Fuse_1_1/Modified_Face&Box_2_1/Left][Fuse_1_1/Modified_Face&Box_2_1/Bottom][Translation_1_1/MF:Translated&Box_2_1/Front]"), False)
SketchPoint_28 = SketchProjection_11.createdFeature()
Sketch_4.setCoincident(SketchLine_22.endPoint(), SketchPoint_28.result())

### Create SketchLine
SketchLine_23 = Sketch_4.addLine(6.464466094067265, 6.464466094067262, 10, 10)
SketchLine_23.setAuxiliary(True)

### Create SketchProjection
SketchProjection_12 = Sketch_4.addProjection(model.selection("EDGE", "Fuse_1_1/Generated_Edge&Box_2_1/Left&Sketch_1/SketchArc_1_2"), False)
SketchArc_4 = SketchProjection_12.createdFeature()
Sketch_4.setCoincident(SketchLine_23.startPoint(), SketchArc_4.results()[1])
Sketch_4.setCoincident(SketchAPI_Arc(SketchArc_4).center(), SketchLine_23.endPoint())

### Create SketchPoint
SketchPoint_29 = Sketch_4.addPoint(7.875000000000001, 7.875000000000001)
SketchPoint_29.setAuxiliary(True)
Sketch_4.setCoincident(SketchPoint_29.coordinates(), SketchLine_22.result())
Sketch_4.setMiddlePoint(SketchPoint_29.coordinates(), SketchLine_22.result())
Sketch_4.setCoincident(SketchPoint_29.coordinates(), SketchLine_23.result())

### Create SketchPoint
SketchPoint_30 = Sketch_4.addPoint(7.366086561786749, 5.750000000000043)
Sketch_4.setCoincident(SketchAPI_Arc(SketchArc_4).endPoint(), SketchPoint_30.coordinates())

### Create SketchPoint
SketchPoint_31 = Sketch_4.addPoint(5.750000000000042, 7.366086561786751)
Sketch_4.setCoincident(SketchAPI_Arc(SketchArc_4).startPoint(), SketchPoint_31.coordinates())
model.do()

### Create Edge
Edge_1 = model.addEdge(Part_1_doc, model.selection("VERTEX", "Sketch_4/SketchPoint_31"), model.selection("VERTEX", "Sketch_1/SketchLine_13_StartVertex"))

### Create Edge
Edge_2 = model.addEdge(Part_1_doc, model.selection("VERTEX", "Sketch_4/SketchLine_23_StartVertex"), model.selection("VERTEX", "Sketch_1/SketchPoint_11"))

### Create Edge
Edge_3 = model.addEdge(Part_1_doc, model.selection("VERTEX", "[Fuse_1_1/Modified_Face&Box_2_1/Left][Fuse_1_1/Modified_Face&Box_2_1/Bottom][Fuse_1_1/Modified_Face&Sketch_1/SketchArc_1_2][Fuse_1_1/Modified_Face&Sketch_3/SketchArc_3_2]"), model.selection("VERTEX", "Sketch_1/SketchLine_14_StartVertex"))

### Create Sketch
Sketch_5 = model.addSketch(Part_1_doc, model.selection("FACE", "Fuse_1_1/Modified_Face&Box_2_1/Back"))

### Create SketchLine
SketchLine_24 = Sketch_5.addLine(10, -5.75, 5.75, -10)
SketchLine_24.setAuxiliary(True)

### Create SketchProjection
SketchProjection_13 = Sketch_5.addProjection(model.selection("VERTEX", "[Fuse_1_1/Modified_Face&Box_2_1/Back][Translation_1_1/MF:Translated&Box_2_1/Right][Fuse_1_1/Modified_Face&Box_2_1/Bottom]"), False)
SketchPoint_32 = SketchProjection_13.createdFeature()
Sketch_5.setCoincident(SketchLine_24.startPoint(), SketchPoint_32.result())

### Create SketchProjection
SketchProjection_14 = Sketch_5.addProjection(model.selection("VERTEX", "[Fuse_1_1/Modified_Face&Box_2_1/Back][Fuse_1_1/Modified_Face&Box_2_1/Left][Translation_1_1/MF:Translated&Box_2_1/Top]"), False)
SketchPoint_33 = SketchProjection_14.createdFeature()
Sketch_5.setCoincident(SketchLine_24.endPoint(), SketchPoint_33.result())

### Create SketchPoint
SketchPoint_34 = Sketch_5.addPoint(7.875, -7.875)
SketchPoint_34.setAuxiliary(True)
Sketch_5.setCoincident(SketchPoint_34.coordinates(), SketchLine_24.result())
Sketch_5.setMiddlePoint(SketchPoint_34.coordinates(), SketchLine_24.result())

### Create SketchLine
SketchLine_25 = Sketch_5.addLine(10, -10, 6.464466093900326, -6.464466094100319)
SketchLine_25.setAuxiliary(True)

### Create SketchProjection
SketchProjection_15 = Sketch_5.addProjection(model.selection("VERTEX", "Fuse_1_1/Generated_Edge&Box_2_1/Back&Sketch_2/SketchArc_2_2__cc"), False)
SketchPoint_35 = SketchProjection_15.createdFeature()
Sketch_5.setCoincident(SketchLine_25.startPoint(), SketchPoint_35.result())

### Create SketchProjection
SketchProjection_16 = Sketch_5.addProjection(model.selection("EDGE", "Fuse_1_1/Generated_Edge&Box_2_1/Back&Sketch_2/SketchArc_2_2"), False)
SketchArc_5 = SketchProjection_16.createdFeature()
Sketch_5.setCoincident(SketchLine_25.endPoint(), SketchArc_5.results()[1])
Sketch_5.setCoincident(SketchPoint_34.coordinates(), SketchLine_25.result())

### Create SketchPoint
SketchPoint_36 = Sketch_5.addPoint(5.750000000000041, -7.36608656178675)
Sketch_5.setCoincident(SketchAPI_Arc(SketchArc_5).endPoint(), SketchPoint_36.coordinates())

### Create SketchPoint
SketchPoint_37 = Sketch_5.addPoint(7.366086561786746, -5.750000000000043)
Sketch_5.setCoincident(SketchAPI_Arc(SketchArc_5).startPoint(), SketchPoint_37.coordinates())
model.do()

### Create Edge
Edge_4 = model.addEdge(Part_1_doc, model.selection("VERTEX", "Sketch_5/SketchPoint_36"), model.selection("VERTEX", "Sketch_2/SketchPoint_18"))

### Create Edge
Edge_5 = model.addEdge(Part_1_doc, model.selection("VERTEX", "Sketch_5/SketchLine_25_EndVertex"), model.selection("VERTEX", "Sketch_2/SketchPoint_19"))

### Create Edge
Edge_6 = model.addEdge(Part_1_doc, model.selection("VERTEX", "Sketch_5/SketchPoint_37"), model.selection("VERTEX", "Sketch_2/SketchLine_17_EndVertex"))

### Create Sketch
Sketch_6 = model.addSketch(Part_1_doc, model.selection("FACE", "Fuse_1_1/Modified_Face&Box_2_1/Bottom"))

### Create SketchLine
SketchLine_26 = Sketch_6.addLine(10, -5.75, 5.75, -10)
SketchLine_26.setAuxiliary(True)

### Create SketchProjection
SketchProjection_17 = Sketch_6.addProjection(model.selection("VERTEX", "[Fuse_1_1/Modified_Face&Box_2_1/Left][Fuse_1_1/Modified_Face&Box_2_1/Bottom][Translation_1_1/MF:Translated&Box_2_1/Front]"), False)
SketchPoint_38 = SketchProjection_17.createdFeature()
Sketch_6.setCoincident(SketchLine_26.startPoint(), SketchPoint_38.result())

### Create SketchProjection
SketchProjection_18 = Sketch_6.addProjection(model.selection("VERTEX", "[Fuse_1_1/Modified_Face&Box_2_1/Back][Translation_1_1/MF:Translated&Box_2_1/Right][Fuse_1_1/Modified_Face&Box_2_1/Bottom]"), False)
SketchPoint_39 = SketchProjection_18.createdFeature()
Sketch_6.setCoincident(SketchLine_26.endPoint(), SketchPoint_39.result())

### Create SketchPoint
SketchPoint_40 = Sketch_6.addPoint(7.874999999999999, -7.874999999999999)
SketchPoint_40.setAuxiliary(True)
Sketch_6.setCoincident(SketchPoint_40.coordinates(), SketchLine_26.result())
Sketch_6.setMiddlePoint(SketchPoint_40.coordinates(), SketchLine_26.result())

### Create SketchLine
SketchLine_27 = Sketch_6.addLine(10, -10, 6.464466094067263, -6.464466094067264)
SketchLine_27.setAuxiliary(True)

### Create SketchProjection
SketchProjection_19 = Sketch_6.addProjection(model.selection("VERTEX", "Fuse_1_1/Generated_Edge&Box_2_1/Bottom&Sketch_3/SketchArc_3_2__cc"), False)
SketchPoint_41 = SketchProjection_19.createdFeature()
Sketch_6.setCoincident(SketchLine_27.startPoint(), SketchPoint_41.result())

### Create SketchProjection
SketchProjection_20 = Sketch_6.addProjection(model.selection("EDGE", "Fuse_1_1/Generated_Edge&Box_2_1/Bottom&Sketch_3/SketchArc_3_2"), False)
SketchArc_6 = SketchProjection_20.createdFeature()
Sketch_6.setCoincident(SketchLine_27.endPoint(), SketchArc_6.results()[1])
Sketch_6.setCoincident(SketchPoint_40.coordinates(), SketchLine_27.result())

### Create SketchPoint
SketchPoint_42 = Sketch_6.addPoint(5.750000000000044, -7.366086561786744)
Sketch_6.setCoincident(SketchAPI_Arc(SketchArc_6).endPoint(), SketchPoint_42.coordinates())

### Create SketchPoint
SketchPoint_43 = Sketch_6.addPoint(7.366086561786751, -5.750000000000042)
Sketch_6.setCoincident(SketchAPI_Arc(SketchArc_6).startPoint(), SketchPoint_43.coordinates())
model.do()

### Create Edge
Edge_7 = model.addEdge(Part_1_doc, model.selection("VERTEX", "Sketch_6/SketchPoint_42"), model.selection("VERTEX", "Sketch_3/SketchLine_19_EndVertex"))

### Create Edge
Edge_8 = model.addEdge(Part_1_doc, model.selection("VERTEX", "Sketch_6/SketchLine_27_EndVertex"), model.selection("VERTEX", "Sketch_3/SketchPoint_25"))

### Create Edge
Edge_9 = model.addEdge(Part_1_doc, model.selection("VERTEX", "Sketch_6/SketchPoint_43"), model.selection("VERTEX", "Sketch_3/SketchLine_20_EndVertex"))

### Create Split
Split_1_objects_2 = [model.selection("EDGE", "Edge_1_1"),
                     model.selection("EDGE", "Edge_2_1"),
                     model.selection("EDGE", "Edge_3_1"),
                     model.selection("EDGE", "Edge_4_1"),
                     model.selection("EDGE", "Edge_5_1"),
                     model.selection("EDGE", "Edge_6_1"),
                     model.selection("EDGE", "Edge_7_1"),
                     model.selection("EDGE", "Edge_8_1"),
                     model.selection("EDGE", "Edge_9_1")]
Split_1 = model.addSplit(Part_1_doc, [model.selection("SOLID", "Fuse_1_1")], Split_1_objects_2, keepSubResults = True)

model.end()

###
### SHAPERSTUDY component
###

model.publishToShaperStudy()
import SHAPERSTUDY
Split_1_1, = SHAPERSTUDY.shape(model.featureStringId(Split_1))

if salome.sg.hasDesktop():
  salome.sg.updateObjBrowser()
