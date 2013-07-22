template = Handlebars.templates["ApplicationTemplate"]
context = {}
html = template(context)
$('body').html(html)