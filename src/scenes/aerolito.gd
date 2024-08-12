extends Area2D
class_name Aerolito

@export var speed = 100

func _process(delta):
	#position.angle(speed * delta)
	position.y += speed * delta

