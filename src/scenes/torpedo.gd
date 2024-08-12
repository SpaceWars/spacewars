extends Area2D
class_name Laser

@export var speed = 300
# Called every frame. 'delta' is the elapsed time since the previous frame.
func _process(delta):
	position.y -= delta*speed


func _on_area_entered(area:CollisionObject2D):
	if area.visibility_layer == 10:
		area.queue_free()
		self.queue_free()
