import requests
from bs4 import BeautifulSoup
import os

def scrape_website(url):
    # requestsを使ってウェブページを取得する
    response = requests.get(url)
    # ウェブページの内容をパースするためにBeautifulSoupを使用する
    soup = BeautifulSoup(response.content, 'html.parser')
    # テキストデータを抽出する
    texts = soup.find_all('p')  # 'p'タグが段落を表していることが多いため
    return [text.get_text(strip=True) for text in texts]

def save_text_to_file(directory, text_data):
    # ディレクトリが存在しない場合は作成する
    if not os.path.exists(directory):
        os.makedirs(directory)

    # 連番ファイル名を生成して存在しないファイル名を見つける
    i = 1
    while True:
        file_path = os.path.join(directory, f"site{i}.txt")
        if not os.path.isfile(file_path):  # ファイルが存在しない場合
            break
        i += 1

    # テキストデータをファイルに書き込む
    with open(file_path, 'w', encoding='utf-8') as file:
        for line in text_data:
            file.write(f"{line}\n")
    
    return file_path

def main():
    # ユーザーにURLを入力してもらう
    url = input("ウェブページのURLを入力してください: ")
    # スクレイピング実行
    text_data = scrape_website(url)
    # テキストを保存するディレクトリを指定
    directory = "dataset"
    # ファイルに保存してファイル名を取得
    file_path = save_text_to_file(directory, text_data)
    print(f"テキストデータが {file_path} に保存されました。")

if __name__ == '__main__':
    main()
