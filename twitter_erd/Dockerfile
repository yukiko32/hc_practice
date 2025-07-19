FROM haskell:8

WORKDIR /opt/erd

# アーカイブリポジトリのURLへ置換する
RUN sed -i 's|http://deb.debian.org/debian|http://archive.debian.org/debian|g' /etc/apt/sources.list && \
  # Debianのセキュリティリポジトリも古いリリースに対応していないため削除
  sed -i '/security/d' /etc/apt/sources.list && \
  # aptに対して「パッケージの有効期限（Valid-Until）」チェックを無効にする設定ファイルを追加（古いリポジトリではReleaseファイルが期限切れになっていることがあるため）
  echo 'Acquire::Check-Valid-Until "false";' > /etc/apt/apt.conf.d/99no-check-valid-until && \
  # APTパッケージリストを更新しgraphvizをインストール
  apt-get update && apt-get install -y graphviz

RUN cabal v2-update && cabal v2-install erd

ENTRYPOINT ["erd"]
