import socket
import threading

IP = "0.0.0.0"
PORT = 5000

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((IP, PORT))
server.listen()

clientes = []

def manejar_cliente(cliente_socket, direccion):
    print(f"Cliente conectado desde {direccion}")
    while True:
        try:
            mensaje = cliente_socket.recv(1024).decode()
            if mensaje:
                print(f"Mensaje recibido de {direccion}: {mensaje}")
                broadcast(mensaje, cliente_socket)
            else:
                print(f"Cliente {direccion} desconectado.")
                clientes.remove(cliente_socket)
                cliente_socket.close()
                break
        except:
            print(f"Error al manejar el cliente {direccion}.")
            clientes.remove(cliente_socket)
            cliente_socket.close()
            break

def broadcast(mensaje, cliente_excluido):
    for cliente in clientes:
        if cliente != cliente_excluido:
            try:
                cliente.send(mensaje.encode())
            except:
                print("Error al enviar el mensaje a un cliente.")
                clientes.remove(cliente)
                cliente.close()

print(f"Servidor escuchando en {IP}:{PORT}")
while True:
    cliente_socket, direccion = server.accept()
    clientes.append(cliente_socket)
    hilo = threading.Thread(target=manejar_cliente, args=(cliente_socket, direccion))
    hilo.start()