from fastapi import FastAPI
from strawberry.fastapi import GraphQLRouter
from schemas import schema

app = FastAPI()

graphql_app = GraphQLRouter(schema)
app.include_router(graphql_app, prefix="/graphql")

@app.get("/")
async def root():
    return {"message": "API Gateway running with GraphQL"}
