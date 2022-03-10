import json


def get_msg_count() -> str:
	metric_file = open("metrics.json", "r")
	data = json.load(metric_file)
	metric_file.close()
	msg_count = data["conversation"]
	msg_count = round(msg_count/1000000, 2)
	return f"{msg_count}M"


def increment_field_count(field: str) -> None:
	metric_file = open("metrics.json", "r")
	data = json.load(metric_file)
	metric_file.close()

	data[field] = data[field] + 1

	metric_file = open("metrics.json", "w+")
	metric_file.write(json.dumps(data))
	metric_file.close()


def increment_conversation_count() -> None:
	increment_field_count("conversation")


def increment_tictactoe_count() -> None:
	increment_field_count("tictactoe")


def increment_rps_count() -> None:
	increment_field_count("rps")

