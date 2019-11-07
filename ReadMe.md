# Get Lyrics

This is a very simple python project where I scrape google search results for lyrics. The program will prompt the user for the name of a song and the name of an artist or group. The program will then conduct a google search using the selenium chrome driver. This is a demo of a simple use case of Selenium and BeatifulSoup.

## Instructions

You can run this either directly or as a module. To run directly, run this command in your shell: 

```bash
cd path/to/project # make sure you are inside the project directory
python main.py
```

To run as a module, perform the following:
```bash
python -m GetLyrics   # make sure you're not inside the project directory
```

Your shell should return plain, unformatted text of the lyrics to your song. If there the scraper cannot find the song on Google, then the program will merely return text indicating that the song was not found and that you should search for another song.