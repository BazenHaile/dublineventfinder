# Dublin Event Finder

## Overview

Dublin Event Finder is a comprehensive web application designed to connect event organizers and attendees in Dublin. Built with Django and leveraging modern web technologies, this platform offers an intuitive interface for discovering, creating, and managing events across the city.

**Live Demo:** https://dublineventfinder.onrender.com

## Key Features

- **User Authentication:** Secure sign-up, login, and profile management
- **Event Management:** Create, edit, delete, and view detailed event information
- **Advanced Search:** Filter events by name, date, category, and location
- **Interactive Map:** Visualize event locations using Leaflet.js
- **Messaging System:** In-app communication between users
- **Responsive Design:** Mobile-friendly interface using Bootstrap 5

## Technology Stack

- **Backend:** Django 4.2.13
- **Database:** PostgreSQL
- **Frontend:** HTML, CSS, JavaScript, Bootstrap 5
- **Map Integration:** Leaflet.js
- **API Integration:** OpenCage Geocoding API
- **Security:** Django Cryptography for data encryption
- **Deployment:** Render
- **Version Control:** Git & GitHub

## Prerequisites

- Python 3.8 or higher
- PostgreSQL
- pip (Python package manager)

## Installation and Setup

1. **Clone the repository:**
   git clone https://github.com/BazenHaile/dublineventfinder.git
   cd dublineventfinder

2. **Set up a virtual environment:**
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`

3. **Install dependencies:**
   pip install -r requirements.txt

4. **Configure environment variables:**
   Create a `.env` file in the project root with the following:
   
   
   SECRET_KEY=your_secret_key_here
   
   DEBUG=True
   
   DATABASE_URL=postgres://user:password@localhost/dbname
   
   OPENCAGE_API_KEY=your_opencage_api_key
   
   EMAIL_HOST_USER=your_email@example.com
   
   EMAIL_HOST_PASSWORD=your_email_password
   

6. **Set up the database:**
   python manage.py migrate

7. **Create a superuser:**
   python manage.py createsuperuser

8. **Run the development server:**
   python manage.py runserver

9. Access the application at `http://127.0.0.1:8000/`

## Usage Guide

1. **Registration and Authentication:**
   - Sign up for a new account or log in
   - Customize your user profile

2. **Event Management:**
   - Create new events from your dashboard
   - Edit or delete your events as needed

3. **Discovering Events:**
   - Use the search bar to find events by name, date, or category
   - Explore events on the interactive map

4. **Interaction:**
   - Apply to attend events
   - Send messages to event organizers or other attendees

5. **Admin Functions:**
   - Access the Django admin interface at `/admin` for site management

## Deployment

The application is hosted on Render. To update the deployed version:

1. Push changes to the GitHub repository:
   
   git add .

   git commit -m "Your descriptive commit message"

   git push origin master

3. Render will automatically detect the changes and redeploy the application.

## Security Features

- HTTPS enforcement
- Sensitive data encryption using django-cryptography
- CSRF and XSS protection
- Secure password hashing
- Environment variable management for sensitive credentials

## Contributing

We welcome contributions to the Dublin Event Finder project! Here's how you can contribute:

1. Fork the repository
2. Create a new branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

Please ensure your code adheres to the project's coding standards and includes appropriate tests.

## Troubleshooting

If you encounter any issues during setup or usage:

1. Ensure all dependencies are correctly installed
2. Verify that your `.env` file contains all necessary configurations
3. Check the console and server logs for error messages
4. For persistent problems, please open an issue on GitHub with a detailed description

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

## Acknowledgments

- OpenCage for providing geocoding services
- Render for hosting the application
- All contributors and supporters of the project

## Contact

For questions, suggestions, or support, please open an issue on the GitHub repository.

---

Thank you for your interest in Dublin Event Finder. We hope this platform enhances your experience with Dublin's vibrant event scene!
