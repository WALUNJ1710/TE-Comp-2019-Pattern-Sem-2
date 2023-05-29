from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
  
document_A = "Jupiter is the largest Planet"
document_B = "Mars is the fourth planet from the Sun"

def stop_word(sentence):
    stop_words = set(stopwords.words('english'))
    word_tokens = word_tokenize(sentence)
    filtered_sentence = [w for w in word_tokens if not w.lower() in stop_words]
    filtered_sentence = []

    for w in word_tokens:
        if w not in stop_words:
            filtered_sentence.append(w)
            
    print(filtered_sentence)
    
stop_word(document_A)
stop_word(document_B)
