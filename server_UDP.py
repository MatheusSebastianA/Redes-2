import socket

def servidor_udp(porta):
    # Cria o socket UDP
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as servidor_socket:
        servidor_socket.bind(('', porta))
        print("Servidor UDP escutando na porta", porta)
        
        while True:
            # Recebe dados do cliente
            dados, endereco_cliente = servidor_socket.recvfrom(1024)
            print(f"Dados recebidos de {endereco_cliente}: {dados.decode('utf-8')}")
