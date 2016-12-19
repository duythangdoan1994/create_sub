import glob
import os


for file in glob.glob("*.mp4"):
    print file
    os.system("autosub %s" % file)
