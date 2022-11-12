FROM postgres
ENV POSTGRES_PASSWORD advicehealth
ENV POSTGRES_DB postgres
COPY create_db.sql /docker-entrypoint-initdb.d/