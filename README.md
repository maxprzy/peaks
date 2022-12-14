Django Rest Framework project for Meteo France to do CRUD operation with mountain peaks running on Docker with PostgreSQL server.

Ton run the project:

- clone the repository
- cd into peaks folder
- run 'docker compose up -d' to start the server
- run 'docker exec peaks-web-1 sh -c 'python manage.py migrate'

To interact with the API:

Create a peak:
- send a JSON form with POST method with expected keys at http://<ip_of_docker_host>:8000/ . Expected keys:
  - title
  - altitude
  - lat
  - long

List all peaks:
- send a http request with a GET method at http://<ip_of_docker_host>:8000/

See a peak in particular:
- send a http request with a GET method precising the ID of the peak at http://<ip_of_docker_host>:8000/<peak_ID>/

Update a peak:
- send JSON form with PATCH/PUT method with expected keys and the ID of the peak you want to update at http://<ip_of_docker_host>:8000/<peak_ID>/update/

Delete a peak:
- send a http request with DELETE method and the ID of the peak at http://<ip_of_docker_host>:8000/<peak_ID>/delete/

Retrieve a list of peaks in a given geographical bounding box:
- send a JSON form with a POST method with the coordinates of the box as expected keys at http://<ip_of_docker_host>:8000/precise/ . Expected keys:
  - tleft (for the top left coordinates of the box in the form : "x:y")
  - tright (for the top right coordinates of the box in the form : "x:y")
  - bright (for the bottom right coordinates of the box in the form : "x:y")
  - bleft (for the bottom left coordinates of the box in the form : "x:y")
