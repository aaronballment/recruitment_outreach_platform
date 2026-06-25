import re
import config
import tldextract

def clean_company_name(name: str) -> str:
    '''
    Returns a cleaned version of the company name.
    
    Parameters:
    - Name (str): Uncleaned company name 
    
    Returns:
    - Str: Cleaned company name
    '''
    if not isinstance(name, str):
        return ''
    
    clean_name = name.strip()
    
    suffix_patterns = r'\b(pty\b\.?|ltd\b\.?|limited\b\.?|inc\b\.?)\b'
    clean_name = re.sub(suffix_patterns, '', clean_name, flags=re.IGNORECASE)
    
    clean_name = re.sub(r'\S+"', " ", clean_name).strip(" ,.-")
    
    return clean_name.title()


def get_first_name(full_name: str) -> str:
    '''
    Returns the persons first name
    
    Preconditions: 
    - full_name is a non-empty string
    - every name is seperated by 1 space
    
    Returns:
    - str: person's first name
    '''
    
    names = full_name.strip().split()
    
    return names[0].title()


def normalise_url(url: str) -> str:
    '''
    Returns the domain from a website url.
    
    Preconditions: url should be a non-empty string and a valid url.
    
    Parameters:
    - url (str): company website url
    
    Returns:
    - str: domain from URL.
    
    >>> normalise_url('https://portal.apexbrokers.com.au/dashboard')
    'apexbrokers.com.au'
    
    >>> normalise_url('staging.lendingfirm.com')
    'lendingfirm.com'
    
    >>> normalise_url('au.marketingagency.sydney')
    'marketingagency.sydney'
    
    >>> normalise_url(' ')
    ''
    
    >>> normalise_url('https://app.summer.optiver.net.au/offer')
    'optiver.net.au'
    
    '''
    
    if not isinstance(url, str) or '.' not in url:
        return ''
    
    extracted = tldextract.extract(url.strip().lower())
    
    if not extracted.domain or not extracted.suffix:
        return ''
    
    return f'{extracted.domain}.{extracted.suffix}'
    

def normalise_job_location(job_location: str) -> str:
    '''
    Returns a cleaned job_location variable.
    
    Parameters:
    - job_location (str): the raw location for the advertised job.
    
    Returns:
    - str: cleaned job_location
    
    >>> normalise_job_location('Maroochydore, Queensland, Australia')
    'Maroochydore'
    
    >>> normalise_job_location('Brisbane')
    'Brisbane'
    
    >>> normalise_job_location('')
    ''
    
    >>> normalise_job_location(' ')
    ''
    
    >>> normalise_job_location('10')
    ''
    
    '''
    if not isinstance(job_location, str) or not job_location.strip() or (
        job_location.isdigit()):
        return ''
    
    return job_location.split(',')[0]


def job_posting(job_title: str, job_location: str='') -> str:
    '''
    Returns the job_posting variable "<job_title> in <job_location>".
    
    If no location is specified, it will just return <job_title>.
    
    Parameters:
    - job_title (str): Job title posted in job ad.
    - job_location (str): location of the job ad.
    
    Returns:
    - str: job posting variable
    '''
    
    if not job_location:
        return job_title
    
    return f'{job_title} in {job_location}'


def recruiter_keyword_check(name: str) -> bool:
    '''
    Returns True if <name> contains recruitment keywords.
    
    Parameters:
    - name (str): Company name or Domain.
    
    Returns:
    - bool: True if flagged as recruiter and False if not.
    
    >>> recruiter_keyword_check('XYZ recruitment')
    True
    
    >>> recruiter_keyword_check('recruitmentxyz.com.au')
    True
    
    >>> recruiter_keyword_check('')
    False
    
    >>> recruiter_keyword_check('hero roofing')
    False
    '''
    
    if not isinstance(name, str) or not name.strip():
        return False
    
    if '.' in name:
        pattern = r"(recruitment|staffing|talent|recruiting|executive search)"
        
    else:
        pattern = r"\b(recruitment|staffing|talent|recruiting|executive search)\b"
    
    return bool(re.search(pattern, name.lower()))
    
    
def is_blacklisted(domain: str) -> bool:
    '''
    Returns True if the domain is blacklisted.
    
    Parameters:
    - domain (str): the domain being checked
    
    Returns:
    - bool: True if blacklisted, False if not.
    
    >>> config.BLACKLIST = {"abc.com", "xyz.com.au"}
    
    >>> is_blacklisted('abc.com')
    True
    
    >>> is_blacklisted('abc.com.au')
    False
    
    >>> is_blacklisted('')
    False
    '''
    
    BLACKLIST = config.BLACKLIST
    
    return bool(domain in BLACKLIST)


def is_title_invalid(job_title: str) -> bool:
    '''
    Returns True if <job_title> is a invalid title.
    
    Parameters:
    - job_title (str): unchecked job title.
    
    Returns:
    - bool: True if invalid, False if not.
    
    >>> config.VALID_TITLES = {"sales"}
    
    >>> config.INVALID_TITLES = {"retail", "real estate"}
    
    >>> is_title_invalid('retail sales manager')
    True
    
    >>> is_title_invalid('sales representative')
    False
    
    >>> is_title_invalid('')
    False
    '''
    
    VALID_TITLES = config.VALID_TITLES
    
    INVALID_TITLES = config.INVALID_TITLES
    
    if not isinstance(job_title, str) or not job_title.strip():
        return False
    
    clean_title = job_title.lower()
    
    for invalid in INVALID_TITLES:
        if re.search(fr'\b{invalid}\b', clean_title):
            return True
        
    for valid in VALID_TITLES:
        if re.search(fr'\b{valid}\b', clean_title):
            return False
    
    return True
            
def qualification(job_title: str, company_name: str, domain: str) -> bool:
    '''
    Returns True if the company pass all qualification steps.
    
    Preconditions: ALL parameters are non empty strings.
    
    Parameters:
    - job_title (str): job title in job ad.
    - company_name (str): company name to be checked for recruimtent keywords
    - domain (str): domain to be checked in blacklist and recruitment keywords
    
    Returns:
    - bool: True if passes all qualifications, False if not
    
    >>> qualification('sales manager', 'recruitmentxyz', 'recruitmentxyz.com')
    False
    
    >>> qualification('sales manager', 'abcfinance', 'abcfinance.com')
    True
    '''
    
    return not (
        recruiter_keyword_check(company_name) or 
        recruiter_keyword_check(domain) or
        is_blacklisted(domain) or 
        is_title_invalid(job_title)
    )
    
def non_empty(job_title: str, company_name: str, domain: str, job_ad_url: str
              ) -> bool:  
    '''
    Returns True if all required fields and non-empty strings.
    
    Parameters:
    job_title (str): job title related to job ad
    company_name (str): name of the company advertising
    domain (str): domain associated with advertising company
    job_ad_url (str): the link to the job ad
    '''
    
    return bool(
        isinstance(job_title, str) and job_title.strip() and
        isinstance(company_name, str) and company_name.strip() and
        isinstance(domain, str) and domain.strip() and
        isinstance(job_ad_url, str) and job_ad_url.strip()
    )
    

#-----Testing:
if __name__ == '__main__':
    
    import doctest
    doctest.testmod(verbose=True)