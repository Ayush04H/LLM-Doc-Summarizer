# Use the official Node.js image as a base
FROM node:18

# Set the working directory in the container
WORKDIR /app

# Install dependencies
COPY package.json package-lock.json ./
RUN npm install

# Copy the frontend code to the container
COPY . /app

# Start the React application
CMD ["npm", "start"]
