import random
import string


def random_string_generator(size,
                            chars=string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


def unique_sku_generator(instance, size):
    new_sku = random_string_generator(size)

    Klass = instance.__class__

    qs_exists = Klass.objects.filter(
                    sku=new_sku).exists()
    if qs_exists:
        return unique_sku_generator(instance, size)
    return new_sku
