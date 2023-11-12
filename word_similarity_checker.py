from gensim.models import Word2Vec

def calculate_similarity(model, word1, word2):
    if word1 in model.wv.key_to_index and word2 in model.wv.key_to_index:
        return model.wv.similarity(word1, word2)
    else:
        return "一方または両方の単語がボキャブラリーにありません。"

def main():
    # モデルのロード
    model = Word2Vec.load("text_word2vec.model")

    # ユーザーからの入力を受け取る
    word1 = input("類似度を計算するための単語1を入力してください: ")
    word2 = input("類似度を計算するための単語2を入力してください: ")

    # 類似度の計算
    similarity = calculate_similarity(model, word1, word2)
    
    # 類似度の結果を出力
    print(f"'{word1}' と '{word2}' の類似度は: {similarity}")

if __name__ == '__main__':
    main()
