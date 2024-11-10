import socket
import time

def cliente_tcp(ip_servidor, porta):
    endereco_servidor = (ip_servidor, porta)

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as cliente_socket:
        cliente_socket.connect(endereco_servidor)  # Conexão já faz o processo SYN/SYN ACK/ACK
        print("Conectado ao servidor TCP.")

        dados = b"Oi\n"
        start_time = time.time()

        for _ in range(100):  # Envia os dados 100 vezes
            cliente_socket.sendall(dados)

            # Aguarda a confirmação do servidor
            resposta = cliente_socket.recv(1024)
            

        end_time = time.time()
        print("Dados enviados.")
        tempo_total = end_time - start_time
        print(f"Tempo total: {tempo_total} segundos.")

        cliente_socket.close()
        print("Conexão com o servidor encerrada pelo cliente")
# Executa o cliente
cliente_tcp("192.168.5.137", 5001)
