import random


def handle_response(message) -> str:
    p_message = message.lower()

    if p_message == 'hello':
        return 'hola'

    if p_message == 'test':
        return 'test successful, good job Charlie!'

    if p_message == 'roll':
        return str(random.randint(1, 6))

    if p_message == '!help':
        return 'this is a help message you can change'

    return 'I don\'t understand that yet!'
