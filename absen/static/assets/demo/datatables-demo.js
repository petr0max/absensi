// Call the dataTables jQuery plugin
$(document).ready(function() {
  var table = $('#dataTable').DataTable({
      lengthChange: false,
      dom: 'Bfrtip',
      buttons: [
        'csvHtml5',
        'excelHtml5',
        'pdfHtml5',
        'printHtml5'
    ]
  });

  table.buttons().container()
      .insertBefore('#dataTable_filter');
});
