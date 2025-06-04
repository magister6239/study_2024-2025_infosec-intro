import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider


verts = np.array([
    [ 1,  0,  1],
    [-1,  0,  1],
    [-1,  0, -1],
    [ 1,  0, -1],
    [ 0,  2,  0]
])

faces = [(0, 1, 4), (1, 2, 4), (2, 3, 4), (3, 0, 4), (0, 1, 2, 3)]
edges = set()
for f in faces:
    for i in range(len(f)):
        a, b = f[i], f[(i + 1) % len(f)]
        edges.add(tuple(sorted((a, b))))
edges = list(edges)

basis3d = np.eye(3)

def rot_X(theta_deg):
    theta = np.radians(theta_deg)
    return np.array([
        [1,       0,        0, 0],
        [0,  np.cos(theta), -np.sin(theta), 0],
        [0,  np.sin(theta),  np.cos(theta), 0],
        [0,       0,        0, 1]
    ], dtype=float)

def rot_Y(theta_deg):
    theta = np.radians(theta_deg)
    return np.array([
        [ np.cos(theta), 0, np.sin(theta), 0],
        [       0,   1,       0,   0],
        [-np.sin(theta), 0, np.cos(theta), 0],
        [       0,   0,       0,   1]
    ], dtype=float)

def rot_Z(theta_deg):
    theta = np.radians(theta_deg)
    return np.array([
        [np.cos(theta), -np.sin(theta), 0, 0],
        [np.sin(theta),  np.cos(theta), 0, 0],
        [      0,         0,    1, 0],
        [      0,         0,    0, 1]
    ], dtype=float)

def oblique_matrix(alpha_deg, beta_deg):
    alpha = np.radians(alpha_deg)
    beta = np.radians(beta_deg)
    tan_beta = np.tan(beta)
    f = 1.0 / tan_beta

    return np.array([
        [ 1,                 0,                  0, 1],
        [ 0,                 1,                  0, 0],
        [-f * np.cos(alpha), -f * np.sin(beta),  0, 0],
        [ 0,                 0,                  0, 1]
    ])

def oriented_area(tri2d):
    (x1, y1), (x2, y2), (x3, y3) = tri2d
    return 0.5 * ((x2 - x1) * (y3 - y1) - (x3 - x1) * (y2 - y1))

def draw(ax, alpha, beta, rx, ry, rz):
    ax.clear()
    ax.set_aspect("equal")
    ax.set_xlim(-3, 3)
    ax.set_ylim(-3, 3)
    ax.grid(True)

    R = rot_Z(rz) @ rot_Y(ry) @ rot_X(rx)
    M_obl = oblique_matrix(alpha, beta)
    P_full = M_obl @ R

    N = verts.shape[0]
    verts_hom = np.hstack([verts, np.ones((N,1))])

    proj_hom = verts_hom @ P_full.T
    proj2d = proj_hom[:, :2]

    hidden = set()
    for face in faces[:-1]:
        tri2d = proj2d[list(face)]
        if oriented_area(tri2d) < 0:
            for i in range(3):
                e = tuple(sorted((face[i], face[(i + 1) % 3])))
                hidden.add(e)

    for e in edges:
        if e in hidden:
            P1, P2 = proj2d[e[0]], proj2d[e[1]]
            ax.plot([P1[0], P2[0]], [P1[1], P2[1]], "-", linewidth=2, color="black")

    for e in edges:
        if e not in hidden:
            P1, P2 = proj2d[e[0]], proj2d[e[1]]
            ax.plot([P1[0], P2[0]], [P1[1], P2[1]], "-", linewidth=2, color="gray")

    mult = 8
    colors = "rgb"
    for i, c in enumerate(colors):
        e3 = basis3d[i]
        e4 = np.array([*e3, 0])
        p4 = P_full @ e4
        x2, y2 = p4[0], p4[1]
        ax.plot([-x2 * mult, x2 * mult], [-y2 * mult, y2 * mult], color=c, linewidth=1)

    fx = np.linalg.norm(P_full[:2, 0])
    fy = np.linalg.norm(P_full[:2, 1])
    fz = np.linalg.norm(P_full[:2, 2])
    cotb = 1 / np.tan(np.radians(beta))
    ax.set_title(
        f"alpha={alpha:.1f}, beta={beta:.1f} (cot_beta={cotb:.2f})  |  "
        f"rx={rx:.1f}, ry={ry:.1f}, rz={rz:.1f}  →  "
        f"fx={fx:.2f}, fy={fy:.2f}, fz={fz:.2f}"
    )

alpha0, beta0 = 0, 45
rx0, ry0, rz0 = 30, 30, 30

fig, ax = plt.subplots(figsize=(8, 8))
plt.subplots_adjust(left=0.25, bottom=0.50)

draw(ax, alpha0, beta0, rx0, ry0, rz0)

ax_a  = plt.axes([0.25, 0.40, 0.65, 0.03])
ax_b  = plt.axes([0.25, 0.35, 0.65, 0.03])
ax_rx = plt.axes([0.25, 0.30, 0.65, 0.03])
ax_ry = plt.axes([0.25, 0.25, 0.65, 0.03])
ax_rz = plt.axes([0.25, 0.20, 0.65, 0.03])

slider_a  = Slider(ax_a,  "alpha (deg)",      1, 179, valinit=alpha0)
slider_b  = Slider(ax_b,  "beta (deg)" ,      1, 179, valinit=beta0)
slider_rx = Slider(ax_rx, "rotX (deg)" ,      0, 360, valinit=rx0)
slider_ry = Slider(ax_ry, "rotY (deg)" ,      0, 360, valinit=ry0)
slider_rz = Slider(ax_rz, "rotZ (deg)" ,      0, 360, valinit=rz0)

def on_change(_):
    draw(ax,
         slider_a.val,
         slider_b.val,
         slider_rx.val,
         slider_ry.val,
         slider_rz.val)

for s in (slider_a, slider_b, slider_rx, slider_ry, slider_rz):
    s.on_changed(on_change)

plt.show()
