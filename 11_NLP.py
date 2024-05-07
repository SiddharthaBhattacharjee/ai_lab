import re
import inflect
import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer

# Download necessary NLTK data
nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

# Initialize objects
p = inflect.engine()
ps = PorterStemmer()
lemmatizer = WordNetLemmatizer()
stop_words = set(stopwords.words('english'))

def preprocess_text(input_str):
    # Lowercase the text
    input_str = input_str.lower()
    
    # Remove numbers or convert them to text
    input_str = re.sub(r'\d+', '', input_str)  # Remove numbers
    # input_str = ' '.join([p.number_to_words(i) if i.isdigit() else i for i in input_str.split()])  # Convert numbers to words
    
    # Remove punctuation
    input_str = re.sub(r'[^\w\s]', '', input_str)
    
    # Remove whitespace
    input_str = ' '.join(input_str.split())
    
    # Remove stopwords
    tokens = nltk.word_tokenize(input_str)
    filtered_tokens = [word for word in tokens if not word in stop_words]
    
    # Stemming
    stemmed_tokens = [ps.stem(word) for word in filtered_tokens]
    
    # Lemmatization
    lemmatized_tokens = [lemmatizer.lemmatize(word, pos='v') for word in filtered_tokens]
    
    return {
        'filtered': filtered_tokens,
        'stemmed': stemmed_tokens,
        'lemmatized': lemmatized_tokens
    }

# Example usage
input_string = "Hey, did you know that the summer break is coming? Amazing right !! It's only 5 more days !!"
preprocessed_data = preprocess_text(input_string)

print("Filtered Tokens:", preprocessed_data['filtered'])
print("Stemmed Tokens:", preprocessed_data['stemmed'])
print("Lemmatized Tokens:", preprocessed_data['lemmatized'])
