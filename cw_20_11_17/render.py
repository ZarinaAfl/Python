


from lxml import html, etree

with open("size.html", 'r') as  f:
    str = f.read()

tree = html.fromstring(str)


def render(elem):
    tree = etree.Element(elem)
    root = tree.getRoot()

    #if root.findAll('td')




#def render_final(elem):

