# Generating Random
import random

# All of the phrase
def create_responses_file(filename):
    responses = [
        "Yes, of course!",
        "Without a doubt, yes.",
        "You can count on it.",
        "For sure!",
        "Ask me later!",
        "I'm not sure.",
        "I can't tell you right now.",
        "I'll tell you after my nap.",
        "No way!",
        "I don't think so.",
        "Without a doubt, no.",
        "The answer is clearly NO!"
    ]

    with open(filename, 'w') as file:
        for response in responses:
            file.write(response + '\n')

def read_responses_file(filename):
    with open(filename, 'r') as file:
        responses = file.read().splitlines()
    return responses

# Having random response every answer
def magic_8_ball(responses):
    while True:
        question = input("Ask a yes/no question (or type 'quit' to exit): ")
        if question.lower() == 'quit':
            break
        response = random.choice(responses)
        print(response)

# Part 1 file
def main():
    filename = '8ball_responses.txt'
    create_responses_file(filename)
    responses = read_responses_file(filename)
    magic_8_ball(responses)

if __name__ == "__main__":
    main()
