# Portafolio SOC Jr | Anthony | Python + Bash + SIEM

Repositorio de evidencia técnica para rol de Analista SOC Jr. Proyecto 100% desarrollado en Termux/Linux en Android.

## 🎯 Objetivo del Proyecto
Simular un entorno SOC real: ingesta de logs Apache, detección de patrones de ataque, extracción de IoC y generación de reporte ejecutivo para bloqueo en Firewall.

## 🛠️ Stack Técnico
- **Lenguaje:** Python 3, Bash
- **Entorno:** Termux en Android 
- **Skills:** Análisis de Logs, Detección de Amenazas, Kill Chain, Automatización, Git/GitHub

## 📦 Componentes del Portafolio

| Archivo | Función SOC |
| --- | --- |
| `siem_basico.py` | Mini-SIEM: Detecta 404/403 y cuenta intentos por IP |
| `deteccion.py` | Motor de detección de ataques por fuerza bruta |
| `correlacion.py` | Correlaciona eventos y extrae IoC: `45.33.32.156` |
| `cazar_ips.py` | Threat Hunting básico sobre `ataque.log` |
| `auditoria_puertos.py` | Escaneo de superficie de ataque simulado |
| `generar_reporte.py` | Automatiza `reporte_SOC_03-07-2025.txt` para el CISO |

## 📈 Resultado Clave
El script detectó 4 intentos de ataque desde la IP `45.33.32.156`. Se generó un reporte ejecutivo con lista de bloqueo lista para implementar en Firewall.

## 🚀 Cómo Ejecutar
```bash
python siem_basico.py
python generar_reporte.py

