import socket

def main():
    # # 自身のIPアドレスを取得
    soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 取得したIPアドレスを元に接続
    soc.connect(("client", 50006))    # 指定したホスト(IP)とポートをソケットに設定
    while(1):
        data = soc.recv(1024)
        data = data.decode('utf-8')
        print("Server>", data)      # サーバー側の書き込みを表示
        print("Client>")
        data = input().encode('utf-8') # 入力待機
        soc.send(data)              # ソケットに入力したデータを送信
        data = data.decode('utf-8') # 入力待機
        if data == "q":             # qが押されたら終了
            soc.close()
            break

main()


