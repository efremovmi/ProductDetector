import click

from app.backend.session import create_session
from app.schemas.auth import CreateUserSchema
from app.services.v1.auth import AuthService


@click.command()
@click.option("--name", type=str, help="User name")
@click.option("--email", type=str, help="Email")
@click.option("--password", type=str, help="Password")
def main(name: str, email: str, password: str) -> None:
    user = CreateUserSchema(name=name, email=email, password=password)
    session = next(create_session())
    AuthService(session).create_user(user)
    session.commit()


if __name__ == "__main__":
    main()
