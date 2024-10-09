
# HoopStats Search Engine
* HoopStats Search Engine is a web application designed to search and display basketball player statistics from the movie Space Jam. 
* It includes both frontend and backend components, allowing users to easily query player data, display statistics, and view player performance across multiple games.

# Introduction
* The HoopStats Search Engine is a basketball statistics platform that allows users to search for players by name and retrieve detailed game stats. 
* The application is built with a robust frontend that interacts with a backend API to provide real-time data to the users.
* The project has been designed with scalability and usability in mind, utilizing modern web development technologies for both the frontend and backend.

# Demo
https://github.com/user-attachments/assets/a32a3428-fb56-4ec0-92e5-6e5d13448caf

https://github.com/user-attachments/assets/9099115e-80a3-4d47-9448-acfeefee1893



# Technologies Used
## Frontend:
* Angular: A robust framework for building single-page applications.
* Bootstrap 5: For responsive design and modern UI components.
* TypeScript: For static typing and clean code structure.
* SCSS: For custom styling and flexibility in design.
* Tailwind CSS: A utility-first CSS framework to streamline the design process.

## Backend:
* Django: A high-level Python web framework used for developing the backend API.
* Django REST Framework: For creating RESTful APIs.
* PostgreSQL: A powerful, open-source object-relational database system.
* Gunicorn: WSGI HTTP Server for running the Django application.

# Frontend Overview
* The frontend of HoopStats is built using Angular and styled using Bootstrap 5 and Tailwind CSS. 
* It provides a clean and interactive user interface for searching player stats, displaying game summaries, and visualizing player performances.

## Features:
* Search for players by name.
* Autocomplete feature for player names.
* Display detailed player statistics including game history, shots taken, and field goals made.
* Responsive design that works across mobile, tablet, and desktop devices.

## UI Design:
* Bootstrap 5 and Tailwind CSS were used to create a modern, user-friendly interface.
* The input fields, buttons, and navigation tabs are styled to provide visual feedback and an intuitive user experience.
* The game statistics are displayed in a table format for easy readability, and the shots are listed in a two-column layout to reduce vertical scrolling.


## How to Run the Frontend:
1. Navigate to the frontend directory.
2. Install the dependencies:
    ```
    npm install
    ```
3. Run the development server:
    ```
    npm start
    ```
4. Open http://localhost:4200 to view it in the browser.

# Backend Overview
* The backend of HoopStats is built using Django and Django REST Framework. 
* It serves as the API layer that provides player data and game statistics to the frontend.

## Features:
* RESTful API endpoints for searching and fetching player data.
* SQL queries optimized to fetch player stats and game performance efficiently.
* Error handling for invalid queries and missing data.
* Integration with PostgreSQL for data storage.

## Database Schema:
* Player: Contains player information like name and ID.
* Teams: Contains team information like name and ID.
* Games: Contains game information like date and ID. 
* Player Stats: Stores game-specific statistics for each player (e.g., minutes played, points scored).
* Shot: Records the location of each shot taken in a game and whether it was made or missed.

## Populating Database
* The database is populated with raw game and player information using a custom Python script. 
* This script reads raw game statistics and player data, processes the information, and inserts it into the PostgreSQL database.

* The script can be run as follows after setting up the database:
    ```
    python populate_database.py
    ```
* This script ensures that all game data, including shot locations, field goal attempts, and other player stats, are accurately recorded for querying by the frontend.

## API Endpoints:
* `/api/v1/playerAutocomplete?query=<name>`: Fetch player name suggestions based on a search query.
* `/api/v1/playerSummary/<playerName>`: Fetch detailed player statistics, including game stats and shot performance.

## How to Run the Backend:
1. Navigate to the backend directory.
2. Create and activate a virtual environment:
    ```
    python -m venv .venv
    source .venv/bin/activate
    ```

3. Install the dependencies:
    ```
    pip install -r requirements.txt
    ```

4. Apply database migrations:
    ```
    python manage.py migrate
    ```

5. Run the development server:
    ```
    python manage.py runserver
    ```
6. The backend will be available at http://localhost:8000.

# Installation

## Prerequisites:
* Node.js: Ensure you have Node.js (v16.20.x) installed for the frontend.
* Python 3.x: Required for running the Django backend.
* PostgreSQL: Set up a PostgreSQL database for storing player and game data.

## Steps:
1. Clone the repository:
    ```
    git clone <repository-url>
    ```
2. Follow the instructions in the Frontend and Backend sections to install and run the application.

