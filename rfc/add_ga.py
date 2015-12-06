#!/bin/env python

ga = """
<script>
(function(i,s,o,g,r,a,m){i['GoogleAnalyticsObject']=r;i[r]=i[r]||function(){
(i[r].q=i[r].q||[]).push(arguments)},i[r].l=1*new Date();a=s.createElement(o),
m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m)
})(window,document,'script','//www.google-analytics.com/analytics.js','ga');
ga('create', 'UA-46086503-7', 'auto');
ga('send', 'pageview');
</script>
</body>
"""

f = open('./netjson.html', 'r+')
html = f.read()
html = html.replace('</body>', ga)
f.write(html)
print('Added google analytics tracking code to HTML RFC')
