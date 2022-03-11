
import pytest
from django.urls import reverse
from pytest_django.asserts import assertTemplateUsed

# Create your tests here.
@pytest.mark.django_db
def test_status_code(client):
    res = client.get(reverse("index"))
    assert res.status_code == 200
    assertTemplateUsed(res, 'index.html')
    print(res.content.decode(),6666666666666)
    # content = res.content.decode('utf-8')
    # expected_content = '<title>Holiday Homes</title>| <h1>Welcome to Holiday Homes</h1> | <div><a href="/profiles/">Profiles</a></div> | <div><a href="/lettings/">Lettings</a></div>'
    # assert content ==expected_content
    
    