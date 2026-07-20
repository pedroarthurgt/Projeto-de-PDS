let dictTest = {
    celula: "Teste",
    data: "data",
    relatorio: "relatório"
};

function addTableRow(dictAdd) {
    const tbodyRef = document.getElementById('relatorios').getElementsByTagName('tbody')[0];
    const newRow = tbodyRef.insertRow();
    for (var value in dictAdd) {

        const newCell = newRow.insertCell();
        const newText = document.createTextNode(dictAdd[value]);
        newCell.appendChild(newText);
    }
}

addTableRow(dictTest);
addTableRow(dictTest);
addTableRow(dictTest);