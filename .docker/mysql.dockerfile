FROM mysql as development

ENV APP_ENV=development

# Database initialisation files
COPY .docker/mysql_scripts/initdb/init.sql /docker-entrypoint-initdb.d/init.sql


# Possible start for production image
#FROM mysql as production
#
#ENV APP_ENV=production