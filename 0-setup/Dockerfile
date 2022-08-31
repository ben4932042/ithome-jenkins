FROM ghcr.io/ben4932042/jenkins-ithome:main

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

ENTRYPOINT [ "/opt/bitnami/scripts/jenkins/entrypoint.sh" ]
CMD [ "/opt/bitnami/scripts/jenkins/run.sh" ]

