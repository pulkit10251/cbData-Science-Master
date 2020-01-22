from nltk.tokenize import RegexpTokenizer
from nltk.stem import PorterStemmer
from nltk.corpus import stopwords
import sys

tokenizer=RegexpTokenizer(r'\w+')
ps=PorterStemmer()
en_stopwords=set(stopwords.words('English'))


sample_text="""I loved this movie since I was 7 and I saw it on the opening day. It was so touching and beautiful. I strongly recommend seeing for all. It's a movie to watch with your family by far.<br /><br />My MPAA rating: PG-13 for thematic elements, prolonged scenes of disastor, nudity/sexuality and some language."""

def get_cleanedreview(review):
    review=review.lower()
    review=review.replace("<br /><br />"," ")
    tokens=tokenizer.tokenize(review)
    new_tokens=[token for token in tokens if token not in en_stopwords]
    stemmed_token=[ps.stem(token) for token in new_tokens]
    
    cleaned_review=' '.join(stemmed_token)
    
    return cleaned_review


    
    