bl_info = {
    "name": "Custom Addon",
    "author": "Kenzel Keenan D'souza",
    "version": (1, 0),
    "blender": (3, 0),
    "location": "View3D > Add > Mesh > New Object",
    "description": "Adds a new Mesh Object",
    "warning": "",
    "doc_url": "",
    "category": "Add Mesh",
}

import bpy
from random import randint
from bpy.types import (Panel, Operator)

class ButtonOperator(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "random.1"
    bl_label = "Simple Random Operator"
    
    def execute(self,context):
        for i in range (100):
            randomScale = randint(0,2)
            x = randint(-10,10)
            y = randint(-10,10)
            z = randint(-10,10)
            bpy.ops.mesh.primitive_ico_sphere_add(radius= randomScale, enter_editmode=False, align='WORLD', location=(x, y, z), scale=(1, 1, 1))
            bpy.ops.object.shade_smooth()
    
        return {'FINISHED'}

class CustomPanel(bpy.types.Panel):
    bl_label = "Random Panel"
    bl_idname = "OBJECT_PT_random"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "Random Spheres"

    def draw(self, context):
        layout = self.layout
        obj = context.object
        row = layout.row()
        row.operator(ButtonOperator.bl_idname, text="Generate", icon='SPHERE')

from bpy.utils import register_class, unregister_class
_classes =  [   
    ButtonOperator,
    CustomPanel
]

def register():
   for cls in _classes:
       register_class(cls)

def unregister():
    for cls in _classes:
       unregister_class(cls)
   
if __name__ == "__main__":
    register()
