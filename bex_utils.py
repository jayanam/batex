import bpy

# Get a copy of an object's location
def get_object_loc(obj):
  return obj.location.copy()

# Set the location of an object
def set_object_to_loc(obj, loc):
  obj.location = loc

def get_children(obj): 
  children = [] 
  for ob in bpy.data.objects: 
      if ob.parent == obj: 
          children.append(ob) 
  return children 

def get_cursor_loc(context):
  return context.scene.cursor.location.copy()

def selected_to_cursor():
  bpy.ops.view3d.snap_selected_to_cursor()

def set_cursor_loc(context, loc : tuple):
  context.scene.cursor.location = loc


