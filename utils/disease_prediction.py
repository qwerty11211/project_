import os
import speech_recognition as sr
import openai
openai.api_key = os.environ.get("OPENAI_API_KEY")


r = sr.Recognizer()
with sr.Microphone() as source:
    print("listening")
    audio = r.listen(source)


text = r.recognize_google(audio)
print(text)
symptom = text.split("symptom")[1:]


def make_openapi_call(prompt):
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=2048
    )
    result = response["choices"][0]["text"]
    print(result)
    return result


diseases = make_openapi_call(
    f"List as points without explanation the top 2 names of disease that is likely given the following symptoms  : {', '.join(symptoms)}")
print("disease is", diseases)
medicine = ''

for disease in diseases.split("\n"):
    print(disease)
    medicine += make_openapi_call(f"What are the  medication for {disease}")
