# Charan
Title : - First web scraping project

Pre- requisites :-
 - Create a Virtual Environment
 - Install Scrapy thorugh Anaconda prompt with command 'conda install scrapy'
 
 IDE used :- Visual Studio Code
 
 Frame work used :- Scrapy
 
 Project Breakdown :-
 * Opened a folder from VS code in which a virtual environment is created so that all the installed packages and frameworks are isolated      into this particular folder and doesn't intervene with future python projects
 *In the same folder created a project named quotetutorial using Scrapy command 'scrapy startproject quotetutorial
 *The quotetutorial project gets created with inbuilt python files created by scrapy 
 *This path 'Charan/quotetutorial/quotetutorial/spiders/' contains the 'quotes_spider.py' python file ,which is the spider that crawls the data from a URL
 * Charan/quotetutorial/quotetutorial/ this path contains the items.py file ,which is the container of the items that are crawled from the given urls ,an instance/object of this class is called in the spider file that extracts the data
 * Charan/quotetutorial/ this path contains the 'items.csv' file that has all the data that has been crawled from the website .
 
 

