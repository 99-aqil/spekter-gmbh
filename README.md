# Sentiment Analysis API Documentation

## Introduction

The Sentiment Analysis API is a web application that allows users to analyze the sentiment of text input. It leverages a pre-trained machine learning model to determine whether the sentiment is positive, negative, or neutral. This documentation provides an overview of the project's architecture, API endpoints, usage examples, installation instructions, and customization options.

## Table of Contents

- [Architecture](#architecture)
- [API Endpoints](#api-endpoints)
- [Usage Examples](#usage-examples)
- [Handling Errors](#handling-errors)
- [Installation](#installation)
- [Customization](#customization)
- [Conclusion](#conclusion)

## Architecture

The Sentiment Analysis API is built using the Django framework, which follows the Model-View-Controller (MVC) architectural pattern. The project structure consists of the following components:

- **Models**: The application does not have any custom models as it mainly focuses on integrating a pre-trained sentiment analysis model.
- **Views**: Contains the logic for handling HTTP requests, processing input, and generating responses.
- **Templates**: Holds HTML templates for rendering frontend views.
- **URLs**: Defines the routing configuration for different endpoints.
- **Static Files**: Stores static assets such as CSS and JavaScript files.

The API integrates a pre-trained sentiment analysis model from the "setfit" library to perform sentiment analysis on the input text.

## API Endpoints

### Analyze Endpoint

- **Endpoint**: `/analyze/`
- **Method**: POST
- **Request Payload**:
  - JSON object with the following structure:
    ```json
    {
        "text": "Text to be analyzed"
    }
    ```
- **Response**:
  - JSON object with the following structure:
    ```json
    {
        "sentiment": "positive/negative/neutral"
    }
    ```

## Usage Examples

Here are a few examples to demonstrate how to use the Sentiment Analysis API:

### Analyzing Sentiment

**Request:**

```http
POST /analyze/ HTTP/1.1
Content-Type: application/json

{
    "text": "I loved the spiderman movie!"
}
```

**Response:**

```http
HTTP/1.1 200 OK
Content-Type: application/json

{
    "sentiment": "positive"
}
```

## Handling Errors

If there is an error during the analysis process or if the request payload is invalid, the API will respond with an appropriate error message.

**Request:**

```http
POST /analyze/ HTTP/1.1
Content-Type: application/json

{
    "text": ""
}
```

**Response:**

```http
HTTP/1.1 400 Bad Request
Content-Type: application/json

{
    "error": "Empty text provided"
}
```
