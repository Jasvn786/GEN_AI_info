from transformers import pipeline

model = pipeline("question-answering",
model = "distilbert-base-cased-distilled-squad")

context = """ jasvnt is placed in microsoft 
ai eng and ml work and do any thing father name is jagdish_rathor
work on skill python , mysql , al eng
"""
while True:
    ques = input("what is your question? ")

    if ques == "quit":
        break

    result = model(question = ques,context = context)
    print(result)
