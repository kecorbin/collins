FROM node:4
RUN npm install newman --global;
WORKDIR /workspace
CMD newman run api-tests.json -e environment.json