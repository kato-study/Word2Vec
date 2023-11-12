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

# モデルを更新する関数
def update_model(model, new_sentences):
    # モデルの語彙を更新
    model.build_vocab(new_sentences, update=True)
    # 新しい文でモデルをトレーニング
    model.train(new_sentences, total_examples=model.corpus_count, epochs=model.epochs)

# メイン関数
def main():
    # 既存のモデルをロード
    model = Word2Vec.load("word2vec_updated.model")

    # 新しいテキストファイルのパス
    new_file_path = 'dataset/site1.txt'

    # 新しいトークン化された文章を取得
    new_tokenized_texts = read_text_file(new_file_path)
    
    # モデルを更新
    update_model(model, new_tokenized_texts)

    # 更新したモデルの保存
    model.save("word2vec_updated.model")

if __name__ == '__main__':
    main()
