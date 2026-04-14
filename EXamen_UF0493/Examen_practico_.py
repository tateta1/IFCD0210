1. Aplicación interna

Usaría una intranet con acceso solo desde la empresa o por VPN.
Seguridad básica: login con cuentas de empleados, roles (admin/usuario), HTTPS, acceso limitado por IP, sistema actualizado y registro de accesos.

2. Despliegue en Linux

Primero contratas un servidor y le instalas Linux.
Abres puertos 80 y 443, instalas Nginx/Apache, el lenguaje que uses (Node, PHP, etc.) y la base de datos.
Subes el proyecto, configuras variables, activas HTTPS y arrancas la app.
Luego revisas que funcione y configuras backups.

3. Pérdida de datos

Se soluciona con backups.
Restauras una copia anterior al fallo, compruebas que esté bien y vuelves a poner la app en marcha.
Lo ideal es tener copias automáticas y en otro servidor.

4. Muchos datos

Depende del tipo:

SQL → datos organizados
NoSQL → datos más flexibles

Importa: que escale bien, sea rápido, tenga copias de seguridad, buena seguridad y no sea muy caro.