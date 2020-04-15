from konlpy.tag import Mecab
from textblob.classifiers import NaiveBayesClassifier
import nltk

# pos_tagger = Mecab()

text = open('pos.txt', 'r' , encoding='UTF8')
text2 = open('nag.txt', 'r' , encoding='UTF8')
# while True:
#     line = text.readline()
#     if not line: break
#     print(line)
# text.close()
a = []
b = []
# while True:
#     line = text.readline()
#     line = line[:-1]

    
#     if not line:
#         break
#     elif line == "유명하":
#         a.append("('" +"유명하다" + "'," + "'긍정'"  + ")")
#     else:
#         a.append("('" + line + "'," '긍정)')
# text = open('./nag.txt', 'r')

# while True:
#     line = text.readline()
#     line = line[:-1]

    
#     if not line:
#         break
#     elif line == "불안":
#         b.append("('" +"불안증" + "'," + "'부정'"  + ")")
#     else:
#         b.append("('" + line + "'," '부정)')


while True:
    line = text.readline()
    line = line[:-1]
    if not line:
        break
        #a.append("('" +"유명하다" + "'," + "'긍정'"  + ")")
    else:
        d = (str(line), "긍정")
        a.append(d)


while True:
    line = text2.readline()
    line = line[:-1]
    if not line:
        break
    else:
        f = ((str(line), "부정"))
        b.append(f)
        
        
        
train = [
    ('사랑', '긍정')
]

train.extend(a)
train.extend(b)

test = [
    ('사랑', '긍정'),
    ('좋다', '부정'),
    ('안 좋아요.', '부정'),
    ('놀라워요!', '긍정'),
    ('친구', '긍정'),
    ('없다.', '부정')
]

# train_data = [(['/'.join(token) for token in pos_tagger.pos(sentence)],result) for [sentence, result] in train]


nltk.download('punkt')
cl = NaiveBayesClassifier(train)
cl.show_informative_features()
print(cl.accuracy(test))
