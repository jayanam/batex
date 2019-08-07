import bpy

from bpy.types import Operator

from . bex_export import BatEx_Export
	
class BatEx_OT_Operator(Operator):
    bl_idname = "object.bex_ot_operator"
    bl_label = "Batch Export"
    bl_description = "Export selected objects as fbx" 
    bl_options = {'REGISTER'}
    
    def execute(self, context):

        bat_export = BatEx_Export(context)
        bat_export.do_export()
        
        self.report({'INFO'}, "Exported to " + context.scene.export_folder)
        return {'FINISHED'}


