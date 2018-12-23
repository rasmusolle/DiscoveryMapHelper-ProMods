import zipfile
import sys
import os

modfile = "pm_dmh.scs"
modfolder = "pm_dmh"

def addDirToZip(zipHandle, path, basePath=""):
	basePath = basePath.rstrip("\\/") + ""
	basePath = basePath.rstrip("\\/")
	for root, dirs, files in os.walk(path):
		for file in files:
			filePath = os.path.join(root, file)
			inZipPath = filePath.replace(basePath, "", 1).lstrip("\\/")
			zipHandle.write(filePath, inZipPath)

if os.path.exists(modfile):
	os.remove(modfile)

zipf = zipfile.ZipFile(modfile, "w", zipfile.ZIP_DEFLATED)
addDirToZip(zipf, modfolder, modfolder)
zipf.close()
