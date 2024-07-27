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
model.addParameter(Part_1_doc, "inner_margin", '2')
model.addParameter(Part_1_doc, "outer_margin", '1')
model.addParameter(Part_1_doc, "holes_width", '1')
model.addParameter(Part_1_doc, "grooves_size", '0.5')
model.addParameter(Part_1_doc, "box_length", '25.1327')
model.addParameter(Part_1_doc, "box_width", '3*holes_width+2*inner_margin+2*outer_margin')

### Create Point
Point_2 = model.addPoint(Part_1_doc, "0", "2*holes_width+inner_margin+outer_margin", "3*holes_width+2*inner_margin+outer_margin")

### Create Point
Point_3 = model.addPoint(Part_1_doc, "0", "holes_width+inner_margin+outer_margin", "3*holes_width+2*inner_margin+outer_margin")

### Create Point
Point_4 = model.addPoint(Part_1_doc, "0", "holes_width+inner_margin+outer_margin", "2*holes_width+2*inner_margin+outer_margin")

### Create Point
Point_5 = model.addPoint(Part_1_doc, "0", "2*holes_width+inner_margin+outer_margin", "2*holes_width+2*inner_margin+outer_margin")

### Create Edge
Edge_1 = model.addEdge(Part_1_doc, model.selection("VERTEX", "Point_1"), model.selection("VERTEX", "Point_2"))
Edge_1.setName("Point_1_to_Point_2")
Edge_1.result().setName("Edge_1_1")

### Create Edge
Edge_2 = model.addEdge(Part_1_doc, model.selection("VERTEX", "Point_2"), model.selection("VERTEX", "Point_3"))
Edge_2.setName("Point_2_to_Point_3")
Edge_2.result().setName("Edge_2_1")

### Create Edge
Edge_3 = model.addEdge(Part_1_doc, model.selection("VERTEX", "Point_3"), model.selection("VERTEX", "Point_4"))
Edge_3.setName("Point_3_to_Point_4")
Edge_3.result().setName("Edge_3_1")

### Create Edge
Edge_4 = model.addEdge(Part_1_doc, model.selection("VERTEX", "Point_4"), model.selection("VERTEX", "Point_1"))
Edge_4.setName("Point_4_to_Point_1")
Edge_4.result().setName("Edge_4_1")

### Create Face
Face_1_objects = [model.selection("EDGE", "Edge_1_1"),
                  model.selection("EDGE", "Edge_2_1"),
                  model.selection("EDGE", "Edge_3_1"),
                  model.selection("EDGE", "Edge_4_1")]
Face_1 = model.addFace(Part_1_doc, Face_1_objects)
Face_1.result().setName("Face_1_1")

### Create Point
Point_6 = model.addPoint(Part_1_doc, "0", "3/2*holes_width+inner_margin+outer_margin", "5/2*holes_width+2*inner_margin+outer_margin")
Point_6.setName("Face_1_middle")
Point_6.result().setName("Point_5")

### Create Interpolation
Interpolation_1 = model.addInterpolation(Part_1_doc, "t", "-1.5*inner_margin*sin(t*0.25)", "-3*inner_margin*sin(t*0.125)", 0, 25.1327, 100)

### Create Pipe
Pipe_1 = model.addPipe(Part_1_doc, [model.selection("FACE", "Face_1_1")], model.selection("EDGE", "Interpolation_1_1"), model.selection("EDGE", "PartSet/OZ"))

### Create Box
Box_1 = model.addBox(Part_1_doc, "box_length", "box_width", "box_width")

### Create Sketch
Sketch_1 = model.addSketch(Part_1_doc, model.selection("FACE", "Box_1_1/Back"))

### Create SketchLine
SketchLine_1 = Sketch_1.addLine(4, -5, 5, -5)

### Create SketchLine
SketchLine_2 = Sketch_1.addLine(5, -5, 5, -4)

### Create SketchLine
SketchLine_3 = Sketch_1.addLine(5, -4, 4, -4)

