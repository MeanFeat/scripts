import maya.cmds as cmds

def GetFilePath():
    splitPath = cmds.file(query = True, expandName=True)
    splitPath = splitPath.split('/')
    splitPath.pop()
    path = "";
    for item in splitPath:
        path += item + "/"
    return path

def FailExit(message):
    cmds.error(message)
    sys.exit()

def GetFileName():
	fileName = cmds.file(query = True, expandName=True)
	fileName = fileName.split('.')
	fileName = fileName[0].split('/')
	return fileName[-1]

def GetFileExtension():
	fileName = cmds.file(query = True, expandName=True)
	fileName = fileName.split('.')
	return '.' + fileName[-1]