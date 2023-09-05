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
model.addParameter(Part_1_doc, "L", '8*pi')
model.addParameter(Part_1_doc, "margin", '3')
model.addParameter(Part_1_doc, "l", '11')

### Create Point
Point_2 = model.addPoint(Part_1_doc, "0", "l/2-0.5", "l/2-0.5")

### Create Point
Point_3 = model.addPoint(Part_1_doc, "0", "l/2-0.5", "l/2+0.5")

### Create Point
Point_4 = model.addPoint(Part_1_doc, "0", "l/2+0.5", "l/2+0.5")

### Create Point
Point_5 = model.addPoint(Part_1_doc, "0", "l/2+0.5", "l/2-0.5")

### Create Edge
Edge_1 = model.addEdge(Part_1_doc, model.selection("VERTEX", "Point_3"), model.selection("VERTEX", "Point_2"))

### Create Edge
Edge_2 = model.addEdge(Part_1_doc, model.selection("VERTEX", "Point_2"), model.selection("VERTEX", "Point_1"))

### Create Edge
Edge_3 = model.addEdge(Part_1_doc, model.selection("VERTEX", "Point_1"), model.selection("VERTEX", "Point_4"))

### Create Edge
Edge_4 = model.addEdge(Part_1_doc, model.selection("VERTEX", "Edge_3_1/Modified_Vertex&Point_4/Point_4"), model.selection("VERTEX", "Edge_1_1/Modified_Vertex&Point_3/Point_3"))

### Create Face
Face_1_objects = [model.selection("EDGE", "Edge_1_1"),
                  model.selection("EDGE", "Edge_2_1"),
                  model.selection("EDGE", "Edge_3_1"),
                  model.selection("EDGE", "Edge_4_1")]
Face_1 = model.addFace(Part_1_doc, Face_1_objects)

### Create Extrusion
Extrusion_1 = model.addExtrusion(Part_1_doc, [model.selection("FACE", "Face_1_1")], model.selection(), model.selection(), 0, model.selection(), "L", "Faces|Wires")

### Create Point
Point_6 = model.addPoint(Part_1_doc, "0", "l/2-1.5-margin", "l/2-0.5")

### Create Point
Point_7 = model.addPoint(Part_1_doc, "0", "l/2-1.5-margin", "l/2+0.5")

### Create Point
Point_8 = model.addPoint(Part_1_doc, "0", "l/2-0.5-margin", "l/2+0.5")

### Create Point
Point_9 = model.addPoint(Part_1_doc, "0", "l/2-0.5-margin", "l/2-0.5")

### Create Edge
Edge_5 = model.addEdge(Part_1_doc, model.selection("VERTEX", "Point_7"), model.selection("VERTEX", "Point_6"))

### Create Edge
Edge_6 = model.addEdge(Part_1_doc, model.selection("VERTEX", "Point_6"), model.selection("VERTEX", "Point_5"))

### Create Edge
Edge_7 = model.addEdge(Part_1_doc, model.selection("VERTEX", "Point_5"), model.selection("VERTEX", "Point_8"))

### Create Edge
Edge_8 = model.addEdge(Part_1_doc, model.selection("VERTEX", "Edge_7_1/Modified_Vertex&Point_8/Point_8"), model.selection("VERTEX", "Edge_5_1/Modified_Vertex&Point_7/Point_7"))

### Create Face
Face_2_objects = [model.selection("EDGE", "Edge_5_1"),
                  model.selection("EDGE", "Edge_6_1"),
                  model.selection("EDGE", "Edge_7_1"),
                  model.selection("EDGE", "Edge_8_1")]
Face_2 = model.addFace(Part_1_doc, Face_2_objects)

### Create Point
Point_10 = model.addPoint(Part_1_doc, "0", "l/2-1-margin", "l/2")

### Create Interpolation
Interpolation_1 = model.addInterpolation(Part_1_doc, "t", "6*sin(t*0.125)+L/2-margin-1", "-3*sin(t*0.25)+(L/2)", 0, 25.13274122871834, 100)

### Create Point
Point_11 = model.addPoint(Part_1_doc, "0", "l/2-2-margin", "l/2")
Point_11.setName("Point_11")
Point_11.result().setName("Point_11")

### Create Axis
Axis_4 = model.addAxis(Part_1_doc, model.selection("VERTEX", "Point_9"), model.selection("VERTEX", "Point_11"))
Axis_4.setName("Axis_2")
Axis_4.result().setName("Axis_2")

### Create Pipe
Pipe_1 = model.addPipe(Part_1_doc, [model.selection("FACE", "Face_2_1")], model.selection("EDGE", "Interpolation_1_1"), model.selection("EDGE", "Axis_2"))

### Create Box
Box_1 = model.addBox(Part_1_doc, "L", "l", "l")

### Create Cut
Cut_1 = model.addCut(Part_1_doc, [model.selection("COMPOUND", "all-in-Box_1")], [model.selection("COMPOUND", "all-in-Extrusion_1")], keepSubResults = True)

### Create Cut
Cut_2 = model.addCut(Part_1_doc, [model.selection("COMPOUND", "all-in-Cut_1")], [model.selection("COMPOUND", "all-in-Pipe_1")], keepSubResults = True)

