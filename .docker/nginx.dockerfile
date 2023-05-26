FROM nginx as development

ENV APP_ENV=development

# Copy custom nginx config
COPY ./.docker/config/nginx.development.conf /etc/nginx/nginx.conf


# Possible start for production image
#FROM nginx as production
#
#ENV APP_ENV=production
#
## Copy custom nginx config
#COPY ./.docker/config/nginx.production.conf /etc/nginx/nginx.conf

