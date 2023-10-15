import asyncio
from functionality.shared_functions import create_reminder_tree, turn_reminder_to_string
from types import TracebackType
from Reminder import Reminder

reminders = {}

async def add_reminder(ctx, client):
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
    #sorted_reminder = dict(sorted(reminders[ctx.author.id].items(), key=lambda item: item[1]))
    #first_element = next(iter(sorted_reminder.items()))
    # Extract the key and value
    #lowest_desc, lowest_time = first_element
    #await reminder1(ctx,client,lowest_time, lowest_desc)

#async def reminder():
    #async def reminder1(ctx,client,time_in_seconds,description):
    #    await asyncio.sleep(time_in_seconds)
    #    await ctx.send(f"Reminder: {description}")
        #ctx.loop.create_task(reminder())
        #await asyncio.sleep(time_in_seconds)
        #await ctx.send(f"Reminder: {description}")

async def check_reminders(ctx, client):
    for user_id, user_reminders in list(reminders.items()):
        for idx, (description, time_in_seconds) in enumerate(user_reminders):
            if time_in_seconds <= 0:
                user = client.get_user(user_id)
                if user:
                    await user.send(f"Reminder: {description}")
                user_reminders.pop(idx)
            else:
                user_reminders[idx] = (time_in_seconds - 10, description)