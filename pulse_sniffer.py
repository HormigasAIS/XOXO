import time
import json
import random

# Configuración del Nodo según Protocolo LBH
NODE_ID = "XOXO-Alpha"
VALID_AUTHORITY = "6EE9F0A93E9EFFFC"

def sniff_bus():
    print(f"📡 [NODO: {NODE_ID}] Sniffer LBH activo... Escuchando feromonas.")
    print("------------------------------------------------------------")
    
    try:
        while True:
            # Simulando la captura de un pulso del bus
            is_valid = random.random() > 0.2  # 80% de probabilidad de pulso legítimo
            
            pulse = {
                "timestamp": time.time(),
                "type": "mosquito_pulse",
                "origin": "manager_alpha" if is_valid else "unknown_node",
                "signature": VALID_AUTHORITY if is_valid else "FAILED_SIG_0x000"
            }
            
            # Lógica de Reacción de la Hormiga Stanford
            if pulse["signature"] == VALID_AUTHORITY:
                print(f"🟢 [VALIDADO] Feromona detectada de {pulse['origin']}. Estado: RESONANCIA.")
            else:
                print(f"🔴 [ALERTA] Firma inválida detectada! Origen: {pulse['origin']}. Ejecutando BLOQUEO.")
            
            time.sleep(3) # Intervalo de pulso
            
    except KeyboardInterrupt:
        print("\n🛑 [SISTEMA] Sniffer detenido por el Manager Alpha. Hibernando...")

if __name__ == "__main__":
    sniff_bus()
