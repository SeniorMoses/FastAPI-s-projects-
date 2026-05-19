HiveBot API

Simple chatbot API built with FastAPI and TheFuzz for text matching.

The bot can reply to messages and also learn new responses through an API endpoint.

Built using Python and deployed from a phone.

Features

Chat endpoint for conversations

Teach the bot new responses

Fuzzy text matching with TheFuzz

Stores learned responses in JSON

Lightweight and beginner-friendly

Persistent local data storage


Tech Stack

Python

FastAPI

TheFuzz

JSON


Endpoints

Metho 

GET	/	Server status
GET	/chat	Chat with the bot
POST	/teach	Teach the bot new responses


How It Works

The bot compares user messages with saved questions using fuzzy matching.

If a close match is found, it returns the saved answer.
If not, it responds with a fallback message.

New responses can be added through the /teach endpoint and are saved automatically in response.json.

Run Locally

1. Clone or download the project


2. Install the required packages


3. Start the FastAPI server


4. Open the API in your browser or testing tool



Notes

This project was built while learning backend development and API development with Python.

Created mainly from a phone as part of practicing FastAPI and building real projects consistently.
