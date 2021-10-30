FROM node:lts-alpine as build-stage

WORKDIR /app
COPY package*.json ./
RUN npm install && npm install @vue/cli -g
COPY . .
EXPOSE 8080

FROM node:lts-alpine as compile-stage

WORKDIR /app
COPY --from=build-stage /app .
RUN npm run build

FROM nginx:stable-alpine as production-stage
COPY --from=compile-stage /app/dist /usr/share/nginx/html
RUN rm /etc/nginx/conf.d/default.conf
COPY --from=compile-stage /app/nginx/nginx.conf /etc/nginx/conf.d/default.conf
EXPOSE 80 443
CMD ["nginx", "-g", "daemon off;"]