template = Handlebars.templates["ApplicationTemplate"]

html = template()
$(document).ready(
    () ->
      $('body').html(html)
  )