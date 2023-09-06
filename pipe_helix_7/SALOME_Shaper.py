#!/usr/bin/env python

import sys
import salome

salome.salome_init()

###
### SHAPER component
###

from salome.shaper import model
from SketchAPI import *

model.begin()
partSet = model.moduleDocument()

### Create Part
Part_1 = model.addPart(partSet)
Part_1_doc = Part_1.document()
model.addParameter(Part_1_doc, "h", "0.15")

### Create Sketch
Sketch_1 = model.addSketch(Part_1_doc, model.defaultPlane("XOY"))

### Create SketchProjection
SketchProjection_1 = Sketch_1.addProjection(model.selection("VERTEX", "PartSet/Origin"), False)
SketchPoint_1 = SketchProjection_1.createdFeature()

### Create SketchProjection
SketchProjection_2 = Sketch_1.addProjection(model.selection("EDGE", "PartSet/OX"), False)
SketchLine_1 = SketchProjection_2.createdFeature()
SketchLine_1.setName("SketchLine_2")
SketchLine_1.result().setName("SketchLine_2")

### Create SketchArc
SketchArc_1 = Sketch_1.addArc(0, 0, 0.009905484798404638, 0.001371630747896318, 0.009905484798404638, -0.001371630747896318, False)
SketchArc_1.setName("SketchArc_5")
SketchArc_1.result().setName("SketchArc_5")
SketchArc_1.results()[1].setName("SketchArc_5_2")
Sketch_1.setCoincident(SketchPoint_1.result(), SketchArc_1.center())
Sketch_1.setRadius(SketchArc_1.results()[1], 0.01)

### Create SketchLine
SketchLine_2 = Sketch_1.addLine(0.009905484798404638, -0.001371630747896318, 0.009905484798404638, 0.001371630747896318)
SketchLine_2.setName("SketchLine_3")
SketchLine_2.result().setName("SketchLine_3")
SketchLine_2.setAuxiliary(True)
Sketch_1.setCoincident(SketchArc_1.endPoint(), SketchLine_2.startPoint())
Sketch_1.setCoincident(SketchArc_1.startPoint(), SketchLine_2.endPoint())
Sketch_1.setVertical(SketchLine_2.result())

### Create SketchArc
SketchArc_2 = Sketch_1.addArc(0.01136103592819204, -1.908423938418855e-24, 0.009905484798404638, -0.001371630747896318, 0.009905484798404638, 0.001371630747896318, False)
SketchArc_2.setName("SketchArc_2")
SketchArc_2.result().setName("SketchArc_2")
SketchArc_2.results()[1].setName("SketchArc_2_2")
Sketch_1.setCoincident(SketchLine_1.result(), SketchArc_2.center())
Sketch_1.setCoincident(SketchArc_2.endPoint(), SketchLine_2.result())
Sketch_1.setCoincident(SketchArc_1.startPoint(), SketchArc_2.endPoint())
Sketch_1.setCoincident(SketchArc_2.startPoint(), SketchArc_1.results()[1])
Sketch_1.setRadius(SketchArc_2.results()[1], 0.002)
model.do()

### Create Face
Face_1 = model.addFace(Part_1_doc, [model.selection("FACE", "Sketch_1/Face-SketchArc_5_2f-SketchArc_2_2f")])

### Create Vertex
Vertex_1 = model.addVertex(Part_1_doc, [model.selection("VERTEX", "Sketch_1/SketchArc_2")], False)
#Vertex_1 = model.addVertex(Part_1_doc, [model.selection("VERTEX", "PartSet/Origin")], False)

step = 50
model.addParameter(Part_1_doc, "step", "%i"%step)

