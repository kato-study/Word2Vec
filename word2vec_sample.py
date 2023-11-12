from gensim.models import Word2Vec
from nltk.tokenize import word_tokenize
import nltk
nltk.download('punkt')

def train_word2vec(sentences):
    # トークン化
    tokenized_sentences = [word_tokenize(sentence) for sentence in sentences]
    # Word2Vecモデルの学習
    model = Word2Vec(sentences=tokenized_sentences, vector_size=100, window=5, min_count=1, workers=4)
    return model

def main():
    # サンプルテキストデータ
    sentences = ["機械学習は面白い", "ディープラーニングも機械学習の一部", "自然言語処理はテキストデータを扱う"]

    model = train_word2vec(sentences)

    # 単語の入力
    word = input("類似単語を検索したい単語を入力してください：")

    # 類似単語の検索と表示
    if word in model.wv:
        similar_words = model.wv.most_similar(word, topn=5)
        print(f"{word} に似ている単語:")
        for w, similarity in similar_words:
            print(f"- {w} (類似度: {similarity:.2f})")
    else:
        print(f"'{word}' は学習データに存在しない単語です。")

if __name__ == "__main__":
    main()
