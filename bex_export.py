import bpy

class BatEx_Export:

  def __init__(self, context):
    self.__export_folder = context.scene.export_folder
    self.__center_transform = context.scene.center_transform
    self.__export_objects = context.selected_objects
      
  def do_export(self):

    bpy.ops.object.mode_set(mode='OBJECT')

    for obj in self.__export_objects:
      bpy.ops.object.select_all(action='DESELECT') 
      obj.select_set(state=True)

      # Export the selected object as fbx
      bpy.ops.export_scene.fbx(check_existing=False,
      filepath=self.__export_folder + "/" + obj.name + ".fbx",
      filter_glob="*.fbx",
      use_selection=True,
      use_armature_deform_only=True,
      add_leaf_bones=False,
      path_mode='ABSOLUTE')

