import openai
import time

openai.api_key = ""

def chat_with_gpt(prompt):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message['content'].strip()
    except openai.error.RateLimitError as e:
        print("Rate limit exceeded. Please check your OpenAI plan and billing details.")
        return "I'm sorry, I can't respond right now due to API limits."

if __name__ == "__main__":
    last_request_time = 0
    cooldown_period = 60  # Time in seconds

    while True:
        user_input = input("You: ")
        if user_input.lower() in ["quit", "exit", "bye"]:
            break
        
        current_time = time.time()
        if current_time - last_request_time < cooldown_period:
            print("Please wait a moment before asking another question.")
        else:
            response = chat_with_gpt(user_input)
            print("Chatbot: ", response)
            last_request_time = current_time
