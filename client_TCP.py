import socket
import time

def cliente_tcp(ip_servidor, porta):
    # Define o endereço do servidor
    endereco_servidor = (ip_servidor, porta)

    # Cria o socket TCP
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as cliente_socket:
        cliente_socket.connect(endereco_servidor)  # Conecta ao servidor
        print("Conectado ao servidor TCP.")

        # Envia dados e mede o tempo
        dados = b"Exemplo de dados para envio via TCP"
        start_time = time.time()
        
        # Enviar dados várias vezes para medir a taxa de transferência
        for _ in range(1000):  # Envia os dados 1000 vezes, por exemplo
            cliente_socket.sendall(dados)
        
        end_time = time.time()
        print("Dados enviados.")
        
        # Calcular e exibir a taxa de transferência
        tempo_total = end_time - start_time
        print(f"Tempo total: {tempo_total} segundos.")

# Executa o cliente
cliente_tcp("192.168.5.137", 5001)
