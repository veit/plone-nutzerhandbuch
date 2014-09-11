import sys                                    
import uuid
import lxml.html
from lxml.etree import Element


def main():

    html = open(sys.argv[1], 'rb').read()
    root = lxml.html.fromstring(html)

    # strip $b6 from <a> anchors
    for node in root.xpath('//a'):
        if node.text == u'\xb6':
            node.text = u''

    # inject lang=de
    body = root.find('body')
    body.attrib['lang'] = 'de'

    # inject onload attribute and <script> tag for loading JS file

    head = root.find('head')
    script = Element('script')
    script.attrib['src'] = 'pdfreactor.js'
    head.append(script)

    body.attrib['onload'] = 'init()'

    # fix href="index.html#...." links
    for node in root.xpath('//a'):
        if 'href' in node.attrib:
            href= node.attrib['href']
            if href.startswith('index.html#'):
                href = href.replace('index.html#', '#')
                node.attrib['href'] = href

    # remove "Inhalt:"
    nodes = root.xpath('//*[text()="Inhalt:"]')
    if nodes:
        toc_node = nodes[0]
        toc_node.attrib.update({'id': 'toc'})
        toc_node.getparent().remove(toc_node)

        # Table of contents
        if False:
            toc = list()
            for count, node in enumerate(root.xpath('//*[self::h2 or self::h3 or self::h4 or self::h5]')):
                anchor = node.find('a')
                del anchor.attrib['href']
                anchor_id = anchor.attrib.get('name')
                if not anchor_id:
                    anchor.attrib.update({'name': 'toc-{}'.format(count)})
                    anchor.attrib.update({'id': 'toc-{}'.format(count)})
                    anchor_id = anchor.attrib['name']
                    
                level = int(node.tag[1:]) - 1 # H2 -> H1...
                toc.append(u'<li><a class="level-{}" href="#{}">{}</a></li>'.format(level, anchor_id, node.text))

            toc_html = u'<ul id="toc-entries">' + u'\n'.join(toc) + u'</ul>'
            html = u'<section id="toc"><span id="toc-title">Inhaltsverzeichnis</span>{}</section>'.format(toc_html)
            node = lxml.etree.fromstring(html)
            toc_node.insert(0, node)

    html_out = lxml.html.tostring(root)
    open(sys.argv[1] + '.out', 'wb').write(html_out)


if __name__ == '__main__':
    main()
