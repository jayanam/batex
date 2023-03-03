import bpy
from bpy.types import Panel

class BATEX_PT_Panel(Panel):
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_label = "Batch Unity Fbx export"
    bl_category = "Batex Unity"
    
    def draw(self, context):
        
        layout = self.layout
        scene = context.scene

        row = layout.row()
        row.label(text="Export folder:")

        row = layout.row()
        col = row.column()
        col.prop(context.scene, "export_folder", text="")

        col = row.column()
        col.operator('object.bex_ot_openfolder', text='', icon='FILE_TICK')

        row = layout.row()
        layout.row().label(text="Exports only visible objects.")
        layout.row().label(text="Splits by top level collection.")
        layout.row().label(text="Applies unity style transform.")
        layout.row().label(text="Names files <collection>.fbx")

        row = layout.row()
        row.operator('object.bex_ot_operator', text='Export')


