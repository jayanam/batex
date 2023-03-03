bl_info = {
    "name" : "Batex-unity",
    "author" : "jayanam,mahu",
    "descrtion" : "Batch export as Unity Fbx",
    "blender" : (3, 4, 1),
    "version" : (0, 9, 0, 1),
    "location" : "Batex panel",
    "warning" : "",
    "category" : "Import-Export"
}

import bpy
from bpy.props import *

from . bex_panel import *
from . bex_op import *
from . bex_folder_op import *

bpy.types.Scene.export_folder = StringProperty(name="Export folder", 
               subtype="DIR_PATH", 
               description="Directory to export the fbx files into")

classes = ( BATEX_PT_Panel, BATEX_OT_Operator, BATEX_OT_OpenFolder )

register, unregister = bpy.utils.register_classes_factory(classes)
    
if __name__ == "__main__":
    register()
