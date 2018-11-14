 # -*- coding: utf-8 -*
import sys
import os
import zipfile
#定义反编译路径, 把dex2jar, ji-gui等放到ApkDecompile文件夹下
dapk_path=os.path.abspath('apkd.py')
decompile_lib=dapk_path[0:dapk_path.rindex("/")] + "/libs/"

if len(sys.argv) <2:
	print('Usage: python apkd.py [Apk/Dex filepath]')
else:
	apk_path = sys.argv[1]
	apk_decompile_path = apk_path[0:apk_path.index(".")]

	print("apkd will process:"+apk_path)
	#反编译apk
	if "apk" in apk_path:
		print("process apk:" + apk_path)
		os.system("{}/apktool.sh d {} -o {} -f".format(decompile_lib, apk_path, apk_decompile_path))
		print (apk_path[0:apk_path.index(".")])
		filesInZip = zipfile.ZipFile(apk_path, "r")
		filesInZip.extract("classes.dex", apk_decompile_path)
		filesInZip.close()
		apk_path = apk_decompile_path + "/classes.dex"

	#反编译dex
	if "dex" in apk_path:
		print("process dex:"+apk_path)
		os.system("{}/dex2jar-2.0/d2j-dex2jar.sh {} -o {}/output.jar --force".format(decompile_lib, apk_path ,apk_decompile_path))

	os.system("java -jar {}/jd-gui/jd-gui-1.4.0.jar {}/output.jar".format(decompile_lib, apk_decompile_path))
