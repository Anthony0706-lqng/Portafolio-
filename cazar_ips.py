log = open('ataque.log').readlines()

ips_sospechosas = []
for linea in log:
    if "404" in linea or "403" in linea: # Solo errores = ataques
        ip = linea.split(" ")[0] # La IP es la primera palabra
        ips_sospechosas.append(ip)

# Quitar duplicados con set()
ips_unicas = set(ips_sospechosas)

print("=== CAZADOR DE IPS SOC ===")
print(f"IPs maliciosas detectadas: {len(ips_unicas)}")
for ip in ips_unicas:
    print(f" - ALERTA: {ip} -> Bloquear en Firewall")
