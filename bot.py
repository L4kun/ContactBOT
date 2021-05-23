import discord, json, config, requests, os
client = discord.Client()
power = True
logo = """
█▀▀█ █░░█ █▀▀ █▀▀ ▀▀█▀▀ ░▀░ █▀▀█ █▀▀▄   █▀▀▄ █▀▀█ ▀▀█▀▀
█░░█ █░░█ █▀▀ ▀▀█ ░░█░░ ▀█▀ █░░█ █░░█   █▀▀▄ █░░█ ░░█░░
▀▀▀█ ░▀▀▀ ▀▀▀ ▀▀▀ ░░▀░░ ▀▀▀ ▀▀▀▀ ▀░░▀   ▀▀▀░ ▀▀▀▀ ░░▀░░
"""
logo2 = """
█▀▀▄ █▀▀█ ▀▀█▀▀   █▀▀█ █▀▀ █▀▀█ █▀▀▄ █░░█
█▀▀▄ █░░█ ░░█░░   █▄▄▀ █▀▀ █▄▄█ █░░█ █▄▄█
▀▀▀░ ▀▀▀▀ ░░▀░░   ▀░▀▀ ▀▀▀ ▀░░▀ ▀▀▀░ ▄▄▄█
"""

@client.event
async def on_ready():
    os.system("cls")
    print(logo)
    print("====================================================")
    print(logo2)
    print("===================봇 정보==========================")
    print("봇 이름:" , client.user)
    print("봇 아이디:",client.user.id)
    print("====================================================")
    if power:
        await client.change_presence(activity=discord.Game(config.BotOptions.ON_GAME), status=discord.Status.online)
    else:
        
        await client.change_presence(activity=discord.Game(config.BotOptions.OFF_GAME), status=discord.Status.idle)

    

@client.event
async def on_message(msg: discord.Message):
    global power
    if msg.author.bot:
        return
    if msg.content == config.OtherOptions.ONOFF_COMMAND:
        if msg.author.id == config.BotOptions.owner:
            if power == True:
                await msg.channel.send(config.OtherOptions.OFF_MESSAGE)
                await client.change_presence(activity=discord.Game(config.BotOptions.OFF_GAME), status=discord.Status.idle)
                power = False
            else:
                await client.change_presence(activity=discord.Game(config.BotOptions.ON_GAME), status=discord.Status.online)
                await msg.channel.send(config.OtherOptions.ON_MESSAGE)
                power = True
    category = client.get_channel(config.OtherOptions.CATEGORY)
    if not isinstance(category, discord.CategoryChannel):
        print("Error: config.OtherOptions.CATEGORY is not CategoryChannel")
        return
    log = client.get_channel(config.OtherOptions.LOG_CHANNEL)
    if not isinstance(log, discord.TextChannel):
        print("Error: config.OtherOptions.CATEGORY is not CategoryChannel")
        return
    if msg.channel in category.text_channels:
        if power == False:
            await msg.delete()
            await msg.author.send("답변을 보낼 수 없습니다.")
            return
        if msg.channel.topic == "" or msg.channel.topic == None:
            return
        
        user = await client.http.get_user()(int(msg.channel.topic))
        if msg.content == config.OtherOptions.CLOSE_COMMAND:
            embed = embed=discord.Embed(
                    title=config.CloseMessages.TITLE,
                    description=config.CloseMessages.MESSAGE,
                    colour=discord.Colour.red()
                    )
            embed.set_footer(text=config.CloseMessages.AUTHOR)
            await user.send(embed=embed)
            await msg.channel.delete()
            return

        await user.send(
             embed=discord.Embed(
                 description=config.AnswerMessage.MESSAGE.replace("%name%",msg.author.name).replace("%message%",msg.content).replace("%top_role%",msg.author.top_role.name),
                 colour=discord.Colour.green()
             ),
        #await user.send(
            # embed=discord.Embed(
            #     description=config.AnswerMessage.MESSAGE.replace("%name%",msg.author.name).replace("%message%",msg.content).replace("%top_role%",msg.author.top_role.name),
            #     colour=discord.Colour.green()
            # ),
            
        )
        await log.send(str(msg.author) + " : " + msg.content)
        try:
           
            await user.send(msg.attachments[0].url)

        except:
            pass
        await msg.add_reaction(config.Emoji.MESSAGE)
    if isinstance(msg.channel, discord.DMChannel):
        if power == False:
            await msg.delete()
            embed = embed=discord.Embed(
                title=config.NoQuestionMessage.TITLE,
                description=config.NoQuestionMessage.MESSAGE,
                colour=0xFFFF00
            )
            embed.set_footer(text=config.NoQuestionMessage.AUTHOR)
            await user.send(embed=embed)
            await msg.channel.delete()
            return
        channel = None
        for _channel in category.text_channels:
            if _channel.topic == str(msg.author.id):
                channel = _channel
        if channel == None:
            channel = await category.create_text_channel(name=msg.author.name, topic=str(msg.author.id))
            embed = discord.Embed(
                    title=config.FirstMessages.TITLE,
                    description=config.FirstMessages.MESSAGE,
                    colour=discord.Colour.green()
                    )
            embed.set_footer(text=config.FirstMessages.AUTHOR)
            await msg.channel.send(embed=embed)
            
            for emoji in config.Emoji.FIRST:
                await msg.add_reaction(emoji)
        await channel.send(
            embed=discord.Embed(
                description=config.QuestionMessage.MESSAGE.replace("%name%",msg.author.name).replace("%message%",msg.content),
                colour=discord.Colour.green()
            )
        )
        await log.send(str(msg.author) + " : " +  msg.content)
        try:
            await user.send(msg.attachments[0].url)
        except:
            pass
        
        
            

client.run(config.BotOptions.TOKEN)
