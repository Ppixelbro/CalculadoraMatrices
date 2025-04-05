import numpy as np
import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
from fractions import Fraction

class MatrizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculadora de Matrices")
        self.root.geometry("900x600")
        self.root.configure(bg="#f0f0f0")

        self.matrices = []
        self.resultado_actual = None

        # Estilos
        self.style = ttk.Style()
        self.style.theme_use('clam')
        self.style.configure('TButton', font=('Arial', 10), background='#4a7abc', foreground='black')
        self.style.configure('TLabel', font=('Arial', 11), background='#f0f0f0')
        self.style.configure('TFrame', background='#f0f0f0')
        self.style.configure('Header.TLabel', font=('Arial', 14, 'bold'), background='#f0f0f0')

        self.crear_interfaz()

    def crear_interfaz(self):
        # Frame principal
        main_frame = ttk.Frame(self.root)
        main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        # Frame izquierdo para crear matrices
        left_frame = ttk.Frame(main_frame)
        left_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=5, pady=5)

        # Frame derecho para mostrar matrices y resultados
        right_frame = ttk.Frame(main_frame)
        right_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=5, pady=5)

        # Sección de creación de matrices
        crear_label = ttk.Label(left_frame, text="Crear Matriz", style='Header.TLabel')
        crear_label.pack(pady=10)

        # Frame para dimensiones
        dim_frame = ttk.Frame(left_frame)
        dim_frame.pack(pady=5)

        ttk.Label(dim_frame, text="Filas:").grid(row=0, column=0, padx=5)
        self.filas_var = tk.StringVar(value="3")
        ttk.Entry(dim_frame, textvariable=self.filas_var, width=5).grid(row=0, column=1, padx=5)

        ttk.Label(dim_frame, text="Columnas:").grid(row=0, column=2, padx=5)
        self.columnas_var = tk.StringVar(value="3")
        ttk.Entry(dim_frame, textvariable=self.columnas_var, width=5).grid(row=0, column=3, padx=5)

        # Botón para generar campos de entrada
        ttk.Button(left_frame, text="Generar campos", command=self.generar_campos).pack(pady=10)

        # Frame para campos de matriz
        self.matriz_frame = ttk.Frame(left_frame)
        self.matriz_frame.pack(fill=tk.BOTH, expand=True, pady=10)

        # Botón para guardar matriz
        ttk.Button(left_frame, text="Guardar matriz", command=self.guardar_matriz).pack(pady=10)

        # Botón para añadir matriz identidad
        ttk.Button(left_frame, text="Añadir matriz identidad", command=self.anadir_identidad).pack(pady=5)

        # Sección de operaciones
        operaciones_label = ttk.Label(left_frame, text="Operaciones", style='Header.TLabel')
        operaciones_label.pack(pady=10)

        # Frame para seleccionar matrices
        select_frame = ttk.Frame(left_frame)
        select_frame.pack(pady=5)

        ttk.Label(select_frame, text="Matriz A:").grid(row=0, column=0, padx=5)
        self.matriz_a_var = tk.StringVar()
        self.matriz_a_combo = ttk.Combobox(select_frame, textvariable=self.matriz_a_var, width=5, state="readonly")
        self.matriz_a_combo.grid(row=0, column=1, padx=5)

        ttk.Label(select_frame, text="Matriz B:").grid(row=0, column=2, padx=5)
        self.matriz_b_var = tk.StringVar()
        self.matriz_b_combo = ttk.Combobox(select_frame, textvariable=self.matriz_b_var, width=5, state="readonly")
        self.matriz_b_combo.grid(row=0, column=3, padx=5)

        # Botones de operaciones
        op_frame = ttk.Frame(left_frame)
        op_frame.pack(pady=5)

        # Primera fila de botones
        ttk.Button(op_frame, text="A + B", command=lambda: self.realizar_operacion('suma')).grid(row=0, column=0,
                                                                                                 padx=5, pady=5)
        ttk.Button(op_frame, text="A - B", command=lambda: self.realizar_operacion('resta')).grid(row=0, column=1,
                                                                                                  padx=5, pady=5)
        ttk.Button(op_frame, text="A × B", command=lambda: self.realizar_operacion('multiplicacion')).grid(row=0,
                                                                                                           column=2,
                                                                                                           padx=5,
                                                                                                           pady=5)

        # Segunda fila de botones
        ttk.Button(op_frame, text="Det(A)", command=lambda: self.realizar_operacion('determinante')).grid(row=1,
                                                                                                          column=0,
                                                                                                          padx=5,
                                                                                                          pady=5)
        ttk.Button(op_frame, text="Inv(A)", command=lambda: self.realizar_operacion('inversa')).grid(row=1, column=1,
                                                                                                     padx=5, pady=5)
        ttk.Button(op_frame, text="Gauss-Jordan", command=lambda: self.realizar_operacion('gauss')).grid(row=1,
                                                                                                         column=2,
                                                                                                         padx=5, pady=5)

        # Tercera fila de botones
        ttk.Label(op_frame, text="Escalar:").grid(row=2, column=0, padx=5, pady=5)
        self.escalar_var = tk.StringVar(value="2")
        ttk.Entry(op_frame, textvariable=self.escalar_var, width=5).grid(row=2, column=1, padx=5, pady=5)
        ttk.Button(op_frame, text="A × escalar", command=lambda: self.realizar_operacion('escalar')).grid(row=2,
                                                                                                          column=2,
                                                                                                          padx=5,
                                                                                                          pady=5)

        # Botón para resolver sistemas (Cramer)
        ttk.Button(op_frame, text="Resolver sistema (Cramer)", command=lambda: self.realizar_operacion('cramer')).grid(
            row=3, column=0, columnspan=3, padx=5, pady=5)

        # Cuarto botón para guardar resultado
        ttk.Button(op_frame, text="Guardar resultado", command=self.guardar_resultado).grid(row=4, column=0,
                                                                                            columnspan=3, padx=5,
                                                                                            pady=5)

        # Sección para mostrar matrices y resultados
        matrices_label = ttk.Label(right_frame, text="Matrices Almacenadas", style='Header.TLabel')
        matrices_label.pack(pady=10)

        # Área de texto para mostrar matrices
        self.matrices_text = scrolledtext.ScrolledText(right_frame, width=40, height=15)
        self.matrices_text.pack(fill=tk.BOTH, expand=True, pady=5)

        # Sección para mostrar resultados
        resultados_label = ttk.Label(right_frame, text="Resultado", style='Header.TLabel')
        resultados_label.pack(pady=10)

        # Área de texto para mostrar resultados
        self.resultados_text = scrolledtext.ScrolledText(right_frame, width=40, height=10)
        self.resultados_text.pack(fill=tk.BOTH, expand=True, pady=5)

        # Actualizar listas de matrices
        self.actualizar_listas_matrices()

    def generar_campos(self):
        # Limpiar frame anterior
        for widget in self.matriz_frame.winfo_children():
            widget.destroy()

        try:
            filas = int(self.filas_var.get())
            columnas = int(self.columnas_var.get())

            if filas <= 0 or columnas <= 0:
                raise ValueError("Filas y columnas deben ser positivas")

            # Crear canvas para scroll si es necesario
            canvas = tk.Canvas(self.matriz_frame)
            scrollbar = ttk.Scrollbar(self.matriz_frame, orient="vertical", command=canvas.yview)
            scrollable_frame = ttk.Frame(canvas)

            scrollable_frame.bind(
                "<Configure>",
                lambda e: canvas.configure(
                    scrollregion=canvas.bbox("all")
                )
            )

            canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
            canvas.configure(yscrollcommand=scrollbar.set)

            canvas.pack(side="left", fill="both", expand=True)
            scrollbar.pack(side="right", fill="y")

            # Crear campos de entrada
            self.entradas_matriz = []
            for i in range(filas):
                fila_entries = []
                for j in range(columnas):
                    entry = ttk.Entry(scrollable_frame, width=5)
                    entry.grid(row=i, column=j, padx=2, pady=2)
                    entry.insert(0, "0")
                    fila_entries.append(entry)
                self.entradas_matriz.append(fila_entries)

        except ValueError as e:
            messagebox.showerror("Error", str(e))

    def guardar_matriz(self):
        try:
            if not hasattr(self, 'entradas_matriz') or not self.entradas_matriz:
                raise ValueError("No hay matriz para guardar")

            filas = len(self.entradas_matriz)
            columnas = len(self.entradas_matriz[0])

            # Crear matriz de numpy con fracciones
            matriz_datos = []
            for i in range(filas):
                fila = []
                for j in range(columnas):
                    valor_str = self.entradas_matriz[i][j].get().strip()
                    # Manejar fracciones y decimales
                    if '/' in valor_str:
                        num, den = valor_str.split('/')
                        valor = float(int(num) / int(den))
                    else:
                        valor = float(valor_str)
                    fila.append(valor)
                matriz_datos.append(fila)

            matriz = np.array(matriz_datos, dtype=float)
            self.matrices.append(matriz)

            messagebox.showinfo("Éxito", f"Matriz guardada con índice {len(self.matrices) - 1}")
            self.actualizar_listas_matrices()

        except Exception as e:
            messagebox.showerror("Error", f"Error al guardar matriz: {str(e)}")

    def anadir_identidad(self):
        try:
            n = int(self.filas_var.get())
            if n <= 0:
                raise ValueError("El tamaño debe ser positivo")

            identidad = np.eye(n)
            self.matrices.append(identidad)

            messagebox.showinfo("Éxito", f"Matriz identidad {n}x{n} guardada con índice {len(self.matrices) - 1}")
            self.actualizar_listas_matrices()

        except ValueError as e:
            messagebox.showerror("Error", str(e))

    def actualizar_listas_matrices(self):
        # Actualizar comboboxes
        indices = [str(i) for i in range(len(self.matrices))]
        self.matriz_a_combo['values'] = indices
        self.matriz_b_combo['values'] = indices

        if indices:
            self.matriz_a_combo.current(0)
            self.matriz_b_combo.current(0)

        # Actualizar texto
        self.matrices_text.delete(1.0, tk.END)
        for i, m in enumerate(self.matrices):
            self.matrices_text.insert(tk.END, f"Matriz {i}:\n")
            self.matrices_text.insert(tk.END, self.formato_matriz(m) + "\n\n")

    def formato_matriz(self, matriz, precision=4):
        # Verificar si es un número o una matriz
        if not isinstance(matriz, np.ndarray):
            return str(matriz)

        # Si es vector columna (resultado de Cramer), formatearlo especialmente
        if matriz.shape[1] == 1 if len(matriz.shape) > 1 else False:
            resultado = ""
            for i in range(matriz.shape[0]):
                valor = matriz[i, 0]
                if abs(valor - round(valor)) < 1e-10:  # Si es prácticamente un entero
                    resultado += f"x{i + 1} = {int(valor)}\n"
                else:
                    # Intentar convertir a fracción para mejor visualización
                    try:
                        frac = Fraction(float(valor)).limit_denominator(1000)
                        if frac.denominator != 1:
                            resultado += f"x{i + 1} = {frac.numerator}/{frac.denominator} ≈ {valor:.{precision}f}\n"
                        else:
                            resultado += f"x{i + 1} = {frac.numerator}\n"
                    except:
                        resultado += f"x{i + 1} = {valor:.{precision}f}\n"
            return resultado

        filas, columnas = matriz.shape
        resultado = ""
        for i in range(filas):
            for j in range(columnas):
                valor = matriz[i, j]
                # Si es casi un entero, mostrarlo como entero
                if abs(valor - round(valor)) < 1e-10:
                    resultado += f"{int(valor):>6} "
                else:
                    # Intentar mostrar como fracción si es apropiado
                    try:
                        frac = Fraction(float(valor)).limit_denominator(100)
                        if frac.denominator != 1 and frac.denominator <= 10:
                            resultado += f"{frac.numerator}/{frac.denominator:>6} "
                        else:
                            resultado += f"{valor:>6.{precision}f} "
                    except:
                        resultado += f"{valor:>6.{precision}f} "
            resultado += "\n"
        return resultado

    def guardar_resultado(self):
        if self.resultado_actual is not None:
            self.matrices.append(self.resultado_actual)
            messagebox.showinfo("Éxito", f"Resultado guardado como matriz {len(self.matrices) - 1}")
            self.actualizar_listas_matrices()
        else:
            messagebox.showwarning("Advertencia", "No hay resultado para guardar")

    def realizar_operacion(self, operacion):
        try:
            self.resultados_text.delete(1.0, tk.END)

            if not self.matrices:
                raise ValueError("No hay matrices almacenadas")

            # Para operaciones que requieren una sola matriz
            if operacion in ['determinante', 'inversa', 'gauss', 'escalar', 'cramer']:
                indice_a = int(self.matriz_a_var.get())
                A = self.matrices[indice_a]

                if operacion == 'determinante':
                    if A.shape[0] != A.shape[1]:
                        raise ValueError("El determinante solo se puede calcular para matrices cuadradas")
                    resultado = np.linalg.det(A)

                    # Intentar mostrar como fracción si es apropiado
                    try:
                        frac = Fraction(float(resultado)).limit_denominator(1000)
                        if frac.denominator != 1:
                            resultado_str = f"Determinante: {frac.numerator}/{frac.denominator} ≈ {resultado:.6f}"
                        else:
                            resultado_str = f"Determinante: {frac.numerator}"
                    except:
                        resultado_str = f"Determinante: {resultado:.6f}"

                    self.resultados_text.insert(tk.END, resultado_str)
                    self.resultado_actual = None

                elif operacion == 'inversa':
                    if A.shape[0] != A.shape[1]:
                        raise ValueError("La inversa solo se puede calcular para matrices cuadradas")

                    # Registrar pasos para mostrar
                    pasos = [f"Calculando la inversa de la matriz {indice_a}:"]

                    # Verificar si el determinante es cero
                    det = np.linalg.det(A)
                    if abs(det) < 1e-10:
                        raise ValueError("La matriz no tiene inversa porque su determinante es 0")

                    pasos.append(f"Determinante: {det:.6f}")

                    # Calcular la inversa
                    resultado = np.linalg.inv(A)

                    # Mostrar pasos y resultado
                    for paso in pasos:
                        self.resultados_text.insert(tk.END, paso + "\n")
                    self.resultados_text.insert(tk.END, "\nMatriz inversa:\n")
                    self.resultados_text.insert(tk.END, self.formato_matriz(resultado))
                    self.resultado_actual = resultado

                elif operacion == 'gauss':
                    # Implementación de Gauss-Jordan con pasos
                    filas, columnas = A.shape
                    # Crear matriz aumentada si es necesario
                    if columnas > filas:
                        # Asumir que ya es una matriz aumentada [A|b]
                        matriz_aum = A.copy()
                    else:
                        # Crear matriz aumentada con identidad
                        matriz_aum = np.hstack((A, np.eye(filas)))

                    pasos = ["Pasos de eliminación Gauss-Jordan:"]
                    matriz_original = matriz_aum.copy()

                    # Algoritmo de Gauss-Jordan con registro de pasos
                    for i in range(filas):
                        # Buscar pivote adecuado
                        if abs(matriz_aum[i, i]) < 1e-10:
                            # Buscar fila con elemento no-cero
                            for j in range(i + 1, filas):
                                if abs(matriz_aum[j, i]) > 1e-10:
                                    # Intercambiar filas
                                    matriz_aum[[i, j]] = matriz_aum[[j, i]]
                                    pasos.append(f"Intercambiar fila {i + 1} con fila {j + 1}")
                                    break
                            else:
                                if i < filas - 1:  # Si no es la última fila
                                    pasos.append(f"Advertencia: Pivote cero en fila {i + 1}")
                                continue  # Ir a la siguiente columna si no hay intercambio

                        # Dividir la fila por el pivote
                        pivote = matriz_aum[i, i]
                        if abs(pivote) < 1e-10:
                            pasos.append(f"Pivote cero en fila {i + 1}, continuando...")
                            continue

                        matriz_aum[i, :] = matriz_aum[i, :] / pivote
                        pasos.append(f"Dividir fila {i + 1} por {pivote:.4f}")

                        # Hacer ceros arriba y abajo del pivote
                        for j in range(filas):
                            if i != j:
                                factor = matriz_aum[j, i]
                                matriz_aum[j, :] = matriz_aum[j, :] - factor * matriz_aum[i, :]
                                pasos.append(f"Restar {factor:.4f} veces la fila {i + 1} de la fila {j + 1}")

                    # Mostrar pasos y resultado
                    for paso in pasos:
                        self.resultados_text.insert(tk.END, paso + "\n")

                    self.resultados_text.insert(tk.END, "\nMatriz original:\n")
                    self.resultados_text.insert(tk.END, self.formato_matriz(matriz_original))

                    self.resultados_text.insert(tk.END, "\nResultado final (forma escalonada reducida):\n")
                    self.resultados_text.insert(tk.END, self.formato_matriz(matriz_aum))

                    # Si era cuadrada, la parte derecha es la inversa
                    if A.shape[0] == A.shape[1]:
                        resultado = matriz_aum[:, filas:]
                        self.resultados_text.insert(tk.END, "\nParte derecha (inversa si la matriz era cuadrada):\n")
                        self.resultados_text.insert(tk.END, self.formato_matriz(resultado))
                    else:
                        resultado = matriz_aum

                    self.resultado_actual = resultado

                elif operacion == 'escalar':
                    escalar = float(self.escalar_var.get())
                    resultado = escalar * A
                    self.resultados_text.insert(tk.END, f"Matriz {indice_a} multiplicada por {escalar}:\n")
                    self.resultados_text.insert(tk.END, self.formato_matriz(resultado))
                    self.resultado_actual = resultado

                elif operacion == 'cramer':
                    # La matriz debe ser aumentada [A|b] donde A es cuadrada
                    filas, columnas = A.shape

                    if columnas != filas + 1:
                        raise ValueError("Para usar Cramer, la matriz debe ser aumentada [A|b] con una columna extra")

                    # Extraer A y b
                    coef = A[:, :-1]
                    const = A[:, -1:]

                    # Verificar determinante
                    det_A = np.linalg.det(coef)
                    if abs(det_A) < 1e-10:
                        raise ValueError("El sistema no tiene solución única (det(A) = 0)")

                    # Resolver el sistema
                    # Para matrices pequeñas, usar directamente el método de Cramer
                    if filas <= 4:  # Cramer es ineficiente para matrices grandes
                        pasos = ["Resolviendo por regla de Cramer:"]
                        pasos.append(f"Determinante de A = {det_A:.6f}")

                        # Vector para almacenar soluciones
                        soluciones = np.zeros((filas, 1))

                        for i in range(filas):
                            # Crear matriz Ai
                            A_i = coef.copy()
                            A_i[:, i] = const.flatten()  # Reemplazar columna i con vector b

                            # Calcular determinante
                            det_A_i = np.linalg.det(A_i)

                            # Calcular solución
                            x_i = det_A_i / det_A
                            soluciones[i, 0] = x_i

                            # Agregar paso
                            pasos.append(f"Det(A{i + 1}) = {det_A_i:.6f}")
                            pasos.append(f"x{i + 1} = Det(A{i + 1})/Det(A) = {x_i:.6f}")

                        # Mostrar pasos
                        for paso in pasos:
                            self.resultados_text.insert(tk.END, paso + "\n")

                        resultado = soluciones
                    else:
                        # Para matrices grandes usar solucionador directo
                        resultado = np.linalg.solve(coef, const)

                    self.resultados_text.insert(tk.END, "\nSolución del sistema:\n")
                    self.resultados_text.insert(tk.END, self.formato_matriz(resultado))
                    self.resultado_actual = resultado

            # Para operaciones que requieren dos matrices
            else:
                indice_a = int(self.matriz_a_var.get())
                indice_b = int(self.matriz_b_var.get())
                A = self.matrices[indice_a]
                B = self.matrices[indice_b]

                if operacion == 'suma':
                    if A.shape != B.shape:
                        raise ValueError("Las matrices deben tener las mismas dimensiones para la suma")
                    resultado = A + B
                    self.resultados_text.insert(tk.END, f"Suma de matrices {indice_a} y {indice_b}:\n")

                elif operacion == 'resta':
                    if A.shape != B.shape:
                        raise ValueError("Las matrices deben tener las mismas dimensiones para la resta")
                    resultado = A - B
                    self.resultados_text.insert(tk.END, f"Resta de matrices {indice_a} - {indice_b}:\n")

                elif operacion == 'multiplicacion':
                    if A.shape[1] != B.shape[0]:
                        raise ValueError(
                            f"Dimensiones incompatibles: ({A.shape[0]}×{A.shape[1]}) × ({B.shape[0]}×{B.shape[1]})")
                    resultado = np.matmul(A, B)
                    self.resultados_text.insert(tk.END, f"Multiplicación de matrices {indice_a} × {indice_b}:\n")

                self.resultados_text.insert(tk.END, self.formato_matriz(resultado))
                self.resultado_actual = resultado

        except Exception as e:
            messagebox.showerror("Error", str(e))
            self.resultado_actual = None


if __name__ == "__main__":
    root = tk.Tk()
    app = MatrizApp(root)
    root.mainloop()