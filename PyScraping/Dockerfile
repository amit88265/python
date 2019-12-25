FROM python:3

LABEL author="Amit Kumar" 

WORKDIR /user/src/app

COPY latest_news_crawler.py /user/src/app

RUN pip install --no-cache-dir requests pandas beautifulsoup4

ENTRYPOINT [ "python3", "latest_news_crawler.py" ]