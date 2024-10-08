# ROADMAP

- WP関連：機能追加
    - 記事カテゴリの自動付与
    - DALL-E3でのサムネイル自動生成&アップロード
    - ブロックエディタ対応
        - 生成後にブロックエディタで簡単に装飾できるようにする
        - M1-70S比較ブロックみたいなものを自然に文章中に埋め込めるようにする
    - RAGの導入
        - トップページにAIヘルパー（RAGベースで応答）を導入する
- 記事生成：既存機能の改良
    - 商品情報のテーブル作成（一目でスペック比較を簡単にできるように）
        - 構想
        - テーブルカテゴリ：イヤホン、ヘッドホン、スピーカー、スピーカーアンプ、スピーカープレイヤー、ヘッドホンアンプ、DAP、イヤーピース、ケーブル
        - 共通項目：製品名、製品画像、価格、ドライバー、インピーダンス、感度、周波数特性、ケーブル長、重量、付属品、保証、製品URL
    - Agentの追加
        - Agentを追加することで便利になる部分を考える
- 記事生成：機能追加
    - スレッド読み込み機能（スレッドのURLを入力するだけで、スレッド内の情報を取得する。要約というよりも抜粋/並べ替え機能。Progress.`get_threds.py`）
        - `要約して`というプロンプトから`抜粋して`に変わるため、`interpreter`モジュールに大幅変更が必要になる。
    - 事前学習済みモデルを用いた記事生成機能
        - 現状だと、コメントが一般的回答すぎる。例えばX（Twitter）らしさや掲示板らしさ、ニュース記事らしさ等を好みに応じて事前学習できる機能があれば、より自然な文章が生成できるかもしれない。
    - 製品画像のDL&記事に埋め込む機能
        - 紹介製品の画像をDLして、適切なコメントに画像を埋め込む機能
    - 記事内容：既存製品との比較機能
        - オーディオ製品での例：BAドバイバー4機：の製品の紹介記事であれば、BAドライバー4機の機種は他にどのようなものがあるのか、従来のBA4機の特徴はどのようなものだったのか。BA3機とBA4機ではどのような違いがあるのか。等詳細情報まで記載してコメントする機能。
- 開発環境の改善
    - 今は各モジュールに`test_~.py`ファイルがある。`tests/`ディレクトリにまとめる（可読性の向上）