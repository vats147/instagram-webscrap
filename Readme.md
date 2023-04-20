# Instagram Web Scraping Tool

This tool allows you to scrape data from your Instagram profile, which including your followers' usernames and their post count, followers, following. It uses the `selenium` package to automate interactions with the Instagram website.

## Installation

1. Download the appropriate version of the [Chrome WebDriver](https://chromedriver.chromium.org/downloads) for your operating system and browser version.

2. Add chromedriver path in `PATH` variable.

3. Clone the repository to your local machine:
   ```
   git clone https://github.com/vats147/instagram-webscrap.git
   ```

4. Install the required Python packages:
   ```
   pip install -r requirements.txt
   ```

## Usage

1. Replace your instagram `Username` and `password` in `scarp.py` file.

2. Run the `scrap.py` script:
   ```
   python scrap.py
   ```

   This will launch a Chrome browser window and navigate to the Instagram login page.

3. Once you are logged in, the script will scrape your followers' usernames and profile links, their post, their followers,their following  and save them to a  `result.csv`  file in the same directory.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

* The `selenium` package for Python: https://selenium-python.readthedocs.io/
* The Chrome WebDriver: https://chromedriver.chromium.org/
