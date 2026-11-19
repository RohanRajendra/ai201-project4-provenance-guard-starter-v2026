# Provenance Guard in a container: the Hugging Face Space (stretch 3), and
# the same image locally:
#   docker build -t provenance-guard . && docker run -p 7860:7860 provenance-guard
FROM python:3.13-slim

# Spaces run the container as uid 1000
RUN useradd -m -u 1000 user
USER user
ENV HOME=/home/user PATH=/home/user/.local/bin:$PATH HOST=0.0.0.0 PORT=7860
WORKDIR /home/user/app

# CPU torch first: PyPI's Linux wheel pulls in gigabytes of CUDA. Then the
# exact pins (torch==2.15.0 is already satisfied by 2.15.0+cpu).
COPY --chown=user requirements.lock.txt .
RUN pip install --no-cache-dir --user torch==2.15.0 --index-url https://download.pytorch.org/whl/cpu \
 && pip install --no-cache-dir --user -r requirements.lock.txt

COPY --chown=user . .
# Bake gpt2 (548 MB) into the image, so a start never downloads it.
RUN python detector.py

EXPOSE 7860
CMD ["gunicorn", "-c", "gunicorn.conf.py", "app:app"]
