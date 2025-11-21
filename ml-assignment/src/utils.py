
import re
from collections import defaultdict

# Function to create nested defaultdicts of arbitrary depth
def make_dict(n=3):
    if n == 1:
        return defaultdict(int)
    else:
        return defaultdict(lambda: make_dict(n-1))

def preprocess(text,endtoken= "__END__"):
    
    # Remove URLs
    text = re.sub(r'http\S+|www\S+|https\S+', '', text)

    # Replace multiple dots "......" with a single  " "
    text = re.sub(r'\.{2,}', ' ', text)

    # # text = re.sub(r"\.(\s+)", r"." + endtoken + r" \1", text)
    text = re.sub(r"(\n)", r"\1" + endtoken +" ",text)

    # Replace multiple spaces with single space
    text = re.sub(r'\s+', ' ', text)
    text = text.lower()

    return text.strip()





def getcounts(words,n,counts,context_counts):
    
    for i in range(len(words) - n + 1):
        ngram = tuple(words[i:i+n])
        context = ngram[:-1]
        if ngram in counts.keys():
            counts[context][ngram[-1]]+=1
        else:
            counts[context][ngram[-1]] = 1
        if context in context_counts.keys():
            context_counts[context]+=1      
        else:
            context_counts[context]=1   
        
    # print(counts)
    # print(context_counts)
