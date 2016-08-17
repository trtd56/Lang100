import random

Text = "I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."

sp_text = Text.split()

def replace_middle(word):
    m_word = word[1:len(word)-1]
    m_word = "".join(random.sample(m_word,len(m_word)))
    return word[0] + m_word + word[-1]

print(" ".join([replace_middle(i) if len(i) > 4 else i for i in sp_text]))
