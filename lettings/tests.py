from django.urls import reverse
import pytest
from pytest_django.asserts import assertTemplateUsed, assertContains
from lettings.models import Letting, Address


@pytest.mark.django_db
def test_lettings_index_view(client):

    response = client.get(reverse("lettings:index"))
    assertTemplateUsed(response, "lettings/index.html")
    assert response.status_code == 200
    assertContains(response, "Lettings")


@pytest.mark.django_db
def test_lettings_address_view(client):
    title = "Joshua Tree Green Haus /w Hot Tub"
    address = Address.objects.create(
        number=7217,
        street="Bedford Street",
        city="Brunswick",
        state="GA",
        zip_code=31525,
        country_iso_code="USA",
    )
    Letting.objects.create(title=title, address=address)
    res = client.get(reverse("lettings:letting", args=[1]))
    assertTemplateUsed(res, "lettings/letting.html")
    assert res.status_code == 200
    # print (res.content.decode(),3333333333333)
    assertContains(res, "Joshua Tree Green Haus /w Hot Tub")
