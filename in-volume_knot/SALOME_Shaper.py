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
model.addParameter(Part_1_doc, "cube_length", '1', 'Length of the cubes -> width of the knot path')
model.addParameter(Part_1_doc, "outer_margin", '1.5', 'margin between the knot and the bounding box (XY)')
model.addParameter(Part_1_doc, "inner_margin", '1', 'margin between 2 branches of the knot (XY)')
model.addParameter(Part_1_doc, "branch_length", '10', 'length of a branch of the knot')
model.addParameter(Part_1_doc, "knot_height", '3')

### Create Box
Box_1 = model.addBox(Part_1_doc, "cube_length", "cube_length", "cube_length")

### Create Translation
Translation_1 = model.addTranslation(Part_1_doc, [model.selection("COMPOUND", "all-in-Box_1")], vector = ["outer_margin+cube_length+inner_margin", 0, "outer_margin + knot_height - cube_length"], keepSubResults = True)
Translation_1.result().setName("Translated_Box_1")

### Create Box
Box_2 = model.addBox(Part_1_doc, "cube_length", "cube_length", "cube_length")

### Create Translation
Translation_2 = model.addTranslation(Part_1_doc, [model.selection("COMPOUND", "all-in-Box_2")], vector = ["outer_margin+cube_length+inner_margin", "outer_margin+cube_length+branch_length", "outer_margin + 0.5*knot_height-0.5*cube_length"], keepSubResults = True)
Translation_2.result().setName("Translated_Box_2")

### Create Box
Box_3 = model.addBox(Part_1_doc, "cube_length", "cube_length", "cube_length")

### Create Translation
Translation_3 = model.addTranslation(Part_1_doc, [model.selection("COMPOUND", "all-in-Box_3")], vector = ["outer_margin+2*cube_length+inner_margin+branch_length", "outer_margin+cube_length+branch_length", "outer_margin"], keepSubResults = True)
Translation_3.result().setName("Translated_Box_3")

### Create Box
Box_4 = model.addBox(Part_1_doc, "cube_length", "cube_length", "cube_length")

### Create Translation
Translation_4 = model.addTranslation(Part_1_doc, [model.selection("COMPOUND", "all-in-Box_4")], vector = ["outer_margin+2*cube_length+inner_margin+branch_length", "outer_margin", "outer_margin + knot_height - cube_length"], keepSubResults = True)
Translation_4.result().setName("Translated_Box_4")

### Create Box
Box_5 = model.addBox(Part_1_doc, "cube_length", "cube_length", "cube_length")

### Create Translation
Translation_5 = model.addTranslation(Part_1_doc, [model.selection("COMPOUND", "all-in-Box_5")], vector = ["outer_margin", "outer_margin", "outer_margin"], keepSubResults = True)
Translation_5.result().setName("Translated_Box_5")

### Create Box
Box_6 = model.addBox(Part_1_doc, "cube_length", "cube_length", "cube_length")

### Create Translation
Translation_6 = model.addTranslation(Part_1_doc, [model.selection("COMPOUND", "all-in-Box_6")], vector = ["outer_margin", "outer_margin+2*cube_length+branch_length+inner_margin", "outer_margin + 0.5*knot_height - 0.5*cube_length"], keepSubResults = True)
Translation_6.result().setName("Translated_Box_6")

### Create Box
Box_7 = model.addBox(Part_1_doc, "cube_length", "cube_length", "cube_length")

### Create Translation
Translation_7 = model.addTranslation(Part_1_doc, [model.selection("COMPOUND", "all-in-Box_7")], vector = ["outer_margin+cube_length+branch_length", "outer_margin+2*cube_length+branch_length+inner_margin", "outer_margin + knot_height - cube_length"], keepSubResults = True)
Translation_7.result().setName("Translated_Box_7")

### Create Box
Box_8 = model.addBox(Part_1_doc, "cube_length", "cube_length", "cube_length")

### Create Translation
Translation_8 = model.addTranslation(Part_1_doc, [model.selection("COMPOUND", "all-in-Box_8")], vector = ["outer_margin+cube_length+branch_length", 0, "outer_margin"], keepSubResults = True)
Translation_8.result().setName("Translated_Box_8")

### Create Loft
Loft_1 = model.addLoft(Part_1_doc, model.selection("FACE", "Translation_1_1_1/MF:Translated&Box_1_1/Right"), model.selection("FACE", "Translation_2_1_1/MF:Translated&Box_2_1/Left"))
Loft_1.setName("Loft_Box_1_to_Box_2")
Loft_1.result().setName("Translated_Box_1")

### Create Recover
Recover_1 = model.addRecover(Part_1_doc, Loft_1, [Translation_1.result().subResult(0), Translation_2.result().subResult(0)])
Recover_1.setName("Recover_Box_1_and_Box_2")
Recover_1.result().setName("Recover_1_1")
Recover_1.results()[1].setName("Recover_1_2")

### Create Loft
Loft_2 = model.addLoft(Part_1_doc, model.selection("FACE", "Recover_1_1/Modified_Face&Box_2_1/Front"), model.selection("FACE", "Translation_3_1_1/MF:Translated&Box_3_1/Back"))
Loft_2.setName("Loft_Box_2_to_Box_3")
Loft_2.result().setName("Loft_2_1")

### Create Recover
Recover_2 = model.addRecover(Part_1_doc, Loft_2, [Recover_1.result(), Translation_3.result().subResult(0)])
Recover_2.setName("Recover_Box2_and_Box_3")
Recover_2.result().setName("Recover_2_1")
Recover_2.results()[1].setName("Recover_2_2")

