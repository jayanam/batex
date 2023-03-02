bl_info = {
    "name" : "Batex-mahu",
    "author" : "jayanam",
    "descrtion" : "Batch export as Fbx (mahu ver)",
    "blender" : (2, 80, 0),
    "version" : (999, 7, 0, 0),
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

bpy.types.Scene.center_transform = BoolProperty(name="Center transform",
                default=True,
                description="Set the pivot point of the object to the center")

bpy.types.Scene.apply_transform = BoolProperty(name="Apply transform",
                default=True,
                description="Applies scale and transform (Experimental)")

bpy.types.Scene.export_smoothing = EnumProperty(
    name="Smoothing",
    description="Defines the export smoothing information",
    items=(
        ('EDGE', 'Edge', 'Write edge smoothing',0),
        ('FACE', 'Face', 'Write face smoothing',1),
        ('OFF', 'Normals Only', 'Write normals only',2)
        ),
    default='OFF'
    )

bpy.types.Scene.export_animations = BoolProperty(name="Export Rig & Animations",
                default=False,
                description="Export rig and animations")

bpy.types.Scene.one_material_ID = BoolProperty(name="One material ID",
                default=True,
                description="Export just one material per object")

bpy.types.Scene.export_unity_coordinate = BoolProperty(name="Unity coordinate system",
                default=True,
                description="Export geometry with Unity compatibility.")

classes = ( BATEX_PT_Panel, BATEX_OT_Operator, BATEX_OT_OpenFolder )

register, unregister = bpy.utils.register_classes_factory(classes)
    
if __name__ == "__main__":
    register()
