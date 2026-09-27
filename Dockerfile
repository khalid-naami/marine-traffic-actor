# Use official Apify Python base image
FROM apify/actor-python:3.12

# Install dependencies
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy source code and actor definition
COPY . ./

# Run the actor
CMD ["python3", "-m", "src.main"]
