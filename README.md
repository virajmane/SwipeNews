# News Scraper Web App

## Overview
This is a web application built using Flask that fetches and displays news articles from [inshorts](https://www.inshorts.com/). The app allows users to view news articles and record their preferences through left and right swipes.

**Note: This project is still incomplete and under development.**

## Features
- Fetches news articles from various categories.
- Displays news articles with images, titles, and content.
- Allows users to swipe left, right, or up to express their preferences.
- Records user preferences through AJAX requests to the server.

## Screenshots
![image](https://github.com/virajmane/SwipeNews/assets/62030782/b0142edb-f0ae-4773-a19c-929df43fa623)
*Caption for Screenshot 1*

![image](https://github.com/virajmane/SwipeNews/assets/62030782/bd58994c-d6aa-4fa8-ba84-6f4c180990b0)
*Caption for Screenshot 2*

## Setup
1. Install the required dependencies by running:
    ```bash
    pip install -r requirements.txt
    ```

2. Run the Flask application:
    ```bash
    python app.py
    ```

3. Open your web browser and navigate to `http://localhost:5000` to view the app.

## Project Structure
- `app.py`: Flask application file.
- `newsscrapper.py`: Module for scraping news from inshorts.
- `templates/`: HTML templates for the web app.
- `screenshots/`: Folder containing screenshots of the app.

## Dependencies
- Flask
- requests
- BeautifulSoup (bs4)

## Acknowledgments
This project uses data from [inshorts](https://www.inshorts.com/), and its purpose is for educational and learning purposes only.

## TODO
- [ ] Implement user authentication.
- [ ] Add database to store user preferences.
- [ ] Enhance the user interface.
- [ ] Improve error handling and logging.

## Contributing
Contributions are welcome! Feel free to open issues or pull requests.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
