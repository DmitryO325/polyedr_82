#!/usr/bin/env -S python3 -B

from time import time
from common.tk_drawer import TkDrawer, x, y
from preoptimize.polyedr import Polyedr


def draw_line(self, p, q):
    self.canvas.create_line(x(p), y(p), x(q), y(q), fill="black", width=1)


setattr(TkDrawer, 'draw_line', draw_line)

tk = TkDrawer()

try:
    for name in ["figure_1", "figure_2", "ccc", "cube", "box"]:
        print("=======================================================")
        print(f"Начало работы с полиэдром '{name}'")
        start_init_time = time()
        print("Инициализация -------------------------> ", end="", flush=True)
        poly = Polyedr(f"data/{name}.geom")
        start_shadow_time = time()
        print("%6.2f сек." % (start_shadow_time - start_init_time))
        print("Удаление невидимых линий --------------> ", end="", flush=True)
        poly.shadow()
        start_draw_time = time()
        print("%6.2f сек." % (start_draw_time - start_shadow_time))
        print("Изображение полиэдра ------------------> ", end="", flush=True)
        print("%6.2f сек." % (time() - start_draw_time))
        poly.count_area()
        print(f"Сумма площадей проекций граней: {round(poly.area, 14)}")
        poly.draw(tk)
        tk.root.update()
        input("Hit 'Return' to continue -> ")
except (EOFError, KeyboardInterrupt):
    print("\nStop")
    tk.close()
