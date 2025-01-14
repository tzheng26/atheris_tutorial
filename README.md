# This is a Tutorial on how to use Atheris

Atheris is a coverage-guided, native Python fuzzer. 

In `/learn` you will find tutorials on how to use Atheris.

We suggest you to run the code in a docker environment.

You can use our dockerfile to build a docker image and create a container.:
```bash
docker build -f learn/dockerfile -t atheris-image .

docker run -itd --name atheris -v /home/user/lectures/atheris:/home/atheris atheris-image bash
```

Or use the official docker configuration:

See `/deployment`