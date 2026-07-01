log = "45.33.32.156 - [03/Jul/2025] GET /admin.php"
if "22" in log or "admin.php" in log:
    print("ALERTA: Intento de acceso sospechoso detectado")
else:
    print("Todo normal")
