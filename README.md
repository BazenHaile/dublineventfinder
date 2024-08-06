# dublineventfinder

dublineventfinder is a Django-based web application that allows users to discover, create, and manage events. Users can also send messages to each other about events, making it a comprehensive platform for event organization and networking. This application is now live in render at the address https://dublineventfinder-spjl.onrender.com

## Features
- User authentication (sign up, log in, log out)
- Create, edit, and delete events
- Search and filter events
- User messaging system
- Map integration for event locations
- Encrypted storage of sensitive information

## Technologies Used
- Django
- PostgreSQL
- OpenCage Geocoding API
- Django Cryptography
- Leaflet.js (for maps)
- HTML,CSS,JavaScript(Bootstrap)

## Prerequisites
- Python 3.8 or higher
- PostgreSQL
- pip (Python package manager)

## Installation
1. Clone the repository: https://github.com/BazenHaile/dublineventfinder.git
2. Create a virtual environment and activate it:
python -m venv myenv
source myenv/bin/activate  # On Windows use myenv\Scripts\activate
3. Install required packages:
pip install -r requirements.txt
4. Set up the database:
python manage.py migrate
5. Create a superuser:
python manage.py createsuperuser
6. Run the development server:
python manage.py runserver
7. Open a web browser and go to `http://127.0.0.1:8000/`

## Configuration

1. Create a `.env` file in the project root and add your secret key and database configuration:
SECRET_KEY=your_secret_key_here
DEBUG=True
DATABASE_URL=postgres://user:password@localhost/dbname
2. Get an API key from OpenCage Geocoding API and add it to your `.env` file:
OPENCAGE_API_KEY=your_api_key_here

## Usage

- Register a new account or log in
- Create new events from the dashboard
- Search for events using the search bar
- View event details and location on the map
- Send messages to event organizers and attendees

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.