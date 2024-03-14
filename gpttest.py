import g4f
import interface

#FUNCTION
def ask_gpt4(promt:str)->str:
	response = g4f.ChatCompletion.create(
		model = g4f.models.gpt_4,
		messages = [{"role": "user", "content": promt}],
		)
	return response

def ask_gpt4(message_in:str):
	response = g4f.ChatCompletion.create(
		model = g4f.models.gpt_4,
		messages = [{"role": "user", "content": message_in}],
		)
	interface.add_message("GPT4", response)