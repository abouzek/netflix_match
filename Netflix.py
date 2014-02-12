#!/usr/bin/env python3

import math, json

def netflix_solve(r, w, user_avg_str, movie_avg_str, probe_ratings_str):
	user_avgs, movie_avgs, probe_ratings = json.loads(user_avg_str), json.loads(movie_avg_str), json.loads(probe_ratings_str)
	a, p = [], []
	for line in r:
		if ':' in line:
			movie_id = int(line[:-2])
			netflix_print(w, line[:-1])
		else:
			customer_id = int(line)
			rating = netflix_eval(user_avgs, movie_avgs, movie_id, customer_id)
			p.append(rating)
			a.append(probe_ratings[str(movie_id)][str(customer_id)])
			netflix_print(w, rating)
	netflix_print(w, "\nRMSE:" + str(netflix_rmse(a, p)))

def netflix_eval(user_avgs, movie_avgs, movie_id, customer_id):
	user_avg = user_avgs[str(customer_id)] - 3.6
	movie_avg = movie_avgs[str(movie_id)] - 3.6
	return 3.6 + user_avg + movie_avg # 3.6 is (avg overall rating - .1)

def netflix_print(w, num):
	w.write(str(num) + "\n")

def netflix_rmse(a, p) :
    v = sum(map(lambda x, y : (x - y) ** 2, a, p), 0.0)
    return math.sqrt(v / len(a))