var learning_loaded = false;
var email_loaded = false;

$(window).load(function() {
  first_load();
  setInterval(function() {
    check("learning");
    check("email");
  }, 10000);
});

function check(service) {
  $.ajax({url: "/check_service/" + service, statusCode: {
    200: function(data) {
      var data = $.parseJSON(data);
      var d = new Date(data["timestamp"] * 1000);
      var n = d.toLocaleString();
      $("#" + service + "_server_status").html(data["message"] + "  "+ n);
      $("#" + service + "_box").removeClass("fail");
      $("#" + service + "_box").addClass("success");
      show_if_ready(service);
    },
    404: function() {
      $("#" + service + "_server_status").html("No..... status code 404");
      $("#" + service + "_box").removeClass("success");
      $("#" + service + "_box").addClass("fail");
      show_if_ready(service);
    },
    500: function() {
      $("#" + service + "_server_status").html("No..... status code 500");
      $("#" + service + "_box").removeClass("success");
      $("#" + service + "_box").addClass("fail");
      show_if_ready(service);
    },
    503: function() {
      $("#" + service + "_server_status").html("No..... status code 503");
      $("#" + service + "_box").removeClass("success");
      $("#" + service + "_box").addClass("fail");
      show_if_ready(service);
    },
  }});
}

function first_load() {
  $("#spinner").spin({lines:13, length:10, width:3, radius:14, color:'#aaa', top:'20px'});
  check("learning");
  check("email");
}

function show_if_ready(service) {
  if (learning_loaded && email_loaded) return;

  if (service == "learning") learning_loaded = true;
  else if (service == "email") email_loaded = true;

  if (learning_loaded && email_loaded) {
    $("#spinner").spin(false);
    $("#spinner").hide();
    $("#email_box").show();
    $("#learning_box").show();
  }
}
