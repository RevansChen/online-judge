# Python - 3.6.0

spin_words = lambda sentence: ' '.join([word[::-1] if len(word) >= 5 else word for word in sentence.split(' ')])
