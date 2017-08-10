from nltk import word_tokenize
from nltk import Text
import nltk

nltk.path.append('/home/yuangang/nltk_data/')
tokens= word_tokenize("Here is some not very interesting text")
text = Text(tokens)
