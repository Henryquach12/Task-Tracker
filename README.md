# Task Tracker (CLI)

## Overview
This project idea was inspired by the Task Tracker project from roadmap.sh: 
https://roadmap.sh/projects/task-tracker

Have you ever felt frustrated because you couldn’t keep track of all your tasks and ended up missing important ones? You may definitely need this app.

Task Tracker is a Command-Line Interface (CLI) application that allows users to manage and track their daily tasks efficiently.
The application:
- Accepts user input via command-line arguments using argparse
- Stores task data in a local JSON file
- Provides multiple commands to manage tasks (add, update, delete, mark, and list).

## Features
Add function:
- Create a new task to keep track of upcoming todo ones.
Update:
- Modify an existing task using its unique ID.
- Useful for correcting typos or updating task descriptions.
Delete:
- Remove a task permanently by specifying its ID.
Mark:
- Mark a task as in-progress when you start working on it..
- Mark a task as done once it is completed. Good jobs!
List:
- Display all tasks.
- Can be sorted by the status of the task (todo, in-process, done)

## Performance
The project is intentionally designed to be simple, modular, and easy to maintain. It follows a clean separation of responsibilities across three main files:
Main.py:
- Acts as the entry point of the application.
- Handles command-line input using argparse.
- Routes commands to the appropriate logic functions.
Logic.py:
- Contains the core business logic of the application.
- Implements task operations such as add, update, delete, mark, and list.
Database:
- Manages data persistence using a JSON file.
- Responsible for reading from and writing to the storage file.

# Input:
The application requires commands to follow specific patterns in the terminal.
Add a task:
- python main.py add "Task description"
Update a task: 
- python main.py update <task_id> "New description"
Delete a task:
- python main.py delete <task_id>
Mark a task:
- python main.py mark-in-progress <task_id>
or
- python main.py mark-done <task_id>
List a task:
- python main.py list
or 
- python main.py list todo
- python main.py list in-progress
- python main.py list done





