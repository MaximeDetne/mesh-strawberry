# mesh-strawberry

For debug purposes on file uploads

## GraphQL API

cd strawberry_django_api
pipenv shell
pipenv install
python manage.py makemigrations
python manage.py migrate
python manage.py runserver

-> http://localhost:8000

## Mesh gateway

cd graphqlMesh
yarn

#### If you want to generate the supergraph (once the upstream API is running)

npx mesh-compose > supergraph.graphql

#### Run the gateway

DEBUG=1 npx hive-gateway supergraph supergraph.graphql

-> http://localhost:4001/graphql
