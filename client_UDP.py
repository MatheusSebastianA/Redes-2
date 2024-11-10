import socket

def cliente_udp(ip_servidor, porta):
    # Define o endereço do servidor
    endereco_servidor = (ip_servidor, porta)

    # Cria o socket UDP
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as cliente_socket:
        dados = b"Exemplo de dados para envio via UDP"
        
        # Envia dados 1000 vezes para o servidor
        for _ in range(1000):
            cliente_socket.sendto(dados, endereco_servidor)
        print("Dados enviados.")

# Executa o cliente
cliente_udp("192.168.5.137", 5001)
