FROM node:18-alpine as builder

WORKDIR /app

COPY . .

RUN npm install
RUN npm run build

FROM node:18-alpine
ENV NODE_ENV=production
EXPOSE 3000

COPY --from=builder /app/package.json .
COPY --from=builder /app/build .
COPY --from=builder /app/data ./data
RUN apk update && \
    apk add --update git && \
    apk add --update openssh
RUN npm install --omit=dev
CMD [ "node", "index.js" ]