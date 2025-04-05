# 🧮 CalculadoraMatrices

[![Python Version](https://img.shields.io/badge/python-3.6+-blue.svg)](https://www.python.org/downloads/)
[![NumPy](https://img.shields.io/badge/numpy-1.19+-green.svg)](https://numpy.org/)

## 📋 Descripción

**MatrixCalc** es una calculadora de matrices avanzada con interfaz gráfica, desarrollada en Python. Combina la potencia de cálculos matriciales precisos con una interfaz Tkinter intuitiva y atractiva.

## ✨ Características

- 🔢 **Creación de matrices** personalizadas y matrices identidad
- ➕ **Operaciones básicas**: suma, resta, multiplicación de matrices
- 🔄 **Operaciones avanzadas**:
  - Cálculo de determinantes
  - Inversión de matrices
  - Eliminación Gauss-Jordan con visualización paso a paso
  - Resolución de sistemas por el método de Cramer
- 🧮 **Multiplicación por escalar**
- 📊 **Visualización clara** de resultados y pasos intermedios
- 💾 **Almacenamiento de resultados** para reutilizarlos en otras operaciones

## 🚀 Instalación

```bash
# Clonar el repositorio
git clone https://github.com/Ppixelbro/CalculadoraMatrices.git
cd CalculadoraMatrices

```

## 🔧 Requisitos

- Python 3.6+
- Tkinter (incluido en la mayoría de instalaciones de Python)

## 💻 Uso

```bash
python CalculadoraMatrices.py
```

### Crear una matriz

1. Ingresa el número de filas y columnas
2. Haz clic en "Generar campos"
3. Completa los valores de la matriz
4. Presiona "Guardar matriz"

### Realizar operaciones

1. Selecciona las matrices desde los menús desplegables
2. Haz clic en el botón de la operación deseada
3. Visualiza el resultado en el panel derecho
4. Opcionalmente, guarda el resultado como una nueva matriz

## 📚 Guía rápida

| Operación | Descripción | Requisitos |
|-----------|-------------|------------|
| A + B | Suma de matrices | Matrices de igual dimensión |
| A - B | Resta de matrices | Matrices de igual dimensión |
| A × B | Multiplicación de matrices | Columnas(A) = Filas(B) |
| Det(A) | Determinante | Matriz cuadrada |
| Inv(A) | Matriz inversa | Matriz cuadrada con det ≠ 0 |
| Gauss-Jordan | Eliminación G-J | Cualquier matriz |
| A × escalar | Multiplicación por escalar | Cualquier matriz |
| Cramer | Resolución de sistemas | Matriz aumentada [A\|b] |


<p align="center">
  <sub>Desarrollado con ❤️ por Ppixelbro</sub>
</p>
