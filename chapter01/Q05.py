import functools

Text = "I am an NLPer"

def n_gram(text, n, preprocess):
    words = preprocess(text)
    return [tuple(words[i:i+n]) for i in range(0,len(words)) if i < (len(words)-1)]

def text2word(text):
    return text.split()

def text2char(text):
    return text

word_n_gram = functools.partial(n_gram, preprocess=text2word)
char_n_gram = functools.partial(n_gram, preprocess=text2char)


if __name__=="__main__":
    print(word_n_gram(Text,2))
    print(char_n_gram(Text,2))
