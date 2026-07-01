log = open('ataque.log').readlines()

ips_sospechosas = set()
ataques_totales = 0

for linea in log:
    if "404" in linea or "403" in linea:
        ip = linea.split(" ")[0]
        ips_sospechosas.add(ip)
        ataques_totales += 1

# Crear el reporte.txt
reporte = open('reporte_SOC_03-07-2025.txt', 'w')
reporte.write("=== REPORTE SOC - TURNO MATUTINO ===\n")
reporte.write("Analista: Anthony\n")
reporte.write("Fecha: 03/07/2025\n")
reporte.write(f"Total Ataques Detectados: {ataques_totales}\n")
reporte.write(f"IPs Maliciosas Unicas: {len(ips_sospechosas)}\n\n")
reporte.write("LISTA DE BLOQUEO RECOMENDADA:\n")
for ip in ips_sospechosas:
    reporte.write(f" - {ip} -> BLOQUEAR EN FIREWALL\n")
reporte.write("\nVeredicto: ALERTA ROJA. Turno cerrado.")
reporte.close()

print("Reporte generado: reporte_SOC_03-07-2025.txt")