faces = [Face_1.result()]
points = [Vertex_1.result()]
for i in range(1, step+1):
    # translate and rotate the point (for path)
    Vertex_i = model.addVertex(Part_1_doc, [model.selection("VERTEX", "Sketch_1/SketchArc_2")])
    Translation_vi = model.addTranslation(Part_1_doc, [Vertex_i.result()], model.selection("EDGE", "PartSet/OZ"), "h/step*%i"%i)
    Rotation_vi = model.addRotation(Part_1_doc, [Translation_vi.result()], model.selection("EDGE", "PartSet/OZ"), "360/step*%i"%i)
    points.append(Rotation_vi.result())

# Create the path
Interpolation_1 = model.addInterpolation(Part_1_doc, points, False, False)

### Create Pipe
Pipe_1 = model.addPipe(Part_1_doc, [model.selection("FACE", "Face_1_1")], model.selection("EDGE", "Interpolation_1_1"), model.selection("EDGE", "PartSet/OZ"))

### Create Rotation
Rotation_51 = model.addRotation(Part_1_doc, [model.selection("SOLID", "Pipe_1_1")], axis = model.selection("EDGE", "PartSet/OZ"), angle = 30, keepSubResults = True)

### Create Sketch
Sketch_2 = model.addSketch(Part_1_doc, model.standardPlane("XOY"))

### Create SketchLine
SketchLine_3 = Sketch_2.addLine(-0.025, 0.04330127018922193, 0.025, 0.04330127018922193)
SketchLine_3.setName("SketchLine_4")
SketchLine_3.result().setName("SketchLine_4")
Sketch_2.setHorizontal(SketchLine_3.result())

### Create SketchLine
SketchLine_4 = Sketch_2.addLine(0.025, 0.04330127018922193, 0.05, 0)
SketchLine_4.setName("SketchLine_5")
SketchLine_4.result().setName("SketchLine_5")
Sketch_2.setCoincident(SketchLine_3.endPoint(), SketchLine_4.startPoint())

### Create SketchLine
SketchLine_5 = Sketch_2.addLine(0.05, 0, 0.025, -0.04330127018922194)
SketchLine_5.setName("SketchLine_6")
SketchLine_5.result().setName("SketchLine_6")
Sketch_2.setCoincident(SketchLine_4.endPoint(), SketchLine_5.startPoint())

### Create SketchLine
SketchLine_6 = Sketch_2.addLine(0.025, -0.04330127018922194, -0.025, -0.04330127018922194)
SketchLine_6.setName("SketchLine_7")
SketchLine_6.result().setName("SketchLine_7")
Sketch_2.setCoincident(SketchLine_5.endPoint(), SketchLine_6.startPoint())
Sketch_2.setHorizontal(SketchLine_6.result())

### Create SketchLine
SketchLine_7 = Sketch_2.addLine(-0.025, -0.04330127018922194, -0.05, 0)
SketchLine_7.setName("SketchLine_8")
SketchLine_7.result().setName("SketchLine_8")
Sketch_2.setCoincident(SketchLine_6.endPoint(), SketchLine_7.startPoint())

### Create SketchLine
SketchLine_8 = Sketch_2.addLine(-0.05, 0, -0.025, 0.04330127018922193)
SketchLine_8.setName("SketchLine_9")
SketchLine_8.result().setName("SketchLine_9")
Sketch_2.setCoincident(SketchLine_7.endPoint(), SketchLine_8.startPoint())
Sketch_2.setCoincident(SketchLine_3.startPoint(), SketchLine_8.endPoint())

### Create SketchProjection
SketchProjection_3 = Sketch_2.addProjection(model.selection("EDGE", "PartSet/OX"), False)
SketchLine_9 = SketchProjection_3.createdFeature()
SketchLine_9.setName("SketchLine_10")
SketchLine_9.result().setName("SketchLine_10")
Sketch_2.setCoincident(SketchLine_5.startPoint(), SketchLine_9.result())

