FROM alpine:3.8

RUN apk add --update bash gcc musl-dev make zlib-dev ncurses-dev bzip2-dev xz-dev python3 python3-dev

WORKDIR /app

RUN wget https://github.com/samtools/samtools/releases/download/1.9/samtools-1.9.tar.bz2 && tar x -f samtools-1.9.tar.bz2

WORKDIR /app/samtools-1.9

RUN make

ADD requirements.txt /app/requirements.txt
RUN pip3 install --upgrade --force-reinstall -r /app/requirements.txt

ADD mpileup /app/mpileup
ADD run.py /app/run.py

RUN chmod +x /app/run.py

CMD ["python3", "-u", "/app/run.py"]