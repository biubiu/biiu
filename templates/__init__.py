from web.template import CompiledTemplate, ForLoop, TemplateResult


# coding: utf-8
def base (page):
    __lineoffset__ = -4
    loop = ForLoop()
    self = TemplateResult(); extend_ = self.extend
    extend_([u'<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN">\n'])
    extend_([u'<html>\n'])
    extend_([u'<head>\n'])
    extend_([u'  <meta http-equiv="Content-type" content="text/html; charset=utf-8">\n'])
    extend_([u'  <title>', escape_(page.title, True), u' | Company, Inc</title>\n'])
    extend_([u'  <link href="/static/screen.css" type="text/css" rel="stylesheet" />\n'])
    extend_([u'  ', escape_(page.get('head'), False), u'\n'])
    extend_([u'</head>\n'])
    extend_([u'<body>\n'])
    extend_([u'  ', escape_(page, False), u'\n'])
    extend_([u'</body>\n'])
    extend_([u'</html>\n'])

    return self

base = CompiledTemplate(base, 'templates/base.html')
join_ = base._join; escape_ = base._escape

# coding: utf-8
def index():
    __lineoffset__ = -5
    loop = ForLoop()
    self = TemplateResult(); extend_ = self.extend
    self['title'] = join_(u'Join Us')
    extend_([u'\n'])
    extend_([u'<form method="post">\n'])
    extend_([u'  <label>Name: <br />\n'])
    extend_([u'    <input type="text" name="name" />\n'])
    extend_([u'  </label>\n'])
    extend_([u'\n'])
    extend_([u'  <label>SSN: <br />\n'])
    extend_([u'    <input type="text" name="ssn" />\n'])
    extend_([u'  </label>\n'])
    extend_([u'\n'])
    extend_([u'  <input type="Submit" value="request membership" />\n'])
    extend_([u'</form>\n'])

    return self

index = CompiledTemplate(index, 'templates/index.html')
join_ = index._join; escape_ = index._escape

# coding: utf-8
def list (people):
    __lineoffset__ = -4
    loop = ForLoop()
    self = TemplateResult(); extend_ = self.extend
    self['title'] = join_(u'Suckers')
    extend_([u'\n'])
    extend_([u'<h3>Statisfied Customers</h3>\n'])
    extend_([u'<ul>\n'])
    for person in loop.setup(people):
        extend_([u'<li>', escape_(person.name, True), u'</li>\n'])
    extend_([u'</ul>\n'])
    extend_([u'\n'])

    return self

list = CompiledTemplate(list, 'templates/list.html')
join_ = list._join; escape_ = list._escape

