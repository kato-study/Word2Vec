from gensim.models.word2vec import Word2Vec
import MeCab

# MeCabによる日本語のトークナイザーの設定
def japanese_tokenizer(text):
    mecab = MeCab.Tagger("-Owakati")
    return mecab.parse(text).strip().split()

# ファイルから文章を読み込んでトークン化する関数
def read_text_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return [japanese_tokenizer(line) for line in file if line.strip()]

# Word2Vecモデルをトレーニングするメイン関数
def main():
    # テキストファイルのパス
    file_path = 'learning_data/sample_ja.txt'
    
    # トークン化された文章を取得
    tokenized_texts = read_text_file(file_path)
    
    # トークン化した文章を使用してWord2Vecモデルをトレーニング
    model = Word2Vec(sentences=tokenized_texts, vector_size=100, window=5, min_count=1, workers=4)
    
    # モデルの保存
    model.save("text_word2vec.model")

# スクリプトが直接実行された場合にのみmain関数を呼び出す
if __name__ == '__main__':
    main()
