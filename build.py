from jinja2 import Template
import preset
import subprocess

with open('pyconkr-2018.html') as file:
    template = Template(file.read())

for sponsor_level in preset.sponsor_levels:
    for sponsor in sponsor_level['sponsors']:
        if sponsor.get('desc'):
            sponsor['desc'] = sponsor['desc'].split('\n')

patrons = []
for patron in preset.patrons:
    patron = patron.rsplit('/', 1)
    if len(patron) == 2:
        patrons.append({'name': patron[0], 'org': patron[1]})
    else:
        patrons.append({'name': patron[0]})

page = template.render({
    'coc': preset.coc,
    'sponsor_levels': preset.sponsor_levels,
    'staffs': preset.staffs,
    'volunteers': preset.volunteers,
    'patrons': patrons,
    'keynotes': preset.keynotes,
    'programs': preset.programs,
    'session_categories': preset.session_categories,
})

p = subprocess.Popen(["prince", "-", "-o", "pyconkr-2018-booklet-test.pdf"], stdin=subprocess.PIPE, stdout=subprocess.PIPE)
outs, errs = p.communicate(page.encode("utf-8"))
