import pytest
from django.urls import reverse
from pytest_django.asserts import assertTemplateUsed, assertContains

# Create your tests here.
@pytest.mark.django_db
def test_status_code(client):
    res = client.get(reverse("index"))
    assert res.status_code == 200
    assertTemplateUsed(res, "index.html")
    assertContains(res, "Holiday Homes")
