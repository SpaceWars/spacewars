extends Area2D

@export var mob_scene: PackedScene
@export var aero_scene: PackedScene

func _on_area_entered(area):
	area.queue_free()

func _on_timer_timeout():
	var mob
	if randi_range(0,1):
		mob = mob_scene.instantiate() as Aerolito
	else:
		mob = aero_scene.instantiate() as Aerolito
	mob.global_position = Vector2(70 +randi()%1400,0)
	add_child(mob)
