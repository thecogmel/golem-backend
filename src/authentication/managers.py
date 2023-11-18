from django.contrib.auth.models import BaseUserManager


class UserManager(BaseUserManager):
    def create(self, **kwargs):
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
            role=self.model.Roles.MEMBER,
            is_superuser=True,
            is_staff=True,
        )
