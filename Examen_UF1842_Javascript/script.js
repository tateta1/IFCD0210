tiempoTag.addEventListener('blur', () => {
    if (tiempoTag.value === '' || tiempoTag.value === null || tiempoTag.value === undefined) {
        tiempoTag.value = '1';
    }
});


tiempoTag.addEventListener('keydown', (e) => {
    e.preventDefault();
});


const sleep = (delay) => new Promise((resolve) => setTimeout(resolve, delay));

const numeros = [3, 7, 2, 9, 5, 10];
const listado = document.querySelector("#listado");
const start = document.querySelector("#start");


let suma = 0;

async function recorrerArray() {
    const tiempo = Number(tiempoTag.value) * 1000;
    
   
    listado.innerHTML = "";
    suma = 0;

    for (let i = 0; i < numeros.length; i++) {
        const li = document.createElement("li");
        suma += numeros[i];
        
        
        li.innerText = `El índice ${i} es: ${numeros[i]}`;

        listado.appendChild(li);
        
        
        await sleep(tiempo);
    }

    const sumaTotal = document.createElement('h3');
    sumaTotal.innerText = `La suma total es: ${suma}`;
    listado.after(sumaTotal);

    start.disabled = true; 
}


const resultadoNotas = document.querySelector("#resultadoNotas");

function calcularResultado(notas) {
    let sumaNotas = 0;
    for (let i = 0; i < notas.length; i++) {
        sumaNotas += notas[i];
    }

    const media = sumaNotas / notas.length;
    let estado = media >= 5 ? "Aprobado" : "Suspenso";
    let calificacion = "";

    if (media < 5) calificacion = "Insuficiente";
    else if (media < 7) calificacion = "Suficiente";
    else if (media < 9) calificacion = "Notable";
    else calificacion = "Sobresaliente";

    return [media, estado, calificacion];
}

function mostrarResultado() {
    const notas = [6, 8, 0, 5, 9];
    const resultado = calcularResultado(notas);

    
    resultadoNotas.innerText = `Media: ${resultado[0].toFixed(2)} | Estado: ${resultado[1]} | Calificación: ${resultado[2]}`;
}