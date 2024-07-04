FROM debian:latest

USER root

RUN apt update  && \ 
    apt upgrade -y && \
    apt install -y wget sudo
RUN wget https://packages.microsoft.com/config/debian/12/packages-microsoft-prod.deb -O packages-microsoft-prod.deb
RUN dpkg -i packages-microsoft-prod.deb
RUN rm packages-microsoft-prod.deb

RUN apt update && \
   sudo apt install -y dotnet-sdk-8.0 && \
   sudo apt install -y dotnet-runtime-8.0

COPY VulnerableLightApp-main /app/vulnerablelightapp
WORKDIR /app/vulnerablelightapp
CMD ["dotnet", "run"]