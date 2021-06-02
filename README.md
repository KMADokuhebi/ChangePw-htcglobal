# How to run?

## Build container
> docker-compose -f docker-compose.prod.yml up -d --build

---

## Build static file
> docker exec -it changepw-htcglobal_web_1 python manage.py collectstatic --noinput
