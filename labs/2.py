import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
from matplotlib.patches import Polygon


def oblique_2x3_matrix(alpha_deg, beta_deg):
    alpha = np.radians(alpha_deg)
    beta = np.radians(beta_deg)
    tan_beta = np.tan(beta)
    f = 1 / tan_beta

    return np.array([
        [1, 0, -f * np.cos(alpha)],
        [0, 1, -f * np.sin(beta)]
    ], dtype=float)

alpha_obl = 0
beta_obl = 45
P_obl = oblique_2x3_matrix(alpha_obl, beta_obl)

GRID_SIZE = 16

verts = np.array([
    [ 0.5, 0,  0.5],
    [-0.5, 0,  0.5],
    [-0.5, 0, -0.5],
    [ 0.5, 0, -0.5],
    [ 0,   1,  0]
])

faces = [(0, 1, 4), (1, 2, 4), (2, 3, 4), (3, 0, 4)]
edges = [(0, 1), (1, 2), (2, 3), (3, 0), (0, 4), (1, 4), (2, 4), (3, 4)]

def oriented_area(tri2d):
    (x1, y1), (x2, y2), (x3, y3) = tri2d
    return 0.5 * ((x2 - x1) * (y3 - y1) - (x3 - x1) * (y2 - y1))

def draw(ax, tx, ty, tz, rot_deg):
    ax.clear()
    ax.set_aspect("equal")
    ax.set_axis_off()

    for i in range(GRID_SIZE):
        for j in range(GRID_SIZE):
            square = np.array([
                [i    , 0, j    ],
                [i + 1, 0, j    ],
                [i + 1, 0, j + 1],
                [i    , 0, j + 1]
            ])
            proj_sq = square @ P_obl.T
            color = "blue" if (i + j) % 2 == 0 else "red"
            ax.add_patch(Polygon(
                proj_sq,
                closed=True,
                facecolor=color,
                edgecolor="black",
                linewidth=0.3
            ))

    theta = np.radians(rot_deg)
    R_axis = np.array([
        [ np.cos(theta), 0, np.sin(theta)],
        [ 0,             1, 0            ],
        [-np.sin(theta), 0, np.cos(theta)]
    ])
    verts_rot = verts @ R_axis.T * 2

    verts_world = verts_rot + np.array([tx, ty, tz])

    proj_pts = verts_world @ P_obl.T

    basis3d = np.eye(3)
    mult = 8
    colors = "rgb"
    for i, c in enumerate(colors):
        e3 = basis3d[i]
        p2 = P_obl @ e3
        x2, y2 = p2[0], p2[1]
        ax.plot(
            [-x2 * mult, x2 * mult],
            [-y2 * mult, y2 * mult],
            color=c, linewidth=1
        )

    hidden = set()
    for f in faces:
        tri = proj_pts[list(f)]
        if oriented_area(tri) > 0:
            for i in range(len(f)):
                hidden.add(tuple(sorted((f[i], f[(i + 1) % len(f)]))))

    hidden_edges = set()
    for f in faces:
        tri2d = proj_pts[list(f)]
        if oriented_area(tri2d) > 0:
            for k in range(3):
                e = tuple(sorted((f[k], f[(k + 1) % 3])))
                hidden_edges.add(e)

    for f in faces:
        tri2d = proj_pts[list(f)]
        if oriented_area(tri2d) < 0:
            ax.add_patch(
                Polygon(tri2d, closed=True,
                        facecolor="gray", edgecolor="black")
            )

    lim = GRID_SIZE / 2
    ax.set_xlim(-lim, lim)
    ax.set_ylim(-lim, lim)
    plt.draw()

fig, ax = plt.subplots(figsize=(8, 8))
plt.subplots_adjust(left=0.25, bottom=0.35)

tx0, ty0, tz0, rot0 = 2, 0, 2, 0
draw(ax, tx0, ty0, tz0, rot0)

ax_x   = plt.axes([0.25, 0.25, 0.65, 0.03])
ax_y   = plt.axes([0.25, 0.20, 0.65, 0.03])
ax_z   = plt.axes([0.25, 0.15, 0.65, 0.03])
ax_rot = plt.axes([0.25, 0.10, 0.65, 0.03])

slider_x   = Slider(ax_x,    "X", valmin = -GRID_SIZE // 2, valmax = GRID_SIZE // 2, valinit = tx0, valstep=1)
slider_y   = Slider(ax_y,    "Y", valmin = 0,               valmax = 5,              valinit = ty0, valstep=1)
slider_z   = Slider(ax_z,    "Z", valmin = -GRID_SIZE // 2, valmax = GRID_SIZE // 2, valinit = tz0, valstep=1)
slider_rot = Slider(ax_rot,  "R", valmin = 0,               valmax =360,             valinit = rot0)

def update(_):
    draw(ax,
         slider_x.val,
         slider_y.val,
         slider_z.val,
         slider_rot.val)

for s in (slider_x, slider_y, slider_z, slider_rot):
    s.on_changed(update)

plt.show()
