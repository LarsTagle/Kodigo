import re

def clean_text(text):
    url_pattern = re.compile(r'https?://\S+')
    text = url_pattern.sub('', text)
    
    text = re.sub('[^.,a-zA-Z0-9 \n\/."“”()\'-]', '', text)
    
    text = text.replace('\n\n', '. ')
    text = text.replace('..', '. ')
    text = text.replace('\n', ' ')
    text = text.replace('   ', ' ')
    text = text.replace('  ', ' ')
    text = text.replace(' o ', ' ')
    
    return text