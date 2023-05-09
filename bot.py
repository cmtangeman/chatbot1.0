import discord
import responses


async def send_message(message, user_message, is_private):
    try:
        response = responses.handle_response(user_message)
        await message.author.send(response) if is_private else await message.channel.send(response)

    except Exception as e:
        print(e)


intents = discord.Intents.default()
intents.message_content = True


def run_discord_bot():
    TOKEN = 'MTEwNTYwMDQ0MjYyNjQ3ODEyMQ.G4pqQz.7SXTjYlys1PIYq0pxCneNPHF4LznJgFeYubg0o'
    client = discord.Client(intents=intents)

    @client.event
    async def on_ready():
        print(f'{client.user}is now running!')

    @client.event
    async def on_message(message):
        if message.author == client.user:
            return

        username = str(message.author)
        user_message = str(message.content)
        channel = str(message.channel)

        print(f"{username}said: '{user_message}' ({channel})")

        if user_message and user_message[0] == '?':
            user_message = user_message[1:]
            await send_message(message, user_message, is_private=True)
        else:
            await send_message(message, user_message, is_private=False)

    client.run(TOKEN)
