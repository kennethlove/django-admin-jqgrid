$(function() {
    var lastSel;
    $("#result_list").jqGrid({
        url: "/api/something/?format=xml",
        datatype:'xml',
        mtype: 'GET',
        xmlReader: {
            root: "objects",
            row: "object",
            repeatitems: false
        },
        colNames: ['ID', 'Name', 'Age', 'Sex'],
        colModel: [
            {
                name: 'id',
                index: 'id',
                width: 30,
                sortable: true,
                sorttype: 'int',
                xmlmap: 'id'
            },
            {
                name: 'name',
                index: 'name',
                width: 300,
                sortable: true,
                sorttype: 'text',
                xmlmap: 'name',
                editable: true,
                edittype: 'text',
                editoptions: {
                    size: 300,
                    maxlength: 85
                }
            },
            { name: 'age', index: 'age', width: 300, sortable: true, xmlmap: 'age' },
            { name: 'sex', index: 'sex', width: 300, sortable: true, xmlmap: 'sex' }
        ],
        viewrecords: true,
        gridview: true,
        onSelectRow: function(id) {
            if (id && id !== lastSel) {
                $('#result_list').restoreRow(lastSel);
                lastSel = id;
            }
            $('#result_list').editRow(id, true);
        },
        beforeSubmitCell: function(rowid, cellname, value, iRow, iCol) {
            $.ajax({
                url: "/api/something/" + rowid + "/",
                type: "POST",
                data: {
                    'name': value
                },
                success: function(data) {
                    alert(data);
                }
            });
        },
        cellEdit: true,
        cellsubmit: 'remote',
        cellurl: "/api/something/"
    });
});
