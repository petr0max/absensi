$.fn.dataTable.ext.search.push(
  function( settings, data, dataIndex ) {
      var min = minDate.val();
      var max = maxDate.val();
      var date = new Date( data[4]  );
       
      if (
          ( min === null && max === null  ) ||
          ( min === null && date <= max  ) ||
          ( min <= date   && max === null  ) ||
          ( min <= date   && date <= max  )
      ) {
          return true;
      }
      return false;
  }
);
$(document).ready(function() {
  // Create date inputs
  minDate = new DateTime($('#min'), {
      format: 'Do MMMM YYYY'
  });
  maxDate = new DateTime($('#max'), {
      format: 'Do MMMM YYYY'
  });

  // DataTables initialisation
  var table = $('#data_hadir').DataTable( {
      dom: 'Bfrtip',
      buttons: ['csv', 'excel', 'pdf', 'print'],
      responsive: true,
      rowReorder: {
          selector: 'td:nth-child(2)'
      }
  });
  // Refilter the table
$('#min, #max').on('change', function() {
  table.draw();
});
});
$(document).ready(function() {
  var table = $('#data_sakit').DataTable( {
      dom: 'Bfrtip',
      buttons: ['csv', 'excel', 'pdf', 'print'],
      responsive: true,
      rowReorder: {
          selector: 'td:nth-child(2)'
      }
  });
  var table = $('#data_izin').DataTable( {
      dom: 'Bfrtip',
      buttons: ['csv', 'excel', 'pdf', 'print'],
      responsive: true,
      rowReorder: {
          selector: 'td:nth-child(2)'
      }
  });
});
