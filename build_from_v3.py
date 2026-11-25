# Rebuilds index.html (live site) from ../v3/concept-d.html
import pathlib
src=pathlib.Path(__file__).parent.parent/'v3'/'concept-d.html'
s=src.read_text()
s=s.replace('<title>Sapiens — Concept D</title>','<title>Sapiens | Robotics as a Service</title>',1)
s=s.replace("document.title=name+' \\u2014 Concept D';","document.title=name+' | Robotics as a Service';")
assert 'Concept D' not in s
og='''<meta property="og:title" content="Sapiens | Robotics as a Service">
<meta property="og:description" content="We buy proven robots from the world's leading manufacturers, install them on your line and run them for you. One monthly fee.">
<meta property="og:url" content="https://sapiensrobotics.ai/">
<link rel="canonical" href="https://sapiensrobotics.ai/">
<link rel="icon" type="image/png" sizes="64x64" href="favicon.png?v=2">
<link rel="apple-touch-icon" href="apple-touch-icon.png?v=2">
'''
s=s.replace('</title>','</title>\n'+og,1)
here=pathlib.Path(__file__).parent
(here/'index.html').write_text(s)
import shutil
for d in (here, here.parent/'deploy-industries'):
    for f in ('favicon.png','apple-touch-icon.png'):
        shutil.copy(here.parent/'v3'/'icons'/f, d/f)
# mirror for sapiens.industries: same page, own og:url (canonical stays on sapiensrobotics.ai)
s2=s.replace('<meta property="og:url" content="https://sapiensrobotics.ai/">','<meta property="og:url" content="https://sapiens.industries/">')
(here.parent/'deploy-industries'/'index.html').write_text(s2)
print('index.html (both sites)', len(s)//1024, 'KB')
print('Next: git commit + push in marca/web/deploy and marca/web/deploy-industries')
