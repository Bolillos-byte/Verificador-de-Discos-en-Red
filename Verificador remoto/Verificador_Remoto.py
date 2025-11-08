import paramiko
import json
import csv
import time

def cargar_hosts(ruta="hosts.json"):
    try:
        with open(ruta, "r") as f:
            return json.load(f)
    except Exception as e:
        print(f"Error al cargar hosts: {e}")
        return []

def verificar_smart(host):
    ip = host["ip"]
    user = host["user"]
    password = host["password"]
    estado = "No verificado"
    detalles = ""

    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(ip, username=user, password=password, timeout=10)

        discos = ["/dev/sda", "/dev/sdb", "/dev/nvme0n1"]
        for disco in discos:
            stdin, stdout, stderr = ssh.exec_command(f"sudo smartctl -H {disco}")
            salida = stdout.read().decode()
            error = stderr.read().decode()

            if "PASSED" in salida:
                estado = "Salud buena"
            elif "FAILED" in salida:
                estado = "Fallo detectado"
            elif "SMART support is: Unavailable" in salida:
                estado = "SMART no disponible"
            else:
                estado = "Sin datos claros"

            detalles += f"{disco}: {estado}\n"

        ssh.close()
    except Exception as e:
        detalles = f"Error de conexión: {e}"

    return {
        "ip": ip,
        "estado": estado,
        "detalles": detalles.strip()
    }

def guardar_resultados(resultados, ruta="resultados_red.csv"):
    with open(ruta, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["IP", "Estado", "Detalles"])
        for r in resultados:
            writer.writerow([r["ip"], r["estado"], r["detalles"]])

def main():
    print("🔍 Verificador de discos en red")
    hosts = cargar_hosts()
    resultados = []

    for host in hosts:
        print(f"Conectando a {host['ip']}...")
        resultado = verificar_smart(host)
        print(f"{resultado['ip']}: {resultado['estado']}")
        resultados.append(resultado)
        time.sleep(1)

    guardar_resultados(resultados)
    print("\n✅ Verificación completada. Resultados guardados en 'resultados_red.csv'.")

if __name__ == "__main__":
    main()