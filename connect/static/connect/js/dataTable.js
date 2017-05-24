/* Custom filtering function which will search data in column four between two values */
$.fn.dataTable.ext.search.push(
    function( settings, data, dataIndex ) {
        var time_min = $('#min');
        var time_max = $('#max');
        var date_min = $('#date_min');
        var date_max = $('#date_max');
        var timestart = data[6]
        return true;
    }
);

$(document).ready(function() {
    var table = $('#example').DataTable();

    // Event listener to the two range filtering inputs to redraw on input
    $('#date_min', '#date_max', '#min, #max').keyup( function() {
        table.draw();
    } );
} );