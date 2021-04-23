import pytest

from pytest_django.asserts import assertTemplateUsed

pytestmark = pytest.mark.django_db

# Model testing

# View testing


def test_bag_view_uses_correct_template(client):
    response = client.get("/bag/")
    assertTemplateUsed(response, "bag/bag.html")
