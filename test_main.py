
from app.move_snake import get_move

import time
import os

if __name__ == '__main__':
	start = time.time()

	#data = {"game": {"id": "5a46bdde-0190-4769-8430-50dce56bd746"}, "turn": 41, "board": {"height": 11, "width": 11, "food": [{"x": 1, "y": 0}], "snakes": [{"id": "gs_YpY8wRY37b6CpyCxHjk7d8yK", "name": "Dunno", "health": 83, "body": [{"x": 4, "y": 3}, {"x": 4, "y": 4}, {"x": 5, "y": 4}, {"x": 5, "y": 5}, {"x": 4, "y": 5}, {"x": 3, "y": 5}], "shout": ""}, {"id": "gs_vQFxgrCCTrddwxXcbfK3TWRM", "name": "Cool_as_ice", "health": 80, "body": [{"x": 3, "y": 2}, {"x": 3, "y": 3}, {"x": 2, "y": 3}, {"x": 2, "y": 2}], "shout": ""}, {"id": "gs_r8DcWqCXQDfwVdVwDkJk6t99", "name": "Dragonborn", "health": 96, "body": [{"x": 3, "y": 6}, {"x": 2, "y": 6}, {"x": 1, "y": 6}, {"x": 0, "y": 6}, {"x": 0, "y": 7}, {"x": 1, "y": 7}, {"x": 2, "y": 7}, {"x": 3, "y": 7}], "shout": ""}, {"id": "gs_QCMrDxJvTQrRgk8XRwtvt8p3", "name": "shielded-woodland", "health": 93, "body": [{"x": 3, "y": 4}, {"x": 2, "y": 4}, {"x": 1, "y": 4}, {"x": 1, "y": 5}, {"x": 0, "y": 5}], "shout": ""}]}, "you": {"id": "gs_QCMrDxJvTQrRgk8XRwtvt8p3", "name": "shielded-woodland", "health": 93, "body": [{"x": 3, "y": 4}, {"x": 2, "y": 4}, {"x": 1, "y": 4}, {"x": 1, "y": 5}, {"x": 0, "y": 5}], "shout": ""}}
	#data = {"game": {"id": "a82b77d8-b3a3-461d-b865-74e5635d063e"}, "turn": 160, "board": {"height": 11, "width": 11, "food": [{"x": 2, "y": 1}, {"x": 2, "y": 0}, {"x": 5, "y": 10}], "snakes": [{"id": "gs_TqqWfTB97cf3p446fPCt7dmK", "name": "shielded-woodland", "health": 94, "body": [{"x": 6, "y": 8}, {"x": 7, "y": 8}, {"x": 7, "y": 7}, {"x": 8, "y": 7}, {"x": 9, "y": 7}, {"x": 9, "y": 8}, {"x": 10, "y": 8}, {"x": 10, "y": 7}, {"x": 10, "y": 6}, {"x": 10, "y": 5}, {"x": 10, "y": 4}, {"x": 10, "y": 3}, {"x": 10, "y": 2}], "shout": "I like em big... I like em Chunky!"}, {"id": "gs_7wVmbGrvdFpvvpVBR8mGycWb", "name": "csnek", "health": 99, "body": [{"x": 4, "y": 8}, {"x": 4, "y": 7}, {"x": 5, "y": 7}, {"x": 5, "y": 6}, {"x": 6, "y": 6}, {"x": 7, "y": 6}, {"x": 7, "y": 5}, {"x": 6, "y": 5}, {"x": 5, "y": 5}, {"x": 4, "y": 5}, {"x": 3, "y": 5}, {"x": 2, "y": 5}, {"x": 2, "y": 4}, {"x": 2, "y": 3}], "shout": ""}]}, "you": {"id": "gs_TqqWfTB97cf3p446fPCt7dmK", "name": "shielded-woodland", "health": 94, "body": [{"x": 6, "y": 8}, {"x": 7, "y": 8}, {"x": 7, "y": 7}, {"x": 8, "y": 7}, {"x": 9, "y": 7}, {"x": 9, "y": 8}, {"x": 10, "y": 8}, {"x": 10, "y": 7}, {"x": 10, "y": 6}, {"x": 10, "y": 5}, {"x": 10, "y": 4}, {"x": 10, "y": 3}, {"x": 10, "y": 2}], "shout": "I like em big... I like em Chunky!"}}
	#data = {"game": {"id": "2a60cf5b-dbdb-4364-a2f2-6ed4a1b2877c"}, "turn": 53, "board": {"height": 11, "width": 11, "food": [{"x": 6, "y": 2}], "snakes": [{"id": "gs_HxvW3xmh9tkByqxmKMfSYxJd", "name": "Dragonborn", "health": 100, "body": [{"x": 1, "y": 0}, {"x": 2, "y": 0}, {"x": 3, "y": 0}, {"x": 4, "y": 0}, {"x": 4, "y": 1}, {"x": 4, "y": 2}, {"x": 4, "y": 3}, {"x": 4, "y": 4}, {"x": 3, "y": 4}, {"x": 2, "y": 4}, {"x": 2, "y": 4}], "shout": ""}, {"id": "gs_MRkF3HF8dm4fVBhMh4TmvydH", "name": "shielded-woodland", "health": 52, "body": [{"x": 6, "y": 3}, {"x": 6, "y": 4}, {"x": 5, "y": 4}, {"x": 5, "y": 3}], "shout": "I like em big... I like em Chunky!"}, {"id": "gs_rYKdcTxDqpdS8pq9wRggbPt9", "name": "S-1000", "health": 70, "body": [{"x": 6, "y": 7}, {"x": 7, "y": 7}, {"x": 7, "y": 6}, {"x": 7, "y": 5}, {"x": 6, "y": 5}, {"x": 6, "y": 6}], "shout": ""}]}, "you": {"id": "gs_MRkF3HF8dm4fVBhMh4TmvydH", "name": "shielded-woodland", "health": 52, "body": [{"x": 6, "y": 3}, {"x": 6, "y": 4}, {"x": 5, "y": 4}, {"x": 5, "y": 3}], "shout": "I like em big... I like em Chunky!"}}
	#data = {"game": {"id": "45776f81-b029-405a-9d54-89d6511d086e"}, "turn": 32, "board": {"height": 11, "width": 11, "food": [{"x": 10, "y": 2}, {"x": 7, "y": 1}], "snakes": [{"id": "gs_HKQTqFfbQVGvcxryKY9Ykvxc", "name": "shielded-woodland", "health": 85, "body": [{"x": 9, "y": 7}, {"x": 8, "y": 7}, {"x": 7, "y": 7}, {"x": 6, "y": 7}, {"x": 5, "y": 7}, {"x": 5, "y": 8}], "shout": "I like em big... I like em Chunky!"}, {"id": "gs_fkC9TcVDk4bWR3PJgKcHfr3M", "name": "k-snek", "health": 92, "body": [{"x": 10, "y": 4}, {"x": 10, "y": 5}, {"x": 10, "y": 6}, {"x": 10, "y": 7}, {"x": 10, "y": 8}], "shout": ""}, {"id": "gs_VRwXwHTT76GvfKp7KgphYDQM", "name": "Dragonborn", "health": 93, "body": [{"x": 6, "y": 2}, {"x": 5, "y": 2}, {"x": 4, "y": 2}, {"x": 3, "y": 2}, {"x": 2, "y": 2}, {"x": 2, "y": 3}], "shout": ""}, {"id": "gs_BcmWtTQSrGy7cqYJj6CqvVxT", "name": "dontdie", "health": 78, "body": [{"x": 6, "y": 6}, {"x": 5, "y": 6}, {"x": 4, "y": 6}, {"x": 3, "y": 6}], "shout": ""}]}, "you": {"id": "gs_HKQTqFfbQVGvcxryKY9Ykvxc", "name": "shielded-woodland", "health": 85, "body": [{"x": 9, "y": 7}, {"x": 8, "y": 7}, {"x": 7, "y": 7}, {"x": 6, "y": 7}, {"x": 5, "y": 7}, {"x": 5, "y": 8}], "shout": "I like em big... I like em Chunky!"}}
	
	#single lane instance tests
	#turns right, should turn left
	data = {"game": {"id": "4ed19959-c7bf-4427-b32e-d078dc711478"}, "turn": 70, "board": {"height": 11, "width": 11, "food": [{"x": 4, "y": 10}, {"x": 8, "y": 7}, {"x": 8, "y": 2}], "snakes": [{"id": "gs_4kWvgv6Jhx3DYkqySwHmRV4S", "name": "csnek", "health": 97, "body": [{"x": 4, "y": 4}, {"x": 4, "y": 5}, {"x": 4, "y": 6}, {"x": 4, "y": 7}, {"x": 3, "y": 7}, {"x": 3, "y": 6}, {"x": 3, "y": 5}, {"x": 3, "y": 4}, {"x": 3, "y": 3}], "shout": ""}, {"id": "gs_BH93TJDTvPgkFbMy7y6XHcdY", "name": "Ereptile Disfunction", "health": 75, "body": [{"x": 5, "y": 1}, {"x": 4, "y": 1}, {"x": 4, "y": 2}, {"x": 5, "y": 2}, {"x": 6, "y": 2}, {"x": 6, "y": 3}, {"x": 6, "y": 4}, {"x": 6, "y": 5}, {"x": 5, "y": 5}], "shout": ""}, {"id": "gs_HFwGwPPWJ3BvgrrFrDJCQBrF", "name": "shielded-woodland", "health": 91, "body": [{"x": 2, "y": 0}, {"x": 2, "y": 1}, {"x": 3, "y": 1}, {"x": 3, "y": 2}, {"x": 2, "y": 2}, {"x": 1, "y": 2}, {"x": 0, "y": 2}, {"x": 0, "y": 1}], "shout": "I like em big... I like em Chunky!"}]}, "you": {"id": "gs_HFwGwPPWJ3BvgrrFrDJCQBrF", "name": "shielded-woodland", "health": 91, "body": [{"x": 2, "y": 0}, {"x": 2, "y": 1}, {"x": 3, "y": 1}, {"x": 3, "y": 2}, {"x": 2, "y": 2}, {"x": 1, "y": 2}, {"x": 0, "y": 2}, {"x": 0, "y": 1}], "shout": "I like em big... I like em Chunky!"}}
	#turns down or left, should turn up
	data = {"game": {"id": "227a0a85-0465-465c-a774-90c8cd782023"}, "turn": 120, "board": {"height": 11, "width": 11, "food": [{"x": 5, "y": 10}, {"x": 6, "y": 5}], "snakes": [{"id": "gs_h9drYr6qKHvptRSHQGGFg7tY", "name": "Dragonborn", "health": 99, "body": [{"x": 7, "y": 9}, {"x": 7, "y": 8}, {"x": 8, "y": 8}, {"x": 8, "y": 7}, {"x": 7, "y": 7}, {"x": 7, "y": 6}, {"x": 7, "y": 5}, {"x": 7, "y": 4}, {"x": 7, "y": 3}, {"x": 7, "y": 2}, {"x": 6, "y": 2}, {"x": 5, "y": 2}, {"x": 4, "y": 2}, {"x": 3, "y": 2}, {"x": 2, "y": 2}, {"x": 2, "y": 3}, {"x": 2, "y": 4}], "shout": ""}, {"id": "gs_9tpKYdJwYbxhK3JptwffWQdH", "name": "shielded-woodland", "health": 97, "body": [{"x": 9, "y": 9}, {"x": 10, "y": 9}, {"x": 10, "y": 8}, {"x": 10, "y": 7}, {"x": 10, "y": 6}, {"x": 10, "y": 5}, {"x": 10, "y": 4}, {"x": 10, "y": 3}, {"x": 10, "y": 2}, {"x": 9, "y": 2}, {"x": 9, "y": 1}, {"x": 8, "y": 1}, {"x": 7, "y": 1}, {"x": 6, "y": 1}], "shout": "I like em big... I like em Chunky!"}]}, "you": {"id": "gs_9tpKYdJwYbxhK3JptwffWQdH", "name": "shielded-woodland", "health": 97, "body": [{"x": 9, "y": 9}, {"x": 10, "y": 9}, {"x": 10, "y": 8}, {"x": 10, "y": 7}, {"x": 10, "y": 6}, {"x": 10, "y": 5}, {"x": 10, "y": 4}, {"x": 10, "y": 3}, {"x": 10, "y": 2}, {"x": 9, "y": 2}, {"x": 9, "y": 1}, {"x": 8, "y": 1}, {"x": 7, "y": 1}, {"x": 6, "y": 1}], "shout": "I like em big... I like em Chunky!"}}

	#turns left to try to grab food, but goes into single lane doing so, should go right
	data = {"game": {"id": "261da08d-e945-4540-a530-8c359872c14d"}, "turn": 118, "board": {"height": 11, "width": 11, "food": [{"x": 7, "y": 1}, {"x": 2, "y": 1}], "snakes": [{"id": "gs_CCCXGg9SvbvK88mQvSSrBJvY", "name": "Splooshy Snake", "health": 80, "body": [{"x": 6, "y": 6}, {"x": 5, "y": 6}, {"x": 5, "y": 7}, {"x": 4, "y": 7}, {"x": 3, "y": 7}, {"x": 2, "y": 7}, {"x": 2, "y": 6}], "shout": ""}, {"id": "gs_V3cGQFWYx3Fp4cphPGpQyBxP", "name": "huntail-python", "health": 83, "body": [{"x": 6, "y": 2}, {"x": 6, "y": 1}, {"x": 5, "y": 1}, {"x": 4, "y": 1}, {"x": 4, "y": 0}, {"x": 3, "y": 0}, {"x": 3, "y": 1}, {"x": 3, "y": 2}, {"x": 3, "y": 3}, {"x": 3, "y": 4}, {"x": 4, "y": 4}, {"x": 4, "y": 5}], "shout": ""}, {"id": "gs_9jtBCcxY9p7FRhF7Q4CptjX7", "name": "shielded-woodland", "health": 82, "body": [{"x": 8, "y": 0}, {"x": 8, "y": 1}, {"x": 8, "y": 2}, {"x": 8, "y": 3}, {"x": 8, "y": 4}, {"x": 8, "y": 5}, {"x": 8, "y": 6}, {"x": 8, "y": 7}, {"x": 8, "y": 8}, {"x": 8, "y": 9}, {"x": 7, "y": 9}], "shout": "I like em big... I like em Chunky!"}]}, "you": {"id": "gs_9jtBCcxY9p7FRhF7Q4CptjX7", "name": "shielded-woodland", "health": 82, "body": [{"x": 8, "y": 0}, {"x": 8, "y": 1}, {"x": 8, "y": 2}, {"x": 8, "y": 3}, {"x": 8, "y": 4}, {"x": 8, "y": 5}, {"x": 8, "y": 6}, {"x": 8, "y": 7}, {"x": 8, "y": 8}, {"x": 8, "y": 9}, {"x": 7, "y": 9}], "shout": "I like em big... I like em Chunky!"}}

	#Shouldn't go down to cutoff
	data = {"game": {"id": "39c241cf-6d59-438c-b250-94255fc01ef4"}, "turn": 168, "board": {"height": 11, "width": 11, "food": [{"x": 10, "y": 3}, {"x": 4, "y": 3}, {"x": 5, "y": 6}], "snakes": [{"id": "gs_RFVyPVjkV79SwRMqGxhfbW9G", "name": "shielded-woodland", "health": 96, "body": [{"x": 3, "y": 9}, {"x": 2, "y": 9}, {"x": 2, "y": 10}, {"x": 1, "y": 10}, {"x": 0, "y": 10}, {"x": 0, "y": 9}, {"x": 0, "y": 8}, {"x": 0, "y": 7}, {"x": 1, "y": 7}, {"x": 1, "y": 6}, {"x": 0, "y": 6}, {"x": 0, "y": 5}, {"x": 0, "y": 4}], "shout": "I like em big... I like em Chunky!"}, {"id": "gs_H3349wmjxB6xBB6SqQVG9twY", "name": "wubba lubba dub dub", "health": 78, "body": [{"x": 5, "y": 5}, {"x": 6, "y": 5}, {"x": 7, "y": 5}, {"x": 7, "y": 4}, {"x": 7, "y": 3}, {"x": 8, "y": 3}, {"x": 8, "y": 2}, {"x": 8, "y": 1}, {"x": 8, "y": 0}, {"x": 7, "y": 0}, {"x": 6, "y": 0}, {"x": 5, "y": 0}, {"x": 4, "y": 0}, {"x": 3, "y": 0}, {"x": 3, "y": 1}, {"x": 3, "y": 2}], "shout": ""}]}, "you": {"id": "gs_RFVyPVjkV79SwRMqGxhfbW9G", "name": "shielded-woodland", "health": 96, "body": [{"x": 3, "y": 9}, {"x": 2, "y": 9}, {"x": 2, "y": 10}, {"x": 1, "y": 10}, {"x": 0, "y": 10}, {"x": 0, "y": 9}, {"x": 0, "y": 8}, {"x": 0, "y": 7}, {"x": 1, "y": 7}, {"x": 1, "y": 6}, {"x": 0, "y": 6}, {"x": 0, "y": 5}, {"x": 0, "y": 4}], "shout": "I like em big... I like em Chunky!"}}


	move = get_move(data)

	end = time.time()

	elapsed_time = end - start

	print("Time elsapsed: " + str(elapsed_time))