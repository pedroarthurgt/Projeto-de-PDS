let celulasTeste = [
    {
        nome: "celulaTeste1",
        numero: 1,
        lider: "lider"
    },
    {
        nome: "celulaTeste2",
        numero: 1,
        lider: "lider"
    }
]

let dictTest = {
    celula: "Teste",
    data: "data",
    relatorio: "relatório"
};

let pessoasTeste = [{
    nome: "Bruno",
    celula: "celulaTeste1",
    frequencia: 3,
    dataEntrou: new Date(2026, 7, 3)
}
// {
//     nome: "Guto",
//     celula: "celulaTeste1",
//     frequencia: 9,
//     dataEntrou: new Date(2015, 12, 15)
// }
]

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

function getUltimaSegunda(data) {
    let date = new Date(data);
    
    //Se a data for diferente de segunda, ele pega a última segunda
    if (date.getDay() != 1) {
        date.setDate(date.getDate()-date.getDay()+1);
    }
    return date;
}

const ctx = document.getElementById('presencaMedia');
let l = new Array;

for (i in celulasTeste) {
    l.push(celulasTeste[i]['nome'])

}

let freqDict = {};
let dataAgora = new Date(Date.now());
dataAgora.setHours(0);
dataAgora.setMinutes(0);
dataAgora.setSeconds(0);

for (k in l) {
    value = 0;
    let pFreq = new Array;
    for (p in pessoasTeste) {
        let freq = (pessoasTeste[p]['frequencia']/(((getUltimaSegunda(dataAgora)-getUltimaSegunda(pessoasTeste[p]['dataEntrou']))/86400000/7))*100).toFixed(2);
        if (pessoasTeste[p]['celula']==l[k]) pFreq.push(freq);
    }
    freqDict[l[k]] = pFreq.reduce(function (x, y) {
        return (x+y);
    }, 0)/pFreq.length;
}

let freqArr = new Array;
for (i in freqDict) freqArr.push(freqDict[i]);
new Chart(ctx, {
    type: 'bar',
    data: {
        labels: l,
        datasets: [{
            label: '% de frequência',
            data: freqArr,
            borderWidth: 1,
        }]
    },
    options: {
        scales: {
            y: {
                beginAtZero: true
            }
        }
    }
});

// console.log(freqDict);
// console.log(l);
// console.log(pessoasTeste[0]['frequencia']/((getUltimaSegunda(dataAgora)-getUltimaSegunda(pessoasTeste[0]['dataEntrou']))/86400000/7));
// console.log(dataAgora);