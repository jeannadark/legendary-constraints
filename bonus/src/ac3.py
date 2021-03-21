def AC3(csp, queue = None):
	while queue:
		(xi, xj) = queue.pop()
		if remove_inconsistent_values(csp, xi, xj):
			if len(csp.possible_tiles[xi]) == 0:
				return False
			for Xk in csp.constraints[xi]:
				if Xk != xi:
					queue.append((Xk, xi))
	return True


def remove_inconsistent_values(csp, xi, xj):
	removed = False
	if not 
	# ???
	# if current tile assignment to xi and xj messes up the meeting of the target
	# then remove
	# i.e. if current assignment to xi conflicts with xj being assigned to any tile (conflicts means -> messes up the meeting of the target)
	# then revise



def revise(csp, Xi, Xj, removals, checks=0):
    """Return true if we remove a value."""
    revised = False
    for x in csp.curr_domains[Xi][:]:
        # If Xi=x conflicts with Xj=y for every possible y, eliminate Xi=x
        # if all(not csp.constraints(Xi, x, Xj, y) for y in csp.curr_domains[Xj]):
        conflict = True
        for y in csp.curr_domains[Xj]:
            if csp.constraints(Xi, x, Xj, y):
                conflict = False
            checks += 1
            if not conflict:
                break
        if conflict:
            csp.prune(Xi, x, removals)
            revised = True
    return revised, checks