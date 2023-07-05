
```markdown
# City Suggestions API

This is an API that provides suggestions for cities based on a search query and geographical coordinates.

## Requirements

- Python 3.7+
- SQLAlchemy
- FastAPI
- Uvicorn
- Pydantic

## Installation

1. Clone the repository:

```
git clone <repository_url>
cd <repository_directory>
```

2. Install the dependencies:

```
pip install -r requirements.txt
```

3. Configure the Application

- Open the `src.config.py` file.
- Set the `ENVIRONMENT` variable to your desired environment ("dev", "qa", "prod").
- Update the `<your-key-vault-url>` placeholder in the `get_secret` function with the URL of your Azure Key Vault.

4. Start the Application

```
uvicorn main:app --reload
```

## API Usage

The API has the following endpoints:

### Health Check

```
GET /health
```

- Returns the status of the server.

### City Suggestions

```
GET /api/suggestions?q=<query>&latitude=<latitude>&longitude=<longitude>
```

- Retrieves city suggestions based on the provided query, latitude, and longitude.
- The `q` parameter is required and represents the search query.
- The `latitude` and `longitude` parameters are optional and can be used to filter suggestions based on geographical coordinates.

### Example Request

```
GET /api/suggestions?q=London&latitude=51.5074&longitude=-0.1278
```

### Example Response

```json
{
  "suggestions": [
    {
      "name": "London",
      "latitude": "51.5074",
      "longitude": "-0.1278",
      "score": 1.0
    },
    {
      "name": "London Heathrow Airport",
      "latitude": "51.4700",
      "longitude": "-0.4543",
      "score": 0.9
    }
  ]
}
```

## Testing

The project includes a test suite to validate the functionality of the API. To run the tests, use the following command:

```
python test.py
```

## Database Population

The database can be populated with city data using the `db.py` script. The city data should be provided in a TSV file located at `data/cities_canada-usa.tsv`.

To populate the database, run the following command:

```
python src.db.py populate
```

## Contributing

If you want to contribute to this project, you can follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Implement your changes.
4. Write tests to cover your changes (if applicable).
5. Run the existing tests to ensure they pass with your changes.
6. Commit your changes and push them to your fork.
7. Submit a pull request explaining your changes.
