import bpy

class FacialConstraintsHelper(bpy.types.Panel):
    bl_label = "Facial Constraints Helper"
    bl_idname = "facial_constraints_helper"
    bl_space_type = 'PROPERTIES'
    bl_region_type = 'WINDOW'
    bl_context = "object"

    def draw(self, context):
        layout = self.layout
        obj = context.object
        scene = context.scene
        #rigname = StringProperty()

        row = layout.row()
        row.label(text="Active object is: " + obj.name)
        row = layout.row()
        #row.prop_search(scene, "referenceMesh", scene, "objects")

        row = layout.row()
        row.operator("object.add_constraint", text = "lip.T.R.001").newName = "lip.T.R.001"
        row.operator("object.add_constraint", text = "lip.T").newName = "lip.T"
        row.operator("object.add_constraint", text = "lip.T.L.001").newName = "lip.T.L.001"
        row = layout.row()
        row.operator("object.add_constraint", text = "lips.R").newName = "lips.R"
        row.operator("object.add_constraint", text = "lips.L").newName = "lips.L"
        row = layout.row()
        row.operator("object.add_constraint", text = "lip.B.R.001").newName = "lip.B.R.001"
        row.operator("object.add_constraint", text = "lip.B").newName = "lip.B"
        row.operator("object.add_constraint", text = "lip.B.L.001").newName = "lip.B.L.001"
        row = layout.row()
        row.operator("object.add_constraint", text = "chin").newName = "chin"

class AddConstraint(bpy.types.Operator):
    bl_idname = "object.add_constraint"
    bl_label = "Add Constraint"
    #bl_options = {'UNDO'}
    newName = bpy.props.StringProperty()
    rigName = bpy.props.StringProperty()
    
    def execute(self, context):
        obj = context.object
        scene = context.scene
        self.rigName = "rig" #change this name to the name of your character rig if you need to
        bone = scene.objects[self.rigName].pose.bones[self.newName]
        
        '''for b in bone:
            childOfConstraints = [c for c in b.constraints if c.type == 'CHILD_OF']
            for c in childOfConstraints:
                b.constraints.delete(c)'''
        
        constraint = bone.constraints.new('CHILD_OF')
        constraint.show_expanded = True
        constraint.target = scene.objects[self.newName]
        constraint.use_scale_x = False
        constraint.use_scale_y = False
        constraint.use_scale_z = False
        constraint.use_rotation_x = False
        constraint.use_rotation_y = False
        constraint.use_rotation_z = False
        constraint.use_location_y = False
        constraint.childof_set_inverse(constraint = constraint.name, owner = 'BONE')
        #bone.childof_set_inverse(constraint = "Child Of", owner='BONE')
        
        print("str: " + bone.name + " rig name = " + self.rigName + " constr name = " + constraint.owner)
        obj.name = self.newName
        return {'FINISHED'}

def register():
    bpy.utils.register_class(FacialConstraintsHelper)
    bpy.utils.register_class(AddConstraint)

def unregister():
    bpy.utils.unregister_class(FacialConstraintsHelper)
    bpy.utils.unregister_class(AddConstraint)


if __name__ == "__main__":
    register()
