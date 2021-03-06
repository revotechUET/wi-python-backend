const route = require('express').Router();
const controller = require('./controller');

route.get('/list', async (req, res) => {
	try {
		// const {user} = req.query;
		const data = await controller.listProject(req.decoded.username);
		res.status(200).json({data})
	} catch (error) {
		if (error.isOperational) throw error;
		res.status(400).json({message: error.message})
	}
});

route.get('/new', async (req, res) => {
	const {name} = req.query;

	try {
		const data = await controller.newProject(name, req.decoded.username);
		res.status(200).json({data})
	} catch (error) {
		if (!error.isOperational) throw error;
		res.status(400).json({message: error.message})
	}
});

route.get('/open', async (req, res) => {
	const {name} = req.query;

	try {
		const data = await controller.openProject(name, req.decoded.username);
		res.status(200).json({data})
	} catch (error) {
		if (!error.isOperational) throw error;
		res.status(400).json({message: error.message})
	}
});

route.get('/delete', async (req, res) => {
	const {name} = req.query;

	try {
		const data = await controller.deleteProject(name, req.decoded.username);
		res.status(200).json({data})
	} catch (error) {
		if (!error.isOperational) throw error;
		res.status(400).json({message: error.message})
	}
});

route.get('/read-file', async (req, res) => {
	const {dir} = req.query;

	try {
		const data = await controller.readFile(dir, req.decoded.username);
		res.status(200).json({data})
	} catch (error) {
		if (!error.isOperational) throw error;
		res.status(400).json({message: error.message})
	}
});

route.get('/read-folder', async (req, res) => {
	const {dir} = req.query;

	try {
		const data = await controller.readFolder(dir, req.decoded.username);
		res.status(200).json({data})
	} catch (error) {
		if (!error.isOperational) throw error;
		res.status(400).json({message: error.message})
	}
});


module.exports = route;