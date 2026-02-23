from openai import OpenAI

client = OpenAI()

resp = client.responses.create(
    model="gpt-4o",
    input="Vanishing gradient problemini açıkla ve nasıl çözülebileceğini anlat."
)

print(resp.output_text)