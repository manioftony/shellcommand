import urllib
testfile = urllib.URLopener()
import commands;
commands.getoutput("mkdir imagestoday")
for i in range(1,30):
    try:
        testfile.retrieve("http://epaper.dailythanthi.com/downloadpicture.ashx?url=D:\epaper_fs/080917/page/FE_0908_MN_{0:02d}_Cni_mr.jpg".format(i), "imagestoday/file{0:02d}.jpg".format(i))
    except:
        pass
