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

from salome.shaper import model

model.begin()
partSet = model.moduleDocument()

### Create Part
Part_1 = model.addPart(partSet)
Part_1_doc = Part_1.document()
model.addParameter(Part_1_doc, "d", '1')
model.addParameter(Part_1_doc, "D", '10')
model.addParameter(Part_1_doc, "m", '8')

### Create Box
Box_1 = model.addBox(Part_1_doc, 1, 1, 1)
Box_1.setName("Box1")
Box_1.result().setName("Box_1_1")

### Create Box
Box_2 = model.addBox(Part_1_doc, 1, 1, 1)
Box_2.setName("Box2")
Box_2.result().setName("Box_2_1")

### Create Translation
Translation_1 = model.addTranslation(Part_1_doc, [model.selection("COMPOUND", "all-in-Box2")], vector = [0, "m+d+D", -1], keepSubResults = True)
Translation_1.setName("Translation_Box2")
Translation_1.result().setName("Translation_1_1")
Translation_1.result().subResult(0).setName("Translation_1_1_1")

### Create Axis
Axis_4 = model.addAxis(Part_1_doc, model.selection("VERTEX", "[Box_1_1/Back][Box_1_1/Right][Box_1_1/Top]"), model.selection("VERTEX", "[Translation_1_1_1/MF:Translated&Box_2_1/Back][Translation_1_1_1/MF:Translated&Box_2_1/Left][Translation_1_1_1/MF:Translated&Box_2_1/Top]"))
Axis_4.setName("Axis_1_to_2")
Axis_4.result().setName("Axis_1")

### Create ExtrusionFuse
ExtrusionFuse_1 = model.addExtrusionFuse(Part_1_doc, [model.selection("FACE", "Box_1_1/Right")], model.selection("EDGE", "Axis_1"), model.selection("FACE", "Translation_1_1_1/MF:Translated&Box_2_1/Left"), 0, model.selection(), 0, [model.selection("SOLID", "Box_1_1")])
ExtrusionFuse_1.setName("Box1_to_Box2")
ExtrusionFuse_1.result().setName("ExtrusionFuse_1_1")

### Create Box
Box_3 = model.addBox(Part_1_doc, 1, 1, 1)
Box_3.setName("Box3")
Box_3.result().setName("Box_3_1")

### Create Translation
Translation_2 = model.addTranslation(Part_1_doc, [model.selection("COMPOUND", "all-in-Box3")], vector = ["d+D", "m+d+D", -1.5], keepSubResults = True)
Translation_2.setName("Translation_Box3")
Translation_2.result().setName("Translation_2_1")
Translation_2.result().subResult(0).setName("Translation_2_1_1")

### Create Axis
Axis_5 = model.addAxis(Part_1_doc, model.selection("VERTEX", "[Translation_1_1_1/MF:Translated&Box_2_1/Front][Translation_1_1_1/MF:Translated&Box_2_1/Right][Translation_1_1_1/MF:Translated&Box_2_1/Top]"), model.selection("VERTEX", "[Translation_2_1_1/MF:Translated&Box_3_1/Back][Translation_2_1_1/MF:Translated&Box_3_1/Right][Translation_2_1_1/MF:Translated&Box_3_1/Top]"))
Axis_5.setName("Axis_2_to_3")
Axis_5.result().setName("Axis_2")

### Create ExtrusionFuse
ExtrusionFuse_2 = model.addExtrusionFuse(Part_1_doc, [model.selection("FACE", "Translation_1_1_1/MF:Translated&Box_2_1/Front")], model.selection("EDGE", "Axis_2"), model.selection("FACE", "Translation_2_1_1/MF:Translated&Box_3_1/Back"), 0, model.selection(), 0, [model.selection("SOLID", "Translation_1_1_1")])
ExtrusionFuse_2.setName("Box2_to_Box3")
ExtrusionFuse_2.result().setName("ExtrusionFuse_2_1")

### Create Box
Box_4 = model.addBox(Part_1_doc, 1, 1, 1)
Box_4.setName("Box4")
Box_4.result().setName("Box_4_1")

### Create Translation
Translation_3 = model.addTranslation(Part_1_doc, [model.selection("COMPOUND", "all-in-Box4")], vector = ["d+D", "m", 0.5], keepSubResults = True)
Translation_3.setName("Translation_Box4")
Translation_3.result().setName("Translation_3_1")
Translation_3.result().subResult(0).setName("Translation_3_1_1")

### Create Axis
Axis_6 = model.addAxis(Part_1_doc, model.selection("VERTEX", "[Translation_2_1_1/MF:Translated&Box_3_1/Front][Translation_2_1_1/MF:Translated&Box_3_1/Left][Translation_2_1_1/MF:Translated&Box_3_1/Top]"), model.selection("VERTEX", "[Translation_3_1_1/MF:Translated&Box_4_1/Front][Translation_3_1_1/MF:Translated&Box_4_1/Right][Translation_3_1_1/MF:Translated&Box_4_1/Top]"))
Axis_6.setName("Axis_3_to_4")
Axis_6.result().setName("Axis_3")

