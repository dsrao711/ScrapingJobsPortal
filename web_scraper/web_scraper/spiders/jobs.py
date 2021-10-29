import scrapy
from ..items import WebScraperItem

class JobsSpider(scrapy.Spider):
    name = 'jobs'
    start_urls = ['https://in.indeed.com/jobs?q=software%20developer&l&vjk=8a1af5307c18bdec']

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
            
            yield {
                "company_name": company_name , 
                "location": location ,
                "salary" : salary ,
                "description": description
            }