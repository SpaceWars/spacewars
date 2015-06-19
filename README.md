># User Manual

## Requirements

- AMD E-450, dual core 1,66Ghz
- 1GB DDR3
- 10MB (free space)


## Installing **SpaceWars** in your computer


- Download the [source](https://github.com/SpaceWars/spacewars/archive/master.zip).
- Unzip it to your place of preference.
- It is necessary to be able to run files in the directory, so avoid places like a FAT32 / NTFS partition disk while using Unix / Linux systems and mobile media.
- Install the dependencies:
	- Python 2.7
	- python-cocos2d (<=0.6.0)
	- python-pyglet (<=1.2.2)
	- python-six (<=1.9.0)
- Those who have the *pip* installed on their computers can install the dependencies by running the following command in the game's root:

>	# pip install -r requeriments

## Running **SpaceWars** in your computer

With the dependencies installed, simply run the **SpaceWars** file located in the root directory where the game was unpacked. For those who wish the game to run from a launcher or any directory from a terminal, simply generate a symbolic link to the executable folder */usr/bin* or the *~/bin*. Having the full address of the executable as *~/Downloads/SpaceWars/SpaceWars* for example, the following command will create the desirable symbolic link:

>	# ln -s ~/Downloads/SpaceWars/SpaceWars /usr/bin/SpaceWars

## Removing **SpaceWars** in your computer

**SpaceWars** does not generate any files outside its directory. Just remove the folder to get rid of the game. If you created a symbolic link in */usr/bin*, it will be necessary to remove it manually as well.

<br>

>## Game Controls

#### Keyboard

- ← ↑ → ↓
	- Control the ship and navigation menus.
- SPACE
	- Shoot.
- ENTER
	- Confirm action in the menus.
- Esc
	- Return displays the menu navigation or menu opening during the game.
	
#### Joystick

- Directionals
	- Control the ship and navigation menus.
- Buttons
	- Shoot.