### Create Sketch
Sketch_1 = model.addSketch(Part_1_doc, model.selection("FACE", "Box_1_1/Top"))

### Create SketchLine
SketchLine_1 = Sketch_1.addLine(0, 4, 0.5, 4)

### Create SketchProjection
SketchProjection_1 = Sketch_1.addProjection(model.selection("EDGE", "[Cut_2_1/Modified_Face&Box_1_1/Back][Box_1_1/Top]"), False)
SketchLine_2 = SketchProjection_1.createdFeature()
Sketch_1.setCoincident(SketchLine_1.startPoint(), SketchLine_2.result())

### Create SketchLine
SketchLine_3 = Sketch_1.addLine(0.5, 4, 0.5, 3.5)
Sketch_1.setCoincident(SketchLine_1.endPoint(), SketchLine_3.startPoint())
Sketch_1.setVertical(SketchLine_3.result())

### Create SketchLine
SketchLine_4 = Sketch_1.addLine(0.5, 3.5, 0, 3.5)
Sketch_1.setCoincident(SketchLine_3.endPoint(), SketchLine_4.startPoint())
Sketch_1.setCoincident(SketchLine_4.endPoint(), SketchLine_2.result())

### Create SketchLine
SketchLine_5 = Sketch_1.addLine(0, 4, 0, 3.5)
Sketch_1.setCoincident(SketchLine_1.startPoint(), SketchLine_5.startPoint())
Sketch_1.setCoincident(SketchLine_4.endPoint(), SketchLine_5.endPoint())
Sketch_1.setHorizontal(SketchLine_1.result())
Sketch_1.setHorizontal(SketchLine_4.result())
Sketch_1.setDistance(SketchLine_4.endPoint(), SketchAPI_Line(SketchLine_2).startPoint(), 3.5, True)
Sketch_1.setDistance(SketchLine_4.result(), SketchLine_3.startPoint(), 0.5, True)
Sketch_1.setDistance(SketchLine_5.startPoint(), SketchLine_3.startPoint(), 0.5, True)
model.do()

### Create ExtrusionCut
ExtrusionCut_1 = model.addExtrusionCut(Part_1_doc, [model.selection("FACE", "Sketch_1/Face-SketchLine_5f-SketchLine_4r-SketchLine_3r-SketchLine_1r")], model.selection(), 0, 11, [model.selection("SOLID", "Cut_2_1")])

### Create Sketch
Sketch_2 = model.addSketch(Part_1_doc, model.selection("FACE", "ExtrusionCut_1_1/Modified_Face&Box_1_1/Top"))

### Create SketchLine
SketchLine_6 = Sketch_2.addLine(25.13274122871834, 4, 24.63274122871834, 4)

### Create SketchProjection
SketchProjection_2 = Sketch_2.addProjection(model.selection("EDGE", "[ExtrusionCut_1_1/Modified_Face&Box_1_1/Top][Cut_2_1/Modified_Face&Box_1_1/Front]"), False)
SketchLine_7 = SketchProjection_2.createdFeature()
Sketch_2.setCoincident(SketchLine_6.startPoint(), SketchLine_7.result())
Sketch_2.setHorizontal(SketchLine_6.result())

### Create SketchLine
SketchLine_8 = Sketch_2.addLine(24.63274122871834, 4, 24.63274122871834, 3.5)
Sketch_2.setCoincident(SketchLine_6.endPoint(), SketchLine_8.startPoint())
Sketch_2.setVertical(SketchLine_8.result())

### Create SketchLine
SketchLine_9 = Sketch_2.addLine(24.63274122871834, 3.5, 25.13274122871834, 3.5)
Sketch_2.setCoincident(SketchLine_8.endPoint(), SketchLine_9.startPoint())
Sketch_2.setCoincident(SketchLine_9.endPoint(), SketchLine_7.result())
Sketch_2.setHorizontal(SketchLine_9.result())

### Create SketchLine
SketchLine_10 = Sketch_2.addLine(25.13274122871834, 4, 25.13274122871834, 3.5)
Sketch_2.setCoincident(SketchLine_6.startPoint(), SketchLine_10.startPoint())
Sketch_2.setCoincident(SketchLine_9.endPoint(), SketchLine_10.endPoint())
Sketch_2.setDistance(SketchLine_9.endPoint(), SketchAPI_Line(SketchLine_7).startPoint(), 3.5, True)
Sketch_2.setDistance(SketchLine_8.endPoint(), SketchLine_8.startPoint(), 0.5, True)
Sketch_2.setDistance(SketchLine_8.startPoint(), SketchLine_10.startPoint(), 0.5, True)
model.do()

### Create ExtrusionCut
ExtrusionCut_2 = model.addExtrusionCut(Part_1_doc, [model.selection("FACE", "Sketch_2/Face-SketchLine_6r-SketchLine_8f-SketchLine_9f-SketchLine_10r")], model.selection(), 0, 11, [model.selection("SOLID", "ExtrusionCut_1_1")])

model.end()

###
### SHAPERSTUDY component
###

model.publishToShaperStudy()
import SHAPERSTUDY
ExtrusionCut_2_1, = SHAPERSTUDY.shape(model.featureStringId(ExtrusionCut_2))

if salome.sg.hasDesktop():
  salome.sg.updateObjBrowser()
