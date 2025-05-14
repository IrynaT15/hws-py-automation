# Flask Cat App
<img src="cat.png" >

## Project Structure
- flask-app
  -- app.py
  -- requirements.txt
  -- templates
    --index.html
  -- Dockerfile

## How to Build and Run
1. Download and install Docker Desktop: 
   https://www.docker.com/products/docker-desktop

2. Build the Docker Image:
   docker build -t flask_cat_app .

3. Run the Container:
   docker run -p 8866:5001 --name flask_cat_app flask_cat_app

4. Open your browser and go to:
   http://localhost:8866

