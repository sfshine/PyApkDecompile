 # -*- coding: utf-8 -*
import sys
import os
import zipfile
#定义反编译路径, 请把dex2jar, ji-gui等放到ApkDecompile文件夹下
decompile_lib=os.path.split(os.path.realpath(__file__))[0] + "/libs/"
if len(sys.argv) <2:
	print('Usage: python apkd.py [Apk/Dex filepath]')
else:
	file_path = sys.argv[1]
	apk_decompile_path = file_path[0:file_path.index(".")]

	print("apkd will process:"+file_path)
	#反编译apk
	if "apk" in file_path:
		print("process apk:" + file_path)
		os.system("{}/apktool.sh d {} -o {} -f".format(decompile_lib, file_path, apk_decompile_path))
		print (file_path[0:file_path.index(".")])
		filesInZip = zipfile.ZipFile(file_path, "r")
		filesInZip.extract("classes.dex", apk_decompile_path)
		filesInZip.close()
		file_path = apk_decompile_path + "/classes.dex"
	#反编译dex
	if "dex" in file_path:
		print("process dex:"+file_path)
		jar_path = "{}/output.jar".format(apk_decompile_path)
		os.system("{}/dex2jar-2.0/d2j-dex2jar.sh {} -o {} --force".format(decompile_lib, file_path ,jar_path))
	#反编译aar
	if "aar" in file_path:
		print("process aar:" + file_path)
		filesInZip = zipfile.ZipFile(file_path, "r")
		filesInZip.extract("classes.jar", apk_decompile_path)
		filesInZip.close()
		jar_path = apk_decompile_path + "/classes.jar"
	#直接打开jar
	if "jar" in file_path:
		jar_path = file_path;
	os.system("java -jar {}/jd-gui/jd-gui-1.4.0.jar {}".format(decompile_lib, jar_path))
