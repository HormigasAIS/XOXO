# LBH PROTOCOL SPECIFICATION v1.1 - SOBERANÍA DISTRIBUIDA

## 1. Arquitectura de Feromonas (M2M)
El Lenguaje Binario HormigasAIS (LBH) utiliza paquetes JSON firmados para la comunicación entre agentes.

| Tipo de Feromona | Prioridad | Función |
| :--- | :--- | :--- |
| `mosquito_pulse` | ALTA | Latido de vida y sincronización de nodos. |
| `blood_alert` | CRÍTICA | Notificación de intrusión o firma inválida. |
| `task_echo` | MEDIA | Confirmación de tarea completada por obreras. |

## 2. Protocolo de Sucesión y Multi-Firma
Para mitigar el Punto Único de Fallo (SOP), el sistema reconoce tres niveles de autoridad:
1. **Fundador (Master):** ID `6EE9F0A93E9EFFFC` (Control Total).
2. **Nodos Validados (Trust):** Requiere consenso de 2/3 de los agentes para ignorar un pulso corrupto.
3. **Bóveda Fría:** Llave de recuperación física almacenada en San Miguel, El Salvador.

## 3. Estados del Agente
- **HIBERNACIÓN:** < 1% CPU. Espera de interrupción por hardware.
- **RESONANCIA:** Procesamiento activo de feromona validada.
- **BLOQUEO:** Aislamiento de red ante firma GPG no reconocida.
