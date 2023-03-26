import openai
import argparse

openai.api_key = ""  # Replace TU_API_KEY_AQUI with your own OpenAI API key

def generar_respuesta(prompt):
    completado = openai.Completion.create(
        engine="davinci",
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )
    mensaje = completado.choices[0].text
    return mensaje.strip()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Text generator with ChatGPT')
    parser.add_argument('prompt', metavar='PROMPT', type=str,
                        help='the prompt or question to generate a response')
    args = parser.parse_args()

    respuesta = generar_respuesta(args.prompt)
    print(respuesta)