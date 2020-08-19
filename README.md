# FarGen DB Web-UI

## Local testing with Docker

For local testing, first clone repo:

```
git clone https://github.com/olavurmortensen/fargen-reports-webui.git
```

Build the image:

```
cd fargen-reports-webui
sudo docker build . -t fargen-reports-webui
```

And run the app in Docker:

```
sudo docker run --name fargen-reports-ui -p80:80 fargen-reports-webui
```

The app should be running on http://0.0.0.0:80/.

## Local testing *without* Docker

Install dependencies via Conda:

```
conda env create -f environment.yml
```

Activate the Conda environment:

```
conda actrivate fargen-db-webui
```

Set environment variable, telling Flask where the app source code is:

```
export FLASK_APP=$(pwd)/app
```

Run the app:

```
flask run
```

The app should be running on http://127.0.0.1:5000/.

Alternatively, specify a different host and port:

```
flask run --host 0.0.0.0 --port 80
```


