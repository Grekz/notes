function doGet(e) {
  //return ContentService.createTextOutput('Hello World');

  try {
    var ss = SpreadsheetApp.openById(
      "1ClxTzAiekpfuba7RJbNmCk9p99iaGg6QEINAPYdNoNI"
    );
    var sheet = ss.getSheetByName("Sheet1");
    var data = sheet
      .getRange(2, 1, sheet.getLastRow() - 1, sheet.getLastColumn())
      .getValues();
    var jsonData = JSON.stringify(data);
    return ContentService.createTextOutput(jsonData).setMimeType(
      ContentService.MimeType.JSON
    );
  } catch (e) {
    var error = { error: e };
    var jsonError = JSON.stringify(error);
    return ContentService.createTextOutput(jsonError).setMimeType(
      ContentService.MimeType.JSON
    );
  }
}

function doPost(e) {
  try {
    var ss = SpreadsheetApp.openById(
      "1ClxTzAiekpfuba7RJbNmCk9p99iaGg6QEINAPYdNoNI"
    );
    var sheet = ss.getSheetByName("Sheet1");
    var headers = sheet.getRange(1, 1, 1, sheet.getLastColumn()).getValues()[0];
    var holderArray = [];
    for (var x = 0; x < headers.length; x++) {
      var tempValue = !e.parameter[headers[x]] ? " " : e.parameter[headers[x]];
      holderArray.push(tempValue);
    }
    sheet.appendRow(holderArray);
    var results = {
      data: e.parameter,
      holder: holderArray
    };
    var jsonData = JSON.stringify(results);
    return ContentService.createTextOutput(jsonData).setMimeType(
      ContentService.MimeType.JSON
    );
  } catch (e) {
    var error = {
      error: e
    };
    var jsonError = JSON.stringify(error);
    return ContentService.createTextOutput(jsonError).setMimeType(
      ContentService.MimeType.JSON
    );
  }
}
///////////////////
$(function() {
  $("#fillData").click(function() {
    $.ajax({
      url: "https://randomuser.me/api/",
      dataType: "json",
      success: function(data) {
        console.log(data.results[0]);
        var obj = data.results[0];
        $('input[name="First"]').val(obj.name.first);
        $('input[name="Last"]').val(obj.name.last);
        $('input[name="Company"]').val(obj.location.city);
        $('input[name="Group"]').val(obj.nat);
        $('input[name="Email"]').val(obj.email);
      }
    });
  });
  $("#myForm").submit(function(e) {
    e.preventDefault();
    var myData = $("form#myForm :input").serialize();
    var url =
      "https://script.google.com/macros/s/AKfycbz3XKJ4o7B6SADFyiKA0peYuVBtgkV73l9XVPzryea7ib_uYQvB/exec";
    console.log(myData);
    $.ajax({
      url: url,
      method: "POST",
      data: myData,
      success: function(data) {
        console.log(data);
      }
    });
  });
  $("#loadData").click(function() {
    var url =
      "https://script.google.com/macros/s/AKfycbz3XKJ4o7B6SADFyiKA0peYuVBtgkV73l9XVPzryea7ib_uYQvB/exec";
    $.getJSON(url, function(data) {
      var html = "<h3>Google Sheet Data</h3><ul>";
      $.each(data, function(key, val) {
        html += "<li> ";
        for (var x = 0; x < val.length; x++) {
          html += val[x] + " ";
        }
        html += "</li> ";
      });
      html += "</ul> ";
      $("#output").html(html);
    });
  });
});
