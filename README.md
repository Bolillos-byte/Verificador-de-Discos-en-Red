#  Verificador de Discos en Red

Script en Python para verificar el estado de discos duros en múltiples equipos conectados por red vía SSH. Ideal para técnicos, administradores de sistemas o estudiantes que deseen monitorear servidores o estaciones de trabajo desde una máquina central.

---

##  Tecnologías utilizadas

- Python 3  
- Paramiko (conexión SSH)  
- smartctl (en equipos remotos Linux/macOS)  
- Terminal

---

##  Funcionalidades

- Conexión remota vía SSH a múltiples equipos  
- Verificación del estado SMART de discos (`/dev/sda`, `/dev/sdb`, `/dev/nvme0n1`)  
- Registro de resultados en archivo `.csv`  
- Adaptable a redes empresariales o laboratorios escolares  
- Configuración flexible mediante archivo `hosts.json`

---

##  Ejecución

1. Instala las dependencias:

`bash
pip install paramiko


- Asegúrate de tener smartmontools instalado en los equipos remotos:
sudo apt install smartmontools


- Configura el archivo hosts.json con las IPs y credenciales de los equipos:
[
  {
    "ip": "192.168.1.10",
    "user": "admin",
    "password": "admin123"
  },
  {
    "ip": "192.168.1.11",
    "user": "admin",
    "password": "admin123"
  }
]


- Ejecuta el script:
python verificador_remoto.py



 Archivos del proyecto
- verificador_remoto.py → Script principal
- hosts.json → Lista de equipos remotos
- resultados_red.csv → Reporte generado automáticamente
- README.md → Documentación

 Aplicaciones
- Monitoreo de discos en servidores Linux/macOS
- Verificación de salud de discos en estaciones de trabajo conectadas a red
- Registro automatizado para auditorías o mantenimiento preventivo
- Adaptable a entornos con Active Directory o redes mixtas

Contacto
Daniel Rauda
magana.rauda.alandaniel@gmail.com


Licencia
Este proyecto está bajo la licencia MIT. Puedes usarlo, modificarlo y compartirlo libremente
