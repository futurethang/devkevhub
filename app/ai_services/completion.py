from app.dependencies import client

# Function to create a completion using OpenAI's GPT-3.5-turbo model
# This function takes a message and a prompt as input and returns a completion
# 
# Args:
#     message (str): The message to be sent to the model. This is typically a user's input.
#     prompt (str): The prompt to be sent to the model. This is typically a system's input.
# 
# Returns:
#     completion (str): The model's response to the input message and prompt.

def create_completion(message: str, prompt:str) -> str:
    completion = client.chat.completions.create(
      model="gpt-3.5-turbo",
      messages=[
        {"role": "system", "content": prompt},
        {"role": "user", "content": message}
      ]
    )

    return completion.choices[0].message
