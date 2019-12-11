import zipfile
import os

def addDirToZip(zipHandle, path):
	for root, dirs, files in os.walk(path):
		for file in files:
			filePath = os.path.join(root, file)
			inZipPath = filePath.replace(path, "", 1).lstrip("\\/")
			zipHandle.write(filePath, inZipPath)

class mod:
	def __init__(self, modFolder, outputFile, steam = False):
		self.modFolder = modFolder
		self.outputFile = outputFile
		self.steam = steam

	def build(self):
		if os.path.exists(self.outputFile):
			os.remove(self.outputFile)
		zipf = zipfile.ZipFile(self.outputFile, "w", zipfile.ZIP_DEFLATED)
		addDirToZip(zipf, "common")
		addDirToZip(zipf, self.modFolder)
		zipf.close()

modversions = [
	# ProMods
	mod("promods", "dmh_pm.scs"),
	# ProMods w/ middle east addon
	mod("promods-mid", "dmh_pm_mid.scs")
]

def main():
	for modversion in modversions:
		modversion.build()

if __name__ == "__main__":
	main()