### Create ExtrusionFuse
ExtrusionFuse_3 = model.addExtrusionFuse(Part_1_doc, [model.selection("FACE", "Translation_2_1_1/MF:Translated&Box_3_1/Left")], model.selection("EDGE", "Axis_3"), model.selection("FACE", "Translation_3_1_1/MF:Translated&Box_4_1/Right"), 0, model.selection(), 0, [model.selection("SOLID", "Translation_2_1_1")])
ExtrusionFuse_3.setName("Box3_to_Box4")
ExtrusionFuse_3.result().setName("ExtrusionFuse_3_1")

### Create Box
Box_5 = model.addBox(Part_1_doc, 1, 1, 1)
Box_5.setName("Box5")
Box_5.result().setName("Box_5_1")

### Create Translation
Translation_4 = model.addTranslation(Part_1_doc, [model.selection("COMPOUND", "all-in-Box5")], vector = ["-2*d", "m", -2.5], keepSubResults = True)
Translation_4.setName("Translation_Box5")
Translation_4.result().setName("Translation_4_1")
Translation_4.result().subResult(0).setName("Translation_4_1_1")

### Create Axis
Axis_7 = model.addAxis(Part_1_doc, model.selection("VERTEX", "[Translation_3_1_1/MF:Translated&Box_4_1/Back][Translation_3_1_1/MF:Translated&Box_4_1/Left][Translation_3_1_1/MF:Translated&Box_4_1/Top]"), model.selection("VERTEX", "[Translation_4_1_1/MF:Translated&Box_5_1/Front][Translation_4_1_1/MF:Translated&Box_5_1/Left][Translation_4_1_1/MF:Translated&Box_5_1/Top]"))
Axis_7.setName("Axis_4_to_5")
Axis_7.result().setName("Axis_4")

### Create ExtrusionFuse
ExtrusionFuse_4 = model.addExtrusionFuse(Part_1_doc, [model.selection("FACE", "Translation_3_1_1/MF:Translated&Box_4_1/Back")], model.selection("EDGE", "Axis_4"), model.selection("FACE", "Translation_4_1_1/MF:Translated&Box_5_1/Front"), 0, model.selection(), 0, [model.selection("SOLID", "Translation_3_1_1")])
ExtrusionFuse_4.setName("Box4_to_Box5")
ExtrusionFuse_4.result().setName("ExtrusionFuse_4_1")

### Create Box
Box_6 = model.addBox(Part_1_doc, 1, 1, 1)
Box_6.setName("Box6")
Box_6.result().setName("Box_6_1")

### Create Translation
Translation_5 = model.addTranslation(Part_1_doc, [model.selection("COMPOUND", "all-in-Box6")], vector = ["-2*d", "m+3*d+D", 0], keepSubResults = True)
Translation_5.setName("Translation_Box6")
Translation_5.result().setName("Translation_5_1")
Translation_5.result().subResult(0).setName("Translation_5_1_1")

### Create Axis
Axis_8 = model.addAxis(Part_1_doc, model.selection("VERTEX", "[Translation_4_1_1/MF:Translated&Box_5_1/Back][Translation_4_1_1/MF:Translated&Box_5_1/Right][Translation_4_1_1/MF:Translated&Box_5_1/Top]"), model.selection("VERTEX", "[Translation_5_1_1/MF:Translated&Box_6_1/Back][Translation_5_1_1/MF:Translated&Box_6_1/Left][Translation_5_1_1/MF:Translated&Box_6_1/Top]"))
Axis_8.setName("Axis_5_to_6")
Axis_8.result().setName("Axis_5")

### Create ExtrusionFuse
ExtrusionFuse_5 = model.addExtrusionFuse(Part_1_doc, [model.selection("FACE", "Translation_4_1_1/MF:Translated&Box_5_1/Right")], model.selection("EDGE", "Axis_5"), model.selection("FACE", "Translation_5_1_1/MF:Translated&Box_6_1/Left"), 0, model.selection(), 0, [model.selection("SOLID", "Translation_4_1_1")])
ExtrusionFuse_5.setName("Box5_to_Box6")
ExtrusionFuse_5.result().setName("ExtrusionFuse_5_1")

### Create Box
Box_7 = model.addBox(Part_1_doc, 1, 1, 1)
Box_7.setName("Box7")
Box_7.result().setName("Box_7_1")

### Create Translation
Translation_6 = model.addTranslation(Part_1_doc, [model.selection("COMPOUND", "all-in-Box7")], vector = ["-d+D", "m+3*d+D", 0.5], keepSubResults = True)
Translation_6.setName("Translation_Box7")
Translation_6.result().setName("Translation_6_1")
Translation_6.result().subResult(0).setName("Translation_6_1_1")

