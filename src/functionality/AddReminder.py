async def add_reminder(ctx, client):
    reminders = {}
    channel = await ctx.author.create_dm()
    def check(m):
        return m.content is not None and m.channel == channel and m.author == ctx.author
    await channel.send("Lets add a reminder!\n" + "First give me the short description of your reminder:")
    description_message = await client.wait_for("message", check=check)
    description = description_message.content
    await ctx.send("Please enter the time(in minutes) from now for the reminder:")
    time_message = await client.wait_for('message', check=check)
    time = int(time_message.content)
    time_in_seconds = time * 60
    if ctx.author.id not in reminders:
        reminders[ctx.author.id] = []
        reminders[ctx.author.id].append((description,time_in_seconds))
        await ctx.send(f"Reminder set! I will remind you in {time} minutes about '{description}'.")
