from Led import Led as Led
from Ultrasonico import Ultrasonico as ultrasonico
from Temperatura import Temperatura as temp
class interfaz:
    def __init__(self): 
        super().__init__()

    def led():
        Led.led()
    def ultrasonico():
        ultrasonico.leer()
    def temperatura():
        temp.temperatura()
        
    def arduinoSerial(self, nombre):
        ser = serial.Serial('/dev/ttyACM0', 9600) # Reemplaza '/dev/ttyACM0' por el puerto serial en el que está conectado el Arduino
        signal =b''+nombre
        ser.write(signal)
        ser.close()
        puerto = '/dev/ttyUSB0'  # Reemplaza '/dev/ttyUSB0' por el puerto en el que está conectado tu Arduino
        arduino = serial.Serial(puerto, baudrate=9600, timeout=1)
        while True:
            mensaje = arduino.readline()
            if mensaje:
                print(mensaje.decode('utf-8'))
        

    

if __name__=='__main__':
    res = 0
    while res != 4 :
        print("1-leer sensor ultrasonico")
        print("2-leer temperatura y humedad")
        print("3-prender o apagar un led")
        print('4-leer sensor de luz')
        print("5-salir")
        res = input("Que deseas hacer?")
        res = int (res)
        if res == 1:
            interfaz.ultrasonico()
        elif res == 2:
            interfaz.temperatura()
        elif res == 3:
            interfaz.led()
        elif res == 4:
            interfaz.arduinoSerial('Luz')
        else:
            print("Opcion invalida")