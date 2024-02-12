# FastAPI Application Deployment via GitHub Actions to Heroku

This repository contains a FastAPI application configured for automatic deployment to Heroku using Docker containers through GitHub Actions. The setup ensures seamless CI/CD workflows, allowing for automated testing and deployment with minimal manual intervention.

## Project Structure

```bash
Copy code
my_project/
├── app/
│   ├── __init__.py
│   ├── main.py
│   └── routers/
│       ├── items.py
│       ├── users.py
│       └── grimoire.py
├── .github/
│   └── workflows/
│       └── deploy_to_heroku.yml
├── Dockerfile
├── requirements.txt
└── README.md
```

- _app/_: Contains the FastAPI application code, including routers and the main app instance.
- _.github/workflows/deploy_to_heroku.yml_: Defines the GitHub Actions workflow for CI/CD.
- _Dockerfile_: Instructions for building the Docker image.
- _requirements.txt_: Lists the Python dependencies for the application.

## Docker Configuration

The _Dockerfile_ is set up to package the FastAPI application into a Docker container, making it ready for deployment to Heroku. Key considerations:

- Uses python:3.9-slim as the base image.
- Sets /app as the working directory within the container.
- Installs Python dependencies from requirements.txt.
- Copies the application code into the container.
- Starts the application using uvicorn with dynamic port binding to accommodate Heroku's $PORT.

## GitHub Actions CI/CD Workflow

- The CI/CD process is managed through a GitHub Actions workflow defined in .github/workflows/ci_cd.yml. The workflow automates the following steps:

- _Build_: Creates the Docker image based on the Dockerfile.
- _Test_: (Optional) Runs automated tests to ensure the application behaves as expected.
- _Deploy_:
  - Logs into Heroku Container Registry.
  - Pushes the Docker image to the Heroku Container Registry.
  - Releases the image on Heroku, updating the application.

## Deployment to Heroku

Deployment is handled automatically by the GitHub Actions workflow. To deploy manually or make changes:

1. Ensure you have the Heroku CLI installed and logged in.
2. Use heroku container:login to log in to the Heroku Container Registry.
3. Build and push the Docker image to Heroku using docker build and docker push.
4. Release the image on Heroku to update the application.

## Environment Variables

_HEROKU_API_KEY_: Your Heroku API key, stored as a GitHub secret for CI/CD.
_HEROKU_APP_NAME_: The name of your Heroku app, also stored as a GitHub secret.

## Managing Updates

To update the application:

1. Push changes to your GitHub repository.
2. The GitHub Actions workflow will automatically trigger, running through the build, test, and deploy steps.
3. Monitor the Actions tab in GitHub for the status of your CI/CD pipeline.

## Local Development

For local development:

1. Ensure Docker is installed and running.
2. Build the Docker image: docker build -t my_fastapi_app .
3. Run the container: docker run -p 8000:80 my_fastapi_app
4. Adjust port mappings and image names as necessary for your setup.

##Additional Notes
Review the Dockerfile and GitHub Actions workflow to ensure they meet your project's needs.
Modify the .env file or set environment variables in Heroku for any application-specific configuration.
