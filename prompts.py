#Web Search Prompts
def domain_search(company_name: str, job_ad: str='') -> str:
    '''
    Prompt to find company domain. 
    
    ONLY for use with web_search()
    '''
    
    return (
        f''' Your task at hand is to analyse the provided company name and find out the official website associated with the same on search engine, verify it with the company name and get back to me with the final official company website URL for the same. 

herein below is the inputs provided:

COMPANY NAME: {company_name}
JOB AD FROM COMPANY: {job_ad}

steps to achieve the goal inputted:

1. search for "{company_name} official website" on google or any other search engine.
2. scan and pay deep attention to the top few results, go to their webpage to see if you find {company_name} resonance in the webpage.
3. next analyse the content of the page confirmed to see if it matches the company Name and the company details on the job ad.
4. output the website or domain of company.

ENSURE TO ONLY AND ONLY OUTPUT THE COMPANY WEBSITE OR COMPANY DOMAIN and nothing else. no double quotes, extra characters or symbols that doesn't represent a website URL, no additional text, etc.

ENSURE THAT if the following domain names are being the final output to try best to find another official website which best represents the company instead, they are:
business.gov.au
linktr.ee
seek.com.au
linkedin.com

THE FOLLOWING 4 DOMAINS PASTED ABOVE are not to be provided as output as per your research. your goal is to find the domain name of the company that is the best representation, if not found output N/A
'''
)
    
def recruiter_detection(domain: str, company_name:str) -> str:
    '''
    Prompt to determine if the company is a recruiter or not.
    
    ONLY for use with web_search()
    '''
    
    return (f'''#CONTEXT#
You need to verify whether the company, {company_name}, offers recruitment services or acts as a recruiter, focusing only on the information available on their own website.

#OBJECTIVE#
Search on google for 'site:{domain}' and determine if {company_name} is a recruiter or offers recruitment services. Output "All Clear" if they do NOT offer recruitment services. Output "Recruitment" if they do.

#INSTRUCTIONS#
1. Execute a search using the query 'site:{domain}' to find the company website.
2. Review the homepage, "about us," and "our services" pages for any mention of recruitment, staffing, talent acquisition, or similar services.
3. Ignore any mention of internal HR or recruitment teams - focus only on services provided to external clients.
4. Do not check any other websites or external sources.
5. If the company offers recruitment services *for other businesses*, output "Recruitment".
6. If there is no evidence of recruitment services, output "All Clear".

**Do not include businesses that are hiring for themselves or looking for people for their own business.**

#EXAMPLES#
Example input:
Domain: https://examplecompany.com
Company Name: Example Company

Example output:
All Clear

Example input:
Domain: https://recruitmentfirm.com
Company Name: Recruitment Firm
Example output:
Recruitment
'''
    )

#Generate Content Prompts
def job_title_clean(job_title: str) -> str:
    '''
    Prompt to clean the job_title.
    
    ONLY for use with generate_content()
    '''
    return (f'''Your task is to clean a Job title so it can be used in a cold email.

Use the following job title for your task:

Job Title: {job_title}

Your task is to output only the job title and remove all the extra and irrelevant names in the title. 

We want the raw job title found within the input.

You should do the following:
- remove all symbols and ensure that there is only the relevant job title left. 
- remove all locations and company names from the job title.
- remove words like "Experienced", "Qualified" or any filler words that aren't relevant to the job title.

I have some examples for you below. Note the words in quotations before the word "becomes" is the input and your output should be the words in quotations after the word "becomes".

Examples are as follows:
1. "b2b sales executive" becomes "sales executives"
2. "Sales Representative, Enterprise sales" becomes "sales representative"
3. "Manager, Business Development" becomes "business development manager"
4. "Manager, strategic partnerships" becomes "manager for strategic partnerships"
5. "Membership Sales Consultant" becomes "sales consultant"
6. "business development key account manager" becomes "account manager"
7. "conference and events sales manager" becomes "sales manager"
8. "account manager agronomy" becomes "account manager"
9. "commercial fuel account manager" becomes "account manager"
10. "major account sales executive" becomes "sales executive"
11. "inside sales representative" becomes "sales representative"
12. "travelling territory sales representative" becomes "sales representative"

Output the fixed job title and the fixed job title only. 

Do not include any quotation marks in your output.

Make all words lower-case.

Ensure your answer is 110% correct. 

There is no room for error. Think through your answers carefully and thoroughly.
'''
)