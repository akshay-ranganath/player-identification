import json
import requests
import os
from pathlib import Path
from datetime import datetime


def download_image(url):
    """
    Download an image from a URL and store it in the current directory.

    Args:
        url (str): The URL of the image to download

    Returns:
        str: Path to the downloaded image file
    """
    try:
        # Download the image
        response = requests.get(url, timeout=30)
        response.raise_for_status()

        # Get file extension from URL or default to .jpg
        url_path = Path(url)
        extension = url_path.suffix if url_path.suffix else '.jpg'

        # Create a temporary filename with timestamp in current directory
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        temp_filename = f"temp_image_{timestamp}{extension}"
        temp_filepath = os.path.join(os.getcwd(), temp_filename)

        # Write image to file
        with open(temp_filepath, 'wb') as f:
            f.write(response.content)

        print(f"Image downloaded successfully to: {temp_filepath}")
        return temp_filepath

    except requests.exceptions.RequestException as e:
        print(f"Error downloading image: {e}")
        return None


def load_player_data(json_path='cfl_players.json'):
    """
    Load CFL player data from JSON file.

    Args:
        json_path (str): Path to the JSON file

    Returns:
        dict: Player data organized by team -> number -> player name(s)
    """
    try:
        with open(json_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        print(f"Loaded player data for {len(data)} teams")
        return data
    except FileNotFoundError:
        print(f"Error: {json_path} not found")
        return {}
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON: {e}")
        return {}


def main():
    # Load player data
    player_data = load_player_data()

    if not player_data:
        print("Failed to load player data. Exiting.")
        return

    # Get URL from user input
    image_url = input("Enter image URL: ")

    # Download and save the image
    temp_image_path = download_image(image_url)

    if temp_image_path:
        print(f"Temporary image path: {temp_image_path}")
        # Add your image processing logic here
        # player_data is available for player identification
    else:
        print("Failed to download image")


if __name__ == "__main__":
    main()
