# Originally written by... I don't know? Janine? Justin?
# Modified in Winter 2022 by Suraj to draw histograms

from matplotlib.animation import FuncAnimation
import matplotlib.pyplot as plt
import numpy as np

def sampling_animation(population):
    sizes = np.arange(1, 251, 5)
    medians = np.array([])
    np.random.seed(4242)
    for _ in range(sizes[-1]):
        s = population.sample(500)
        m = np.median(s.get('TotalWages'))
        medians = np.append(medians, m)

    bins = np.arange(60000, 85000, 1000)
    n, _ = np.histogram(medians[:1], bins)

    def prepare_animation(bar_container):
        def animate(i):
            plot_data = medians[:sizes[i]]
            n, _ = np.histogram(plot_data, bins)
            for count, rect in zip(n, bar_container.patches):
                rect.set_height(count)
            return bar_container.patches
        return animate

    fig, ax = plt.subplots(figsize=(10, 5))
    _, _, bar_container = ax.hist(medians, bins, density=True,
                                  ec='w');
    ax.set_ylim(top=35)

    ani = FuncAnimation(fig, 
                                  prepare_animation(bar_container), 
                                  frames=50,
                                  repeat=False, blit=True);

    return ani, medians
