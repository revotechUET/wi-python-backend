const http = require('http')
const app = require('./server')
const server = http.createServer(app)
const config = require('config')

const PORT = config.get('port')

const { AppError, errorHandler } = require('./app-error')
const logger = require('./logger')

global.logger = logger
global.AppError = AppError


process.on('unhandledRejection', (reason, p) => {
  throw reason
})
process.on('uncaughtException', (error) => {
  // I just received an error that was never handled, time to handle it and then decide whether a restart is needed
  errorHandler(error)
  if (!error.isOperational) throw error
})


server.listen(PORT, () => logger.info('app is starting on port ' + PORT))