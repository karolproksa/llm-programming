import os
import openai

# TODO: 
# run simluations with different parameters and models
# try diffrent prompts (non-creative, factual, etc.)

# TODO: REMOVE OPENAI KEY -- DON NOT DOXX THAT
openai.api_key = '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'

# Test 01 - no parameters, gpt-3.5-turbo model
# f = open("test1.txt", "a")
# i = 1
# while i <= 10:
#     chat_completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": "Write a poem about mountains. Make it 8 lines long."}])
#     poem = chat_completion.choices[0].message.content
#     f.write(poem + "\n")
#     i += 1

# Test 02 - temperature=0, top_p=0, gpt-3.5-turbo model
# f = open("test2.txt", "a")
# i = 1
# while i <= 10:
#     chat_completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": "Write a poem about mountains. Make it 8 lines long."}], temperature=0, top_p=0)
#     poem = chat_completion.choices[0].message.content
#     f.write(poem + "\n")
#     i += 1

# Test 03 - temperature=0, top_p=0, presence_penalty=2 gpt-3.5-turbo model
# f = open("test3.txt", "a")
# i = 1
# while i <= 100:
#     chat_completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": "Write a poem about mountains. Make it 8 lines long."}], temperature=0, top_p=0, presence_penalty=2)
#     poem = chat_completion.choices[0].message.content
#     f.write(poem + "\n")
#     i += 1

# Test 04 - temperature=0, top_p=0, presence_penalty=2 gpt-4 model
# f = open("test4.txt", "a")
# i = 1
# while i <= 10:
#     chat_completion = openai.ChatCompletion.create(model="gpt-4", messages=[{"role": "user", "content": "Write a poem about mountains. Make it 8 lines long."}], temperature=0, top_p=0, presence_penalty=2)
#     poem = chat_completion.choices[0].message.content
#     f.write(poem + "\n")
#     i += 1

# Test 05 - temperature=0, top_p=0, presence_penalty=2 gpt-3.5-turbo model | non-creative prompt
# f = open("test5.txt", "a")
# i = 1
# while i <= 10:
#     chat_completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": "What year was Sun Tzu born?"}], temperature=0, top_p=0, presence_penalty=2)
#     poem = chat_completion.choices[0].message.content
#     f.write(poem + "\n")
#     i += 1

# Test 06 - temperature=0, top_p=0, presence_penalty=2 gpt-4 model | non-creative prompt | prompt engineered
# f = open("test6.txt", "a")
# i = 1
# while i <= 10:
#     chat_completion = openai.ChatCompletion.create(model="gpt-4", messages=[{"role": "user", "content": "What year was Sun Tzu born? Reply with just the number without any additional characters."}], temperature=0, top_p=0, presence_penalty=2)
#     poem = chat_completion.choices[0].message.content
#     f.write(poem + "\n")
#     i += 1

def get_birth_year(figure):
    chat_completion = openai.ChatCompletion.create(model="gpt-4", messages=[{"role": "user", "content": "What year was" + figure + " born? Reply with just the number without any additional characters."}], temperature=0, top_p=0, presence_penalty=2)
    year = chat_completion.choices[0].message.content
    print(year)
    return year

his_fig = input("Historial figure to get birth year of: ")

i = 1
while i <= 10:
    get_birth_year(his_fig) 