import bpy

MarkersScale = 1.0
MarkersMouthNames = ['lip.T.R.001', 'lip.T', 'lip.T.L.001', 'lips.R', 
					'lips.L', 'lip.B.R.001', 'lip.B', 'lip.B.L.001', 
					'chin']

class FaceMocap_Panel_Tracking(bpy.types.Panel):
    bl_label = "Tracking Markers"
    bl_idname = "afacemotrack0p1.paneltracking"
    bl_space_type = 'CLIP_EDITOR'
    bl_region_type = 'TOOLS'
    bl_category = "MoCap"

    def draw(self, context):
        #global NoteLabel
        
        layout = self.layout
        obj = context.object
        
        row = layout.row()
        row.label(text="Active object is: " + obj.name)
        row = layout.row()
        layout.operator("mesh.add_cube_sample", icon = 'MESH_CUBE', text = "add cube")

        '''row = layout.row(align=True)
        sub = row.row(align=True)
        sub.operator("afacemotrack0p1.resizeup", icon="ZOOMIN")
        sub.operator("afacemotrack0p1.createreset")
        sub.operator("afacemotrack0p1.resizedown", icon="ZOOMOUT")
        
        #based in panel TRACK
        row = layout.row(align=True)
        row.label(text="Track:")
        row.operator("afacemotrack0p1.trackprev", icon='FRAME_PREV')
        row.operator("afacemotrack0p1.trackreverse", icon='PLAY_REVERSE')
        row.operator("afacemotrack0p1.trackplay", icon='PLAY')
        row.operator("afacemotrack0p1.tracknext", icon='FRAME_NEXT')
        
        col = layout.column(align=True)
        row = col.row(align=True)
        row.label(text="Clear:")
        row.scale_x = 2.0
        props = row.operator("clip.clear_track_path", text="", icon='BACK')
        props.action = 'UPTO'
        props = row.operator("clip.clear_track_path", text="", icon='FORWARD')
        props.action = 'REMAINED'
        '''

#--button _CREATE/RESET TRACKS_
class AFaceMoTrack0p1_CreateReset(bpy.types.Operator):
    bl_label = "Create/Reset Markers"
    bl_idname = "afacemotrack0p1.createreset"
    bl_space_type = 'CLIP_EDITOR'
    bl_region_type = 'TOOLS'
    bl_category = "MoCap"
    
    '''def execute(self, context):
        global MarkersScale
        MarkersScale = 1.0
        AFaceMoTrack0p1_def_CreateReset()
        return {'FINISHED'}'''

def AFaceMoTrack0p1_def_CreateReset():
    #--capture current video name
    nameCurrentClip = bpy.context.space_data.clip.name
    
    #--delete all tracks
    bpy.ops.clip.select_all(action='SELECT')
    bpy.ops.clip.delete_track()
    
    #--add news tracks with correct positions and names
    x = (0.47 - 0.5) * MarkersScale + 0.5
    y = (0.415 - 0.5) * MarkersScale + 0.5
    bpy.ops.clip.add_marker(location=(x,y))
    bpy.data.movieclips[nameCurrentClip].tracking.tracks.active.name = "A_ Nose R"
    
    x = (0.53 - 0.5) * MarkersScale + 0.5
    y = (0.415 - 0.5) * MarkersScale + 0.5
    bpy.ops.clip.add_marker(location=(x,y))
    bpy.data.movieclips[nameCurrentClip].tracking.tracks.active.name = "A_ Nose L"
    
        
    x = (0.46 - 0.5) * MarkersScale + 0.5
    y = (0.495 - 0.5) * MarkersScale + 0.5
    bpy.ops.clip.add_marker(location=(x,y))
    bpy.data.movieclips[nameCurrentClip].tracking.tracks.active.name = "A_ Lid B R"
    
    x = (0.46 - 0.5) * MarkersScale + 0.5
    y = (0.54 - 0.5) * MarkersScale + 0.5
    bpy.ops.clip.add_marker(location=(x,y))
    bpy.data.movieclips[nameCurrentClip].tracking.tracks.active.name = "A_ Lid T R"
    
    x = (0.42 - 0.5) * MarkersScale + 0.5
    y = (0.505 - 0.5) * MarkersScale + 0.5
    bpy.ops.clip.add_marker(location=(x,y))
    bpy.data.movieclips[nameCurrentClip].tracking.tracks.active.name = "A_ Lid R"
    
    x = (0.54 - 0.5) * MarkersScale + 0.5
    y = (0.495 - 0.5) * MarkersScale + 0.5
    bpy.ops.clip.add_marker(location=(x,y))
    bpy.data.movieclips[nameCurrentClip].tracking.tracks.active.name = "A_ Lid B L"
    
    x = (0.54 - 0.5) * MarkersScale + 0.5
    y = (0.54 - 0.5) * MarkersScale + 0.5
    bpy.ops.clip.add_marker(location=(x,y))
    bpy.data.movieclips[nameCurrentClip].tracking.tracks.active.name = "A_ Lid T L"
    
    x = (0.58 - 0.5) * MarkersScale + 0.5
    y = (0.505 - 0.5) * MarkersScale + 0.5
    bpy.ops.clip.add_marker(location=(x,y))
    bpy.data.movieclips[nameCurrentClip].tracking.tracks.active.name = "A_ Lid L"
    
    
    x = 0.5
    y = (0.585 - 0.5) * MarkersScale + 0.5
    bpy.ops.clip.add_marker(location=(x,y))
    bpy.data.movieclips[nameCurrentClip].tracking.tracks.active.name = "A_ Brow"
    
    x = (0.44 - 0.5) * MarkersScale + 0.5
    y = (0.585 - 0.5) * MarkersScale + 0.5
    bpy.ops.clip.add_marker(location=(x,y))
    bpy.data.movieclips[nameCurrentClip].tracking.tracks.active.name = "A_ Brow R"
    
    x = (0.56 - 0.5) * MarkersScale + 0.5
    y = (0.585 - 0.5) * MarkersScale + 0.5
    bpy.ops.clip.add_marker(location=(x,y))
    bpy.data.movieclips[nameCurrentClip].tracking.tracks.active.name = "A_ Brow L"
    
    
    x = 0.5
    y = (0.7 - 0.5) * MarkersScale + 0.5
    bpy.ops.clip.add_marker(location=(x,y))
    bpy.data.movieclips[nameCurrentClip].tracking.tracks.active.name = "A_ Forehead"
    
    
    x = 0.5
    y = 0.5
    bpy.ops.clip.add_marker(location=(x,y))
    bpy.data.movieclips[nameCurrentClip].tracking.tracks.active.name = "A_ Nose"
    
    #--select all tracks
    bpy.ops.clip.select_all(action='SELECT')
    
    #--resize scale of all tracks
    bpy.ops.transform.resize(value=(MarkersScale,MarkersScale,MarkersScale))

class OperatorTest(bpy.typer.Operator):
	bl_idname = "wm.hello_world"
    bl_label = "Minimal Operator"

    def execute(self, context):
        print("Hello World")
        return {'FINISHED'}

def register():
	bpy.utils.register_class(FaceMocap_Panel_Tracking)
	bpy.utils.register_class(AFaceMoTrack0p1_CreateReset)
	bpy.utils.register_class(OperatorTest)

def unregister():
	bpy.utils.unregister_class(FaceMocap_Panel_Tracking)
	bpy.utils.unregister_class(AFaceMoTrack0p1_CreateReset)
	bpy.utils.unregister_class(OperatorTest)

if __name__ == "__main__":
	register()		