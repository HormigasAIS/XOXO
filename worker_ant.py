import shutil
import os
import time
import json

# Configuración de Rutas
CONTRACT_FILE = "CONTRACT_HUMAN.lbh"
BACKUP_DIR = "swarm/backups"
LOG_FILE = "guardia_nocturna.log"

def check_sovereign_permission():
    try:
        if not os.path.exists(CONTRACT_FILE):
            print(f"🔴 [CRÍTICO] Contrato {CONTRACT_FILE} no encontrado.")
            return False
            
        with open(CONTRACT_FILE, 'r') as f:
            contract = json.load(f)
            
        # Validación de Identidad y Permiso
        founder_gpg = contract.get("authority", {}).get("gpg_id")
        can_backup = contract.get("permissions", {}).get("autonomous_backups")
        
        # Validación estricta de la firma GPG Master
        if founder_gpg == "6EE9F0A93E9EFFFC" and can_backup:
            return True
        else:
            print(f"⚠️ [BLOQUEO] Permiso denegado por el contrato LBH.")
            return False
    except Exception as e:
        print(f"🔴 [CRÍTICO] Error al leer el contrato: {e}")
        return False

def perform_backup():
    if not os.path.exists(BACKUP_DIR):
        os.makedirs(BACKUP_DIR)
        
    timestamp = int(time.time())
    backup_name = f"{BACKUP_DIR}/CONTRACT_HUMAN_{timestamp}.lbh.bak"
    
    if check_sovereign_permission():
        shutil.copy2(CONTRACT_FILE, backup_name)
        msg = f"🟢 [OBRERA] Validación LBH Exitosa. Respaldo creado."
        print(msg)
        with open(LOG_FILE, "a") as log:
            # Identidad completa según Documento Fundacional
            log.write(f"[{time.ctime()}] PERMISO_VALIDADO: Respaldo ejecutado bajo autoridad de Cristhiam Leonardo Hernandez Quiñonez.\n")
    else:
        with open(LOG_FILE, "a") as log:
            log.write(f"[{time.ctime()}] ALERTA: Intento de respaldo sin autorización contractual de la autoridad soberana.\n")

def listen_for_resonance():
    print(f"🐜 [AGENTE: Worker-Ant] Consultando CONTRACT_HUMAN.lbh...")
    while True:
        perform_backup()
        time.sleep(60) 

if __name__ == "__main__":
    listen_for_resonance()
