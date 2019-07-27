
class Workout():
	def __init__(self, name, weight, reps):
		self._name = name
		self._weight = weight
		self._reps = reps
		self._status = "Idle"

	def start(self):
		self._status = "Started"

	def finish(self):
		self._status = "Idle"

	@property
	def name(self):
		return self._name

	@property
	def weight(self):
		return self._weight

	@property
	def reps(self):
		return self._reps

	@property
	def status(self):
		return self._status

	def __str__(self):
		output = "{}: {}kg, {} reps\n".format(self._name, self._weight, self._reps)
		output = "Status: {}\n".format(self._status)
		return output
