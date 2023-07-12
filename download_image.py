import requests

url='https://images.pexels.com/photos/15795337/pexels-photo-15795337/free-photo-of-masa-mavi-gokyuzu-bulut-ahsap.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1'

img=requests.get(url)

with open('image.jpeg', 'wb') as f:
    f.write(img.content)
