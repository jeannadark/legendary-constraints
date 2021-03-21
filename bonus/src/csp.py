import numpy as np


class CSP:
	def __init__(self, landscape: np.array, total_bushes: dict, domains: dict):
		self.landscape = landscape
		self.domains = domains
		self.total_bushes = total_bushes # to-do: count total number of different bushes in matrix
		self.tile_assignment = dict()
		self.area_bushes = dict()
		self.possible_tiles = dict()
		self.constraints = dict()

		area = 0
		for i in range(0, self.landscape.shape[0], 4):
		    for j in range(0, self.landscape.shape[1], 4):
		        self.area_bushes[area] = self.landscape[i:i+4, j:j+4]
		        area += 1

		for area in self.area_bushes.keys():
			if area not in self.possible_tiles:
				self.possible_tiles[area] = ['full_block'] * self.domains['full_block'] + ['outer_boundary'] * self.domains['outer_boundary'] + ['el_shape'] * self.domains['el_shape']

	def get_bushes_in_area(self, area: int) -> np.array:
		return self.area_bushes[area]

	def decrement_bushes(self, bush: np.array, tile_type: str) -> None:
		if tile_type == 'full_block':
			for i in range(0, bush.shape[0]):
				for j in range(0, bush.shape[1]):
					if bush[i, j] == '1':
						self.total_bushes['1'] -= 1
					elif bush[i, j] == '2':
						self.total_bushes['2'] -= 1
					elif bush[i, j] == '3':
						self.total_bushes['3'] -= 1
					elif bush[i, j] == '4':
						self.total_bushes['4'] -= 1
					else:
						pass
		elif tile_type == 'outer_boundary':
			for i in range(1, 3):
				for j in range(1, 3):
					if bush[i, j] == '1':
						self.total_bushes['1'] -= 1
					elif bush[i, j] == '2':
						self.total_bushes['2'] -= 1
					elif bush[i, j] == '3':
						self.total_bushes['3'] -= 1
					elif bush[i, j] == '4':
						self.total_bushes['4'] -= 1
					else:
						pass
		else:
			for i in range(1, 4):
				for j in range(1, 4):
					if bush[i, j] == '1':
						self.total_bushes['1'] -= 1
					elif bush[i, j] == '2':
						self.total_bushes['2'] -= 1
					elif bush[i, j] == '3':
						self.total_bushes['3'] -= 1
					elif bush[i, j] == '4':
						self.total_bushes['4'] -= 1
					else:
						pass

	def increment_bushes(self, bush: np.array, tile_type: str) -> None:
		if tile_type == 'full_block':
			for i in range(0, bush.shape[0]):
				for j in range(0, bush.shape[1]):
					if bush[i, j] == '1':
						self.total_bushes['1'] += 1
					elif bush[i, j] == '2':
						self.total_bushes['2'] += 1
					elif bush[i, j] == '3':
						self.total_bushes['3'] += 1
					elif bush[i, j] == '4':
						self.total_bushes['4'] += 1
					else:
						pass
		elif tile_type == 'outer_boundary':
			for i in range(1, 3):
				for j in range(1, 3):
					if bush[i, j] == '1':
						self.total_bushes['1'] += 1
					elif bush[i, j] == '2':
						self.total_bushes['2'] += 1
					elif bush[i, j] == '3':
						self.total_bushes['3'] += 1
					elif bush[i, j] == '4':
						self.total_bushes['4'] += 1
					else:
						pass
		else:
			for i in range(1, 4):
				for j in range(1, 4):
					if bush[i, j] == '1':
						self.total_bushes['1'] += 1
					elif bush[i, j] == '2':
						self.total_bushes['2'] += 1
					elif bush[i, j] == '3':
						self.total_bushes['3'] += 1
					elif bush[i, j] == '4':
						self.total_bushes['4'] += 1
					else:
						pass

	def assign_tile(self, area: int, tile_type: str) -> None:
		if self.domains[tile_type] > 0:
			self.tile_assignment[area] = tile_type
			self.domains[tile_type] -= 1
			bush = self.get_bushes_in_area(area)
			self.decrement_bushes(bush, tile_type)

	def unassign_tile(self, area: int, tile_type: str) -> None:
		if area in self.tile_assignment:
			del self.tile_assignment[area]
			self.domains[tile_type] += 1
			bush = self.get_bushes_in_area(area)
			self.increment_bushes(bush, tile_type)

	def generate_constraints(self):
		self.constraints = {area: [] for area in self.area_bushes.keys()}
		for area in self.constraints.keys():
			for another_area in self.area_bushes.keys():
				if area ! = another_area:
					self.constraints[area].append(another_area)

