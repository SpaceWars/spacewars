extends Control

func _ready():
	$MainMenu/start.grab_focus()

func _process(delta):
	if Input.is_action_just_pressed("return"):
		if get_node("MainMenu").visible:
			_on_exit_button_down()
		elif get_node("Options").visible:
			_on_return_button_down()

func _on_start_button_down():
	get_tree().change_scene_to_file("res://scenes/main.tscn")


func _on_options_button_down():
	var main_menu = get_node("MainMenu")
	var options_menu = get_node("Options")
	main_menu.visible = false
	options_menu.visible = true
	$Options/return.grab_focus()


func _on_exit_button_down():
	get_tree().quit()


func _on_return_button_down():
	get_node("MainMenu").visible = true
	get_node("Options").visible = false
	$MainMenu/start.grab_focus()
