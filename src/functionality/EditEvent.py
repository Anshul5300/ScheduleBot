import discord
from functionality.highlights import convert_to_12
from functionality.shared_functions import read_event_file, create_event_tree, delete_event_from_file, edit_event_in_file
import json

async def edit_event(ctx,arg):
    """
    Function:
        edit_event
    Description:
        A existing event is edited from the user's schedule file
    Input:
        ctx: the current context
        arg: the instance of the bot
    Output:
        - A reply saying whether the event was edited or not
    """
 
    channel = await ctx.author.create_dm()
    await channel.send(
                    "Enter the name of the event from the following to be edited: "
                )
    def check(m):
        return m.content is not None and m.channel == channel and m.author == ctx.author

    # Open and read user's calendar file
    create_event_tree(str(ctx.author.id))
    rows = read_event_file(str(ctx.author.id))
    print(str(ctx.author.id))
    print("\n\n\n\n\n")

    event = {'Name': '', 'StartDate': '', 'StartTime': '', 'EndDate': '', 'EndTime': '','Priority':'', 'Type': '', 'Description': '', 'Location': ''}
    events = []
    eventFlag = False

    # If there are events in the file
    if len(rows) > 1:
        # For every row in calendar file
        for row in rows[1:]:
            # Get event details
            event['Name'] = row[1]
            start = row[2].split()
            event['StartDate'] = start[0]
            event['StartTime'] = convert_to_12(start[1][:-3])  # Convert to 12 hour format
            end = row[3].split()
            event['EndDate'] = end[0]
            event['EndTime'] = convert_to_12(end[1][:-3])  # Convert to 12 hour format
            event['Priority'] = row[4]
            event['Type'] = row[5]
            event['Description'] = row[6]
            event['Location']=row[7]
            # dates = [event['startDate'], event['endDate']]

            events.append(event)

            # reset event
            event = {'Name': '', 'StartDate': '', 'StartTime': '', 'EndDate': '', 'EndTime': '','Priority':'', 'Type': '', 'Description': '', 'Location': ''}

            # find all the existing schedules and display them
        if len(events) != 0:
            for e in events:
                embed = discord.Embed(colour=discord.Colour.magenta(), timestamp=ctx.message.created_at,title="Event Details-")
                embed.set_footer(text=f"Requested by {ctx.author}")
                embed.add_field(name="Event Name:", value=e['Name'], inline=False)
                embed.add_field(name="Start Date:", value=e['StartDate'], inline=True)
                embed.add_field(name="Start Time:", value=e['StartTime'], inline=True)
                embed.add_field(name="End Date:", value=e['EndDate'], inline=True)
                embed.add_field(name="End Time:", value=e['EndTime'], inline=True)
                embed.add_field(name="Event Priority:", value=e['Priority'], inline=False)
                embed.add_field(name="Event Type:", value=e['Type'], inline=False)
                embed.add_field(name="Description:", value=e['Description'], inline=False)
                if 'Location' in e.keys():
                    embed.add_field(name="Location:", value=e['Location'], inline=False)
                else:
                    embed.add_field(name="Location:", value='None', inline=False)
                await channel.send(f"You have \"{e['Name']}\" scheduled , from {e['StartDate']} {e['StartTime']} to {e['EndDate']} {e['EndTime']}")
                await ctx.send(embed=embed)
        else:
            await channel.send("You don't have any event scheduled..!!")

    else:
        eventFlag = True
        await channel.send("Looks like your schedule is empty. You can add events using the '!schedule' command!")

    # edit the event
    if not eventFlag:
        foundEvent = False
        while not foundEvent:
            await channel.send("Please enter the name of the event you want to edit")
            event_msg = await arg.wait_for("message", check=check)  # Waits for user input
            event_msg = event_msg.content  # Strips message to just the text the user entered
            eventTobeEdited = None
            for e in events:
                # Get event details
                    if e['Name'].lower() == event_msg.lower():
                        await channel.send(f'''Following are the current details of the event "{e['Name']}": \n 
                        StartDate: {e['StartDate']} \n
                        StartTime: {e['StartTime']} \n
                        EndDate: {e['EndDate']} \n
                        EndTime: {e['EndTime']} \n
                        Priority: {e['Priority']} \n
                        Type: {e['Type']} \n
                        Description: {e['Description']} \n
                        Location : {e['Location']}
                        ''')
                        foundEvent = True
                        eventTobeEdited = e
                        break
            if not foundEvent:
                await channel.send("The entered event name does not exists..!! Please try again")

        await channel.send("Enter the fields you want to update (except Name)\n" + "Here is the format you should follow\n" + "\{\"Field_Name\"(same as mentioned above)}: \"New_Value\"} [JSON Format]")
        keyFlag = False
        valueFlag = True
        dt_flag = False

        while not(keyFlag and valueFlag):

            event_msg = await arg.wait_for("message", check=check)  # Waits for user input
            input_data = json.loads(event_msg.content)

            try:
                if all(k in eventTobeEdited.keys() for k in input_data.keys()):
                    keyFlag = True
                else:
                    await channel.send("Enter the fields in correct format!!")
                    continue
            except:
                await channel.send("Enter the fields in correct format!!")
                continue
            
            for key in input_data.keys():

                if(key == 'StartDate' or key == 'StartTime' or key == 'EndDate' or key == 'EndTime'):
                    dt_flag = True

                if(key == 'Priority'):
                    if not(1 <= int(input_data[key]) <= 5):
                        await channel.send("Priority value is not correct, (should be 1-5)")
                        await channel.send("Please re-enter the enitre event data with all values correct")
                        valueFlag = False
    
        eventTobeEdited.update(input_data)
        edit_event_in_file(str(ctx.author.id),eventTobeEdited, dt_flag)

        await channel.send(f"The event \"{eventTobeEdited['Name']}\" was edited..!!")
