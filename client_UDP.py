import socket
import time

def cliente_udp(ip_servidor, porta):
    # Define o endereço do servidor
    endereco_servidor = (ip_servidor, porta)

    # Cria o socket UDP
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as cliente_socket:
        dados = b"Oi\n"
        start_time = time.time()

        # Envia dados 100 vezes para o servidor
        for _ in range(100):
            cliente_socket.sendto(dados, endereco_servidor)

        print("Dados enviados.")
    
        end_time = time.time()
        tempo_total = end_time - start_time
        print(f"Tempo total: {tempo_total} segundos.")

# Executa o cliente
cliente_udp("192.168.5.137", 5001)
