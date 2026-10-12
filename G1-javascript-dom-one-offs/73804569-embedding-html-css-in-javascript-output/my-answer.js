// Code from my Stack Overflow answer https://stackoverflow.com/a/73848802 (posted 2022-09-26), extracted verbatim; may need the question's context to run.
function jsonToTable(jsOp, colNames){
    var op = '', rowHtml = '';
    for (let c=0; c<colNames.length; c++) {
        rowHtml += `<th>${colNames[c]}</th>`;
    }
    op += `<tr>${rowHtml}</tr>`;
    for (let r=0; r< jsOp.length; r++){
        rowHtml = ''; var rowData = jsOp[r];
        var rowStyle = i%2==0 ? '' : ' style="border-bottom: 1px solid black;';
        for (let c=0; c<colNames.length; c++) {
            var colName = colNames[c];
            rowHtml += `<td>${rowData[colName]}</td>`;
        }
        op += `<tr ${rowStyle}>${rowHtml}</tr>`;
    }
    return `<table>${op}</table>`;
}
