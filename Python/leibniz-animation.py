import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from PIL import Image

n_terms = 200  # Adjust as needed

def leibniz_partial_sum(n_terms):
    n = np.arange(n_terms)
    terms = (-1)**n / (2 * n + 1)
    return np.cumsum(terms)

# Setup plot
fig, ax = plt.subplots(figsize=(10, 6))
ax.set_xlim(0, n_terms)
ax.set_ylim(0.6, 1.0)  # Better focus on convergence
ax.set_title('Leibniz Series: Convergence to π/4')
ax.set_xlabel('Number of Terms')
ax.set_ylabel('Partial Sum')
ax.axhline(np.pi/4, color='r', linestyle='--', label='π/4 ≈ 0.7854')
ax.grid(True, alpha=0.3)

line, = ax.plot([], [], 'b-', label='Leibniz Series')
text_sum = ax.text(n_terms / 2, 0.95, '', ha='center', fontsize=10)
text_gap = ax.text(n_terms / 2, 0.90, '', ha='center', fontsize=10, color='purple')
ax.legend()

# Generate frames for GIF
frames = []
for frame in range(n_terms):
    partial_sums = leibniz_partial_sum(frame + 1)
    x_data = np.arange(1, frame + 2)
    line.set_data(x_data, partial_sums)
    current_sum = partial_sums[-1]
    gap = abs(current_sum - np.pi / 4)
    text_sum.set_text(f'Terms: {frame + 1}  |  Sum: {current_sum:.6f}')
    text_gap.set_text(f'Gap to π/4: {gap:.6f}')
    fig.canvas.draw()
    frames.append(Image.fromarray(np.array(fig.canvas.renderer.buffer_rgba())))

# Save GIF
frames[0].save(
    'leibniz_convergence.gif',
    save_all=True,
    append_images=frames[1:],
    duration=100,
    loop=0  # Infinite loop
)

plt.close()  # Prevents duplicate display if running in a notebook
