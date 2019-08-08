import bpy

from bpy.types import Operator

class BatEx_OT_OpenFolder(Operator):
  
  bl_idname = "object.bex_ot_openfolder"
  bl_label = "Open Export Folder"
  bl_description = "Open the export folder" 
  bl_options = {'REGISTER'}

  def execute(self, context):
    bpy.ops.wm.path_open(filepath=context.scene.export_folder)
    return {'FINISHED'}
