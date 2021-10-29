import scrapy
from ..items import WebScraperItem

class JobsSpider(scrapy.Spider):
    
    name = 'jobs'
    page_number = 2
    
    def __init__(self, job_title, **kwargs):
        # Input from user for designation
        self.job_title = job_title
        self.start_urls = ["https://in.indeed.com/jobs?q={}&start={}".format(
            job_title.lower().rstrip().replace(" ", "-"), i*10) for i in range(0, 20)]
        super().__init__(**kwargs)

    def parse(self, response):
        
        jobs = response.css("div.slider_container")
        items = WebScraperItem()
        print(len(jobs))
        
        for job in jobs:
            
            company_name =  job.css("div.heading6.company_location.tapItem-gutter").css("span.companyName::text").get()
            location =  job.css("div.heading6.company_location.tapItem-gutter").css("div.companyLocation::text").get()
            salary = job.css("div.heading6.tapItem-gutter.metadataContainer").css("div.salary-snippet").css("span::text").get() 
            description = job.css("div.heading6.tapItem-gutter.result-footer").css("div.job-snippet").css("ul").css("li::text").getall()
            
            # Sending to Items container
            
            items['company_name'] = company_name
            items['location'] = location
            items['salary'] = salary
            items['description'] = description
            
            yield items
            
        next_page = 'https://in.indeed.com/jobs?q=software%20developer&start=' + str((JobsSpider.page_number)*10) +'&vjk=ff3041e9314624a9'
        
        # Scraping 20 pages
        
        if JobsSpider.page_number <= 19:
            JobsSpider.page_number += 1
            print("Page number ..." , JobsSpider.page_number)
            yield response.follow(next_page , callback = self.parse)