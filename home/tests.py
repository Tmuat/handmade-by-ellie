import pytest

from pytest_django.asserts import assertTemplateUsed


def test_home_view_uses_correct_template(client):
    response = client.get('/')
    assertTemplateUsed(response, 'home/index.html')