### Create SketchLine
SketchLine_4 = Sketch_1.addLine(4, -4, 4, -5)
Sketch_1.setCoincident(SketchLine_4.endPoint(), SketchLine_1.startPoint())
Sketch_1.setCoincident(SketchLine_1.endPoint(), SketchLine_2.startPoint())
Sketch_1.setCoincident(SketchLine_2.endPoint(), SketchLine_3.startPoint())
Sketch_1.setCoincident(SketchLine_3.endPoint(), SketchLine_4.startPoint())
Sketch_1.setPerpendicular(SketchLine_1.result(), SketchLine_2.result())
Sketch_1.setPerpendicular(SketchLine_2.result(), SketchLine_3.result())
Sketch_1.setPerpendicular(SketchLine_3.result(), SketchLine_4.result())
Sketch_1.setHorizontalDistance(SketchLine_2.startPoint(), SketchLine_4.endPoint(), "holes_width")
Sketch_1.setVerticalDistance(SketchLine_2.startPoint(), SketchLine_3.startPoint(), "holes_width")

### Create SketchProjection
SketchProjection_1 = Sketch_1.addProjection(model.selection("VERTEX", "[Box_1_1/Back][Box_1_1/Left][Box_1_1/Bottom]"), False)
SketchPoint_1 = SketchProjection_1.createdFeature()
Sketch_1.setVerticalDistance(SketchLine_3.startPoint(), SketchAPI_Point(SketchPoint_1).coordinates(), "inner_margin+holes_width+outer_margin")
Sketch_1.setHorizontal(SketchLine_1.result())
Sketch_1.setHorizontalDistance(SketchLine_3.endPoint(), SketchAPI_Point(SketchPoint_1).coordinates(), "inner_margin+holes_width+outer_margin")
model.do()

### Create ExtrusionCut
ExtrusionCut_1 = model.addExtrusionCut(Part_1_doc, [model.selection("FACE", "Sketch_1/Face-SketchLine_1r-SketchLine_2f-SketchLine_3f-SketchLine_4f")], model.selection(), 0, "box_length", [model.selection("SOLID", "Box_1_1")])

### Create Cut
Cut_1 = model.addCut(Part_1_doc, [model.selection("SOLID", "ExtrusionCut_1_1")], [model.selection("SOLID", "Pipe_1_1")], keepSubResults = True)

### Create Sketch
Sketch_2 = model.addSketch(Part_1_doc, model.selection("FACE", "Box_1_1/Left"))

### Create SketchLine
SketchLine_5 = Sketch_2.addLine(0.5, 6.25, 0, 6.25)

### Create SketchProjection
SketchProjection_2 = Sketch_2.addProjection(model.selection("EDGE", "[Cut_1_1/Modified_Face&Box_1_1/Back][Box_1_1/Left]"), False)
SketchLine_6 = SketchProjection_2.createdFeature()
Sketch_2.setCoincident(SketchLine_5.endPoint(), SketchLine_6.result())

### Create SketchLine
SketchLine_7 = Sketch_2.addLine(0, 6.25, 0, 5.75)

### Create SketchLine
SketchLine_8 = Sketch_2.addLine(0, 5.75, 0.5, 5.75)

### Create SketchLine
SketchLine_9 = Sketch_2.addLine(0.5, 5.75, 0.5, 6.25)
Sketch_2.setCoincident(SketchLine_9.endPoint(), SketchLine_5.startPoint())
Sketch_2.setCoincident(SketchLine_5.endPoint(), SketchLine_7.startPoint())
Sketch_2.setCoincident(SketchLine_7.endPoint(), SketchLine_8.startPoint())
Sketch_2.setCoincident(SketchLine_8.endPoint(), SketchLine_9.startPoint())
Sketch_2.setPerpendicular(SketchLine_5.result(), SketchLine_7.result())
Sketch_2.setPerpendicular(SketchLine_7.result(), SketchLine_8.result())
Sketch_2.setPerpendicular(SketchLine_8.result(), SketchLine_9.result())

