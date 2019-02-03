import MeCab

tagger = MeCab.Tagger("-Ochasen")

with open('neko.txt', 'r') as f:
    for line in f:
        line = line.replace('\n', '')
        text_elem = tagger.parse(line)
        words_info = text_elem.split('\n')
        words_info = [w for w in words_info if w not in ['EOS', '']]
        plt_words = []
        for w_info in words_info:
            word, _, _, pos, _, _ = w_info.split('\t')
            pos = pos.split('-')[0]
            if pos == '名詞' and len(plt_words) == 0:
                plt_words.append(word)
                continue
            elif word == 'の' and len(plt_words) == 1:
                plt_words.append(word)
                continue
            elif pos == '名詞' and len(plt_words) == 2:
                plt_words.append(word)
                print(''.join(plt_words))
            plt_words = []
