# Proxies-Generator
Crawls kuaidaili.com to gain a list of non-mainland anonymous proxy addresses to be used for web-scraping

# Function

Crawls the first 1000 pages on http://www.kuaidaili.com/free/outha/, which are all anonymous proxy ip address outside of mainland China. The script validates each ip address by making a request to www.baidu.com and those who recieve response in five seconds would be saved in to the text file. 

# Update 1.11
Tested to be able to crawl

## Future
1. Might need to change the format of saving for eaiser future uses on other web-scraping project. 
2. Might also be useful to record the response time of each address.
3. Might also need to seperate out the validate function, and create more data-collecting method to collect from other proxy-provider websites.
