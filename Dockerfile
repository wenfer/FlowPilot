FROM python:3.11-slim

WORKDIR /app

# Copy all files into the container
COPY . .

# Set container-friendly environment variables
# Bind to 0.0.0.0 inside the container so it's accessible from the host system
ENV FLOWPILOT_HOST="0.0.0.0"
ENV FLOWPILOT_PORT="17373"

# Expose the default helper port
EXPOSE 17373

# Define volume mount point for persistent execution logs and history data
VOLUME ["/app/data"]

# Run the hotmail helper
CMD ["python", "scripts/hotmail_helper.py"]
