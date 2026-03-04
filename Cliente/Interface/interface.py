import socket
import json



class Interface:
    def __init__(self):
        self.COMMAND_SIZE = 9
        self.INT_SIZE = 8
        self.PORT = 9999
        self.SERVER_ADDRESS = "10.1.58.181"
        pass

    def receive_str(self,connect, n_bytes: int) -> str:
        """
        :param n_bytes: The number of bytes to read from the current connection
        :return: The next string read from the current connection
        """
        data = connect.recv(n_bytes)
        return data.decode()


    def receive_int(self, connect: socket.socket, n_bytes: int) -> int:
        data = connect.recv(n_bytes)
        return int.from_bytes(data, byteorder='big', signed=True)


    def send_str(self,connect, value: str) -> None:
        connect.send(value.encode())

    def send_int(self,connect: socket.socket, value: int, n_bytes: int) -> None:
        connect.send(value.to_bytes(n_bytes, byteorder="big", signed=True))

    # TODO
    # Implement a method that sends and object and returns an object.
    # ...
    def send_object(self,connection, obj):
        """1º: envia tamanho, 2º: envia dados."""
        data = json.dumps(obj).encode('utf-8')
        size = len(data)
        self.send_int(connection, size, self.INT_SIZE)  # Envio do tamanho
        connection.send(data)  # Envio do objeto

    def receive_object(self,connection):
        """1º: lê tamanho, 2º: lê dados."""
        size = self.receive_int(connection, self.INT_SIZE)  # Recebe o tamanho
        data = connection.recv(size)  # Recebe o objeto
        return json.loads(data.decode('utf-8'))


    def execute(self):
        # Socket & ligação
        connection = socket.socket()
        connection.connect((self.SERVER_ADDRESS, self.PORT))
        # Testar a operação de soma

        a = int(input("digite um numero: "))
        b = int(input("digite  outro numero:"))

        dicionario = {"oper": "+", "op1": 12, "op2": 12}

        self.send_str(connection, "add      ")
        self.send_int(connection, a, self.INT_SIZE)
        self.send_int(connection, b, self.INT_SIZE)
        res = self.receive_int(connection, self.INT_SIZE)
        print("O resultado da soma é:", res)
        # Execute a new type of operation: OBJ_OP
        # Client sends a dictionary.
        # Example: {"oper":"+","oper1":4,"oper2":5}
        # It receives an intreger a result of the operation
        # ...
        # Testar duas operações de subtração

        for i in range(2):
            a += 1
            # Operação de subtração
            self.send_str(connection, "sub      ")
            self.send_int(connection, a, self.INT_SIZE)
            self.send_int(connection, b, self.INT_SIZE)
            res = self.receive_int(connection, self.INT_SIZE)

            print("O resultado da subtração é:", res)
        self.send_str(connection, "add_obj  ")
        self.send_object(connection, dicionario)
        print("o resultado da operacao é:", self.receive_int(connection,self.INT_SIZE))
        # 1 Fechar a conexão apenas do lado do cliente ou...
        self.send_str(connection, "bye      ")

        print("Connection is going to close...")
        connection.close()


