import socket

def servidor_tcp(porta):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as servidor_socket:
        servidor_socket.bind(('', porta))
        servidor_socket.listen()
        print("Servidor TCP escutando na porta", porta)

        conn, addr = servidor_socket.accept()
        with conn:
            print("Conectado por", addr)
            while True:
                dados = conn.recv(1024)
                if not dados:
                    print("Conexão fechada pelo cliente.")
                    break

                # Envia uma resposta de volta ao cliente (confirmação de recebimento)
                conn.sendall(b"Dados recebidos com sucesso!")
            
            conn.close()
            print("Conexão com o cliente encerrada pelo servidor")
# Executa o servidor
servidor_tcp(5001)
