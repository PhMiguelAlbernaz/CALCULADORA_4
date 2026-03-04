from servidor.maquinas.maquina import Maquina
from cliente.interface.interface import Interface
def main():
    print("Executing Main in cliente")
    maq = Maquina()
    int = Interface(maq)
    int.execute()
if __name__ == '__main__':
    main()
