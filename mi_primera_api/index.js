import esImpar from 'is-odd-num'

let resultado = esImpar(10)

console.log(resultado)

const miCalculoImpar = (numero) => {
    if (numero % 2 === 0) {
        return false
    } else {
        return true
    }
}

resultado = miCalculoImpar(10)

// operador ternario
// condicion ? VERDADERA : FALSE
console.log(resultado === true ? 'Es impar' : 'Es par')

// operador AND &&
// si la primera condicion es true o no es null o undefined pasara a la segunda expresion
// se utiliza si queremos validar si la condicion solamente es verdadera, osea no tener un else
console.log(resultado === false && 'Otra cosa')

// operador OR ||
// si la primera expresion es verdad se quedara ahi pero si es false o es null o undefined pasara a la segunda
console.log(0 || 'Otra cosa')

// operador Nullish coalescing operator ??
// es un operador logico que retornara lo de la derecha si la parte de la izquierda es null o undefinided de otra manera retornara lo de la izquierda
// el caracter 0 indica nulidad en js 
console.log(0 ?? 'otra cosa')