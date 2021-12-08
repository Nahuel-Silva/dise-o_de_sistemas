const express = require('express')
const app = express()
const puerto = 3000

app.get('/home', (req, res) => {
  res.send('El home de la Mendoza me contesta el server')
})
app.get('/home/sub1', (req, res) => {
    res.send('Desde el sub1')
  })

app.get('/home/sub2', (req, res) => {
res.send('Desde el sub2')
})

app.post('/home', (req, res) => {
    res.send('Contesto desde el post')
    })

app.listen(puerto, () => console.log(`Example app listening on port port!`))