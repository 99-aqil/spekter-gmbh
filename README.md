# Sentiment Analysis API

The Sentiment Analysis API is a web application that allows users to analyze the sentiment of text input. It leverages a pre-trained machine learning model to determine whether the sentiment is positive, negative, or neutral. This API provides a simple interface to integrate sentiment analysis capabilities into your applications.

## API Endpoints

### Analyze Sentiment

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

## Usage Example

### Request

```http
POST /analyze/ HTTP/1.1
Content-Type: application/json

{
    "text": "I loved the spiderman movie!"
}
