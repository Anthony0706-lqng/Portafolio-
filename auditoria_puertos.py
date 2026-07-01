log = """
10.0.0.50:54321 > 192.168.1.10:22 ESTAB TCP
10.0.0.99:12345 > 192.168.1.10:80 ESTAB TCP 
45.33.32.156:60001 > 192.168.1.10:23 ESTAB UDP
"""

print("=== AUDITORIA DE PUERTOS SOC ===")
puertos = [":22", ":80", ":23"]
for p in puertos:
    if p in log:
        print(f"ALERTA: Puerto {p} con tráfico detectado")

if "TCP" in log:
    print("PROTOCOLO: TCP = Confiable, usado para SSH/Web")
if "UDP" in log:
    print("PROTOCOLO: UDP = No confiable, posible escaneo/DDoS")

if ":23" in log and "UDP" in log:
    print("VEREDICTO: ALERTA ROJA. Telnet :23 + UDP = Servicio viejo y peligroso")
