# The original image can be any Python version according to your usage.
FROM python:3.10

# Specifies the working directory in the container. This can also be changed as desired.
# However, it must match the destination directory name specified in the following COPY command.
WORKDIR /app

# poetryのインストール先の指定
ENV POETRY_HOME=/opt/poetry
# poetryインストール
RUN curl -sSL https://install.python-poetry.org | python3 - && \
# シンボリックによるpathへのpoetryコマンドの追加
    cd /usr/local/bin && \
    ln -s /opt/poetry/bin/poetry && \
# 仮想環境を作成しない設定(コンテナ前提のため，仮想環境を作らない)
    poetry config virtualenvs.create false 


    