### Create Axis
Axis_9 = model.addAxis(Part_1_doc, model.selection("VERTEX", "[Translation_5_1_1/MF:Translated&Box_6_1/Front][Translation_5_1_1/MF:Translated&Box_6_1/Right][Translation_5_1_1/MF:Translated&Box_6_1/Top]"), model.selection("VERTEX", "[Translation_6_1_1/MF:Translated&Box_7_1/Back][Translation_6_1_1/MF:Translated&Box_7_1/Right][Translation_6_1_1/MF:Translated&Box_7_1/Top]"))
Axis_9.setName("Axis_6_to_7")
Axis_9.result().setName("Axis_6")

### Create ExtrusionFuse
ExtrusionFuse_6 = model.addExtrusionFuse(Part_1_doc, [model.selection("FACE", "Translation_5_1_1/MF:Translated&Box_6_1/Front")], model.selection("EDGE", "Axis_6"), model.selection("FACE", "Translation_6_1_1/MF:Translated&Box_7_1/Back"), 0, model.selection(), 0, [model.selection("SOLID", "Translation_5_1_1")])
ExtrusionFuse_6.setName("Box6_to_Box7")
ExtrusionFuse_6.result().setName("ExtrusionFuse_6_1")

### Create Box
Box_8 = model.addBox(Part_1_doc, 1, 1, 1)
Box_8.setName("Box8")
Box_8.result().setName("Box_8_1")

### Create Translation
Translation_7 = model.addTranslation(Part_1_doc, [model.selection("COMPOUND", "all-in-Box8")], vector = ["D-d", 0, -2.5], keepSubResults = True)
Translation_7.setName("Translation_Box8")
Translation_7.result().setName("Translation_7_1")
Translation_7.result().subResult(0).setName("Translation_7_1_1")

### Create Axis
Axis_10 = model.addAxis(Part_1_doc, model.selection("VERTEX", "[Translation_6_1_1/MF:Translated&Box_7_1/Front][Translation_6_1_1/MF:Translated&Box_7_1/Left][Translation_6_1_1/MF:Translated&Box_7_1/Top]"), model.selection("VERTEX", "[Translation_7_1_1/MF:Translated&Box_8_1/Front][Translation_7_1_1/MF:Translated&Box_8_1/Right][Translation_7_1_1/MF:Translated&Box_8_1/Top]"))
Axis_10.setName("Axis_7_to_8")
Axis_10.result().setName("Axis_7")

### Create ExtrusionFuse
ExtrusionFuse_7 = model.addExtrusionFuse(Part_1_doc, [model.selection("FACE", "Translation_6_1_1/MF:Translated&Box_7_1/Left")], model.selection("EDGE", "Axis_7"), model.selection("FACE", "Translation_7_1_1/MF:Translated&Box_8_1/Right"), 0, model.selection(), 0, [model.selection("SOLID", "Translation_6_1_1")])
ExtrusionFuse_7.setName("Box7_to_Box8")
ExtrusionFuse_7.result().setName("ExtrusionFuse_7_1")

### Create CompSolid
CompSolid_1_objects = [model.selection("SOLID", "ExtrusionFuse_1_1"),
                       model.selection("SOLID", "ExtrusionFuse_2_1"),
                       model.selection("SOLID", "ExtrusionFuse_3_1"),
                       model.selection("SOLID", "ExtrusionFuse_4_1"),
                       model.selection("SOLID", "ExtrusionFuse_5_1"),
                       model.selection("SOLID", "ExtrusionFuse_6_1"),
                       model.selection("COMPOUND", "Translation_7_1"),
                       model.selection("SOLID", "ExtrusionFuse_7_1")]
CompSolid_1 = model.addCompSolid(Part_1_doc, CompSolid_1_objects)
CompSolid_1.result().setName("CompSolid_1_1")

### Create Box
Box_9 = model.addBox(Part_1_doc, "2*m+2*d+D", "2*m+2*d+D", "3+4*d")

### Create Translation
Translation_8 = model.addTranslation(Part_1_doc, [model.selection("COMPSOLID", "CompSolid_1_1")], vector = ["4*d+D/2", 0, "1.5+2*d"], keepSubResults = True)

### Create Cut
Cut_1 = model.addCut(Part_1_doc, [model.selection("SOLID", "Box_9_1")], [model.selection("COMPSOLID", "Translation_8_1")], keepSubResults = True)

model.end()

###
### SHAPERSTUDY component
###

model.publishToShaperStudy()
import SHAPERSTUDY
Cut_1_1, = SHAPERSTUDY.shape(model.featureStringId(Cut_1))

if salome.sg.hasDesktop():
  salome.sg.updateObjBrowser()
