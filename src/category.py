from abc import ABC, abstractmethod
from src.workout import Workout

class Category():
	def __init__(self):
		self._streak

class Gym():
	def __init__(self):
		self._workout_list = []

	def add_workout(self, workout):
		self._workout_list.append(workout)

	def delete_workout(self, workout):
		self._workout_list.remove(workout)

	def start_workout(self, workout):
		for key in self._workout_list:
			if key.name is workout:
				key.start()

	def finish_workout(self, workout):
		for key in self._workout_list:
			if key.name is workout:
				key.finish()

	def __str__(self):
		output = "Workouts:\n"
		for workout in self._workout_list:
			output += "{}\n".format(workout)

		return output


gym = Gym()
workout = Workout("bench press", 69, 1)
workout2 = Workout("squats", 6969, 2)
gym.add_workout(workout)
gym.add_workout(workout2)
print(gym)
gym.start_workout(workout.name)
print(gym)
gym.finish_workout(workout.name)
gym.delete_workout(workout2)
print(gym)
