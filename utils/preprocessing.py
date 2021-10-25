import re
import spacy
import string

nlp = spacy.load('en_core_web_md')

def preprocess_text(text):
    """
    Apply a simple preprocessing to a string.

    Parameters
    ----------

    text: str.
        String to preprocess

    Returns
    -------
    Preprocessed string.
    """

    text = text.lower()                            # Convert to lowercase
    
    text = re.sub('http\S+', '', text)             # Remove urls
    text = re.sub('[\t\n\r\x0b\x0c]', '', text)    # Remove whitespaces
    
    # text = re.sub('#\w+', '', text)                # Remove hashtags
    # text = re.sub('@\w+', '', text)                # Remove usernames
    
    # Simplify repeated punctuation symbols that appear more than 2 times,
    # for example, "whats up??!!!!!" -> "whats up?!"
    for punctuation in string.punctuation.replace('\\', ''):
        pattern = f'\\{punctuation}{{2,}}'
        text = re.sub(pattern, punctuation, text)
    
    # Remove leading and trailing whitespaces
    text = text.strip()
    
    return text