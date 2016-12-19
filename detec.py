import glob
import os


os.chdir("my_video")
for file in glob.glob("*.mp4"):
    os.system("python autosub_app.py %s" % file)
