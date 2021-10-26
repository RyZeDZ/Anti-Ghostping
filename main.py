import diskord, datetime

client = diskord.Client()

@client.event
async def on_ready():
	print(f"Logged in as {client.user}")


@client.event
async def on_message_delete(message):
	if message.mentions or message.role_mentions or message.mention_everyone:
		emb = diskord.Embed(title = f"{message.author} caught in 4K", description = f"**Deleted message:** \n{message.content}", color = diskord.Colour.blue(), timestamp = datetime.datetime.utcnow())
		if message.type == diskord.MessageType.reply:
			emb.set_footer(text = "Reply Ghostping", icon_url = message.author.avatar.url)
		else:
			emb.set_footer(text = "Normal Ghostping", icon_url = message.author.avatar.url)
		await message.channel.send(embed = emb)
	if message.embeds and "caught in 4K" in message.embeds[0].title:
		print(f"{message.embeds}\n\n{message.embeds[0].title}")
		title = message.embeds[0].title
		desc = message.embeds[0].description
		footer = message.embeds[0].footer.text
		icon = message.embeds[0].footer.icon_url
		emb = diskord.Embed(title = title, description = desc, color = diskord.Colour.red(), timestamp = datetime.datetime.utcnow())
		emb.set_footer(text = footer, icon_url = icon)
		await message.channel.send(embed = emb)


client.run("TOKEN")
