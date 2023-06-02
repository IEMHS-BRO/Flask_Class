FROM python:3.8

# root 권한
# 유저를 추가해줄껀데, 패스워드를 입력하지않아도되게끔 할거야, 그리고 홈 디렉토리도 자동생성됩니다.
RUN adduser --disabled-password python

# 위에서 생성한 python유저로 전환 (root -> python)
USER python

# 의존성 패키지 복사
COPY ./requirements.txt /tmp/requirements.txt

# 의존성 패키지 설치
RUN pip install --user -r /tmp/requirements.txt
RUN pip install --user gunicorn==20.1.0

# 프로젝트 복사
COPY --chown=python:python ./ /var/www/strawberrymarket

# 복사한 프로젝트 경로로 이동
WORKDIR /var/www/strawberrymarket

# 설치한 패키지 명령어를 사용하기 위해 환경변수를 등록!
ENV PATH="/home/python/.local/bin:${PATH}"

# 엔트리포인트 쉘 실행권한 추가
RUN chmod +x ./etc/docker-entrypoint.sh

# 8080 포트를 노출 시켜줄거야
EXPOSE 8080

# 유니콘 실행
# CMD gunicorn --bind :8080 --workers 2 --threads 8 'app:create_app()'