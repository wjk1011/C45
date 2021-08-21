from graphviz import Digraph
dot = Digraph(comment='The Round Table', format='svg')
dot.node('A', 'King Arthur')
dot.node('B', 'Sir Bedevere the Wise')
dot.node('L', 'Sir Lancelot the Brave')
dot.edges(['AC', 'AL'])
dot.edge('B', 'L', constraint='false')
print(dot.source) # doctest: +NORMALIZE_WHITESPACE
dot.render('test-output/round-table.gv', view=True)