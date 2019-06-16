import chart as chart
from a_star import AStar
import graph_structure as gs
import setup_nodes_and_links as setup


def initialize():
    new_graph = gs.Graph()
    setup.build_graph(new_graph)

    a_star = AStar()
    a_star.search(new_graph, '15', '35')

    standard_links = a_star.standard_links
    transition_links = a_star.transition_links
    roundabout_links = a_star.roundabout_links
    chart.render_chart(roundabout_links, transition_links, standard_links)


initialize()