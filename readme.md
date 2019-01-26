## WHAT
Docker利用してコンテナを二つ作成しソケット通信をするプログラム。

## WHY

ソケットプログラミングの際にlocalhostで通信することがよくあったが
それだとクライアントとサーバー別れていないのが気になったため作成

## HOW
まずDockerを使用可能な環境にする

```
make start
```
二つのDockerコンテナを起動
ターミナル画面を二つ用意し
```
docker exec -it socket_server_1  /bin/bash

docker exec -it socket_client_1  /bin/bash
```

でコンテナの中にはいる

```
python server.py
python client.py
```

を二つの画面で実行してあげることで
ソケット通信が可能
qを押すと停止する。

コンテナは

```
make kill
```

で消去可能
