import matplotlib.pyplot as plt


def render_chart(roundabout_links, transition_links, standard_links):
    # Data to plot
    labels = 'Roundabout street links', 'Standard street links', 'Transition street links'
    sizes = [roundabout_links, standard_links, transition_links]
    colors = ['gold', 'yellowgreen', 'orange']
    explode = (0.01, 0.01, 0.01)

    # Plot
    plt.pie(sizes, explode=explode, labels=labels, colors=colors,
            autopct='%1.1f%%', shadow=True, startangle=140)

    plt.axis('equal')
    plt.show()
