FROM node:18-alpine

WORKDIR /app

COPY package.json .
RUN npm install

COPY . .

EXPOSE 3000

CMD ["node", "-e", "require('http').createServer(function(req,res){var fs=require('fs');var p=req.url==='/'?'/public/index.html':req.url;var f=__dirname+p;fs.readFile(f,function(e,d){if(e){res.writeHead(404);res.end('Not Found');}else{res.writeHead(200,{'Content-Type':p.endsWith('.html')?'text/html':p.endsWith('.js')?'application/javascript':'text/css'});res.end(d);}});}).listen(3000)"]
