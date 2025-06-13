FROM openjdk
WORKDIR /app
COPY . /app
RUN javac HelloBBSN.java
CMD ["java","HelloBBSN"]

