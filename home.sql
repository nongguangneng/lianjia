create table if not exists home (
	url VARCHAR(200) PRIMARY KEY,
	total_price VARCHAR(10),
	building_area VARCHAR(10),
	inner_area VARCHAR(10),
	building_per_price FLOAT,
	inner_per_price FLOAT,
	toward VARCHAR(5),
	years_limit VARCHAR(5),
	floor VARCHAR(10),
	decoration VARCHAR(10),
	building_huxing VARCHAR(10),
	room_huxing VARCHAR(10),
	floor_layout VARCHAR(10),
	elevator VARCHAR(10)
	);