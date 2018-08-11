from jinja2 import Template
import preset
import subprocess
import os, sys


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

if os.environ.get('TARGET') == 'production':
    if not os.environ.get('DOCRAPTOR_APIKEY'):
        sys.exit('Please set DOCRAPTOR_APIKEY to bulid production pdf!')
    import docraptor

    baseurl = "https://lqez.github.io/pyconkr-2018-booklet/"
    docraptor.configuration.username = os.environ['DOCRAPTOR_APIKEY']
    doc_api = docraptor.DocApi()

    try:
        create_response = doc_api.create_doc({
            "document_content": page,
            "name": "pyconkr-2018-booklet.pdf",
            "document_type": "pdf",
            "prince_options": {
                "baseurl": baseurl,
            },
        })
        file = open("pyconkr-2018-booklet.pdf", "wb")
        file.write(create_response)
        file.close
        print("Done")
    except docraptor.rest.ApiException as error:
        print(error)
        print(error.message)
        print(error.code)
        print(error.response_body)
else:
    p = subprocess.Popen(["prince", "-", "-o", "pyconkr-2018-booklet-test.pdf"], stdin=subprocess.PIPE, stdout=subprocess.PIPE)
    outs, errs = p.communicate(page.encode("utf-8"))
