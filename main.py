import discord


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


client = MyClient()
client.run('OTc0MzA2MjAwNjAwNTg0MjYz.GBKGN_.cAQX6ZbyH8MCnrig1YOWcZQu7uMJGB4S0DNtU8')
