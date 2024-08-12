extends Area2D

@export var life = 100
@export var speed = 600
@export var damage = 20
var direction = Vector2.ZERO

@onready var collision_shape:CollisionPolygon2D = $CollisionPolygon2D
@onready var _animated_sprite = $AnimatedSprite2D
@onready var sprite = $Sprite2D

signal health_depleted


# Called every frame. 'delta' is the elapsed time since the previous frame.
func _process(delta):
	var forward = Input.get_axis("move_down","move_up")
	var turn = Input.get_axis("move_left","move_right")
	
	if Input.is_action_just_pressed("move_left"):
		_animated_sprite.play("ani_left")
	if  Input.is_action_just_pressed("move_right"):
		_animated_sprite.play("ani_right")
	
	if Input.is_action_just_released("move_right") or Input.is_action_just_released("move_left"):
		_animated_sprite.stop()
	direction = Vector2.ZERO
	if forward > 0 :
		direction += Vector2.UP
	elif forward < 0 :
		direction += Vector2.DOWN
		
		
	if turn > 0:
		direction += Vector2.RIGHT
	elif turn < 0:
		direction += Vector2.LEFT

	position.x += speed * delta * direction.x
	position.y += speed * delta * direction.y
	
	#lock player in the screen
	if position.x < 70 :
		position.x = 70
	if position.x > 1440:
		position.x = 1440
	if position.y > 920:
		position.y = 920
	if position.y < 70:
		position.y = 70	

	if Input.is_action_just_pressed("return"):
		get_tree().change_scene_to_file("res://scenes/menu.tscn")

func _on_area_entered(area):
	if area.visibility_layer == 10:
		area.queue_free()
		life -= damage
		if life <= 0:
			get_tree().change_scene_to_file("res://scenes/menu.tscn")
		health_depleted.emit()
