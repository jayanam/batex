import bpy
import bmesh
import os
from . bex_utils import *

class BatEx_Export:

  def __init__(self, context):
    self.__context = context

    self.__export_folder = context.scene.export_folder
    if self.__export_folder.startswith("//"):
      self.__export_folder = os.path.abspath(
          bpy.path.abspath(context.scene.export_folder))

  def do_export(self):
    
    for coll in bpy.context.view_layer.layer_collection.children:
      print(f"Exporting top level collection {coll.name}")
      if coll.exclude:
        print(f"Collection will be excluded.")
        continue

      bpy.context.view_layer.active_layer_collection = coll

      ex_object_types = { 'MESH', 'ARMATURE' }

      # Export the selected object as fbx
      bpy.ops.export_scene.fbx(check_existing=False,
        filepath=self.__export_folder + "/" + coll.name + ".fbx",
        filter_glob="*.fbx",
        use_active_collection=True,
        use_visible=True,
        object_types=ex_object_types,
        bake_anim=True,
        bake_anim_use_all_bones=True,
        bake_anim_use_all_actions=True,
        use_armature_deform_only=True,
        bake_space_transform=True,
        mesh_smooth_type='OFF',
        add_leaf_bones=False,
        apply_scale_options='FBX_SCALE_ALL',
        use_space_transform=True,
        path_mode='ABSOLUTE')