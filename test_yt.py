import json
from groq import Groq

# Create the Groq client
client = Groq(
    api_key="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"
)

# Set the system prompt
system_prompt = {
    "role": "system",
    "content": "You are a helpful assistant"
}

# Initialize the chat history
chat_history = [system_prompt]

# User input for testing
user_input = "About software testing"

# Append the user input to the chat history
chat_history.append({"role": "user", "content": user_input})

# Make a request to the model for a response
response = client.chat.completions.create(
    model="llama3-70b-8192",
    messages=chat_history,
    max_tokens=5000,
    temperature=1.2,
    top_p=1,
    stop=None,
)

# Get the assistant's response
assistant_response = response.choices[0].message.content

# Prepare the output as a dictionary
output = {
    "user_input": user_input,
    "assistant_response": assistant_response
}

# Convert the output to JSON format
output_json = json.dumps(output, indent=4)

# Print the final JSON output
print(output_json)