### Create SketchCircle
SketchCircle_1 = Sketch_2.addCircle(2.136318508641679e-26, 1.4617801265323e-26, 0.05)
SketchCircle_1.setAuxiliary(True)
Sketch_2.setCoincident(SketchLine_4.endPoint(), SketchCircle_1.results()[1])
Sketch_2.setCoincident(SketchCircle_1.results()[1], SketchLine_3.endPoint())
Sketch_2.setCoincident(SketchLine_8.endPoint(), SketchCircle_1.results()[1])
Sketch_2.setCoincident(SketchLine_7.endPoint(), SketchCircle_1.results()[1])
Sketch_2.setCoincident(SketchLine_7.startPoint(), SketchCircle_1.results()[1])
Sketch_2.setCoincident(SketchLine_6.startPoint(), SketchCircle_1.results()[1])
Sketch_2.setCoincident(SketchLine_7.endPoint(), SketchLine_9.result())
Sketch_2.setEqual(SketchLine_3.result(), SketchLine_6.result())
Sketch_2.setEqual(SketchLine_3.result(), SketchLine_8.result())
Sketch_2.setRadius(SketchCircle_1.results()[1], 0.05)

### Create SketchProjection
SketchProjection_4 = Sketch_2.addProjection(model.selection("VERTEX", "PartSet/Origin"), False)
SketchPoint_2 = SketchProjection_4.createdFeature()
Sketch_2.setCoincident(SketchCircle_1.center(), SketchAPI_Point(SketchPoint_2).coordinates())

### Create SketchOffset
SketchOffset_1_objects = [SketchLine_8.result(), SketchLine_3.result(), SketchLine_4.result(), SketchLine_5.result(), SketchLine_6.result(), SketchLine_7.result()]
SketchOffset_1 = Sketch_2.addOffset(SketchOffset_1_objects, 0.015, True)
[SketchLine_10, SketchLine_11, SketchLine_12, SketchLine_13, SketchLine_14, SketchLine_15] = SketchOffset_1.offset()
SketchLine_15.setName("SketchLine_16")
SketchLine_15.result().setName("SketchLine_16")
SketchLine_14.setName("SketchLine_15")
SketchLine_14.result().setName("SketchLine_15")
SketchLine_13.setName("SketchLine_14")
SketchLine_13.result().setName("SketchLine_14")
SketchLine_12.setName("SketchLine_13")
SketchLine_12.result().setName("SketchLine_13")
SketchLine_11.setName("SketchLine_12")
SketchLine_11.result().setName("SketchLine_12")
SketchLine_10.setName("SketchLine_11")
SketchLine_10.result().setName("SketchLine_11")
SketchLine_10.setAuxiliary(True)
SketchLine_11.setAuxiliary(True)
SketchLine_12.setAuxiliary(True)
SketchLine_13.setAuxiliary(True)
SketchLine_14.setAuxiliary(True)
SketchLine_15.setAuxiliary(True)
model.do()

### Create Vertex
Vertex_52_objects = [model.selection("VERTEX", "Sketch_2/SketchLine_14_StartVertex"),
                     model.selection("VERTEX", "Sketch_2/SketchLine_13_StartVertex"),
                     model.selection("VERTEX", "Sketch_2/SketchLine_12_StartVertex"),
                     model.selection("VERTEX", "Sketch_2/SketchLine_16_EndVertex"),
                     model.selection("VERTEX", "Sketch_2/SketchLine_16_StartVertex"),
                     model.selection("VERTEX", "Sketch_2/SketchLine_15_StartVertex")]
Vertex_52 = model.addVertex(Part_1_doc, Vertex_52_objects, False)

### Create Translation
Translation_51 = model.addTranslation(Part_1_doc, [model.selection("SOLID", "Rotation_51_1")], startPoint = model.selection("VERTEX", "PartSet/Origin"), endPoint = model.selection("VERTEX", "Sketch_2/SketchLine_14_StartVertex"), keepSubResults = True)

### Create Recover
Recover_1 = model.addRecover(Part_1_doc, Translation_51, [Rotation_51.result()])

