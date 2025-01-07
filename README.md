
# Pushups Logger

A simple Flask application for tracking your pushup workouts. This app allows users to sign up, log in, create and track their workouts.

## Features

- **Sign up and Login**: Users can sign up for an account, log in, and manage their sessions.
- **Workout Logging**: Users can create and track their pushups, with an optional comment on each workout.
- **Profile and Workout History**: View your profile and all past workouts.
- **Workout Management**: Edit or delete individual workouts.

## Technologies Used

- **Flask**: Web framework for building the application.
- **Flask-Login**: For user authentication and session management.
- **SQLAlchemy**: ORM for interacting with the database.
- **Werkzeug**: Library for password hashing and security.
- **HTML/CSS**: For the frontend templates.

## Installation

### Clone the repository:

```bash
git clone https://github.com/olaz20/pushup_tracker.git
cd pushup_tracker
```

### Set up a virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

### Install dependencies:

```bash
pip install -r requirements.txt
```

### Set up the database:

```bash
# Set up your database (make sure you have SQLite or another DB set up)
python
from app import db
db.create_all()
```

### Run the application:

```bash
flask run
```

The app should now be running at [http://localhost:5000](http://localhost:5000).

## Endpoints

- **/signup**: Allows new users to sign up.
- **/login**: Allows existing users to log in.
- **/logout**: Logs out the current user.
- **/profile**: Displays the user's profile information.
- **/new**: Allows users to create a new workout.
- **/all**: Displays all workouts logged by the user.
- **/workout/<id>/update**: Allows users to update a specific workout.
- **/workout/<id>/delete**: Allows users to delete a specific workout.

## File Structure

```
/app
    /templates
        - signup.html
        - login.html
        - profile.html
        - create_workout.html
        - all_workouts.html
        - update_workout.html
    /models
        - User.py (Defines the `User` model)
        - Workout.py (Defines the `Workout` model)
    /views
        - auth.py (Handles authentication logic)
        - main.py (Handles workout logic)
```

## Contributing

Feel free to fork the repository and submit pull requests. Issues and suggestions are welcome.
