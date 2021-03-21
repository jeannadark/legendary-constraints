from csp import csp


def get_most_constrained_area(csp: Any):
	unassigned = []
	for area in csp.possible_tiles.keys():
		if area not in csp.tile_assignment.keys():
			unassigned.append(area)

	mrv_heuristic = lambda area: len(csp.possible_tiles[area])
	next_area = min(unassigned, key = mrv_heuristic)
	return next_area


def get_least_constraining_values(csp: Any, area: int):
	if len(csp.possible_tiles) == 1:
		return csp.possible_tiles[area]

	lcv_heuristic = lambda tile: get_number_of_conflicts(csp=csp, area=area, tile=tile)
	next_values = sorted(csp.possible_tiles[area], key=lcv_heuristic)

	return next_values


def get_number_of_conflicts(csp, area, tile) -> int:
	# the check for bushes will take place through remove_incons values in AC3
	cnt = 0
	for another_area in csp.constraints[area]:
		if len(csp.possible_tiles[another_area]) > 1 and tile in csp.possible_tiles[another_area]:
			cnt += 1
	return cnt


def is_ok(csp, tile, area):
	is_ok = True
	if csp.domains[tile] <= 0:
		is_ok = False
	return is_ok


def check_if_target_met(targets, totals_so_far):
	check = True
	for key in targets.keys():
		if targets[key] != totals_so_far[key]:
			check = False
	return check

