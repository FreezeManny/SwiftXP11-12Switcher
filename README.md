# SwiftXP11-12Switcher
This script allows you to switch Swift Version 0.12.2 between XP11 and XP12 use in a single install.

Instruction:
set up config.json
1. At first find out the paths of the folder where the X-Plane 11 and X-Plane 12 .exe file is located at. Enter these paths in the "" behind the "xp1X_path".
2. Now we will find the appdata folder of swift in the appdata. For that enter %appdatalocal% into the taskbar and look for the org.swift.XXXX folder. In this folder you will find the folders containing the saved data from Swift. Select one of those and copy the path to "swift_appdata_path".
3. Finally we will be looking for the main swift folder, where the bin, shared, etc. folders are located at. Enter this path behind "swift_exe_path".
4. Now we have set up the config.json and it should look something like this 
  ```
  {
    "xp11_path": "",
    "xp12_path": "",
    "swift_appdata_path": "",
    "swift_exe_path":""
  }
  ```
A detailed installation Video will follow shortly
