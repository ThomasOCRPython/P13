from django.test import TestCase
from django.urls import reverse
import pytest
from pytest_django.asserts import assertTemplateUsed
from lettings.models import Letting, Address



@pytest.mark.django_db
def test_lettings_index_view(client):

    response = client.get(reverse('lettings:index'))
    assertTemplateUsed(response, 'lettings/index.html')
    assert response.status_code == 200


@pytest.mark.django_db
def test_lettings_address_view(client):
    address = Address.objects.create(
            number= 7217,					
            street="Bedford Street",
            city="Brunswick",
            state="GA",
            zip_code=31525,
            country_iso_code="USA"
        )
    Letting.objects.create(address=address)
    response = client.get(reverse('lettings:letting', args=[1]))
    assertTemplateUsed(response, 'lettings/letting.html')
    assert response.status_code == 200



