log = open('ataque.log').read()
ataques = log.count('45.33.32.156')

print("=== SIEM BASICO ===")
print(f"IP 45.33.32.156 atacó {ataques} veces")

if ataques > 3:
    print("VEREDICTO: ALERTA ROJA. Bloquear IP inmediatamente")
else:
    print("VEREDICTO: Verde. Tráfico normal")
