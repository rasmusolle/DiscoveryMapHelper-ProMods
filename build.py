import zipfile
import sys
import os

def addDirToZip(zipHandle, path, basePath=""):
	basePath = basePath.rstrip("\\/") + ""
	basePath = basePath.rstrip("\\/")
	for root, dirs, files in os.walk(path):
		for file in files:
			filePath = os.path.join(root, file)
			inZipPath = filePath.replace(basePath, "", 1).lstrip("\\/")
			zipHandle.write(filePath, inZipPath)

def build_mod(modfolder, outputfile, steam = False):
	if os.path.exists(outputfile):
		os.remove(outputfile)
	zipf = zipfile.ZipFile(outputfile, "w", zipfile.ZIP_DEFLATED)
	addDirToZip(zipf, "common", "common")
	addDirToZip(zipf, modfolder, modfolder)
	zipf.close()

# ProMods
build_mod("promods", "dmh_pm.scs")
# ProMods w/ middle east addon
build_mod("promods-mid", "dmh_pm_mid.scs")
