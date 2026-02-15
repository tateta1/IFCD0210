function analizarConsumo(consumos) {
    const diasAltos = consumos.filter(c => c > 30).length;
    const total = consumos.reduce((acumulado, actual) => acumulado + actual, 0);
    const minimo = Math.min(...consumos);

    return [diasAltos, total, minimo];
}

const consumos = [28, 35, 22, 40, 31, 18, 25];
const resultado = analizarConsumo(consumos);

console.log(resultado);