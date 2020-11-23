import json


def get_msg_count():
	metric_file = open("metrics.json", "r")
	data = json.load(metric_file)
	metric_file.close()
	msg_count = data["conversation"]
	msg_count = round(msg_count, 2)
	return msg_count


def increment_field_count(field: str):
	metric_file = open("metrics.json", "r")
	data = json.load(metric_file)
	metric_file.close()

	data[field] = data[field] + 1

	metric_file = open("metrics.json", "w+")
	metric_file.write(json.dumps(data))
	metric_file.close()
	

def increment_conversation_count():
	increment_field_count("conversation")


def increment_tictactoe_count():
	increment_field_count("tictactoe")


def increment_rps_count():
	increment_field_count("rps")

