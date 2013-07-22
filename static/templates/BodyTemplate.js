(function() {
  var template = Handlebars.template, templates = Handlebars.templates = Handlebars.templates || {};
templates['BodyTemplate'] = template(function (Handlebars,depth0,helpers,partials,data) {
  this.compilerInfo = [4,'>= 1.0.0'];
helpers = this.merge(helpers, Handlebars.helpers); data = data || {};
  var buffer = "", stack1, functionType="function", escapeExpression=this.escapeExpression;


  buffer += "<div class=\"application\">\n  <div class=\"top-window\" style=\"border: 1px solid black;\">\n    <h2 class=\"top-window-label\" style=\"\">\n      ";
  if (stack1 = helpers.title) { stack1 = stack1.call(depth0, {hash:{},data:data}); }
  else { stack1 = depth0.title; stack1 = typeof stack1 === functionType ? stack1.apply(depth0) : stack1; }
  buffer += escapeExpression(stack1)
    + "\n    </h2>\n  </div> <!-- top-window -->\n  <div class=\"sources-window\" style=\"width: 100px; border: 1px solid black; height: 500px; float: left; padding: 5px;\">\n    <div class=\"sources-window-label\" style=\"\"> Sources </div>\n    <div class=\"sources-wrapper\">\n      <ul></ul>\n    </div> <!-- sources-wrapper -->\n  </div> <!-- sources-window -->\n  <div class=\"main-window\" style=\"border: 1px solid black; margin-left: 110px; padding: 10px; min-height: 500px;\">\n    Main window\n  </div> <!-- main-window -->\n</div> <!-- application -->";
  return buffer;
  });
})();