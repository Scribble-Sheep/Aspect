from Aspect import *
from Nord import *
from tkinter import *
from functools import partial
import pyperclip as clip

backgroundCol=Nord[0]
foregroundCol=Nord[5]

def CopyFromEntry(textObject: Entry, test=False)-> None:
    if test:
        print(textObject.get())
    else:
        clip.copy(textObject.get())

def createLabeledEntryFrame(root: Frame, scale, labelText: str, variable = "", status="normal", copybutton = "false"):
    newFrame = Frame(root, width=fullWidth*scale, height = 20, bg=backgroundCol)
    newFrame.pack_propagate(0)
    
    if variable !="":
        oEntry = Entry(newFrame, textvariable= variable, state=status, bg=Nord[1], fg=foregroundCol, selectforeground = Nord[1], selectbackground= Nord[8])
    else:
        oEntry = Entry(newFrame, state=status, bg=backgroundCol, fg=foregroundCol, relief=FLAT, selectforeground = Nord[1], selectbackground= Nord[8])
    oEntry.pack(side=RIGHT)
    Label(newFrame, text= labelText, bg=backgroundCol, fg=foregroundCol).pack(side=LEFT)
    if (copybutton==True):
        CopyButton = Button(newFrame, text="C", bd = 0, fg= backgroundCol, bg= Nord[8], activebackground=backgroundCol, activeforeground=foregroundCol)
        CopyButton.pack(side=RIGHT, fill=Y)
        CopyButton.config(command = partial(CopyFromEntry, oEntry))
    return newFrame, oEntry

def outputResults(wEntry: Entry, hEntry: Entry, mEntry: Entry, width, height):
    print(width.get())
    dims= printDimensions(width.get(),height.get())
    wEntry.delete(0, END)
    wEntry.insert(0, dims[0][0])

    hEntry.delete(0, END)
    hEntry.insert(0, dims[0][1])

    mEntry.delete(0, END)
    mEntry.insert(0, "{:,}".format(dims[1]))
    print("hooray!")


#* Window Properties *#
fullWidth = 250
fullHeight = 150
upperBorder = 10

root = Tk()
root.title("FA MP tool")
root.geometry(str(fullWidth)+"x"+str(fullHeight))
root.config(bg=backgroundCol)

width= IntVar(value=1)
height = IntVar(value=1)

#* Set up Frames *#
borderFrame = Frame(root, width=fullWidth, height=upperBorder, bg=backgroundCol)
borderFrame.pack_propagate(0)
borderFrame.pack(side=TOP)

createLabeledEntryFrame(root, 1, "Original Width: ", width)[0].pack(side=TOP)
createLabeledEntryFrame(root, 1, "Original Height: ", height)[0].pack(side=TOP)
calcOnDimensionButton = Button(root, text="calculaaaaaate", relief=FLAT, fg=backgroundCol, bg=Nord[8], activebackground= Nord[8])
calcOnDimensionButton.pack(side=TOP)
# root: Frame, scale, labelText: str, variable = "", status="normal", copybutton = "false"):
entryFrameW = createLabeledEntryFrame(root, 1, "New Width: ", "", "normal", True)
entryFrameW[0].pack(side=TOP)
entryFrameH = createLabeledEntryFrame(root, 1, "New Height: ", "", "normal", True)
entryFrameH[0].pack(side=TOP)

megaPixFrame = createLabeledEntryFrame(root, 1, "Megapixels ")
megaPixFrame[0].pack(side=TOP)

calcOnDimensionButton.config(command=partial(outputResults, entryFrameW[1], entryFrameH[1], megaPixFrame[1], width, height))

root.mainloop()