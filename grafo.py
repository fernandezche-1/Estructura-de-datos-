import tkinter as tk
from tkinter import messagebox
from collections import deque

# ================== GRAFO ==================
class Grafo:
    def __init__(self, dirigido=False):
        self.dirigido = dirigido
        self.vertices = {}
        self.aristas = []

    def agregar_vertice(self, v):
        if v not in self.vertices:
            self.vertices[v] = []

    def agregar_arista(self, v, w):
        if v in self.vertices and w in self.vertices:
            if (v, w) not in self.aristas:
                self.vertices[v].append(w)
                self.aristas.append((v, w))

                if not self.dirigido:
                    self.vertices[w].append(v)
                    self.aristas.append((w, v))
        else:
            messagebox.showerror("Error", "Los vértices no existen")

    def numVertices(self):
        return len(self.vertices)

    def numAristas(self):
        if self.dirigido:
            return len(self.aristas)
        return len(self.aristas)//2

    def verticesAdyacentes(self, v):
        return self.vertices.get(v, [])

    def esAdyacente(self, v, w):
        return w in self.vertices.get(v, [])

    def tiene_ciclo(self):
        visitado = set()
        stack = set()

        def dfs(v):
            visitado.add(v)
            stack.add(v)

            for vecino in self.vertices[v]:
                if vecino not in visitado:
                    if dfs(vecino):
                        return True
                elif vecino in stack:
                    return True

            stack.remove(v)
            return False

        for v in self.vertices:
            if v not in visitado:
                if dfs(v):
                    return True
        return False

    def bfs(self, inicio):
        visitado = set()
        cola = deque([inicio])
        orden = []

        while cola:
            v = cola.popleft()
            if v not in visitado:
                visitado.add(v)
                orden.append(v)
                for vecino in self.vertices[v]:
                    cola.append(vecino)
        return orden


# ================== APP ==================
class App:
    def __init__(self, root):
        self.root = root
        self.root.title("🚀 GRAFO PRO MAX")
        self.root.geometry("1300x750")
        self.root.config(bg="#020617")

        self.grafo = None
        self.pos = {}
        self.dragging = None

        # ====== PANEL IZQUIERDO ======
        panel = tk.Frame(root, bg="#0f172a", width=300)
        panel.pack(side="left", fill="y")

        tk.Label(panel, text="CONFIGURACIÓN", fg="white", bg="#0f172a", font=("Arial", 14, "bold")).pack(pady=10)

        self.tipo = tk.StringVar(value="No Dirigido")
        tk.OptionMenu(panel, self.tipo, "Dirigido", "No Dirigido").pack(pady=5)

        tk.Button(panel, text="Crear Grafo", command=self.crear_grafo).pack(pady=5)

        tk.Label(panel, text="Nodo:", fg="white", bg="#0f172a").pack()
        self.entry_nodo = tk.Entry(panel)
        self.entry_nodo.pack()

        tk.Button(panel, text="Agregar Nodo", command=self.add_vertice).pack(pady=5)

        tk.Label(panel, text="Arista (v1, v2):", fg="white", bg="#0f172a").pack()
        self.v1 = tk.Entry(panel)
        self.v1.pack()
        self.v2 = tk.Entry(panel)
        self.v2.pack()

        tk.Button(panel, text="Agregar Arista", command=self.add_arista).pack(pady=5)

        tk.Button(panel, text="BFS Animado", command=self.animar_bfs).pack(pady=5)
        tk.Button(panel, text="Detectar Ciclo", command=self.ciclo).pack(pady=5)
        tk.Button(panel, text="Mostrar Info", command=self.info).pack(pady=5)

        self.info_box = tk.Text(panel, height=10, width=35)
        self.info_box.pack(pady=10)

        # ====== CANVAS ======
        self.canvas = tk.Canvas(root, bg="#020617")
        self.canvas.pack(side="right", expand=True, fill="both")

        self.canvas.bind("<Button-1>", self.click)
        self.canvas.bind("<B1-Motion>", self.drag)

    # ================= FUNCIONES =================
    def crear_grafo(self):
        self.grafo = Grafo(dirigido=(self.tipo.get() == "Dirigido"))
        self.pos.clear()
        messagebox.showinfo("OK", "Grafo creado")

    def add_vertice(self):
        v = self.entry_nodo.get()
        if self.grafo and v:
            self.grafo.agregar_vertice(v)
            self.pos[v] = (100 + len(self.pos)*80, 200)
            self.dibujar()

    def add_arista(self):
        v1 = self.v1.get()
        v2 = self.v2.get()
        if self.grafo:
            self.grafo.agregar_arista(v1, v2)
            self.dibujar()

    def ciclo(self):
        if self.grafo.tiene_ciclo():
            messagebox.showinfo("Resultado", "🔥 Tiene ciclo")
        else:
            messagebox.showinfo("Resultado", "✅ No tiene ciclo")

    def animar_bfs(self):
        inicio = self.entry_nodo.get()
        if inicio not in self.grafo.vertices:
            messagebox.showerror("Error", "Nodo inválido")
            return
        orden = self.grafo.bfs(inicio)
        self.animar_lista(orden, 0)

    def animar_lista(self, lista, i):
        if i >= len(lista):
            return
        v = lista[i]
        x, y = self.pos[v]
        self.canvas.create_oval(x-30, y-30, x+30, y+30, fill="#facc15")
        self.root.after(600, lambda: self.animar_lista(lista, i+1))

    def info(self):
        if not self.grafo:
            return

        texto = f"""
Vértices: {self.grafo.numVertices()}
Aristas: {self.grafo.numAristas()}

Lista:
{list(self.grafo.vertices.keys())}

Aristas:
{self.grafo.aristas}
"""
        self.info_box.delete(1.0, tk.END)
        self.info_box.insert(tk.END, texto)

    # ================= DRAG =================
    def click(self, event):
        for v, (x, y) in self.pos.items():
            if (x-25 < event.x < x+25) and (y-25 < event.y < y+25):
                self.dragging = v

    def drag(self, event):
        if self.dragging:
            self.pos[self.dragging] = (event.x, event.y)
            self.dibujar()

    # ================= DIBUJO =================
    def dibujar(self):
        self.canvas.delete("all")

        for (v1, v2) in self.grafo.aristas:
            x1, y1 = self.pos.get(v1, (0,0))
            x2, y2 = self.pos.get(v2, (0,0))

            self.canvas.create_line(x1, y1, x2, y2,
                                    arrow=tk.LAST if self.grafo.dirigido else None,
                                    fill="white", width=2)

        for v, (x, y) in self.pos.items():
            self.canvas.create_oval(x-25, y-25, x+25, y+25, fill="#38bdf8")
            self.canvas.create_text(x, y, text=v, fill="white")


# ================= MAIN =================
root = tk.Tk()
app = App(root)
root.mainloop()