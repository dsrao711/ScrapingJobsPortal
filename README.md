## Scraping Jobs Portal (Indeed)

<br>

- Web scraping using Scrapy
- Follow these steps 👇

<br>

### Setup and Installation:
<hr>

```
# Create virtual environment

cd ScrapingJobsPortal
py -m venv env
env\Scripts\activate
pip install -r requirements.txt

```
<br>

### Steps to run
<hr>

Enter your desired designation as input for job_title 
Considering designation of web developer

```

scrapy crawl jobs -a jobs_title=web+developer -O output.csv

```