FROM python:3
ADD main.py /
ADD character_list.txt /
RUN pip3 install numpy
RUN pip3 install scipy
CMD [ "python3", "/main.py"]