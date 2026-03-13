SELECT nombre, precio_venta
FROM producto;



SELECT *
FROM cliente
WHERE pais = 'España';


SELECT *
FROM producto
ORDER BY precio_venta DESC;



SELECT cliente.nombre_cliente, pedido.codigo_pedido
FROM cliente, pedido
WHERE cliente.codigo_cliente = pedido.codigo_cliente;

SELECT cliente.nombre_cliente, pedido.codigo_pedido, producto.nombre
FROM cliente, pedido, detalle_pedido, producto
WHERE cliente.codigo_cliente = pedido.codigo_cliente
AND pedido.codigo_pedido = detalle_pedido.codigo_pedido
AND detalle_pedido.codigo_producto = producto.codigo_producto;

SELECT COUNT(*)
FROM cliente;

SELECT AVG(precio_venta)
FROM producto;


SELECT gama, COUNT(*)
FROM producto
GROUP BY gama;

UPDATE cliente
SET telefono = '600123456'
WHERE codigo_cliente = 10;

DELETE FROM pago
WHERE fecha_pago < '2005-01-01';