### Create Loft
Loft_3 = model.addLoft(Part_1_doc, model.selection("FACE", "Recover_2_1/Modified_Face&Box_3_1/Left"), model.selection("FACE", "Translation_4_1_1/MF:Translated&Box_4_1/Right"))
Loft_3.setName("Loft_Box_3_to_Box_4")
Loft_3.result().setName("Loft_3_1")

### Create Recover
Recover_3 = model.addRecover(Part_1_doc, Loft_3, [Recover_2.result(), Translation_4.result().subResult(0)])
Recover_3.setName("Recover_Box_3_and_Box_4")
Recover_3.result().setName("Recover_3_1")
Recover_3.results()[1].setName("Recover_3_2")

### Create Loft
Loft_4 = model.addLoft(Part_1_doc, model.selection("FACE", "Recover_3_1/Modified_Face&Box_4_1/Back"), model.selection("FACE", "Translation_5_1_1/MF:Translated&Box_5_1/Front"))
Loft_4.setName("Loft_Box_4_to_Box_5")
Loft_4.result().setName("Loft_4_1")

### Create Recover
Recover_4 = model.addRecover(Part_1_doc, Loft_4, [Recover_3.result(), Translation_5.result().subResult(0)])
Recover_4.setName("Recover_Box_4_and_Box_5")
Recover_4.result().setName("Recover_4_1")
Recover_4.results()[1].setName("Recover_4_2")

### Create Loft
Loft_5 = model.addLoft(Part_1_doc, model.selection("FACE", "Recover_4_1/Modified_Face&Box_5_1/Right"), model.selection("FACE", "Translation_6_1_1/MF:Translated&Box_6_1/Left"))
Loft_5.setName("Loft_Box_5_to_Box_6")
Loft_5.result().setName("Loft_5_1")

### Create Recover
Recover_5 = model.addRecover(Part_1_doc, Loft_5, [Recover_4.result(), Translation_6.result().subResult(0)])
Recover_5.setName("Recover_Box_5_and_Box_6")
Recover_5.result().setName("Recover_5_1")
Recover_5.results()[1].setName("Recover_5_2")

### Create Loft
Loft_6 = model.addLoft(Part_1_doc, model.selection("FACE", "Recover_5_1/Modified_Face&Box_6_1/Front"), model.selection("FACE", "Translation_7_1_1/MF:Translated&Box_7_1/Back"))
Loft_6.setName("Loft_Box_6_to_Box_7")
Loft_6.result().setName("Loft_6_1")

### Create Recover
Recover_6 = model.addRecover(Part_1_doc, Loft_6, [Recover_5.result(), Translation_7.result().subResult(0)])
Recover_6.setName("Recover_Box_6_and_Box_7")
Recover_6.result().setName("Recover_6_1")
Recover_6.results()[1].setName("Recover_6_2")

### Create Loft
Loft_7 = model.addLoft(Part_1_doc, model.selection("FACE", "Recover_6_1/Modified_Face&Box_7_1/Left"), model.selection("FACE", "Translation_8_1_1/MF:Translated&Box_8_1/Right"))
Loft_7.setName("Loft_Box_7_to_Box_8")
Loft_7.result().setName("Loft_7_1")

### Create Recover
Recover_7 = model.addRecover(Part_1_doc, Loft_7, [Recover_6.result(), Translation_8.result().subResult(0)])
Recover_7.setName("Recover_Box_7_and_Box_8")
Recover_7.result().setName("Recover_7_1")
Recover_7.results()[1].setName("Recover_7_2")

### Create Fuse
Fuse_1_objects_1 = [model.selection("SOLID", "Translated_Box_1"),
                    model.selection("SOLID", "Recover_1_2"),
                    model.selection("SOLID", "Loft_2_1"),
                    model.selection("SOLID", "Recover_2_2"),
                    model.selection("SOLID", "Loft_3_1"),
                    model.selection("SOLID", "Recover_3_2"),
                    model.selection("SOLID", "Loft_4_1"),
                    model.selection("SOLID", "Recover_4_2"),
                    model.selection("SOLID", "Loft_5_1"),
                    model.selection("SOLID", "Recover_5_2"),
                    model.selection("SOLID", "Loft_6_1"),
                    model.selection("SOLID", "Recover_6_2"),
                    model.selection("SOLID", "Loft_7_1"),
                    model.selection("SOLID", "Recover_7_1"),
                    model.selection("SOLID", "Recover_7_2")]
Fuse_1 = model.addFuse(Part_1_doc, Fuse_1_objects_1, keepSubResults = True)

### Create Box
Box_9 = model.addBox(Part_1_doc, "2*outer_margin + 3*cube_length + branch_length + inner_margin", "2*outer_margin + 3*cube_length + branch_length + inner_margin", "2*outer_margin + knot_height")

### Create Cut
Cut_1 = model.addCut(Part_1_doc, [model.selection("SOLID", "Box_9_1")], [model.selection("SOLID", "Translated_Box_1")], keepSubResults = True)

model.end()

###
### SHAPERSTUDY component
###

model.publishToShaperStudy()
import SHAPERSTUDY
Cut_1_1, = SHAPERSTUDY.shape(model.featureStringId(Cut_1))

if salome.sg.hasDesktop():
  salome.sg.updateObjBrowser()
