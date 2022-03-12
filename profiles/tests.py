from django.urls import reverse
import pytest
from pytest_django.asserts import assertTemplateUsed, assertContains
from django.contrib.auth.models import User
from profiles.models import Profile


@pytest.mark.django_db
def test_lettings_index_view(client):

    response = client.get(reverse("profiles:index"))
    assertTemplateUsed(response, "profiles/index.html")
    assert response.status_code == 200

    assertContains(response, "Profiles")


@pytest.mark.django_db
def test_lettings_address_view(client):
    user = User.objects.create(
        username="4meRomance",
        email="coemperor@famemma.net",
        first_name="John",
        last_name="Rodriguez",
        password=123,
    )

    Profile.objects.create(user=user, favorite_city="Berlin")

    response = client.get(reverse("profiles:profile", args=["4meRomance"]))
    assertContains(response, "4meRomance")
    assertTemplateUsed(response, "profiles/profile.html")
    assert response.status_code == 200
