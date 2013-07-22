

template = Handlebars.templates["BodyTemplate"]
context = {title : "Cornea Reader"}
html = template(context)
$('body').html(html)