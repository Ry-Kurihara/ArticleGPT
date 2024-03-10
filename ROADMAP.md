# ROADMAP

- WP関連：機能追加
    - 記事カテゴリの自動付与
    - DALL-E3でのサムネイル自動生成&アップロード
- 記事生成：既存機能の改良
    - 商品情報のテーブル作成（一目でスペック比較を簡単にできるように）
- 記事生成：機能追加
    - スレッド読み込み機能（スレッドのURLを入力するだけで、スレッド内の情報を取得する。要約というよりも抜粋/並べ替え機能。Progress.`get_threds.py`）
        - プロンプトなどの`interpreter`モジュールに大幅変更が必要になるので、別リポジトリの方が良いかも。
- 開発環境の改善
    - 今は各モジュールに`test_~.py`ファイルがある。`tests/`ディレクトリにまとめる（可読性の向上）