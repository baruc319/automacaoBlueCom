# Este código é para ser utilizado com o Arduino via Firmata
# Você precisará instalar o PyFirmata no Python e carregar o StandardFirmata no Arduino

from pyfirmata import Arduino, util
import time

# Configuração
PORT = 'COM3'  # Altere para a porta serial do seu Arduino
SENSOR_PIN = 2  # Pino digital onde o sensor infravermelho está conectado

# Inicialização
board = Arduino(PORT)
print("Conexão estabelecida com o Arduino")

# Configura o pino do sensor como entrada
board.digital[SENSOR_PIN].mode = pyfirmata.INPUT

# Variáveis para contagem
contagem = 0
ultimo_estado = False
estado_atual = False

try:
    print("Iniciando contagem...")
    while True:
        # Lê o estado do sensor (True = detectado, False = não detectado)
        estado_atual = board.digital[SENSOR_PIN].read()
        
        # Verifica se houve uma mudança de estado (detecção)
        if estado_atual and not ultimo_estado:
            contagem += 1
            print(f"Objeto detectado! Total: {contagem}")
            
            # Pequeno delay para evitar múltiplas contagens do mesmo objeto
            time.sleep(0.1)
        
        ultimo_estado = estado_atual
        time.sleep(0.01)  # Pequeno delay para evitar sobrecarga

except KeyboardInterrupt:
    print("\nPrograma encerrado")
    print(f"Total final de detecções: {contagem}")
    board.exit()