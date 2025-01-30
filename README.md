
## Setup Instructions

To run the project locally, follow these steps:

1. Clone the repository:
    ```sh
    git clone https://github.com/KingHorey/hng_12_basic_api.git
    cd hng_12_basic_api
    ```

2. Create a virtual environment:
    ```sh
    python3 -m venv virtualenv
    source virtualenv/bin/activate  # On Windows use `virtualenv\Scripts\activate`
    ```

3. Install the dependencies:
    ```sh
    pip install -r api_test/requirements.txt
    ```

4. Run the application:
    ```sh
    python api_test/run.py
    ```

The application will be running at `http://0.0.0.0:5000`.

## API Documentation

### Endpoint URL

- `GET /api/`

### Request/Response Format

#### Request

- Method: `GET`
- URL: `http://0.0.0.0:5000/api/`

#### Response

- Status: `200 OK`
- Body:
    ```json
    {
        "email": "oreoluwaakinbo.oa@gmail.com",
        "current_datetime": "2023-10-05T14:48:00Z",
        "github_url": "https://github.com/KingHorey/hng_12_basic_api"
    }
    ```

### Example Usage

You can use `curl` to test the endpoint:

```sh
curl http://0.0.0.0:5000/api/

### HNG BACKLINK
https://hng.tech/hire/python-developers
