//const controller = require('../controller/')
var md_auth = require('../middlewares/authenticated')
var express = require('express')
var cors = require('cors')
var bodyp = require('body-parser')
const { response } = require('express')
var app = express()



app.use(bodyp.urlencoded({extended:true}))
app.use(bodyp.json())
app.use(cors())

var api = express.Router()
app.use('/api', api)


module.exports = api
