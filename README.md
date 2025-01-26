
HackerRank Contest API
====================

This is a simple Flask API that allows you to access the leaderboard of any HackerRank contest based on the contest ID. With this API, users can get real-time ranking data and participant information for any contest hosted on HackerRank.

Features
--------

- Retrieve the leaderboard for any HackerRank contest by contest ID.
- Caching of requests to allow very low latency responses.
- Supports high request throughput using Gunicorn.
- Display rankings of participants along with their scores.
- Available through Docker.
- Thread-safe.
- Built using Flask for easy integration and customization.

Prerequisites
-------------

Before running this API, ensure you have the following installed:

- Python 3.x
- pip (Python package manager)

Usage
-----

### Using Docker (Recommended)

You can run the API with Docker:

```
docker run -d -p 5000:5000 singhaditya4/hackerrank-api
```

### Without Docker

If you prefer to run the API without Docker, follow these steps:

1. Clone the repository:
    ```
    git clone https://github.com/adi-tyasingh/hackerrank-contest-api.git
    ```

2. Enter the project directory:
    ```
    cd hackerrank-contest-api
    ```

3. Install the required dependencies:
    ```
    pip install -r requirements.txt
    ```

4. Run the application using Gunicorn:
    ```
    gunicorn -w 4 -b 0.0.0.0:5000 app:app
    ```

Endpoints
---------

### `GET /leaderboard?contest_id=<CONTEST_ID>`

Retrieve the leaderboard of a specific contest using the contest ID.

#### Example Request:
```
http://localhost:5000/leaderboard?contest_id=spider-sums-showdown
```

#### Example Response:
```json
{
  "available": true,
  "current_hacker": {},
  "models": [
    {
      "avatar": "https://secure.gravatar.com/avatar/b742d5d647a47709f388c92540dc4056?d=https%3A%2F%2Fd1ce3iv5vajdy.cloudfront.net%2Fhackerrank%2Fassets%2Fgravatar.jpg&s=150",
      "company": "",
      "country": "India",
      "hacker": "gdg_voidwreckers",
      "hacker_id": 28096348,
      "index": 0,
      "is_multiple_contest": false,
      "language": null,
      "level": 5,
      "rank": 1,
      "score": 700,
      "submitted_at": "10 days",
      "time_taken": 9477,
      "timestamp": 1737019994,
      "worst_testcase_time": null
    },
    {
      "avatar": "https://d1ce3iv5vajdy.cloudfront.net/hackerrank/assets/gravatar.jpg",
      "company": "",
      "country": "India",
      "hacker": "gdgmdh",
      "hacker_id": 26936116,
      "index": 1,
      "is_multiple_contest": false,
      "language": null,
      "level": 5,
      "rank": 2,
      "score": 657.14,
      "submitted_at": "10 days",
      "time_taken": 10362,
      "timestamp": 1737017667,
      "worst_testcase_time": null
    }
  ],
  "page": 1,
  "self_display": true,
  "total": 2
}
```

Customization
-------------

- To increase the number of workers, or adjust any other configuration, modify the `CMD` in the `Dockerfile`.
- To change the limit of participants shown in the response (currently set to 10,000), modify the URL parameters in `app.py`.

Contributing
------------

If you'd like to contribute to this project, feel free to fork the repository, create a branch, and submit a pull request. Please ensure you follow the project's coding standards and write tests for any new features.

Contact
-------

If you have any questions or suggestions, feel free to reach out to us at [singhaditya4@outlook.in](mailto:singhaditya4@outlook.in).
