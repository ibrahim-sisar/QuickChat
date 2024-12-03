# QuickChat: A Simple Social Media Platform
#### Video Demo: <https://www.youtube.com/watch?v=gQidJSOYlCc>
#### Description
QuickChat is a simple and intuitive social media platform designed for casual users, focusing on ease of use and performance. The platform aims to provide a user-friendly experience by simplifying the complexities that are often found in other social media platforms. Whether you're a tech-savvy user or someone who prefers simplicity, QuickChat has a straightforward interface to accommodate all ages.

## Features:
1. **Simple User Interface**: A minimalistic design to make navigation easy for everyone.
2. **Personal Information**: Users can optionally add personal information to introduce themselves to others.
3. **Friend Search**: Easily search for friends by their full name or username.
4. **Privacy Focused**: Users can control what information is shared with others on the platform.

## Structure:
The project follows the typical Django project structure with the following important directories and files:

1. **manage.py**: Used to run Django management commands.
2. **db.sqlite3**: The database file storing user data and other platform-related information.
3. **venv/**: The virtual environment containing all the required packages for the project.
4. **main/**: Contains the core settings and configuration for the Django project.
   - **QuickChat/**: Contains essential project files like `settings.py`, `urls.py`, `wsgi.py`, and `asgi.py`.
5. **chat/** and **user/**: Two applications within the project.
   - **chat/**: Responsible for handling messages and conversations between users.
   - **user/**: Handles user authentication and profile management.

## Files Breakdown:
- **models.py**: Defines the data structure of the project, such as User profiles and messages.
- **views.py**: Contains the logic for displaying data and managing user requests.
- **urls.py**: Defines the URL routing for each app within the project.

## How to Use:
1. Clone the repository and navigate to the project directory.
2. Set up a virtual environment by running `python -m venv venv` and activate it.
3. Install required dependencies using `pip install -r requirements.txt`.
4. Apply the migrations with `python manage.py migrate`.
5. Start the development server using `python manage.py runserver`.
6. Visit the platform at `http://127.0.0.1:8000/` and start using it!

## Design Choices:
During the development of QuickChat, several key design decisions were made to ensure that the platform was user-friendly:
1. **Minimalistic UI**: This choice was made to make the platform accessible for users of all ages, especially those who prefer simplicity.
2. **Personalized Profiles**: The option for users to add personal information was added to enhance user interaction and help users get to know each other better.
3. **Efficient Search Function**: The friend search functionality allows users to search by full name or username, improving the user experience when connecting with others.

## Future Work:
1. **Mobile App**: There are plans to develop a mobile application for QuickChat to increase its accessibility.
2. **Improved Security Features**: As the platform evolves, adding more security features such as two-factor authentication and better encryption for user data will be a priority.

## Conclusion:
QuickChat is designed to be a simple yet powerful social media platform, focusing on ease of use, privacy, and performance. It’s ideal for casual users who want to connect with friends and family without the complexity of other platforms.

Feel free to contribute or reach out with any feedback!
