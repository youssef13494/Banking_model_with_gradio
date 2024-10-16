# Use the official Python image from the Docker Hub
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt .

RUN pip install -r requirements.txt

# Copy the rest of the application code to the container
COPY . .
COPY model_pipeline.pkl .
# Expose the port that Gradio will use
EXPOSE 7860

# Set the command to run the Gradio app
CMD ["python", "/app/app.py"]