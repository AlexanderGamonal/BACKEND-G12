// CommonJS
// Cuando el archivo tenga la extensiuon cjs indicara que esta escrito en commonJS

const {saludar} = require('./funcionabilidad.cjs')

console.log('Hello World!')

const resultado = saludar()

console.log(resultado)