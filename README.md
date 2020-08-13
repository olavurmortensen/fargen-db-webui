
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

