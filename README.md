# API Documentation

Here is a list of available endpoints for the API:

| Endpoint             | Description                     |
|----------------------|---------------------------------|
| `/api/artists/`      | List and create artists         |
| `/api/artists/{id}/` | Retrieve, update, and delete an artist |
| `/api/albums/`       | List and create albums          |
| `/api/albums/{id}/`  | Retrieve, update, and delete an album |
| `/api/tracks/`       | List and create songs           |
| `/api/tracks/{id}/`  | Retrieve, update, and delete a song |

For more detailed information, refer to the API documentation.

# Spotifake

Welcome to My Project! This is a Django-based project that provides an API for managing artists, albums, and songs.

## Getting Started

Follow these steps to get the project up and running:

1. Clone the repository:<br>
    git clone https://github.com/spotifake/spotifake.git <br>
    cd project
2. Set up a virtual environment and activate it: <br>
    python3 -m venv venv
    source venv/bin/activate <br> On Windows: <br>venv\Scripts\activate
3. Install the required packages: <br>pip install -r requirements.txt
4. Apply migrations to create the database: <br>python3 manage.py makemigrations && python3 manage.py migrate
5. Run the development server: <br>python manage.py runserver

6. Open your browser and go to http://127.0.0.1:8000/api/ to access the API.

## Contributing

telegram: @mirbekov0909


