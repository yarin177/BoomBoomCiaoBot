def do_turn(pw):
	if len(pw.my_fleets()) >= 1:
		return
	if len(pw.my_planets()) == 0:
		return
	for source in pw.my_planets():
		planetsInRange = []
		for planet in pw.not_my_planets():
			if pw.distance(source, planet) < 10:
				planetsInRange.append(planet)
		if len(planetsInRange) == 0:
			for planet in pw.not_my_planets():
				if pw.distance(source, planet) < 20:
					planetsInRange.append(planet)
		growRate = 0
		dest = pw.not_my_planets()[0]
		for planet in planetsInRange:
			#if(planet.num_ships() < source.num_ships()):
			if(growRate < planet.growth_rate()):
				dest = planet
				growRate = planet.growth_rate()
		num_ships = source.num_ships()
		pw.issue_order(source, dest, num_ships)
