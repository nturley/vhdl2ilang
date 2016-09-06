



EXIT = 1

def ast2dot(tree, f):
    f.write('''
digraph {
  ordering=out;
  ranksep=.4;
  bgcolor="lightgrey";
  node [shape=box, fixedsize=false, fontsize=12, fontname="Helvetica-bold", fontcolor="blue"
    width=.25, height=.25, color="black", fillcolor="white", style="filled, solid, bold"];
  edge [arrowsize=.5, color="black", style="bold"]
''')
    auto_index = 0
    ancestry = []
    for node in visit(tree):
        if node is EXIT:
            ancestry.pop()
            continue
        dotname = 'n' + str(auto_index)
        auto_index += 1
        f.write('  ' + dotname +' [label="' + node.name() + '"];\n')
        if len(ancestry)>0:
            f.write('  ' + ancestry[-1] + ' -> ' + dotname + '\n')
        ancestry.append(dotname)
    f.write('}\n')


def visit(node):
    """ recursive generator
    every node should yield itself and EXIT """
    yield node
    for child in node.children:
        for r in visit(child):
            yield r
    yield EXIT
