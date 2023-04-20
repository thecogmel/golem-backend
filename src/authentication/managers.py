from typing import Optional, TypedDict

from django.contrib.auth.models import BaseUserManager
from django.db.models import TextChoices


class UserType(TypedDict):
    name: str
    email: str
    username: str
    role: TextChoices
    password: str
    sector: Optional[str]
    office: Optional[str]


class UserManager(BaseUserManager):
    def create(self, **kwargs: UserType):
        password = kwargs.pop("password")
        if email := kwargs.pop("email"):
            email = self.normalize_email(email).lower()
        user = self.model(
            email=email,
            **kwargs,
        )
        user.set_password(password)
        user.save()

        return user

    def create_superuser(self, email, password, name, username):
        return self.create(
            email=email,
            name=name,
            username=username,
            password=password,
            role=self.model.Roles.ADMIN,
            is_superuser=True,
            is_staff=True,
        )
