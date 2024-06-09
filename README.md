# Personal Assistant API Documentation

## Docker build and run steps

### Docker build step to use as container image

```sh
docker build -t {image_name} --no-cache .
```

```sh
docker run -d --rm --name assistant_api -p 8000:8000 {image_name}
```

## Getting Started

Welcome to the Personal Assistant API! This API provides endpoints to retrieve information about IP addresses, check ports, and perform DNS lookups.

To get started with the API, you can use the following endpoints:

- `/ipinfo`: Retrieve information about the IP address.
- `/portchecker`: Check if a port is open on a specified IP address.
- `/dnschecker`: Perform a DNS lookup for a given domain name.

## Endpoints

### IP Information

#### Get Information about IP Address

**Endpoint:** `/ipinfo/8.8.8.8`

**Method:** `GET`

**Query Parameters:**
- `ip`: The IP address to get information about.

**Example:**

**Response:**
```json
{
  "ip": "8.8.8.8",
  "city": "Mountain View",
  "country": "US"
}
```

### Port Checker

#### Description
Checks if a port is open on a specified IP address.

- **Endpoint:** `/portchecker`
- **Method:** GET
- **Query Parameters:**
  - `ip`: IP address to check port on.
  - `port`: Port number to check.

#### Example

**Request:**
```http
GET /portchecker?ip=8.8.8.8&port=53
```

**Response:**
```json
{
  "message": "Port 53 is open on IP 8.8.8.8"
}
```

### DNS Checker

#### Description
Performs a DNS lookup for a given domain name.

- **Endpoint:** `/dnschecker`
- **Method:** GET
- **Query Parameters:**
  - `dnsname`: Domain name to perform DNS lookup.

#### Example

**Request:**
```http
GET /dnschecker?dnsname=example.com
```

**Response:**
```json
{
  "message": "DNS lookup result for example.com: 93.184.216.34"
}
```
