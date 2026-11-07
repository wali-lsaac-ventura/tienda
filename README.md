# Sistema de Ventas en Python

Sistema de ventas para un colmado, desarrollado en Python. Permite registrar clientes, realizar pedidos, calcular totales y generar facturas, con calculadora integrada y persistencia de datos.

## Características

- Registro de clientes con nombre, edad, teléfono y dirección.
- Catálogo de productos con precios.
- Cálculo automático del total por pedido.
- Generación de factura por cada compra.
- Calculadora integrada con historial de operaciones.
- Contador total de pedidos realizados.
- Separación del código en módulos para mejor mantenimiento.

## Tecnologías utilizadas

- Python 3

## Estructura del proyecto

| Archivo | Descripción |
| --- | --- |
| `tienda.py` | Archivo principal. Gestiona el flujo de la tienda. |
| `datos.py` | Manejo de carga y guardado de datos. |
| `calculadora.py` | Funciones matemáticas y manejo del historial. |

## Instalación

1. Clona el repositorio:
```bash
git clone https://github.com/wali-isaac-ventura/colmado.git