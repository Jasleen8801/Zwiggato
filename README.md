# Zwiggato

This is related to the project for Software Engineering course UCT305 using selenium to compare the prices of food items on various apps like Swiggy and Zomato using a Discord Bot.

## Project Overview

Discord is a VoIP and instant messaging platform and Discord bots are AI-driven tools that can help you automate tasks on your Discord server. Using our bot Foodie-Fi, one can start their own private thread, and then provide with the bot commands to start the procedure.

You’ll need to enter the city name, restaurant name and food item you want to order, and then the bot will process through the various web apps and provide you with the price on each of the apps, where the item is available, along with the redirect url of the website, to take you on the site where you want to place the order on.

Unique Selling Point: The comparison web applications online are usually very less user friendly, here we are creating a discord server where all you’ve to do is enter the product name and it will provide the price on various food ordering apps, depending on the availability.

## Prerequisites

Before running the project, make sure you have the following installed:

- Python 3.X
- Chrome browser
- Discord Account and Server

## Setup

1. Clone the repository:

```bash
git clone https://github.com/Jasleen8801/Zwiggato.git
cd Zwiggato
```

2. Create and activate a virtual environment:

```bash
python -m venv venv
source venv/bin/activate
```

3. Install the required dependencies:

```bash
pip install -r requirements.txt
```

4. Next, create a `.env` file in the root of the directory where `main.py` is present with following format.

```bash
DISCORD_TOKEN=<YOUR_DISCORD_TOKEN>
GUILD_ID=<YOUR_SERVER_ID>
ADMIN_USER_ID=<YOUR_USER_ID>
```

## Accessing Discord Token

1. Create a New Application:

    - Visit the Discord Developer Portal.
    - Log in with your Discord account if you aren't already.
    - Click the "New Application" button.

2. Set Application Name:

    - Provide a name for your application. This name will be visible to users, so choose a meaningful name for your bot.  

3. Create a Bot:

    - In the left sidebar, click on the "Bot" tab.
    - Click the "Add Bot" button.

4. Get the Token:

    - Scroll down to the "TOKEN" section.
    - Click the "Copy" button to copy the token to your clipboard. Keep this token secure and do not share it publicly.

5. Add the Bot to Your Server:

    - In the left sidebar, go back to the "General Information" tab.
    - Copy the "Client ID" under the "APPLICATION ID" section.
    - Visit the following URL (replace YOUR_CLIENT_ID with your actual client ID):
      `https://discord.com/oauth2/authorize?client_id=YOUR_CLIENT_ID&scope=bot&permissions=0`
    - Select the server where you want to add the bot and follow the prompts to authorize it.

6. Add the token to the `.env` file and keep it safe.

## Obtaining the Guild ID

1. Enable Developer Mode:

    - Open Discord and go to the settings.
    - Under "Advanced," enable "Developer Mode."
    - Copy the Guild ID:

2. Right-click on the server name in your server list.

    - Click on "Copy ID" to copy the guild ID to your clipboard.

3. Add the GUILD ID to the `.env` file and keep it safe

## Obtaining the Admin ID

1. Enable Developer Mode:

    - Open Discord and go to the settings.
    - Under "Advanced," enable "Developer Mode."
    - Copy the User ID:

2. Right-click on your username in the user list.

    - Click on "Copy ID" to copy the user ID to your clipboard.

3. Add the ADMIN ID to the `.env` file and keep it safe

## Running the Bot

1. Activate the virtual environment on Linux/MacOS:

```bash
source venv/bin/activate
```

Activate the virtual environment on Windows:

```bash
venv\Scripts\activate
```

2. Run the bot:

```bash
python3 main.py
```

## Features and Endpoints

### Set Value Commands
- `setcity`: Set the city name.
- `setrest`: Set the restaurant name.
- `setfood`: Set the desired food item.

### Web Commands
- `process`: Load required data from food delivery websites.
- `result`: Show results from food delivery websites.

### Basic Commands
- `help`: Display available commands.
- `clear`: Clear values stored in the database.
- `list`: Show currently set values in the database.

### Miscellaneous Commands
- `suggest`: To suggest a food item
- `trending`: To get the trending food items
- `blogs`: To get the latest food blogs
- `report`: To report a bug or issue
- `about`: To know more about the bot

These features enable users to streamline the process of comparing food prices and making informed choices when ordering from different platforms.
