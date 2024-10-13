FROM node:20.11.0-alpine as build
WORKDIR /FE
COPY package*.json ./
RUN npm i
RUN npm install -g @angular/cli
COPY . .
RUN npm run build --configuration=production
FROM nginx:1.17.1-alpine
# Copy dist from ng build to nginx html folder
COPY --from=build /FE/dist/angular-project /usr/share/nginx/html