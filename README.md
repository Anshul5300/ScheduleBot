![ScheduleBot logo](https://raw.githubusercontent.com/lyonva/ScheduleBot/main/docs/img/banner.png)

![Python v3.9](https://img.shields.io/badge/python-v3.9-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![DOI](https://zenodo.org/badge/703561021.svg)](https://zenodo.org/badge/latestdoi/703561021)
![example workflow](https://github.com/Anshul5300/ScheduleBot/actions/workflows/python-app.yml/badge.svg)
![example workflow](https://github.com/Anshul5300/ScheduleBot/actions/workflows/style_checker.yml/badge.svg)
![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/Anshul5300/ScheduleBot)
[![GitHub issues](https://img.shields.io/github/issues/Anshul5300/ScheduleBot)](https://github.com/Anshul5300/ScheduleBot/issues)
[![GitHub release (latest by date including pre-releases)](https://img.shields.io/github/v/release/Anshul5300/ScheduleBot?display_name=release)](https://github.com/Anshul5300/ScheduleBot/releases)
[![GitHub all releases](https://img.shields.io/github/downloads/Anshul5300/ScheduleBot/total)](https://github.com/Anshul5300/ScheduleBot/releases)
[![Platform](https://img.shields.io/badge/platform-discord-blue)](https://discord.com/)
![Commits](https://img.shields.io/github/commit-activity/t/Anshul5300/ScheduleBot)
![Contributors](https://img.shields.io/github/contributors/Anshul5300/ScheduleBot)
[![codecov](https://codecov.io/gh/Anshul5300/ScheduleBot/graph/badge.svg?token=W9YNWEHQ9D)](https://codecov.io/gh/Anshul5300/ScheduleBot)


### Project 2 Submission:
Video of New Functionalities added in Schedule Bot in V4.0(https://youtu.be/oEAZkdvSKbU)

# ScheduleBot

> Don't let the fear of the time it will take to accomplish something stand in the way of your doing it. The time will pass anyway; we might just as well put that passing time to the best possible use. - Earl Nightingale

<p align="center">
  <a href="#rocket-getting-started">Getting Started</a>
  ::
  <a href="#thought_balloon-for-developers">For Developers</a>
  ::
  <a href="#dizzy-features-in-v2">Features in V2</a>
  ::
  <a href="#muscle-whats-new-in-v3">What's new in V3</a>
  ::
  <a href ="#fire-whats-new-in-v4">What's new in V4</a>
</p>


ScheduleBot is a Python application that helps you calendarize events and work through a Discord bot. Want to try it out? Simply follow the steps outlined in the [For Developers](#For-Developers) section. ScheduleBot can be configured to run on your Discord server by adding just one line of code!


With ScheduleBot you can quickly schedule events, state your prefered times for certain types of activities (exercise, homework, meetings, etc.) and quickly find out which times you have available to do more stuff.

https://user-images.githubusercontent.com/34405372/139776326-722e8526-4977-4ffd-b00e-c86a8fd5f706.mp4


:rocket: Getting started
---
To get a list of commands, DM the bot the command:

```
!help
```

The bot will reply back you with the list of available commands.

<img width="283" alt="Screenshot 2023-10-19 at 8 48 09 PM" src="https://github.com/Anshul5300/ScheduleBot/assets/40301987/03d34419-84c3-4118-8f81-6b83e1bc41d2">

### **Scheduling an event**

ScheduleBot's unit of work is the **event**. When you use ScheduleBot to organize your activities, it keeps track of your registered events. Each event consists of a period of time, comprised between a starting and ending date/time, event type, event priority and optional notes.  

To schedule a new event, just DM the bot:

```
!schedule
```

The bot will ask you the details of your new event.

![Schedule](docs/img/!schedul.gif)

### **I forgot my agenda for the day**

You can take a look at your events scheduled for a specfic date with the command:

```
!day today(or tomorrow\yesterday)
```

```
!day 3 (3 days from now)
```

```
!day -3 (3 days ago)
```

```
!day 4/20/22 (On Apr 20, 2022)
```

The bot will show you what you have scheduled for the date. This includes events that start before, or end after this date.

![Day](docs/img/!day.gif)

### **I don't really want to work at 3 a.m.**

You can create custom event types to further organize your schedule. You can define your preferred times by creating a new event type:

```
!typecreate
```

The bot will ask you for the name of the type and your preferred times.

![Type Create](docs/img/Type%20Create.gif)

### Import & Export your calendar

You can import or export their calendar events as a CSV file through the bot. You can also import ICS files downloaded from Google Calendar.

```
!exportfile
```
![Export file](docs/img/!export.gif)

```
!importfile
```
Then drag the file to the Schedulebot.

![Import file](docs/img/!import.gif)

### Looking for the spare time?

ScheduleBot will help you find your free times. Just write:

```
!freetime
```
![Freetime](docs/img/!freetime.gif)

### Find available times for a type of event
When you look for available times, you now can use `!find` to find only the available times in your preferred hours. 

![Find Available times](docs/img/find.gif)

:thought_balloon: For Developers
---

### Get your Discord bot 

 Follow this [tutorial](https://www.freecodecamp.org/news/create-a-discord-bot-with-python/) to create your discord bot account.

### Token
  To "login" to your bot through our program, place a file named `config.py` in your src directory with the content:
  
  ```
  TOKEN = ************(your discord bot token)
  ```
  
### Intall required packages
  ```
  pip install -r requirements.txt
  ```
  
### Connect to Google Cloud
  1. Create a Project 
  2. Setup Billing 
  3. Enable geocoding API and distancematrix API
  4. Generate API key-
      Refer to [this](https://developers.google.com/maps/documentation/geocoding/get-api-key) link for more information about the same.
  5. Store the API key in the following format-
      File name: key.json \
      File Content: 
      ```
      {"key": "your api key here"}
      ```
  6. Key needs to be stored in the json folder.

### Run the schedulebot.py
  ```
  python3 schedulebot.py
  ```
  Then your scheduleBot should start working.
  
## Releases
-   [v1.1](https://github.com/lyonva/ScheduleBot/releases/tag/v1.1): First functional release
-   [v2.0](https://github.com/qchen59/ScheduleBot/releases/tag/v2.0.0): First version 2 release with import/export events function, find available time feature, also supports 24 hour time format and event priority.
-   [v2.1](https://github.com/qchen59/ScheduleBot/releases/tag/v2.1.0): Finalized version 2, check what's new in V2
-   [v3.0](https://github.com/SEProjGrp5/ScheduleBot/releases) Finalized version 3, check out what's new in V3
-   [v4.0](https://github.com/Anshul5300/ScheduleBot/releases/tag/0.01) Finalized version 4, check out what's new in V4

:dizzy: Features in V2:
---

Please note that this is not an exhaustive list, however it does include all major improvements. For a complete list of all changes and bug fixes, please see our closed github issues or commit history.

#### Import & Export your calendar

The user can now import or export their calendar events as a CSV file through the bot. The user can also import ICS files downloaded from Google Calendar.

#### Find time based on schedule + preferred time

ScheduleBot can help you find available times for a type of event based on your schedule and preferred time for the event type.

#### Event types with priority

Users can now assign a priority value for each event. This will help them keep track of important events. It also provides a foundation for future improvements, such as suggesting event removals based on the priority of events.

#### Support 24-hour time format input

We support 24-hour time format input, in addition to the 12-hour format.

#### User's files encryption/decryption

User's data is now encrypted when it is stored in the host server, so the host will not be able to see other users\' schedules as easily. This improves user's privacy when using Schedulebot.

#### Check schedule for arbitrary days 

Users are able to check the schedule for any specific day in addition to today. Previously, only the events occurring today could be retrieved by the user.

#### Code coverage improvement

In this version, we improved the project's code coverage from 39% to 54%.

Code coverage remains low in this project because many sections of code require a Discord channel, and responses from a non-bot user through Discord. However, we were able to create a mock discord channel and user for several tests by using the "dpytest" library.

#### Fixed bugs related to the welcome message sent at startup

At startup, the bot now sends an on_ready welcome message to all servers the bot is currently listening to, instead of just one specific server. The bot also no longer attempts to respond to reactions to the welcome message made by itself or other bots.

#### Fixed bugs related to finding freetime

!freetime function was not working under certain circumstances, such as when there was only one event in the schedule. This has been fixed in the latest version.

## Getting involved

Thank you for caring for this project and getting involved. To start, please check out [contributing](https://github.com/qchen59/ScheduleBot/blob/main/CONTRIBUTING.md) and [code of conduct](https://github.com/qchen59/ScheduleBot/blob/main/CODE_OF_CONDUCT.md). For more technical detail of implementation of code, you can check out the documentation. When you want to get your hands on the project, take a peek into the [github project](https://github.com/qchen59/ScheduleBot/projects/1), assign yourself a task, move it to To-Do, and convert it into an issue and assign it to yourself.

Check out the [internal documentation](https://htmlpreview.github.io/?https://github.com/qchen59/ScheduleBot/blob/main/docs/src/index.html) if you want to contribute or find out about the inner workings of ScheduleBot.

:muscle: What's new in V3:
---
Following are the new features that we have implemented for version 3 : 

#### 1. Connection to Google: 
We have added the functionality to connect the account to google calendar


https://user-images.githubusercontent.com/89954066/144730436-29f74af7-36f2-45d0-a8c1-e19b5271b584.mp4


#### 2. Adding location of an event
We are now storing the location data of the events


https://user-images.githubusercontent.com/89954066/144730441-a65cbfae-80e5-402a-b362-901dd4f9884d.mp4


#### 3. Adding travel time as a separate event before the actual event
The bot adds a separate event to block of travel time to an event


https://user-images.githubusercontent.com/89954066/144730454-1b4c36e7-8230-4f9d-a3df-f4f2d499cc07.mp4


#### 4. Delete Event from schedule
User can delete events from their schedule


https://user-images.githubusercontent.com/89954066/144730459-1a12d11f-d9ad-44dc-a823-5e8acdae20c7.mp4


#### 5. Added a new functionality to check daily summary
Ability to view the daily summary of events


https://user-images.githubusercontent.com/89954066/144730460-5bc5dca7-7758-4106-8ec1-5ccd287ef5c2.mp4


#### 6. Code Coverage improvement
For this version, we have improved the project's code coverage from 54% to 65%.

#### 7. Viewing Google Calender events
User can check their next 10 events in the google calendar


https://user-images.githubusercontent.com/89954066/144730470-7700507e-b2e9-4175-88c0-749c15097702.mp4

:fire: What's new in V4:
---

https://github.com/Anshul5300/ScheduleBot/assets/58720954/cd0c28c0-1968-46d6-a132-fbe9d16c4823

Following are the new features that we have implemented for version 4 : 

#### 1. Recurring events: 
We have added the functionality to help users schedule recurring events(daily/weekly/monthly)

https://github.com/Anshul5300/ScheduleBot/assets/58720954/913f4dfe-62ee-4b38-90ef-0617bb3d8d98

#### 2. Reminder: 
We have added the functionality to remind users when the event starts

https://github.com/Anshul5300/ScheduleBot/assets/58720954/35b067ac-b9b7-4e4c-851e-35b5f8864ef9

#### 3. Snooze Reminder: 
We have added the functionality to help users snooze a reminder of the event by 15 minutes

https://github.com/Anshul5300/ScheduleBot/assets/58720954/cfbfa4fb-7af7-42f7-8efd-2fa586516e29

#### 4. Edit Event: 
We have added the functionality to help users edit their event details

https://github.com/Anshul5300/ScheduleBot/assets/40301987/e7c5208c-0a7a-4bfc-9756-36bb937aef00

#### 5. Delete Event: 
We have fixed the Delete Event functionality which helps users to delete their events

https://github.com/Anshul5300/ScheduleBot/assets/40301987/47310bf4-c56e-406d-87fa-ad6f209c76bc

#### 6. Send event details to other users: 
We have added the functionality to make events more collaborative by sending event details to other members involved in the event.

https://github.com/Anshul5300/ScheduleBot/assets/91055071/1cf611c4-34d0-4fb2-934b-9d5ba436bba7

## Future features
These are example features that could be added to ScheduleBot in the future.

### Integration with online task management tools
Provide the functionality of syncing tasks from tools like Trello and ClickUp. It should help the user to push/pull the tasks to/from the tool.

### Connect Outlook Calendar with Discord Bot
Add a functionality that allows user to add/sync their Outlook calendar with the Schedule bot.

### Quick event creation

You can quickly create a new event with the command

```
!schedulefind type X
```

It will find and schedule the first available X contiguous hours, on your preferred hours of the specified `type`.

### Suggest event removals
When Your entire day is scheduled
You have event 1 of priority 4
You try to find time for another event of priority 3
ScheduleBot should say there is no time but can suggest replacing event 1 as it has less priority.

### Merge Discord events with Google Calendar
Try to create a functionality to merge discord events with Google Calendar.

### Replace the current csv format for storing events with Google Calendar
As of now, the events are stored in a CSV format. In the future implementation,a functionality can be added to store the events in Google Calendar. 

### Edit google events
In this project, you can edit the events from discord. For future implemetation, a new functionalty can be created to edit events directly from Google Calendar.

### Add a "How to do" documentation for discord connection
Help user understand the process of adding the Discord bot to their server.
