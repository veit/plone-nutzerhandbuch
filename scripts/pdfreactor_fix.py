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

    related = root.xpath("//div[@class='related']")
    for r in related or ():
        r.getparent().remove(r)

    related = root.xpath("//div[@id='index-und-suche']")
    if related:
        related = related[0]
        related.getparent().remove(related)

    related = root.xpath("//div[@class='sphinxsidebar']")
    if related:
        related = related[0]
        related.getparent().remove(related)

    # inject lang=de
    body = root.find('body')
    body.attrib['lang'] = 'de'

    # inject onload attribute and <script> tag for loading JS file

    head = root.find('head')
    script = Element('script')
    script.attrib['src'] = 'pdfreactor.js'
    head.append(script)
    script = Element('script')
    script.attrib['src'] = 'awesomizr.js'
    head.append(script)
    link = Element('link')
    link.attrib['rel'] = 'stylesheet'
    link.attrib['href'] = 'awesomizr.css'
    head.append(link)

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

    html_out = lxml.html.tostring(root)
    open(sys.argv[1] + '.out', 'wb').write(html_out)


if __name__ == '__main__':
    main()
