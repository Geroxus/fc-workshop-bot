import discord
from os import getenv

from material_list import mat_list


class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))
        for guild in self.guilds:
            for tc in guild.text_channels:
                if tc.name.startswith('general'):
                    await tc.send('Hello there!\n(This is an automatic message displayed, when I am booted.')
                    break
            print('logged onto: {0.name}'.format(guild))

    async def on_message(self, message):
        print('Message from {0.author}: {0.content}'.format(message))
        if message.content.startswith('echo'):
            await message.channel.send(message.content[4:])
        if message.content.startswith('recipe'):
            value = mat_list('Bronco', 'Sail')
            new_msg = 'Recipe for Bronco Sail\n'
            for index, table in enumerate(value):
                new_msg = new_msg + '**Phase ' + str(index) + '**\n'
                for entry in table:
                    new_msg = new_msg + entry + '\n'
            await message.channel.send(new_msg)




client = MyClient()
client.run(getenv('DiscordBotToken'))
