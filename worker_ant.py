import shutil
import os
import time

# Configuración de Tareas de la Obrera
SOURCE_FILE = "CONTRACT_HUMAN.lbh"
BACKUP_DIR = "swarm/backups"
LOG_FILE = "guardia_nocturna.log"

def perform_backup():
    if not os.path.exists(BACKUP_DIR):
        os.makedirs(BACKUP_DIR)
        
    timestamp = int(time.time())
    backup_name = f"{BACKUP_DIR}/CONTRACT_HUMAN_{timestamp}.lbh.bak"
    
    try:
        shutil.copy2(SOURCE_FILE, backup_name)
        msg = f"🟢 [OBRERA] Tarea completada: Respaldo soberano creado -> {backup_name}"
        print(msg)
        with open(LOG_FILE, "a") as log:
            log.write(f"[{time.ctime()}] RESONANCIA: Respaldo exitoso.\n")
    except FileNotFoundError:
        print(f"⚠️ [ERROR] No se encontró el contrato {SOURCE_FILE}")

def listen_for_resonance():
    print("🐜 [AGENTE: Worker-Ant] Esperando señal de RESONANCIA del Sniffer...")
    # Aquí la obrera simula la escucha del bus interno
    # En una fase avanzada, esto se conectaría vía sockets o señales de sistema
    while True:
        # Simulamos que recibe la señal de éxito del sniffer
        time.sleep(10) 
        perform_backup()
        print("💤 [OBRERA] Tarea finalizada. Entrando en modo ahorro de energía...")
        time.sleep(60) # Espera un ciclo largo para no saturar el disco

if __name__ == "__main__":
    listen_for_resonance()
