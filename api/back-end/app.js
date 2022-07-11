'use strict'

// variables globales
const express = require("express")
const app = express()
var CORS = require("cors")
const bodyParser = require("body-parser")
 var api = express.Router()

//CARGA DE RUTAS
var routes = require("./src/routes/routes")
        
//MIDDLEWARES
app.use(bodyParser.urlencoded({extended: false}))
app.use(bodyParser.json())
app.use(CORS())
console.log("Done")                         
app.use('/api', routes)

module.exports = app
