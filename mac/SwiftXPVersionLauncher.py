#!/usr/bin/env python
#Set your XP11, 12 and Swift Main Folders

import tkinter as tk
import tkinter.font as tkFont

import json
import shutil
import os



#Load Paths
temp_file = open("config.json", "r")
json_object = json.load(temp_file)
temp_file.close()

xp11_path = json_object["xp11_path"]
xp12_path = json_object["xp12_path"]
swift_appdata_path = json_object["swift_appdata_path"]
swift_exe_path = json_object["swift_exe_path"]   


def replaceSimPath(sim_path):
    #sim_path is the directory to each simulator

    #read json
    temp_file = open(swift_appdata_path + "/settings/core/settingssimulatorxplane.json", "r")
    json_object = json.load(temp_file)
    temp_file.close()
    #edit json
    json_object["settingssimulatorxplane"]["value"]["simulatorDirectory"] = sim_path
    #safe json
    temp_file = open(swift_appdata_path + "/settings/core/settingssimulatorxplane.json", "w")
    json.dump(json_object, temp_file)
    temp_file.close()

def replaceModelSet(modelset_path):
    shutil.copy(modelset_path, swift_appdata_path + "/data/cache/core/modelsetxp.json")
    

class App:
    def __init__(self, root):
        #setting title
        root.title("")
        #setting window size
        width=190
        height=200
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        xp11_btn=tk.Button(root)
        xp11_btn["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=18)
        xp11_btn["font"] = ft
        xp11_btn["fg"] = "#000000"
        xp11_btn["justify"] = "center"
        xp11_btn["text"] = "X-Plane 11"
        xp11_btn.place(x=20,y=60,width=150,height=50)
        xp11_btn["command"] = self.xp11_btn_command

        xp12_btn=tk.Button(root)
        xp12_btn["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=18)
        xp12_btn["font"] = ft
        xp12_btn["fg"] = "#000000"
        xp12_btn["justify"] = "center"
        xp12_btn["text"] = "X-Plane 12"
        xp12_btn.place(x=20,y=130,width=150,height=50)
        xp12_btn["command"] = self.xp12_btn_command

        GLabel_167=tk.Label(root)
        ft = tkFont.Font(family='Times',size=11)
        GLabel_167["font"] = ft
        GLabel_167["fg"] = "#333333"
        GLabel_167["justify"] = "center"
        GLabel_167["text"] = "Select Simulator for Swift\nto launch with:"
        GLabel_167.place(x=15,y=10,width=160,height=40)

    def xp11_btn_command(self):
        replaceSimPath(xp11_path)
        replaceModelSet("modelsets/modelsetxp11.json")
        os.system("open " + swift_exe_path + "/bin/swiftguistd.app")
        root.destroy()


    def xp12_btn_command(self):
        replaceSimPath(xp12_path)
        replaceModelSet("modelsets/modelsetxp12.json")
        os.system("open " + swift_exe_path + "/bin/swiftguistd.app")
        root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()