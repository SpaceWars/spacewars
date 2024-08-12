extends Node2D

@export var torpedo_scene:PackedScene

# Called when the node enters the scene tree for the first time.
func _input(event):
	if Input.is_action_just_pressed("shoot"):
		var torpedo = torpedo_scene.instantiate() as Laser
		torpedo.global_position = get_parent().global_position - Vector2(0, 60)
		get_tree().root.get_node("Main").add_child(torpedo)
