#!/bin/bash

# --- CONFIGURACIÓN DEL NODO HORMIGASAIS ---
NODE_NAME="XOXO-Alpha"
LOG_FILE="guardia_nocturna.log"

echo "🐜 [SISTEMA] Iniciando Colonia HormigasAIS en Nodo: $NODE_NAME"
echo "------------------------------------------------------------"

# 1. Limpieza de procesos previos (si existen)
pkill -f pulse_sniffer.py
pkill -f worker_ant.py

# 2. Despertar al Sistema Nervioso (Sniffer)
python3 pulse_sniffer.py > /dev/null 2>&1 &
SNIFFER_PID=$!
echo "🟢 [VIGILANCIA] Sniffer activado (PID: $SNIFFER_PID)"

# 3. Despertar a la Fuerza de Trabajo (Obrera)
python3 worker_ant.py > /dev/null 2>&1 &
WORKER_PID=$!
echo "🟢 [TRABAJO] Hormiga Obrera activada (PID: $WORKER_PID)"

echo "------------------------------------------------------------"
echo "🚀 Nodo operando en segundo plano. Monitoreando feromonas..."
echo "Para ver la actividad, usa: tail -f $LOG_FILE"
