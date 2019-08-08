import bpy
from bpy.types import Panel

class BatEx_PT_Panel(Panel):
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_label = "Batch Fbx export"
    bl_category = "Batch Ex"
    
    def draw(self, context):
        
        layout = self.layout
        scene = context.scene

        row = layout.row()
        row.label(text="Export folder:")

        row = layout.row()
        row.prop(context.scene, "export_folder", text="")

        row = layout.row()
        row.prop(context.scene, "center_transform", text="Center transform")

        row = layout.row()
        row.operator('object.bex_ot_operator', text='Export')

        row = layout.row()
        row.operator('object.bex_ot_openfolder', text='Open export folder')
