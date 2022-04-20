FROM  ubuntu:20.04
RUN apt-get update && apt-get install -y git curl unzip
WORKDIR /home/user

#Instalar flutter sdk (versao 2.10.4)
RUN git clone --depth 1 --branch 2.10.4 https://github.com/flutter/flutter.git
ENV PATH "$PATH:/home/user/flutter/bin"

RUN flutter config --enable-web 
RUN flutter doctor 

WORKDIR /home/user/front/
ADD . /home/user/front/

ENTRYPOINT [ "flutter" , "run" , "-d" , "web-server", "--web-hostname" , "0.0.0.0" , "--web-port","5001" ]