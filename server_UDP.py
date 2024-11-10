import socket

def servidor_udp(porta):
    # Cria um socket UDP (SOCK_DGRAM)
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as servidor_socket:
        servidor_socket.bind(('', porta))  # Associa o socket à porta
        print("Servidor UDP escutando na porta", porta)
        
        while True:
            dados, endereco_cliente = servidor_socket.recvfrom(1024)  # Recebe pacotes

# Inicia o servidor UDP na porta 5001
servidor_udp(5001)
