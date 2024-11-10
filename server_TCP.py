import socket

def servidor_tcp(porta):
    # Cria o socket TCP
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as servidor_socket:
        servidor_socket.bind(('', porta))
        servidor_socket.listen()
        print("Servidor TCP escutando na porta", porta)

        # Aceitar a conexão do cliente
        conn, addr = servidor_socket.accept()
        with conn:
            print("Conectado por", addr)
            conn.settimeout(10)  # Tempo limite de 10 segundos para recepção de dados
            while True:
                try:
                    dados = conn.recv(1024)
                    if not dados:
                        print("Conexão fechada pelo cliente.")
                        break
                    # Exibe os dados recebidos de forma legível
                    print("Dados recebidos:", dados.decode('utf-8'))

                    # Envia uma resposta de volta ao cliente (confirmação de recebimento)
                    conn.sendall(b"Dados recebidos com sucesso!")

                except socket.timeout:
                    print("Tempo de espera excedido. Fechando a conexão.")
                    break
                except Exception as e:
                    print(f"Erro ao receber dados: {e}")
                    break

# Executa o servidor
servidor_tcp(5001)
