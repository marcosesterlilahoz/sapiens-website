# Rebuilds index.html (live site) from ../v3/concept-d.html
import pathlib
src=pathlib.Path(__file__).parent.parent/'v3'/'concept-d.html'
s=src.read_text()
s=s.replace('<title>Sapiens — Concept D</title>','<title>Sapiens — Robotics as a Service</title>',1)
s=s.replace("document.title=name+' \\u2014 Concept D';","document.title=name+' \\u2014 Robotics as a Service';")
assert 'Concept D' not in s
og='''<meta property="og:title" content="Sapiens — Robotics as a Service">
<meta property="og:description" content="We buy proven robots from the world's leading manufacturers, install them on your line and run them for you. One monthly fee.">
<meta property="og:url" content="https://sapiensrobotics.ai/">
<link rel="canonical" href="https://sapiensrobotics.ai/">
<link rel="icon" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 32 32'%3E%3Crect width='32' height='32' rx='7' fill='%23002663'/%3E%3Ctext x='16' y='22' font-family='Arial' font-weight='700' font-size='18' fill='%23fff' text-anchor='middle'%3ES%3C/text%3E%3C/svg%3E">
'''
s=s.replace('</title>','</title>\n'+og,1)
here=pathlib.Path(__file__).parent
(here/'index.html').write_text(s)
# mirror for sapiens.industries: same page, own og:url (canonical stays on sapiensrobotics.ai)
s2=s.replace('<meta property="og:url" content="https://sapiensrobotics.ai/">','<meta property="og:url" content="https://sapiens.industries/">')
(here.parent/'deploy-industries'/'index.html').write_text(s2)
print('index.html (both sites)', len(s)//1024, 'KB')
print('Next: git commit + push in marca/web/deploy and marca/web/deploy-industries')
