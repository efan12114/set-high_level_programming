#!/usr/bin/python3
"""
Sentiment Analysis Tool
Analyzes the sentiment of a given sentence using a public API.
"""
import os
import sys
import requests
API_URL = "https://text-processing.com/api/sentiment/"
def analyze_sentiment(text):
    """Analyze the sentiment of the provided text."""
    api_key = os.getenv("TEXT_PROCESSING_API_KEY")

    if not api_key:
        print(
            "Error: TEXT_PROCESSING_API_KEY environment variable is not set.",
            file=sys.stderr
        )
        return None

    headers = {
        "Authorization": f"Bearer {api_key}"
    }

    payload = {"text": text}

    try:
        response = requests.post(
            API_URL,
            data=payload,
            headers=headers
        )
        response.raise_for_status()

        data = response.json()
        label = data.get("label", "neutral")

        if label == "pos":
            return "positive"
        elif label == "neg":
            return "negative"
        else:
            return "neutral"

    except requests.exceptions.Timeout as e:
        print(f"Request timed out: {e}", file=sys.stderr)
        return None

    except requests.exceptions.ConnectionError as e:
        print(f"Connection error: {e}", file=sys.stderr)
        return None

    except requests.exceptions.HTTPError as e:
        print(f"HTTP Error: {e}", file=sys.stderr)
        return None

    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}", file=sys.stderr)
        return None

    except ValueError as e:
        print(f"Invalid response format: {e}", file=sys.stderr)
        return None

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: ./sentiment_analyzer.py <sentence>")
        sys.exit(1)

    sentence = " ".join(sys.argv[1:])
    result = analyze_sentiment(sentence)

    if result:
        print(result)
    else:
        sys.exit(1)