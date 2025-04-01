import numpy as np
import matplotlib
matplotlib.use('Agg')  # Start with Agg for saving GIF
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from PIL import Image

# Define the function and integral parameters
def f(x):
    return 1 / (1 + x**2)

x = np.linspace(0, 1, 1000)
y = f(x)
n_max = 200  # Maximum number of rectangles

# --- Save GIF with Agg backend ---
# Setup figure for saving
fig_save, ax_save = plt.subplots(figsize=(10, 6))
ax_save.plot(x, y, 'b-', label=r'$f(x) = \frac{1}{1 + x^2}$')
ax_save.set_xlim(0, 1)
ax_save.set_ylim(0, 1.2)
ax_save.set_title(r'Area Under $\frac{1}{1 + x^2}$ from 0 to 1 $\approx \pi/4$')
ax_save.set_xlabel('x')
ax_save.set_ylabel('f(x)')
ax_save.axhline(0, color='gray', alpha=0.5)
ax_save.grid(True, alpha=0.3)

# Initial elements for saving
rects_save = ax_save.fill_between([], [], 0, color='blue', alpha=0.3, label='Riemann Sum')
text_save = ax_save.text(0.5, 1.0, '', ha='center', fontsize=12)

# Animation initialization for saving
def init_save():
    rects_save = ax_save.fill_between([], [], 0, color='blue', alpha=0.3)
    text_save.set_text('')
    ax_save.legend()
    return rects_save, text_save

# Animation update function for saving
def update_save(frame):
    n_rects = frame + 1
    x_rects = np.linspace(0, 1, n_rects + 1)[:-1]
    dx = 1 / n_rects
    heights = f(x_rects)
    area = np.sum(heights * dx)
    
    global rects_save
    rects_save.remove()
    rects_save = ax_save.fill_between(x_rects, 0, heights, step='post', color='blue', alpha=0.3)
    
    text_save.set_text(f'Rectangles: {n_rects}\nArea: {area:.6f}\nTarget: π/4 ≈ 0.785398')
    return rects_save, text_save

# Create animation for saving
ani_save = FuncAnimation(fig_save, update_save, frames=range(n_max), init_func=init_save, interval=100, blit=False)

# Save frames and create infinite-loop GIF
frames = []
for frame in range(n_max):
    update_save(frame)
    fig_save.canvas.draw()
    frame_img = np.frombuffer(fig_save.canvas.tostring_rgb(), dtype='uint8')
    frame_img = frame_img.reshape(fig_save.canvas.get_width_height()[::-1] + (3,))
    frames.append(Image.fromarray(frame_img))

frames[0].save('riemann_area_pi4.gif', save_all=True, append_images=frames[1:], 
               duration=100, loop=0)

# Close the Agg figure to free resources
plt.close(fig_save)

# --- Display animation with interactive backend ---
# Switch to an interactive backend (e.g., TkAgg or default)
matplotlib.use('TkAgg')  # Use TkAgg for display (or omit for default backend on macOS)

# Recreate figure for display
fig_display, ax_display = plt.subplots(figsize=(10, 6))
ax_display.plot(x, y, 'b-', label=r'$f(x) = \frac{1}{1 + x^2}$')
ax_display.set_xlim(0, 1)
ax_display.set_ylim(0, 1.2)
ax_display.set_title(r'Area Under $\frac{1}{1 + x^2}$ from 0 to 1 $\approx \pi/4$')
ax_display.set_xlabel('x')
ax_display.set_ylabel('f(x)')
ax_display.axhline(0, color='gray', alpha=0.5)
ax_display.grid(True, alpha=0.3)

# Initial elements for display
rects_display = ax_display.fill_between([], [], 0, color='blue', alpha=0.3, label='Riemann Sum')
text_display = ax_display.text(0.5, 1.0, '', ha='center', fontsize=12)

# Animation initialization for display
def init_display():
    rects_display = ax_display.fill_between([], [], 0, color='blue', alpha=0.3)
    text_display.set_text('')
    ax_display.legend()
    return rects_display, text_display

# Animation update function for display
def update_display(frame):
    n_rects = frame + 1
    x_rects = np.linspace(0, 1, n_rects + 1)[:-1]
    dx = 1 / n_rects
    heights = f(x_rects)
    area = np.sum(heights * dx)
    
    global rects_display
    rects_display.remove()
    rects_display = ax_display.fill_between(x_rects, 0, heights, step='post', color='blue', alpha=0.3)
    
    text_display.set_text(f'Rectangles: {n_rects}\nArea: {area:.6f}\nTarget: π/4 ≈ 0.785398')
    return rects_display, text_display

# Create animation for display
ani_display = FuncAnimation(fig_display, update_display, frames=range(n_max), init_func=init_display, interval=100, blit=True)

# Display the animation
plt.show()
