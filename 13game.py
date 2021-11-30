# -*- coding: utf-8 -*-
"""
Created on Tue Nov 30 20:29:29 2021

@author: user
"""

import direct.directbase.DirectStart
from direct.gui.OnscreenText import OnscreenText
from direct.gui.DirectGui import *
from panda3d.core import *
from panda3d.core import TextNode

from direct.gui.DirectGui import DirectFrame

numItemsVisible = 4
itemHeight = 0.11

myScrolledList = DirectScrolledList(
    decButton_pos=(0.35, 0, 0.53),
    decButton_text="Up",
    decButton_text_scale=0.04,
    decButton_borderWidth=(0.005, 0.005),

    incButton_pos=(0.35, 0, -0.02),
    incButton_text="Down",
    incButton_text_scale=0.04,
    incButton_borderWidth=(0.005, 0.005),

    frameSize=(0.0, 0.7, -0.05, 0.59),
    frameColor=(1,0,6,1),
    pos=(-0.06, 0, 0.15),
    numItemsVisible=numItemsVisible,
    forceHeight=itemHeight,
    itemFrame_frameSize=(-0.4, 0.4, -0.37, 0.11),
    itemFrame_pos=(0.35, 0, 0.4),
)


for fruit in ['Membaca Novel', 'Rebahan', 'Tidur', 'Lari','Ngopi','Main Bola']:
    l = DirectLabel(text=fruit, text_scale=0.1)
    myScrolledList.addItem(l)

# Add some text
bk_text = "Profil Kelompok 3"
textObject = OnscreenText(text=bk_text, pos=(0.0, 0.85), scale=0.07,
                          fg=(0, 0, 6, 6), align=TextNode.ACenter,
                          mayChange=1)

# Add some text
output = ""
textObject = OnscreenText(text=output, pos=(0.012, -0.75), scale=0.07,
                          fg=(0, 0, 6, 6), align=TextNode.ACenter,
                          mayChange=1)
# Callback function to set text
v = [0]

def itemSel(arg):
    if arg == "Pilih Disini Lihat Anggota":
        # Callback function to set  text
        # Add button
        # No need to add an element
        bk_text = "D3 Teknik Informatika PSDKU Kelas E"
        textObject.setText(text=bk_text),
        imageObject = OnscreenImage(
        image='K3.jpeg', pos=(-0.6, 0, 0.45), scale=0.3,)
        
    if arg == "Anggota 1":
        buttons = [DirectRadioButton(text='Kampus UNS Madiun', variable=v, value=[0],
                             scale=0.05, pos=(-0.013,1,-0.90),)]
        for button in buttons:
            button.setOthers(buttons)
        # No need to add an element
        bk_text = "Nama : Ricky Suparman Saragih Nim : V3920051"
        textObject.setText(text=bk_text),
        imageObject = OnscreenImage(
            image='Ricky.jpeg', pos=(0.0, 0, -0.35), scale=0.3,)
    if arg == "Anggota 2":
        buttons = [DirectRadioButton(text='Kampus UNS Madiun', variable=v, value=[0],
                             scale=0.05, pos=(-0.013,1,-0.90),)]
        for button in buttons:
            button.setOthers(buttons)
        # No need to add an element
        bk_text = "Nama : Ridho Walidayin Rifai Nim :(V3920052)"
        textObject.setText(bk_text),
        imageObject = OnscreenImage(
            image='Ridho.jpeg', pos=(0.0, 0, -0.35), scale=0.3,)

    if arg == "Anggota 3":
        buttons = [DirectRadioButton(text='Kampus UNS Madiun', variable=v, value=[0],
                             scale=0.05, pos=(-0.013,1,-0.90),)]
        for button in buttons:
            button.setOthers(buttons)
        # No need to add an element
        bk_text = "Nama : Rosa Auralia Adhani Saleha Nim : (V3920055)"
        textObject.setText(bk_text),
        imageObject = OnscreenImage(
            image='Rosa.jpeg', pos=(0.0, 0, -0.35), scale=0.3,)

    if arg == "Anggota 4":
        buttons = [DirectRadioButton(text='Kampus UNS Madiun', variable=v, value=[0],
                             scale=0.05, pos=(-0.013,1,-0.90),)]
        for button in buttons:
            button.setOthers(buttons)
        # No need to add an element
        bk_text = "Nama : Zulfkar Ahmadi Rafsanjani Nim : (V3920066)"
        textObject.setText(bk_text),
        imageObject = OnscreenImage(
            image='Zulfikar.jpg', pos=(0.0, 0, -0.35), scale=0.3,)

# Create a frame
menu = DirectOptionMenu(text="options", scale=0.1, initialitem=4, 
                        items=["Pilih Disini Lihat Anggota", "Anggota 1",
                               "Anggota 2", "Anggota 3", "Anggota 4"], 
                        highlightColor=(0.0, 0.0, 0.1, 1),
                        command=itemSel, textMayChange=1)


def showValue():
    return menu



# Procedurally select a item
menu.set(0)

# Run the program
base.run()