window.addEventListener('DOMContentLoaded', event => {
    // Simple-DataTables
    // https://github.com/fiduswriter/Simple-DataTables/wiki

    const data_hadir = document.getElementById('data_hadir');
    if (data_hadir) {
        new simpleDatatables.DataTable(data_hadir);
    }
});
