import random

#from keras.backend import switch


class Agent:
	def chooseAction(self, observations, possibleActions):
		# Access full lidar list
		# (left (45deg), left (10deg), center, right (10deg), right (45deg))
		lidar_values = observations['lidar']

		# Access single lidars
		lid_val_left45 = observations['lidar'][0]
		lid_val_left10 = observations['lidar'][1]
		lid_val_center = observations['lidar'][2]
		lid_val_right10 = observations['lidar'][3]
		lid_val_right45 = observations['lidar'][4]

		# Access velocity
		vel = observations['velocity']

		# Speed control
		# Description:
		# Control to a constant velocity
		if vel < 0.15:
			speed_control = 'accelerate'
		elif vel == 0.15:
			speed_control = 'coast'
		elif vel > 0.15:
			speed_control = 'brake'

		# Direction control
		# Description:
		# If the left 45deg lidar shows a greater distance than the right
		# 45deg lidar, steer left; if the right is greater, steer right;
		# if both are equal, go straight.
		if lid_val_left45 < lid_val_right45:
			dir_control = 'right'
		elif lid_val_left45 == lid_val_right45:
			dir_control = 'straight'
		elif lid_val_left45 > lid_val_right45:
			dir_control = 'left'

		return (dir_control, speed_control)
