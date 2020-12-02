import csv

PROMPT = 0
DEFAULT_MESSAGE = ";)"


def get_dialog_dict(data_path: str) -> dict:
    """Return a map from conversational prompts to responses"""
    dialog_dict = {}
    with open(data_path) as dialog_data:
        conversations = csv.reader(dialog_data, delimiter=',')
        for conversation in conversations:
            prompt, response_pool = parse_conversation(conversation)
            dialog_dict[prompt] = response_pool
    return dialog_dict


def parse_conversation(conversation):
    prompt = conversation[PROMPT]
    if len(conversation) >= 2:
        response_pool = [response for response in conversation[PROMPT+1:] if response != ""]
    else:
        response_pool = [DEFAULT_MESSAGE]
    return prompt, response_pool
