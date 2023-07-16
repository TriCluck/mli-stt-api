import openai
import random
openai.api_key = ""
  
message_list = []
def gptcall(situation, vocab, micro_situational_vocab):
    message_list.append(
        {'role': 'system', 'content': (situation + "\n Response will be made up of words in this list:" + vocab + 
         "\n Potential phrases used will consist of words in this list: " + micro_situational_vocab) }
    )
    
def situations(start, start_weights, mid, mid_weights, end, end_weights, random_event): #need to either import weights list directly into code or input as multiple arrays
    res = []
    starting = random.choice(start, weights = start_weights)
    res.append(starting)
    start_weights[start.index(starting)] = 0 #can be edited as necessary
    random_spot = random.randint(1,5)
    for i in range(5): #change for number of middle events
        middle = random.choice(mid, mid_weights)
        res.append(middle)
        mid_weights[mid.index(middle)] = 0
        if i == random_spot - 1:
            random.choice(random_event)
    ending = random.choice(end, end_weights)
    res.append(ending)
    end_weights[end.index(ending)] = 0
    return res

def script_generation(script, vocab, micro_situational_vocab):
    new_list = []
    newOne = openai.ChatCompletion.create(
            model="gpt-4",
            messages = new_list
        ) #change to davinci if needed
    new_list.append(
        {'role': 'user', 'content': ("Generate a script for the following script: " + script) } #fix for proper generation
    )
    situation = newOne.choices[0].message.content
    gptcall(situation, vocab, micro_situational_vocab)
    return

gptcall("situation", "vocab", "micro_situational_vocab")
while True:
    content = input("User: ") #replace with stt
    message_list.append({"role": "user", "content": content})
    

    
    for i in range(5):
        completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=message_list
        )
        chat_response = completion.choices[0].message.content
        #instead of print call Nick's method for choosing best response
        print(f'John: {chat_response}')
    message_list.append({'role': 'assistant', 'content': chat_response})
    