### Create SketchLine
SketchLine_10 = Sketch_2.addLine(24.6327, 6.25, 25.1327, 6.25)

### Create SketchProjection
SketchProjection_3 = Sketch_2.addProjection(model.selection("EDGE", "[Box_1_1/Left][Cut_1_1/Modified_Face&Box_1_1/Front]"), False)
SketchLine_11 = SketchProjection_3.createdFeature()
Sketch_2.setCoincident(SketchLine_10.endPoint(), SketchLine_11.result())

### Create SketchLine
SketchLine_12 = Sketch_2.addLine(25.1327, 6.25, 25.1327, 5.75)

### Create SketchLine
SketchLine_13 = Sketch_2.addLine(25.1327, 5.75, 24.6327, 5.75)

### Create SketchLine
SketchLine_14 = Sketch_2.addLine(24.6327, 5.75, 24.6327, 6.25)
Sketch_2.setCoincident(SketchLine_14.endPoint(), SketchLine_10.startPoint())
Sketch_2.setCoincident(SketchLine_10.endPoint(), SketchLine_12.startPoint())
Sketch_2.setCoincident(SketchLine_12.endPoint(), SketchLine_13.startPoint())
Sketch_2.setCoincident(SketchLine_13.endPoint(), SketchLine_14.startPoint())
Sketch_2.setPerpendicular(SketchLine_10.result(), SketchLine_12.result())
Sketch_2.setPerpendicular(SketchLine_12.result(), SketchLine_13.result())
Sketch_2.setPerpendicular(SketchLine_13.result(), SketchLine_14.result())
Sketch_2.setVertical(SketchLine_7.result())
Sketch_2.setVertical(SketchLine_12.result())
Sketch_2.setVerticalDistance(SketchLine_9.endPoint(), SketchLine_14.endPoint(), 0)
Sketch_2.setVerticalDistance(SketchLine_8.endPoint(), SketchLine_13.endPoint(), 0)
Sketch_2.setVerticalDistance(SketchLine_9.endPoint(), SketchLine_8.endPoint(), "grooves_size")

### Create SketchPoint
SketchPoint_2 = Sketch_2.addPoint(0.5000000000000006, 6)
SketchPoint_2.setAuxiliary(True)
Sketch_2.setCoincident(SketchPoint_2.coordinates(), SketchLine_9.result())
Sketch_2.setMiddlePoint(SketchPoint_2.coordinates(), SketchLine_9.result())
Sketch_2.setVerticalDistance(SketchPoint_2.coordinates(), SketchAPI_Line(SketchLine_6).endPoint(), "outer_margin+holes_width+inner_margin/2")
Sketch_2.setHorizontalDistance(SketchLine_7.endPoint(), SketchLine_8.endPoint(), "grooves_size")
Sketch_2.setHorizontalDistance(SketchLine_14.startPoint(), SketchLine_12.endPoint(), "grooves_size")
model.do()

### Create ExtrusionCut
ExtrusionCut_2 = model.addExtrusionCut(Part_1_doc, [model.selection("FACE", "Sketch_2/Face-SketchLine_5r-SketchLine_7f-SketchLine_8f-SketchLine_9f")], model.selection(), 0, "box_width", [model.selection("SOLID", "Cut_1_1")])

### Create ExtrusionCut
ExtrusionCut_3 = model.addExtrusionCut(Part_1_doc, [model.selection("WIRE", "Sketch_2/Face-SketchLine_14r-SketchLine_13r-SketchLine_12r-SketchLine_10r_wire")], model.selection(), 0, "box_width", [model.selection("SOLID", "ExtrusionCut_2_1")])

model.end()

###
### SHAPERSTUDY component
###

model.publishToShaperStudy()
import SHAPERSTUDY
ExtrusionCut_3_1, = SHAPERSTUDY.shape(model.featureStringId(ExtrusionCut_3))

if salome.sg.hasDesktop():
  salome.sg.updateObjBrowser()
