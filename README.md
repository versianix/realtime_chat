# realtime_chat

A real-time chat application built with Django, supporting private and group chats with live updates.

## Features

- **Real-time Messaging**: Send and receive messages instantly without refreshing the page.
- **Private Chats**: One-on-one conversations between users.
- **Group Chats**: Create and join group chats with multiple participants.
- **Online Status**: See when users are online.
- **File Sharing**: Share images and files in chats.
- **Responsive Design**: Accessible on both desktop and mobile devices.

## Technologies Used

- **Django**: Backend framework for server-side logic.
- **HTMX**: For handling AJAX requests and WebSocket connections.
- **Alpine.js**: Lightweight JavaScript framework for interactive UI components.
- **Tailwind CSS**: Utility-first CSS framework for styling.
- **WebSockets**: For real-time communication.

## Installation

1. **Clone the repository:**
    ```bash
    git clone https://github.com/versianix/realtime_chat
    ```

2. **Navigate to the project directory:**
    ```bash
    cd realtime_chat
    ```

3. **Create a virtual environment:**
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

4. **Install the requirements:**
    ```bash
    pip install -r requirements.txt
    ```

5. **Apply migrations:**
    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

6. **Create a superuser (optional, for admin access):**
    ```bash
    python manage.py createsuperuser
    ```

7. **Run the development server:**
    ```bash
    python manage.py runserver
    ```

## Usage

1. Open your browser and go to [http://localhost:8000/](http://localhost:8000/).
2. Register a new account or log in with your existing credentials.
3. Start a private chat by visiting a user's profile and clicking "Converse comigo".
4. Create or join group chats to converse with multiple users.

