import os

print("coded by: justakazh\n\n")

os.system("frida-ps -Uai")
i = str(input("APK Identifier : ")) 
os.system("frida -U -f "+i+" -l Frida-android-unpinning-ssl.js --no-pause")