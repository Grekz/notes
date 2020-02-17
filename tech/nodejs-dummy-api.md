# Dummy REST API with NodeJS + Express

## Overview

Hey guys! Welcome back to your channel, it’s me grekz again.
Today we will learn how to create a dummy REST endpoint with NodeJS and Express.
Nowadays whenever we talk about doing some development in Javascript we almost always have to think about bringing alone babel.
And to make our development a little more effective we are including nodemon in the mix.
Nodemon is a tool that allows us to see our changes live, something like hot-reloading for our API.

The dummy REST endpoint we are building will just help us to add two numbers that we are going to send in a GET request.
Please take in consideration that this example doesn’t use best practice on designing APIs.
Without further ado let’s start.

We will start by creating a folder to contain our NodeJS + Express app and init as an npm package.

First we need to install npm and NodeJS in our computer.
I’ll set up the links in the description on how to install NPM and NodeJS.

[Install npm in this link](https://www.npmjs.com/get-npm)

[Install NodeJS in this other link](https://nodejs.org/en/download/)

```bash
mkdir nodejs-app
cd nodejs-app
npm init
## follow all the steps with default values.
```

After we have initialized our package we need to install a couple of things: nodemon, babel, express.

```bash
npm install express nodemon @babel/core @babel/node @babel/preset-env --save-dev
```

On a side note, I am using NVM to have multiple Node versions, but that is not necessary for this small tutorial. In case you are interested in learning or using NVM in your local environment. [More on NVM](https://github.com/nvm-sh/nvm)

Let’s do this! 💪

When we have everything ready we need to create a javascript file that will contain our logic. And while we are in it, we can also create the configuration file for babel:

```bash
touch app.js
touch .babelrc
```

In our `.babelrc` file we will specify what we need from babel, for this example we will use the preset-env config.
So add to `.babelrc` this:
```json
{
  "presets": [
    "@babel/preset-env"
  ]
}
```

Now that we have configured our babel, it is time to start coding our REST endpoint.
Let us add this code to our app.js
```javascript
import express from 'express'
const app = express()
const PORT = 5000
app.listen(PORT, () => {
  console.log(`Server running on http://localhost:${PORT}`)
})
```

This piece of code doesn't do anything relevant to our endpoint, just sets the app to listen on port 5000.

Another thing we need to add is how to run our app in package.json, to do this your package.json should look like:
```json
{
  "name": "nodejs-app",
  "version": "1.0.0",
  "description": "",
  "main": "index.js",
  "scripts": {
    "start": "nodemon --exec babel-node app.js"
  },
  "author": "",
  "license": "ISC",
  "devDependencies": {
    "@babel/core": "^7.8.4",
    "@babel/node": "^7.8.4",
    "@babel/preset-env": "^7.8.4",
    "express": "^4.17.1",
    "nodemon": "^2.0.2"
  }
}
```

Now if you run our start script, we should see the message that the server is running. 
```bash
$ npm start
```

Ok, now that we now that our server is running, it is time that we add a little logic(magic) to sum our parameters
```javascript
// Add this to the bottom of app.js
app.get('/api/v1/add', (req, res) => {
    const { first = 0, second = 0 } = req.query
    const total = parseInt(first) + parseInt(second)
    res.status(200).send({
        success: 'true',
        total
    })
})
```

To test it you can call this url: http://localhost:5000/api/v1/add?first=4&second=5

And success!

Let me know what you think in the comments.