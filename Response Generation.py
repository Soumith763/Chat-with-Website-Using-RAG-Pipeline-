import openai

def generate_response(prompt):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5
    )

    return response['choices'][0]['text']

# Example Usage
prompt = "What is the capital of France?"
response = generate_response(prompt)
print(response)