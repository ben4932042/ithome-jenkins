FROM ghcr.io/ben4932042/jenkins-ithome:v0.0.0

ENTRYPOINT [ "/opt/bitnami/scripts/jenkins/entrypoint.sh" ]
CMD [ "/opt/bitnami/scripts/jenkins/run.sh" ]

