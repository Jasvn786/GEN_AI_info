from transformers import pipeline
gen = pipeline(
    'text-generation',
     model='gpt2')

result = gen("programing-language", max_length = 200)

print(result)