FROM node:18-alpine as build
WORKDIR /app
COPY . .
RUN npm ci
EXPOSE 3000
CMD ["npx", "serve", "-s", "public", "-l", "3000"]
