import os
import time
def dfs():
    cmd=["adb shell input tap 517 1845",
         "adb shell input tap 310 1870",
         "adb shell input tap 578 1687",
         "adb shell input tap 767 2046",
         "adb shell input tap 763 1847",
         "adb shell input tap 541 2030",
         "adb shell input tap 582 1993",
         "adb shell input tap 544 1730 ",
         "adb shell input tap 779 1870",
         "adb shell input tap 292 1858",
         "adb shell input tap 775 2039",
         "adb shell input tap 291 1854",
         "adb shell input tap 90 1550",
         ]
    for i in cmd:
         os.system(i)
    time.sleep(3)
    os.system("adb shell input tap 850 1454")
    time.sleep(20)
    os.system("adb shell input tap 1019 1089")
    for i in range(4):
         os.system("adb shell input tap  982 1695")

for i in range(100):
     dfs()

