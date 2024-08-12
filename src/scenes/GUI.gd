extends PanelContainer

@onready var number_label = $ProgressBar
# Called when the node enters the scene tree for the first time.
func _ready():
	number_label.value = $"../Player".life


func _on_player_health_depleted():
	number_label.value = $"../Player".life
