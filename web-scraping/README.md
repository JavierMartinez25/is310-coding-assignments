# Terms of Service and robots.txt

Before starting this project, I checked the website’s robots.txt file and reviewed the site information before scraping the page.

Terraria Wiki robots.txt:  
https://terraria.fandom.com/robots.txt

I used the Weapons page for this project:  
https://terraria.fandom.com/wiki/Weapons

For this assignment, I only collected a small amount of publicly visible data from one page.

# Choice of Wiki and Data Collected

I chose the Terraria Wiki because I wanted to do something related to gaming, and Terraria is one of my favorite games. I picked the Weapons page because it is a simple page with many useful links and it shows how the wiki organizes information about one of the most important parts of the game.

For this project, I scraped weapon names and their corresponding links from the Weapons page. I focused on weapons because they are a major part of Terraria’s progression and gameplay, and they are clearly organized on the wiki.

This type of data could be useful to researchers because it shows how fan communities organize game information in a structured way. It also helps show how pages connect related topics and how knowledge is presented for players and readers.

# Code Used

I used the `cloudscraper` library to request the webpage and the `BeautifulSoup` library to parse the HTML and extract the data.

# Data Output

The scraped data was saved as a CSV file (`terraria_weapons_links.csv`) in the `web-scraping` directory. This format makes the data easy to read and analyze.