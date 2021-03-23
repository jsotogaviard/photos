# data

## install aws cli
Run the following script to make sure it is installed
'''
aws --version
'''
## Add key in ~/{user}/.aws/credentials
'''
[default]
aws_access_key_id = xxx
aws_secret_access_key = yyy
'''

## Compress the images
''''
py -m pip install --upgrade pip
py -m pip install --upgrade Pillow
'''

'''
py  data/compress/compress_images.py data/out/2005-2010 20
py  data/compress/remove_compressed_images.py data/out/2005-2010 
'''

## To sync from s3 to local computer run:
'''
aws s3 sync s3://sotochassaigne1/ data/out
'''
## To sync from local computer to 3
'''
aws s3 sync data/out s3://sotochassaigne1
'''

aws s3 sync data/out/2005-2010 s3://sotochassaigne1/2005-2010

# ui
## Project setup
```
npm --prefix ui install
```

### Compiles and hot-reloads for development
```
npm --prefix ui run serve
```

### Compiles and minifies for production
```
npm --prefix ui run build
```

### Lints and fixes files
```
npm --prefix ui run lint
```

### Customize configuration
See [Configuration Reference](https://cli.vuejs.org/config/).

