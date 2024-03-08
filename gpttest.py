import g4f

#FUNCTION
def ask_gpt4(promt:str)->str:
	response = g4f.ChatCompletion.create(
		model = g4f.models.gpt_4,
		messages = [{"role": "user", "content": promt}],
		)
	return response