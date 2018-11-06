from lxml import etree

text = '''
<div>
<ul>
<li class="item-o">a href="link1.html">first item</a></li>
<li class="item-1">a href="link2.html">second item</a></li>
<li class="item- inactive">a href="link3.html">third item</a></li>
<li class="item-1"><a href="link4. html">fourth item</a></li>
<li class=" item-o"><a href="link5.html">fifth item</a>
</ul>
</div>

'''
# html = etree.HTML(text)
# res = etree.tostring(html)
# print(res.decode('utf-8'))

# html=etree.parse('./java.html',etree.HTMLParser())
# res = etree.tostring(html)
# print(res.decode('utf-8'))

html=etree.parse('./1.html',etree.HTMLParser())
res=html.xpath('//ul//a')
print(res)