# Use official Node.js image
FROM node:18-bullseye

# Install fortune-mod, cowsay, bash
RUN apt-get update && \
    apt-get install -y fortune-mod cowsay bash && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# Copy server code
COPY server.js .

# Expose port
EXPOSE 4499

# Start the Node.js server
CMD ["node", "server.js"]

