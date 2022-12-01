def predict(inp):
    import pandas as pd
    import numpy as np
    import os
    import time
    import tensorflow
    from tensorflow.keras.preprocessing.sequence import pad_sequences
    from tensorflow.keras.layers import Embedding, LSTM, Dense, Dropout, Bidirectional
    from tensorflow.keras.preprocessing.text import Tokenizer
    from tensorflow.keras.models import Sequential
    from tensorflow.keras.optimizers import Adam
    ### YOUR CODE HERE
    from tensorflow.keras.regularizers import Regularizer
    # Figure out how to import regularizers
    import tensorflow.keras.utils as ku 
    from keras.models import load_model

    #The dataset (P.S. Look, it is TSV)
    data=pd.read_csv('model/angry.csv')
    # removing null values to avoid errors 
    data.dropna(inplace = True) 
    # converting to string data type
    data["Title"]= data["Title"].astype(str)
    # slicing till 2nd last element
    data["lyric"]= data["Title"].str.slice(10,)

    data.lyric.drop_duplicates().tolist()

    IND = data.lyric.drop_duplicates().tolist()
    #Move in the index range
    CHORUSES=[]
    for i in IND:
        CHORUSES.append(data.lyric.tolist())

    CHORUSES=np.array(data.lyric.tolist())
    CHORUSES=CHORUSES.tolist()
    #Write everything in a single line 
    TERM=''
    for c in range(len(CHORUSES)):
        
        TERM= TERM+ CHORUSES[c]+ ' \n '
    

    to_remove = ['[', '\\', ']', '_', '{', '}','~', '§', '…','≡', '了', '人', '作', '制', '卐', '我', '朝', '王', '语', '\ufeff','(', ')','*', '（', '）', '‘', '’', '′', '＇', "'", "'", '.']
    for symbol in to_remove:
        TERM = TERM.replace(symbol,"")

    
    text = open('model/choruses.txt', 'rb').read().decode(encoding='utf-8')
    # Splitting the string into sentences, while converting whole data into lowercase.
    corpus = text.lower().split("\n")
    # To make sure no sentence appears twice in our corpus, we use set. Otherwise, it will make the model biased.
    corpus = list(set(corpus))


    tokenizer = Tokenizer()
    tokenizer.fit_on_texts(corpus)
    total_words = len(tokenizer.word_index) + 1

    input_sequences = []
    for line in corpus:
        token_list = tokenizer.texts_to_sequences([line])[0]
        for i in range(1, len(token_list)):
            n_gram_sequence = token_list[:i+1]
            input_sequences.append(n_gram_sequence)
    
    # pad sequences
    max_sequence_len = max([len(x) for x in input_sequences])
    input_sequences = np.array(pad_sequences(input_sequences,
                        maxlen = max_sequence_len, padding='pre'))
    
    model = load_model('model/my_model.h5')

    hasil = []

    def make_lyrics(seed_text, next_words):
        for _ in range(next_words):
            token_list = tokenizer.texts_to_sequences([seed_text])[0]
            token_list = pad_sequences([token_list],maxlen=max_sequence_len + 1,padding='pre')
            predicted = model.predict(token_list, verbose=0)
            classes = np.argmax(predicted,axis=1)
            output_word = ""
            for word, index in tokenizer.word_index.items():
                if index == classes:
                    output_word = word
                    break
            seed_text += " " + output_word
        hasil.append(seed_text)
        
    make_lyrics(inp, 10)
    return hasil[0]
