docker build -t chinese-parser2 .
docker push larkz/examples:chinese-parser
docker run chinese-parser2 python3 main.py 100 200 50
sudo docker run --rm -p 8787:8787 larkz/examples:chinese-parser python3 main.py 100 200 50
