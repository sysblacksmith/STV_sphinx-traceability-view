"""Public rendering policy; retained engineering sources stay unchanged."""
import re
from docutils import nodes
from sphinx import addnodes

HISTORICAL=('test-execution/', 'concept-reviews/', 'change-requests/')

def evidence_view(app,doctree,docname):
    # Raw historical downloads can contain private checkout locations, command
    # lines, environment reports and archived package READMEs. Retain them in Git,
    # while the website publishes canonical case/execution records and summaries.
    for node in list(doctree.findall(addnodes.download_reference)):
        target=node.get('reftarget','')
        if docname.startswith(HISTORICAL) or 'test-execution/' in target or 'concept-reviews/' in target:
            node.replace_self(nodes.inline(text=node.astext()+' (retained in the engineering checkout)'))
    if docname.startswith('test-execution/'):
        for node in list(doctree.findall(nodes.image)):
            node.replace_self(nodes.paragraph(text='Historical screenshot retained in the engineering checkout.'))


def remove_downloads(app,env):
    # Run before write: removed references must not leave files in _downloads.
    for filename,record in list(env.dlfiles.items()):
        docnames=record[0]
        if any(name.startswith(HISTORICAL) for name in docnames) or any(part in filename.replace('\\','/') for part in ('test-execution/','concept-reviews/')):
            del env.dlfiles[filename]


def setup(app):
    app.connect('doctree-resolved',evidence_view,priority=900)
    app.connect('env-updated',remove_downloads)
    return {'version':'1','parallel_read_safe':True,'parallel_write_safe':True}
