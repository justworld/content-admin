FROM justworld/python-ubuntu:18.04
ENV LANG C.UTF-8
RUN mkdir -p /var/web/content-admin \
    && cd /var/web/content-admin/
WORKDIR /var/web/content-admin/
EXPOSE 8000
COPY requirements.txt /var/web/content-admin/requirements.txt
RUN pip3 install -r requirements.txt -i https://pypi.douban.com/simple
COPY / /var/web/content-admin/
RUN chmod 755 /var/web/content-admin/entrypoint.sh
ENTRYPOINT ["/var/web/content-admin/entrypoint.sh"]