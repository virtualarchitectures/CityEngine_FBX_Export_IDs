'''
Created on 12 Apr 2018
@author: Liam O'Sullivan
Edited on 14 Jan 2019
@editor: Oliver Dawkins
'''
from scripting import *

# get a CityEngine instance
ce = CE()


def export(objects):
    dir = "C:/CityEngineExport/"
    name = "CityEngineExport"
    settings = FBXExportModelSettings()
    settings.setBaseName(name)
    settings.setOutputPath(dir)
    settings.setMeshGranularity("AS_GENERATED")
    settings.setCreateShapeGroups(True)
    settings.setFileType("BINARY")
    ce.export(objects, settings)

if __name__ == '__main__':
    
    objects = ce.getObjectsFrom(ce.scene, ce.isShape)

    for o in objects:
        tempID = ce.getAttribute(o, 'OBJECTID') 
        objID = str(tempID).replace('.0', '')
        
        #sets the name of the shapes in the project
        ce.setName(o, '' +str(objID))
    
    export(ce.getObjectsFrom(objects))
    pass