### Create Translation
Translation_52 = model.addTranslation(Part_1_doc, [model.selection("SOLID", "Recover_1_1")], startPoint = model.selection("VERTEX", "PartSet/Origin"), endPoint = model.selection("VERTEX", "Vertex_52_2"), keepSubResults = True)

### Create Recover
Recover_2 = model.addRecover(Part_1_doc, Translation_52, [Recover_1.result()])

### Create Translation
Translation_53 = model.addTranslation(Part_1_doc, [model.selection("SOLID", "Recover_2_1")], startPoint = model.selection("VERTEX", "PartSet/Origin"), endPoint = model.selection("VERTEX", "Vertex_52_3"), keepSubResults = True)

### Create Recover
Recover_3 = model.addRecover(Part_1_doc, Translation_53, [Recover_2.result()])

### Create Translation
Translation_54 = model.addTranslation(Part_1_doc, [model.selection("SOLID", "Recover_3_1")], startPoint = model.selection("VERTEX", "PartSet/Origin"), endPoint = model.selection("VERTEX", "Vertex_52_4"), keepSubResults = True)

### Create Recover
Recover_4 = model.addRecover(Part_1_doc, Translation_54, [Recover_3.result()])

### Create Translation
Translation_55 = model.addTranslation(Part_1_doc, [model.selection("SOLID", "Recover_4_1")], startPoint = model.selection("VERTEX", "PartSet/Origin"), endPoint = model.selection("VERTEX", "Vertex_52_5"), keepSubResults = True)

### Create Recover
Recover_5 = model.addRecover(Part_1_doc, Translation_55, [Recover_4.result()])

### Create Translation
Translation_56 = model.addTranslation(Part_1_doc, [model.selection("SOLID", "Recover_5_1")], startPoint = model.selection("VERTEX", "PartSet/Origin"), endPoint = model.selection("VERTEX", "Vertex_52_6"), keepSubResults = True)

### Create Recover
Recover_6 = model.addRecover(Part_1_doc, Translation_56, [Recover_5.result()])

### Create Extrusion
Extrusion_1 = model.addExtrusion(Part_1_doc, [model.selection("FACE", "Sketch_2/Face-SketchLine_9r-SketchLine_8r-SketchLine_7r-SketchLine_6r-SketchLine_5r-SketchLine_4r")], model.selection(), "h", 0, "Faces|Wires")

### Create Cut
Cut_1_objects_2 = [model.selection("SOLID", "Translation_51_1"),
                   model.selection("SOLID", "Translation_52_1"),
                   model.selection("SOLID", "Translation_53_1"),
                   model.selection("SOLID", "Translation_54_1"),
                   model.selection("SOLID", "Translation_55_1"),
                   model.selection("SOLID", "Translation_56_1"),
                   model.selection("SOLID", "Recover_6_1")]
Cut_1 = model.addCut(Part_1_doc, [model.selection("SOLID", "Extrusion_1_1")], Cut_1_objects_2, keepSubResults = True)

### Create Group
Group_1 = model.addGroup(Part_1_doc, "Faces", [model.selection("FACE", "Cut_1_1/Modified_Face&Extrusion_1_1/From_Face")])
Group_1.setName("Inlet")
Group_1.result().setName("Inlet")

### Create Group
Group_2 = model.addGroup(Part_1_doc, "Faces", [model.selection("FACE", "Cut_1_1/Modified_Face&Extrusion_1_1/To_Face")])
Group_2.setName("Outlet")
Group_2.result().setName("Outlet")

model.end()

###
### SHAPERSTUDY component
###

model.publishToShaperStudy()
import SHAPERSTUDY
Cut_1_1, Inlet, Outlet, = SHAPERSTUDY.shape(model.featureStringId(Cut_1))

if salome.sg.hasDesktop():
  salome.sg.updateObjBrowser()
