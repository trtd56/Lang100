import MeCab

tagger = MeCab.Tagger("-Ochasen")

with open('neko.txt', 'r') as f:
    most_long = ''
    for line in f:
        line = line.replace('\n', '')
        text_elem = tagger.parse(line)
        words_info = text_elem.split('\n')
        words_info = [w for w in words_info if w not in ['EOS', '']]
        renzoku = ''
        for w_info in words_info:
            word, _, _, pos, _, _ = w_info.split('\t')
            pos = pos.split('-')[0]
            if pos == '名詞':
                renzoku += word
            else:
                if len(renzoku) >= len(most_long):
                    most_long = renzoku
                renzoku = ''
    print(most_long)
