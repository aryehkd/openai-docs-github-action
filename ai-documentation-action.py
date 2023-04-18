import openai

openai.api_key = "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"

prompt = """
def kmToMiles(val):
  conv_fac = 0.621371
  miles = val * conv_fac
  return miles

can you generate python docstrings for this code?
"""

def makeRequest():
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )
    print(completion.choices[0], completion.choices[0].message.content)

makeRequest()