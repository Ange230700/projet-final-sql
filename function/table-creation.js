function CreateTable(row_number, column_number){
    var body_element = document.getElementsByTagName('body')[0];
    var table_element = document.createElement('table');
    table_element.style.width = '100%';
    table_element.setAttribute('border', '1px');
    var tbody_element = document.createElement('tbody');
    for (var i = 0; i < row_number; i++){
        var table_row = document.createElement('tr');
        for (var j = 0; j < column_number; j++){
            var table_column = document.createElement('td');
            table_row.appendChild(table_column);
        }
        tbody_element.appendChild(table_row)
    }
    table_element.appendChild(tbody_element);
    body_element.appendChild(table_element);
}

CreateTable(6, 10);